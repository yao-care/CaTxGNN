---
layout: default
title: Sodium Sulfate
parent: Model Prediction Only (L5)
nav_order: 850
evidence_level: L5
indication_count: 1
---

# Sodium Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Sodium Sulfate: From Bowel Cleansing to Dyspepsia

## One-Sentence Summary

Sodium sulfate is an osmotic (saline) laxative used in bowel-cleansing products. The TxGNN model predicts it may be effective for **dyspepsia**, but the evidence is very weak: the **3 clinical trials** and **4 publications** retrieved do not test sodium sulfate for dyspepsia. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records; the products (e.g., PEGLYTE, COLYTE) are bowel-cleansing preparations |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Sodium sulfate is an osmotic laxative, so it draws water into the bowel and promotes evacuation. It is used in combination bowel-preparation products. Its original indication is not recorded in the Canadian licence data.

No credible mechanistic link to dyspepsia has been established. The high TxGNN score reflects a network-based model prediction, not clinical or mechanistic evidence. A laxative could plausibly worsen upper GI symptoms such as bloating, nausea, and cramping rather than relieve them. The prediction should therefore be treated as a hypothesis with low plausibility until supported by data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06339697](https://clinicaltrials.gov/study/NCT06339697) | Phase 4 | Completed | 194 | Compares laxative bowel preparations (polyethylene glycol electrolyte vs. sodium picosulfate) and their effect on the gut microbiome in patients undergoing colon polypectomy. Dyspepsia is not studied. |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | Oxycodone vs. pregabalin as preemptive analgesia for postoperative pain. Unrelated to sodium sulfate or dyspepsia; likely a spurious match. |
| [NCT07310927](https://clinicaltrials.gov/study/NCT07310927) | Phase 2/3 | Recruiting | 140 | Alginate vs. sucralfate added to PPIs for GERD symptom relief. Upper GI condition, but sodium sulfate is not involved. |

All three trials were graded C (indirect or irrelevant) and provide no support for repurposing.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33918638](https://pubmed.ncbi.nlm.nih.gov/33918638/) | 2021 | Preclinical animal study | Molecules | Dextran sodium sulfate-induced gut injury in pigs altered donepezil pharmacokinetics and gastric myoelectric activity. |
| [34207410](https://pubmed.ncbi.nlm.nih.gov/34207410/) | 2021 | Preclinical animal study | Pharmaceuticals (Basel) | Dextran sodium sulphate-induced gut injury aggravated the effect of galantamine on gastric myoelectric activity in pigs. |
| [36614242](https://pubmed.ncbi.nlm.nih.gov/36614242/) | 2023 | Preclinical animal study | Int J Mol Sci | Atractylodin ameliorated DSS-induced colitis via PPARα agonism. |
| [40391232](https://pubmed.ncbi.nlm.nih.gov/40391232/) | 2025 | Preclinical study | J Inflamm Res | Si-Ni Decoction was studied in a DSS colitis model (network pharmacology and in vivo validation). |

These papers use dextran sodium sulfate (DSS), a chemical that induces colitis in animal models. It is a different compound from sodium sulfate, so they are keyword matches and do not support the prediction.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 00777838 | PEGLYTE POWDER |
| 02378329 | JAMPLYTE |
| 00677442 | COLYTE |
| 02552612 | JAMPLYTE + BISACODYL |
| 02326302 | BI-PEGLYTE |

Dosage form and approved indication text are not available in the retrieved records. Six licences are registered in total; five are listed above.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (L5). The retrieved trials are unrelated to dyspepsia, and the literature concerns DSS animal models, not sodium sulfate. A laxative mechanism also makes benefit in dyspepsia doubtful.

**To proceed, the following is needed:**
- Health Canada package insert, including warnings and contraindications (currently blocking safety screening)
- Mechanism of action data, for example from DrugBank
- Confirmed original indication and approved indication text for each DIN
- Clinical or mechanistic studies of sodium sulfate in functional or organic dyspepsia
- Route and formulation compatibility assessment for a dyspepsia use
- Assessment of whether osmotic laxative effects could worsen upper GI symptoms

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

