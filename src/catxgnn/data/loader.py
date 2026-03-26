"""Health Canada Drug Product Database (DPD) data loader"""

import csv
from pathlib import Path
from typing import Optional

import pandas as pd
import yaml


def load_field_config() -> dict:
    """Load field mapping configuration"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _load_dpd_file(filepath: Path, columns: list[str]) -> pd.DataFrame:
    """Load a DPD file with specified columns.

    DPD files are pipe-separated values with quote delimiter.
    """
    return pd.read_csv(
        filepath,
        names=columns,
        quotechar='"',
        encoding='utf-8',
        on_bad_lines='skip'
    )


def load_drugs(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Load drug product data.

    Args:
        data_dir: Directory containing DPD files

    Returns:
        DataFrame with drug information
    """
    if data_dir is None:
        data_dir = Path(__file__).parent.parent.parent.parent / "data" / "raw"

    config = load_field_config()
    drug_config = config['drug_file']

    filepath = data_dir / drug_config['name']
    if not filepath.exists():
        raise FileNotFoundError(
            f"Drug file not found: {filepath}\n"
            f"Please download from Health Canada DPD:\n"
            f"wget https://www.canada.ca/content/dam/hc-sc/documents/services/drug-product-database/allfiles.zip"
        )

    df = _load_dpd_file(filepath, drug_config['columns'])

    # Filter to human drugs only
    df = df[df['CLASS'] == 'Human'].copy()

    return df


def load_ingredients(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Load active ingredient data.

    Args:
        data_dir: Directory containing DPD files

    Returns:
        DataFrame with ingredient information
    """
    if data_dir is None:
        data_dir = Path(__file__).parent.parent.parent.parent / "data" / "raw"

    config = load_field_config()
    ingred_config = config['ingredient_file']

    filepath = data_dir / ingred_config['name']
    if not filepath.exists():
        raise FileNotFoundError(f"Ingredient file not found: {filepath}")

    return _load_dpd_file(filepath, ingred_config['columns'])


def load_therapeutic_classes(data_dir: Optional[Path] = None) -> pd.DataFrame:
    """Load therapeutic classification (ATC codes).

    Args:
        data_dir: Directory containing DPD files

    Returns:
        DataFrame with ATC codes
    """
    if data_dir is None:
        data_dir = Path(__file__).parent.parent.parent.parent / "data" / "raw"

    config = load_field_config()
    ther_config = config['therapeutic_file']

    filepath = data_dir / ther_config['name']
    if not filepath.exists():
        raise FileNotFoundError(f"Therapeutic file not found: {filepath}")

    return _load_dpd_file(filepath, ther_config['columns'])


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load and merge all drug data.

    This is the main entry point for drug data loading.
    Merges drug, ingredient, and therapeutic data.

    Args:
        filepath: Not used (kept for compatibility)

    Returns:
        DataFrame with merged drug information including:
        - license_id (DIN)
        - brand_name
        - ingredients (semicolon-separated)
        - atc_code
    """
    data_dir = Path(__file__).parent.parent.parent.parent / "data" / "raw"

    # Load base data
    drugs = load_drugs(data_dir)
    ingredients = load_ingredients(data_dir)
    ther = load_therapeutic_classes(data_dir)

    # Aggregate ingredients by drug
    ing_agg = ingredients.groupby('DRUG_CODE').agg({
        'INGREDIENT': lambda x: '; '.join(sorted(set(x.dropna().astype(str))))
    }).reset_index()

    # Get first ATC code per drug
    ther_first = ther.groupby('DRUG_CODE').first().reset_index()

    # Merge
    df = drugs.merge(ing_agg, on='DRUG_CODE', how='left')
    df = df.merge(ther_first[['DRUG_CODE', 'TC_ATC_NUMBER']], on='DRUG_CODE', how='left')

    # Rename to standard columns
    df = df.rename(columns={
        'DRUG_IDENTIFICATION_NUMBER': 'license_id',
        'BRAND_NAME': 'brand_name',
        'INGREDIENT': 'ingredients',
        'TC_ATC_NUMBER': 'atc_code'
    })

    # Create ingredient list for processing
    df['ingredient_list'] = df['ingredients'].apply(
        lambda x: [i.strip() for i in str(x).split(';')] if pd.notna(x) else []
    )

    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """Filter active drugs with valid ingredients.

    Args:
        df: Drug DataFrame

    Returns:
        Filtered DataFrame
    """
    # Filter drugs with ingredients
    active = df[df['ingredients'].notna() & (df['ingredients'] != '')].copy()
    active = active.reset_index(drop=True)
    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """Get drug data summary statistics.

    Args:
        df: Drug DataFrame

    Returns:
        Summary statistics dictionary
    """
    all_ingredients = set()
    for ing_list in df['ingredient_list'].dropna():
        all_ingredients.update(ing_list)

    return {
        "total_count": len(df),
        "with_ingredient": df['ingredients'].notna().sum(),
        "unique_products": df['brand_name'].nunique(),
        "unique_ingredients": len(all_ingredients),
    }


if __name__ == "__main__":
    # Test loading
    df = load_fda_drugs()
    print(f"Loaded {len(df)} drugs")

    df_active = filter_active_drugs(df)
    print(f"Active drugs: {len(df_active)}")

    summary = get_drug_summary(df_active)
    print(f"Summary: {summary}")
