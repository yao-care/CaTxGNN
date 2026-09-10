---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 503
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mesalazine: From Ulcerative Colitis to Rheumatoid Arthritis

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid, 5-ASA) is the aminosalicylate class anti-inflammatory long used for ulcerative colitis and other inflammatory bowel disease, though this evidence pack has no Canadian licensing data on file. Among the seven indications TxGNN predicted, **Rheumatoid Arthritis** carries by far the strongest evidence base — **6 clinical trials** and **20 publications** — while the drug's raw top-scoring predictions (e.g. congenital hypotrichosis with juvenile macular dystrophy) have zero supporting studies and an explicitly implausible mechanism, so they are excluded from further evaluation here.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis / inflammatory bowel disease (aminosalicylate class — general drug knowledge; not captured in this Canada regulatory dataset, see note below) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

*Note: TxGNN's single highest-scoring prediction (congenital hypotrichosis with juvenile macular dystrophy, 99.65%) has no clinical trials, no literature, and the model's own rationale flags no known mechanistic link — it is classified L5/Hold and not discussed further. Osteoarthritis (rank 2, L4, 3 preclinical papers, 0 trials) is mechanistically related to the rheumatoid arthritis findings below and is noted where relevant.*

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data was not retrieved for this pack (data gap DG002). Based on the pharmacology described in the collected literature, 5-ASA inhibits prostaglandin and leukotriene synthesis (COX/5-LOX pathway), suppresses pro-inflammatory cytokine and matrix-metalloproteinase mRNA expression in synovial tissue, and modulates lymphocyte activation — all mechanisms relevant to inflammatory joint disease.

The connection between mesalazine's established use in IBD and the RA prediction is not accidental — it runs in reverse historically. Per PMID 17708602, sulfasalazine (which the gut cleaves into mesalazine + sulfapyridine) **was originally developed in the 1940s specifically to treat rheumatoid arthritis**; its benefit in ulcerative colitis was a later, serendipitous discovery. TxGNN's prediction therefore points back toward the drug's own origin indication rather than an unrelated disease area.

