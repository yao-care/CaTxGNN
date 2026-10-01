---
layout: default
title: Plerixafor
parent: Model Prediction Only (L5)
nav_order: 739
evidence_level: L5
indication_count: 7
---

# Plerixafor
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

# Plerixafor: From Stem Cell Mobilization to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Plerixafor is a CXCR4 antagonist used to mobilize stem cells for transplantation. The TxGNN model predicts it may be effective for **indolent plasma cell myeloma**, but **no clinical trials or publications** currently support this specific prediction. The same prediction list includes **myeloid leukemia**, which has **30 registered trials** and **20 publications** and is the best-supported direction for this drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records provided (stem cell mobilization is the known use) |
| Predicted New Indication | Indolent plasma cell myeloma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Plerixafor is known as a CXCR4 antagonist. It blocks CXCL12 (SDF-1) signalling, which keeps blood and tumour cells anchored in the bone marrow niche. That is how it frees stem cells for harvest.

Plasma cells depend on the bone marrow microenvironment, so a CXCR4 blocker could plausibly disrupt the CXCL12-mediated homing of myeloma cells. This link is untested: there are no trials or publications for this indication. Plerixafor's established role in myeloma is stem cell mobilization, which is a different purpose from treating indolent disease. The high score (99.97%) should be read as a model signal, not as clinical support.

### Best-Supported Alternative: Myeloid Leukemia (Rank 7)

Although the model ranks it lower (score 99.02%), myeloid leukemia has the only real evidence base in this prediction set, graded **L2**.

- **Hypothesis:** Blocking CXCR4 mobilizes leukemic cells out of their protective marrow niche and may sensitize them to chemotherapy.
- **Evidence base:** The support consists of multiple Phase 1 and Phase 1/2 studies combining plerixafor with clofarabine, decitabine, sorafenib/G-CSF, FLAG-Ida and MEC-type regimens, plus reviews supporting CXCR4 as an AML target.
- **Limits:** Efficacy and survival benefit are not established. L2 rests on early-phase studies, not randomized Phase 2 or Phase 3 data. Many listed trials focus on mobilization or conditioning rather than direct anti-leukemic efficacy.

---

## Clinical Trial Evidence

For indolent plasma cell myeloma: currently no related clinical trials registered.

For myeloid leukemia (up to 10 most relevant of 30 registered trials):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01160354](https://clinicaltrials.gov/study/NCT01160354) | Phase 1/2 | Terminated | 22 | Plerixafor + clofarabine in untreated AML, age ≥60. Closed early and never reached the efficacy part |
| [NCT01141543](https://clinicaltrials.gov/study/NCT01141543) | N/A | Completed | 12 | Plerixafor to mobilize leukemic cells within a myeloablative regimen before allograft in AML |
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | Completed | 39 | Plerixafor + G-CSF as chemosensitization in relapsed/refractory AML |
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | Completed | 52 | AMD3100 (plerixafor) + mitoxantrone, etoposide, cytarabine in relapsed/refractory AML |
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | Completed | 71 | Decitabine + plerixafor priming in AML patients ≥60 years |
| [NCT00990054](https://clinicaltrials.gov/study/NCT00990054) | Phase 1 | Completed | 36 | Dose escalation of plerixafor with cytarabine + daunorubicin ("7+3") in newly diagnosed AML |
| [NCT01435343](https://clinicaltrials.gov/study/NCT01435343) | Phase 1/2 | Completed | 55 | Fludarabine, idarubicin, cytarabine, G-CSF + plerixafor in relapsed/refractory AML, age ≤65 |
| [NCT01319864](https://clinicaltrials.gov/study/NCT01319864) | Phase 1 | Completed | 20 | Pediatric safety study of plerixafor with cytarabine + etoposide in relapsed acute leukemia/MDS |
| [NCT01068301](https://clinicaltrials.gov/study/NCT01068301) | Phase 1 | Completed | 12 | Pediatric plerixafor-containing regimen for second allogeneic transplant |
| [NCT06141304](https://clinicaltrials.gov/study/NCT06141304) | Phase 2 | Unknown | 28 | Plerixafor + donor lymphocyte infusion for relapsed acute leukemia after transplant |

---

## Literature Evidence

For indolent plasma cell myeloma: currently no related literature available.

For myeloid leukemia (up to 10 most relevant of 20 publications):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [22308295](https://pubmed.ncbi.nlm.nih.gov/22308295/) | 2012 | Phase 1/2 trial | Blood | Chemosensitization with plerixafor in 52 patients with relapsed/refractory AML |
| [28282031](https://pubmed.ncbi.nlm.nih.gov/28282031/) | 2017 | Phase 1/2 trial | Blood Cancer J | Follow-up study of plerixafor + G-CSF chemosensitization in relapsed/refractory AML |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Phase 1 trial | Haematologica | Decitabine + escalating plerixafor in 69 older patients with newly diagnosed AML |
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Phase 1/2 trial | Ann Hematol | PLERIFLAG: FLAG-Ida + high-dose IV plerixafor in early-relapsed/refractory AML |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Phase 1 trial | Am J Hematol | Sorafenib + G-CSF + plerixafor in 28 patients with relapsed/refractory FLT3-ITD AML |
| [30654137](https://pubmed.ncbi.nlm.nih.gov/30654137/) | 2019 | Phase 1 trial | Biol Blood Marrow Transplant | Safety and tolerability of plerixafor with myeloablative conditioning before allograft in AML |
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | Systematic review / meta-analysis | Leuk Res | Plerixafor with chemotherapy and/or transplant in acute leukemia, covering preclinical and clinical studies |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Review | Leukemia | CXCL12-CXCR4 axis as a therapeutic target in AML |
| [31112940](https://pubmed.ncbi.nlm.nih.gov/31112940/) | 2019 | Proteomic study | Acta Haematol | Signalling changes with G-CSF/plerixafor/Bu-Flu conditioning in AML patients |
| [30150522](https://pubmed.ncbi.nlm.nih.gov/30150522/) | 2018 | Case report | Cancers | Complete remission in a 4-year-old with refractory AML after a plerixafor, cytarabine and melphalan conditioning regimen |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2529815 | PLERIXAFOR INJECTION |
| 2539454 | PLERIXAFOR INJECTION |

The records provided do not include dosage form, manufacturer or approved indication text for these licences.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (indolent plasma cell myeloma) rests on model score alone (L5), with no trials or literature. The mechanistic link is plausible but untested, and plerixafor's established myeloma use is mobilization, not treatment. The better-supported direction is myeloid leukemia (L2, early-phase combination studies), but efficacy is unproven and many trials are mobilization-focused.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indication), which currently blocks safety screening
- Mechanism of action data from DrugBank
- A targeted search for preclinical or clinical evidence on plerixafor in indolent plasma cell myeloma
- Re-evaluation of myeloid leukemia as the lead indication, with confirmation that the trial and literature evidence is anti-leukemic rather than mobilization-only
- Resolution of the ambiguous "CMM7" label, and a check on whether the bronchitis prediction is a knowledge-graph artifact

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

