---
layout: default
title: Febuxostat
parent: Moderate Evidence (L3-L4)
nav_order: 375
evidence_level: L4
indication_count: 3
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Febuxostat: From Gout-Related Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a xanthine oxidoreductase (XOR) inhibitor that lowers uric acid, and it is generally used for chronic hyperuricemia in gout. The Canadian licence records supplied do not state an indication.
The TxGNN model predicts it for **renal hypouricemia**, but the support is very thin: **1 clinical trial** of doubtful relevance and **2 publications** (one narrative review and one single-patient report).
Mechanistically the prediction is counterintuitive, because the drug lowers urate in a condition where urate is already low.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records supplied (drug class use: hyperuricemia in gout) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Febuxostat is known as a non-purine selective XOR inhibitor. It reduces uric acid production, so it is used for hyperuricemia.

Renal hypouricemia is usually caused by loss-of-function variants in the urate transporters URAT1 (SLC22A12) or GLUT9 (SLC2A9). These variants cause excess urate excretion by the kidney and low serum urate. A drug that lowers urate further would not treat this underlying condition, so a direct therapeutic effect is mechanistically counterintuitive. The high TxGNN score most likely reflects the drug–urate-axis connection in the knowledge graph, not a true therapeutic relationship.

The only plausible rationale is a narrow hypothesis. Patients with renal hypouricemia are prone to exercise-induced acute kidney injury (EIAKI). Reducing urate production, the urinary urate load and XOR-derived oxidative stress might help prevent it. A single Japanese case report describes this use in a 16-year-old football player with a URAT1 variant. No controlled clinical data support the approach.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of how uric acid control affects stone recurrence and renal function in patients with hyperuricemia and calculi. The registry title is only a hospital department name, so the condition and intervention cannot be verified as related to renal hypouricemia. This is likely a conventional hyperuricemia study (relevance grade C, not direct evidence). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case report / hypothesis | Internal Medicine | Describes a 16-year-old football player with familial renal hypouricemia (URAT1 compound heterozygous variants) and recurrent EIAKI. Hydration did not prevent episodes, so febuxostat was used as prophylaxis. It proposes non-purine XOR inhibitors as a possible preventive option. The supplied abstract excerpt is truncated, so the outcome is not confirmed here. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia (serum urate < 2 mg/dL) for practising rheumatologists, covering its causes. It is background reading and contains no febuxostat efficacy data. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2466198 | TEVA-FEBUXOSTAT |
| 2490870 | JAMP FEBUXOSTAT |
| 2473607 | MAR-FEBUXOSTAT |
| 2533243 | AURO-FEBUXOSTAT |
| 2539837 | FEBUXOSTAT |

Six licences are recorded in total, and the five above are listed. The records supplied do not include dosage form, manufacturer or approved indication text.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings or contraindications were available in the Evidence Pack, and no drug interaction records were found.

One theoretical concern applies to related XOR-inhibition uses. Blocking XOR raises upstream hypoxanthine and xanthine, which may increase the risk of xanthine nephropathy or stones. This is most relevant if febuxostat is used in purine-overproduction disorders such as HPRT deficiency.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no supporting clinical evidence. The single registered trial is probably about ordinary hyperuricemia, and the literature consists of a general review and one case report. The proposed mechanism runs against the drug's known pharmacology, so the high TxGNN score should be read as a knowledge-graph artifact. Two other predictions in the pack, partial HPRT deficiency and Lesch-Nyhan syndrome, are more mechanistically coherent. They would only address the urate burden, not the underlying enzyme defect or the neurological features, and they are supported only by case-level reports.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Confirmation of what NCT04398251 actually studies
- Controlled or larger case-series data on febuxostat for preventing EIAKI in renal hypouricemia
- A safety assessment for kidney stones and xanthine nephropathy in this population

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

