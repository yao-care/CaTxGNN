---
layout: default
title: Clofarabine
parent: Model Prediction Only (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Clofarabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Clofarabine: From Relapsed/Refractory Pediatric Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Clofarabine is a purine nucleoside analog whose established use, per the cited literature, is relapsed or refractory pediatric acute lymphoblastic leukemia (ALL).
The TxGNN model predicts it may be effective for **myeloid leukemia**, with **50 clinical trials** (including 3 completed Phase 3 trials) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory pediatric ALL (from the literature; the Health Canada approved-indication text is not available) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 by the counting rule (3 completed Phase 3 trials in AML; the source data assigned L2) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank. Based on the published literature, clofarabine is a second-generation purine nucleoside analog. Its active triphosphate metabolite inhibits ribonucleotide reductase and DNA polymerase, and it disrupts mitochondrial membrane integrity. Together these effects deplete the deoxynucleotide pool, block DNA synthesis and repair, and trigger apoptosis in rapidly proliferating blasts.

ALL and myeloid leukemia are both acute leukemias driven by rapidly dividing blast cells. A drug that halts DNA synthesis in lymphoblasts is therefore plausibly active in myeloid blasts. The trial record supports this. Clofarabine has been tested in adult and pediatric AML as a single agent, with cytarabine, with idarubicin, and as a transplant conditioning component. The high TxGNN score (0.9988) is consistent with this mechanistic overlap.

Caveat: the original-indication field in the source data is empty, so part of this "repurposing" signal may simply reflect the drug's known leukemia activity.

---

## Clinical Trial Evidence

Of the 50 trials linked to this prediction, the 10 most relevant are listed below. They are ranked by phase, completion status and direct testing of clofarabine in myeloid disease.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02085408](https://clinicaltrials.gov/study/NCT02085408) | Phase 3 | Completed | 727 | Randomized: clofarabine induction and post-remission therapy vs daunorubicin + cytarabine, then decitabine maintenance vs observation, in newly diagnosed AML aged ≥60 |
| [NCT00317642](https://clinicaltrials.gov/study/NCT00317642) | Phase 3 | Completed | 326 | Double-blind: clofarabine + cytarabine vs cytarabine alone in relapsed/refractory AML aged ≥55 |
| [NCT00703820](https://clinicaltrials.gov/study/NCT00703820) | Phase 3 | Completed | 324 | AML08: clofarabine + cytarabine vs conventional induction in newly diagnosed AML, with NK-cell transplantation |
| [NCT01101880](https://clinicaltrials.gov/study/NCT01101880) | Phase 2 | Completed | 50 | Clofarabine + high-dose cytarabine with G-CSF priming in adults <65 with newly diagnosed AML or advanced MDS |
| [NCT00778375](https://clinicaltrials.gov/study/NCT00778375) | Phase 2 | Completed | 122 | Clofarabine + low-dose cytarabine induction, alternating with decitabine, in frontline AML/high-risk MDS aged ≥60 |
| [NCT00088218](https://clinicaltrials.gov/study/NCT00088218) | Phase 2 | Completed | 95 | Randomized: clofarabine alone vs with low-dose cytarabine in untreated AML/high-risk MDS aged ≥60 |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | Completed | 86 | Clofarabine salvage therapy in relapsed/refractory AML |
| [NCT01457885](https://clinicaltrials.gov/study/NCT01457885) | Phase 2 | Completed | 75 | Myeloablative transplant conditioning with clofarabine + busulfan for non-remission AML |
| [NCT01534702](https://clinicaltrials.gov/study/NCT01534702) | Phase 1/2 | Unknown | 60 | AMLSG 17-10: escalating clofarabine added to cytarabine + idarubicin induction in high-risk AML |
| [NCT00065143](https://clinicaltrials.gov/study/NCT00065143) | Phase 2 | Completed | 60 | Clofarabine + cytarabine in newly diagnosed AML/high-risk MDS aged ≥50 |

Note: the results of the three Phase 3 trials are not included in the data provided. Their efficacy conclusions must be verified from the primary publications.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | RCT (Phase 3) | J Clin Oncol | AML08: clofarabine in the first induction course allowed reduced daunorubicin and etoposide exposure in childhood AML |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Phase 2 | Cancer Med | Clofarabine + cytarabine + mitoxantrone in refractory/relapsed AML: high response rates and effective bridge to transplant |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohort | Transplant Cell Ther | Clofarabine + busulfan myeloablative conditioning in active myeloid malignancies |
| [31637757](https://pubmed.ncbi.nlm.nih.gov/31637757/) | 2020 | Phase 1/2 | Am J Hematol | Clofarabine + 2 Gy TBI non-myeloablative conditioning for AML patients unfit for intensive regimens |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Trial subanalysis | Cancers | Clofarabine improved relapse-free survival in younger AML patients with micro-complex karyotype |
| [29773602](https://pubmed.ncbi.nlm.nih.gov/29773602/) | 2018 | Phase 1b | Haematologica | Clofarabine replacing fludarabine with high-dose cytarabine and liposomal daunorubicin in pediatric relapsed/refractory AML |
| [18756533](https://pubmed.ncbi.nlm.nih.gov/18756533/) | 2008 | Clinical study | Cancer | Clofarabine combinations as AML salvage therapy (idarubicin combination) |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | Role of clofarabine in adult AML, from monotherapy to combination strategies |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leuk Lymphoma | Clofarabine inhibits ribonucleotide reductase and DNA polymerase, with better stability than fludarabine and cladribine |
| [22170975](https://pubmed.ncbi.nlm.nih.gov/22170975/) | 2012 | Review | Ann Pharmacother | Efficacy and tolerability of clofarabine in newly diagnosed AML in older adults |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2330407 | CLOLAR |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog antimetabolite) |
| Myelosuppression Risk | Expected to be high. Literature on clofarabine-based regimens reports grade ≥3 hematologic and infectious toxicity (no quantitative data in the source data) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clofarabine has been tested in myeloid leukemia across many Phase 1 to 3 trials, including three completed Phase 3 trials, and the mechanism fits proliferating blasts. However, the Phase 3 outcomes are not summarized in the source data, and safety information is missing. The other predictions in this pack are not recommended for advancement. The ALL entries reflect established use rather than repurposing. The neuroblastoma prediction has only indirect evidence, and the remaining entries have no supporting studies.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indication), which is a blocking gap for safety screening
- Confirmation of the primary efficacy and survival results of NCT02085408, NCT00317642 and NCT00703820
- DrugBank mechanism of action data
- A dose, toxicity and myelosuppression monitoring plan for older and transplant-eligible AML populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

