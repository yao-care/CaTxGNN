#!/usr/bin/env python3
"""Canada health news fetcher.

Fetches health-related news from Canadian news sources via Google News RSS:
- CBC Health
- CTV Health
- Global News Health
- The Globe and Mail Health

Usage:
    uv run python scripts/fetchers/ca_news.py

Output:
    data/news/ca_news_latest.json
"""

import json
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from urllib.parse import quote_plus

import httpx


@dataclass
class NewsArticle:
    """Represents a news article."""

    title: str
    url: str
    source: str
    published_date: str | None = None
    summary: str | None = None
    keywords: list[str] = field(default_factory=list)
    fetched_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "url": self.url,
            "source": self.source,
            "published_date": self.published_date,
            "summary": self.summary,
            "keywords": self.keywords,
            "fetched_at": self.fetched_at,
        }


class CANewsFetcher:
    """Fetches health news from Canadian news sources via Google RSS."""

    USER_AGENT = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    # Health-related search terms in English and French (Canada)
    HEALTH_TERMS = [
        "Canada health",
        "Canada medicine",
        "Canada drug approval",
        "Health Canada drug",
        "Canadian hospital",
        "Canada santé",
        "Canada médicament",
        "pharmaceutical Canada",
    ]

    def __init__(self, synonyms_path: Path | None = None):
        """Initialize the fetcher.

        Args:
            synonyms_path: Path to synonyms.json for keywords
        """
        self.synonyms = self._load_synonyms(synonyms_path)
        self.client = httpx.Client(
            timeout=30.0,
            follow_redirects=True,
            headers={"User-Agent": self.USER_AGENT},
        )

    def _load_synonyms(self, synonyms_path: Path | None) -> dict:
        """Load synonyms for keyword matching."""
        if synonyms_path is None:
            base_dir = Path(__file__).parent.parent.parent
            synonyms_path = base_dir / "data" / "news" / "synonyms.json"

        if synonyms_path.exists():
            with open(synonyms_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _extract_keywords_from_text(self, text: str) -> list[str]:
        """Extract matching keywords from text."""
        if not self.synonyms:
            return []

        text_lower = text.lower()
        found = []

        # Check indication synonyms
        for eng_name, synonyms in self.synonyms.get("indication_synonyms", {}).items():
            # Check English name
            if eng_name.lower() in text_lower:
                found.append(eng_name)
                continue

            # Check synonyms (French or other variations)
            for term in synonyms:
                if term.lower() in text_lower:
                    found.append(eng_name)
                    break

        # Check drug synonyms
        for eng_name, synonyms in self.synonyms.get("drug_synonyms", {}).items():
            if eng_name.lower() in text_lower:
                found.append(eng_name)
                continue

            for term in synonyms:
                if term.lower() in text_lower:
                    found.append(eng_name)
                    break

        return list(set(found))

    def fetch_google_news_rss(self, query: str, limit: int = 20) -> list[NewsArticle]:
        """Fetch news from Google News RSS.

        Args:
            query: Search query
            limit: Maximum number of articles

        Returns:
            List of NewsArticle objects
        """
        articles = []
        encoded_query = quote_plus(query)
        url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-CA&gl=CA&ceid=CA:en"

        try:
            response = self.client.get(url)
            response.raise_for_status()

            # Parse RSS XML
            root = ET.fromstring(response.content)

            for item in root.findall(".//item")[:limit]:
                title = item.findtext("title", "")
                link = item.findtext("link", "")
                pub_date = item.findtext("pubDate", "")
                source = item.findtext("source", "Google News")

                if not title or not link:
                    continue

                keywords = self._extract_keywords_from_text(title)

                article = NewsArticle(
                    title=title,
                    url=link,
                    source=source,
                    published_date=pub_date,
                    keywords=keywords,
                )
                articles.append(article)

        except (httpx.HTTPError, ET.ParseError) as e:
            print(f"Error fetching Google News for '{query}': {e}")

        return articles

    def fetch_all(self, limit_per_query: int = 10) -> list[NewsArticle]:
        """Fetch from all search terms.

        Args:
            limit_per_query: Maximum articles per search term

        Returns:
            Combined list of NewsArticle objects (deduplicated)
        """
        all_articles = []
        seen_urls = set()

        for term in self.HEALTH_TERMS:
            print(f"  Searching: {term}")
            articles = self.fetch_google_news_rss(term, limit_per_query)

            for article in articles:
                if article.url not in seen_urls:
                    seen_urls.add(article.url)
                    all_articles.append(article)

        return all_articles

    def filter_relevant(self, articles: list[NewsArticle]) -> list[NewsArticle]:
        """Filter articles to only those with matching keywords.

        Args:
            articles: List of articles

        Returns:
            Filtered list with keyword matches
        """
        return [a for a in articles if a.keywords]

    def close(self):
        """Close the HTTP client."""
        self.client.close()


def main():
    print("=" * 60)
    print("Canada Health News Fetcher - CaTxGNN")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent.parent
    news_dir = base_dir / "data" / "news"
    news_dir.mkdir(parents=True, exist_ok=True)

    fetcher = CANewsFetcher()

    try:
        # Fetch all articles
        print("1. Fetching articles from Canadian news sources...")
        articles = fetcher.fetch_all(limit_per_query=10)
        print(f"   Total fetched: {len(articles)}")

        # Filter relevant
        print("2. Filtering for relevant articles...")
        relevant = fetcher.filter_relevant(articles)
        print(f"   Relevant articles: {len(relevant)}")

        # Prepare output
        output = {
            "fetched_at": datetime.now().isoformat(),
            "statistics": {
                "total_fetched": len(articles),
                "relevant": len(relevant),
                "by_source": {},
            },
            "articles": {
                "all": [a.to_dict() for a in articles],
                "relevant": [a.to_dict() for a in relevant],
            },
        }

        # Count by source
        for article in articles:
            source = article.source
            output["statistics"]["by_source"][source] = (
                output["statistics"]["by_source"].get(source, 0) + 1
            )

        # Write output
        output_path = news_dir / "ca_news_latest.json"
        print(f"3. Writing to {output_path}...")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print()
        print("=" * 60)
        print("News Fetch Complete!")
        print("=" * 60)
        print(f"  Total articles: {len(articles)}")
        print(f"  Relevant articles: {len(relevant)}")
        for source, count in sorted(output["statistics"]["by_source"].items()):
            print(f"    - {source}: {count}")
        print(f"  Output: {output_path}")

    finally:
        fetcher.close()


if __name__ == "__main__":
    main()