Whether mesalazine's fragment alone (as opposed to sulfapyridine, or the intact sulfasalazine molecule) drives that RA benefit is contested. Two classic component-isolation studies (PMID 2860942, PMID 8535642) found 5-ASA showed only a weak effect on RA disease activity compared with sulfapyridine, suggesting sulfapyridine — not mesalazine — is the active moiety. However, a 2024 mechanistic study in osteoarthritis (PMID 38310093, evidence for the related OA prediction) shows 5-ASA has genuine, cartilage-protective, joint-relevant activity via the OSCAR–PPARγ axis, independent of sulfapyridine. This newer finding reopens the question of whether mesalazine itself has intrinsic anti-arthritic activity that the older negative RA trials underestimated.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02930343](https://clinicaltrials.gov/study/NCT02930343) | Phase 3 | Terminated | 136 | Sulfasalazine vs. leflunomide as combination DMARD therapy in RA patients failing methotrexate — the only trial directly on-indication, but terminated early so results are incomplete |
| [NCT00514982](https://clinicaltrials.gov/study/NCT00514982) | Phase 2 | Withdrawn | 0 | IBD-therapy step-up approach for Hermansky-Pudlak Syndrome colitis; immunopathogenesis focus, not RA — withdrawn with zero enrollment |
| [NCT06201793](https://clinicaltrials.gov/study/NCT06201793) | Phase 2 | Completed | 46 | Minocycline add-on in ulcerative colitis patients already on mesalamine; tests minocycline, not mesalazine, and targets UC not RA |
| [NCT05580861](https://clinicaltrials.gov/study/NCT05580861) | Phase 1/2 | Recruiting | 64 | Sulfasalazine + induction chemotherapy in elderly AML, exploiting its xCT-inhibition (oncology mechanism), unrelated to RA |
| [NCT03591770](https://clinicaltrials.gov/study/NCT03591770) | Phase 4 | Terminated | 15 | Shingrix vaccine immunogenicity in UC patients on tofacitinib — unrelated to mesalazine efficacy in RA |
| [NCT00637780](https://clinicaltrials.gov/study/NCT00637780) | Phase 4 | Terminated | 2 | Pharmacokinetics only of sulfasalazine in pediatric juvenile idiopathic arthritis — not an efficacy trial, terminated with 2 patients |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2860942](https://pubmed.ncbi.nlm.nih.gov/2860942/) | 1985 | Clinical/Pharmacology | BMJ | Head-to-head test of sulfasalazine's two components in RA: sulfapyridine showed a robust second-line effect; 5-ASA showed only a weak first-line effect — key negative evidence for mesalazine as the active moiety |
| [2877851](https://pubmed.ncbi.nlm.nih.gov/2877851/) | 1986 | Clinical study | Drugs | Open-label 6-month comparison of 5-ASA vs. sulfapyridine in RA; sulfasalazine-arm patients improved significantly, 5-ASA-arm patients did not |
| [8535642](https://pubmed.ncbi.nlm.nih.gov/8535642/) | 1995 | Review | British Journal of Rheumatology | Reviews the "which moiety is active" debate; concludes evidence favors sulfapyridine, though residual activity from absorbed intact sulfasalazine cannot be excluded |
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | Comprehensive review of sulfasalazine's pharmacology and established efficacy as a DMARD in RA; notes uncertainty over which cleavage product is responsible |
| [1356747](https://pubmed.ncbi.nlm.nih.gov/1356747/) | 1992 | Review | Deutsche Medizinische Wochenschrift | Reviews aminosalicylates across both chronic inflammatory bowel disease and rheumatoid arthritis use |
| [2899645](https://pubmed.ncbi.nlm.nih.gov/2899645/) | 1988 | Cohort | Journal of Rheumatology | 12-week sulfasalazine treatment in RA normalized elevated circulating activated lymphocytes, suggesting an immunomodulatory mechanism of action |
| [10743803](https://pubmed.ncbi.nlm.nih.gov/10743803/) | 2000 | In vitro / mechanistic | Journal of Rheumatology | Sulfasalazine and its metabolites (including 5-ASA) suppress inflammatory cytokine and matrix-metalloproteinase mRNA in rheumatoid synovial fibroblasts |
| [7781502](https://pubmed.ncbi.nlm.nih.gov/7781502/) | 1995 | Review | Deutsche Medizinische Wochenschrift | General review of mesalazine pharmacology (abstract not available) |
| [17708602](https://pubmed.ncbi.nlm.nih.gov/17708602/) | 2007 | Review | World Journal of Gastroenterology | Historical review noting 5-ASA therapy was originally designed to treat rheumatoid arthritis before its benefit in ulcerative colitis was discovered |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2025 | Case report | Internal Medicine (Tokyo) | Case of 5-ASA-induced colitis in an RA patient without underlying IBD, confirmed by lymphocyte stimulation test — relevant safety signal for RA patients receiving mesalazine/sulfasalazine |

## Canada Market Information

Mesalazine is **not currently marketed in Canada** under this dataset — no Health Canada Drug Identification Numbers (DINs) are on file (`total_licenses: 0`). No product/dosage-form/indication table can be generated until Canadian licensing data becomes available.

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were retrieved for this pack (blocking data gap DG001 — Health Canada/TFDA label warnings and contraindications not yet sourced).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest RA-specific evidence (component-isolation trials from the 1980s–90s) actually argues *against* mesalazine being the active moiety, pointing instead to sulfapyridine — while a newer 2024 mechanistic study in the related osteoarthritis prediction suggests mesalazine may have genuine, independent joint-protective activity worth re-examining. Combined with a blocking gap in safety/label data and the drug not being marketed in Canada, the evidence is not yet coherent enough to proceed.

**To proceed, the following is needed:**
- Health Canada/TFDA label warnings and contraindications (DG001, blocking)
- DrugBank mechanism-of-action confirmation (DG002)
- A modern trial or mechanistic study testing mesalazine specifically (not sulfasalazine) in RA or osteoarthritis, to resolve the active-moiety question raised by PMID 2860942/8535642 versus the 2024 OSCAR–PPARγ findings
- Monitoring of the osteoarthritis lead (rank 2, L4) as a parallel, mechanistically-linked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

