---
layout: default
title: Mesalazine
parent: Model Prediction Only (L5)
nav_order: 594
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Mesalazine: predicted new indication Congenital hypotrichosis with juvenile macular dystrophy (evidence level L5). Approved use: Ulcerative colitis, inflammatory bowel disease…"
monitor_inn: "MESALAZINE"
predicted_indications: ["congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "rheumatoid arthritis", "seborrheic keratosis", "osteoarthritis susceptibility", "vulvar inverted follicular keratosis", "pseudoachondroplasia"]
---

# Mesalazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Mesalazine: From Ulcerative Colitis to Congenital Hypotrichosis with Juvenile Macular Dystrophy

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid, 5-ASA) is an anti-inflammatory drug originally used to treat ulcerative colitis and other inflammatory bowel conditions.
The TxGNN model's top-ranked prediction is **congenital hypotrichosis with juvenile macular dystrophy**, but there are **0 clinical trials** and **0 publications** supporting it. The score is a graph-based prediction only.
Among the other predictions, **rheumatoid arthritis** has the most supporting material (11 publications, mostly indirect), and it is the more scientifically plausible direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis, inflammatory bowel disease, ulcerative proctosigmoiditis |
| Predicted New Indication | Congenital hypotrichosis with juvenile macular dystrophy |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mesalazine is a 5-aminosalicylate with local anti-inflammatory activity in the intestinal mucosa. Its efficacy in ulcerative colitis is well established.

For the top-ranked prediction, **congenital hypotrichosis with juvenile macular dystrophy**, no mechanistic link has been identified. It is an ultra-rare monogenic disorder caused by CDH3 mutation and does not overlap with inflammatory bowel pathways. The high score (0.996) reflects graph proximity only and is not a reason to expect clinical benefit.

Two other predictions deserve a brief comment:
- **Rheumatoid arthritis (rank 3):** Mesalazine shares its active moiety with sulfasalazine, an established disease-modifying antirheumatic drug. However, the antirheumatic effect of sulfasalazine is generally attributed mainly to the sulfapyridine part, so benefit from mesalazine alone is uncertain.
- **Osteoarthritis (rank 2):** Anti-inflammatory effects (COX/lipoxygenase inhibition, NF-κB modulation, PPAR-γ activation) could plausibly relate to low-grade synovial inflammation. This remains speculative.

The remaining predictions (seborrheic keratosis, osteoarthritis susceptibility, vulvar inverted follicular keratosis, pseudoachondroplasia) have no identified mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction or for any of the other predictions.

---

## Literature Evidence

No literature is available for the top-ranked prediction (congenital hypotrichosis with juvenile macular dystrophy).

For reference, the table below lists the most relevant literature for the best-supported alternative prediction, **rheumatoid arthritis**. Almost all of it is indirect, and no mesalazine trials in rheumatoid arthritis were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | Sulfasalazine is an established DMARD in rheumatoid arthritis. It is split into sulfapyridine and mesalazine, and which part is active remains uncertain. |
| [7781502](https://pubmed.ncbi.nlm.nih.gov/7781502/) | 1995 | Review | Dtsch Med Wochenschr | General review of mesalazine (no abstract available). |
| [7904547](https://pubmed.ncbi.nlm.nih.gov/7904547/) | 1993 | Review | Clin Pharmacokinet | Pharmacokinetics of slow-acting antirheumatic drugs, including sulfasalazine. Clinical effects are delayed by several months. |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | Pharmacovigilance | Gut | Re-evaluation of serious adverse reactions to sulfasalazine and mesalazine from suspected adverse reaction reports. |
| [36855206](https://pubmed.ncbi.nlm.nih.gov/36855206/) | 2023 | Case report | J Med Case Reports | Tofacitinib worked in two patients with IBD-associated arthritis (indirect, not mesalazine). |
| [42565551](https://pubmed.ncbi.nlm.nih.gov/42565551/) | 2026 | Cohort | Rheumatology (Oxford) | Medication use and pregnancy outcomes in women with immune-mediated inflammatory diseases (indirect). |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2026 | Case report | Intern Med | 5-ASA-induced colitis in a rheumatoid arthritis patient without IBD (safety signal). |
| [31830393](https://pubmed.ncbi.nlm.nih.gov/31830393/) | 2019 | Case report | G Ital Nefrol | Acute renal failure from DRESS syndrome after sulfasalazine and mesalazine in a rheumatoid arthritis patient (safety signal). |

---

## Canada Market Information

Mesalazine is marketed in Canada with 18 valid single-ingredient authorizations. Dosage form and approved-indication text are not available for these products.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02529610 | OCTASA | Not available | Not available |
| 02465752 | OCTASA | Not available | Not available |
| 02545012 | MEZERA | Not available | Not available |
| 02112809 | SALOFALK | Not available | Not available |
| 02524481 | MEZERA | Not available | Not available |

Other marketed brands include PENTASA, MEZAVANT and TEVA-5 ASA.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, interstitial nephritis, lipoid nephrosis, pyoureter, liver disease, gallbladder disease, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia) and pyloric stenosis. These need confirmation against the package insert.
- **Drug interactions:** 100 interactions were found. The two classified as **Major** are botulinum neurotoxin A/B immune globulin and cidofovir. Many **Moderate** interactions involve potentially nephrotoxic or otherwise relevant drugs, including NSAIDs (ketorolac, ibuprofen, celecoxib, bromfenac), aminoglycosides and related antibiotics (amikacin, capreomycin, bacitracin), amphotericin B formulations, acyclovir, cisplatin, azathioprine, sulfonylureas (acetohexamide, chlorpropamide) and anisindione.
- **Reports in the literature:** hypersensitivity reactions (DRESS with acute renal failure) and 5-ASA-induced colitis have been described in patients with rheumatoid arthritis.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, congenital hypotrichosis with juvenile macular dystrophy, rests only on a graph-based score. It has no trials, no literature and no plausible mechanism (L5). Mesalazine is well established and widely marketed in Canada, but that does not support this new indication. Rheumatoid arthritis is the more plausible direction (L4, via sulfasalazine), but the evidence is indirect and efficacy of mesalazine alone is uncertain.

**To proceed, the following is needed:**
- Mechanism of action data for mesalazine.
- Package insert warnings and contraindications from Health Canada, as safety screening cannot proceed without them.
- For rheumatoid arthritis, direct clinical evidence for mesalazine (not sulfasalazine) before it is considered further.
- For the top-ranked rare disease, any biological rationale linking mesalazine to CDH3-related pathology before further investment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

