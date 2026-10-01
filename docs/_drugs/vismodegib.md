---
layout: default
title: Vismodegib
parent: Model Prediction Only (L5)
nav_order: 972
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: From Advanced Basal Cell Carcinoma to Medulloblastoma with Extensive Nodularity

## One-Sentence Summary

Vismodegib (Erivedge) is an oral Hedgehog pathway inhibitor used for advanced basal cell carcinoma (BCC). This original indication comes from the supporting literature, because the Health Canada record in the pack is blank.
The TxGNN model predicts it may be effective for **medulloblastoma with extensive nodularity**, but **0 clinical trials** and **0 publications** currently support this specific prediction, so it remains a model-only hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced basal cell carcinoma (from literature; not stated in the Canadian licence record) |
| Predicted New Indication | Medulloblastoma with extensive nodularity |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vismodegib blocks Smoothened (SMO), a key signalling protein in the Hedgehog pathway. Detailed mechanism data are not in the Evidence Pack, but the SMO mechanism is well described in the literature. Over-active Hedgehog signalling drives BCC, and vismodegib was approved on that basis.

Medulloblastoma with extensive nodularity is typically of the SHH (Sonic Hedgehog) molecular subgroup. Both diseases depend on the same pathway, so the prediction is mechanistically plausible.

There is an important caveat. SMO-inhibitor response in medulloblastoma depends on SHH-subgroup status and on mutations downstream of SMO, such as SUFU. A tumour with a downstream mutation would not be expected to respond. The prediction therefore cannot be advanced without tumour molecular profiling.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Other Predicted Candidates Worth Noting

Only the top-ranked candidate is evaluated above. The pack shows that other predictions have more support:

| Predicted Indication | Evidence Level | Support in Pack | Pack Recommendation |
|------|------|------|------|
| Skin cancer (mainly BCC) | L2 | 20 trials (including [NCT01815840](https://clinicaltrials.gov/study/NCT01815840), randomized phase 2, n=229) and 20 publications (including [PMID 22670903](https://pubmed.ncbi.nlm.nih.gov/22670903/), NEJM 2012) | Proceed with Guardrails |
| Xeroderma pigmentosum | L4 | 5 publications, mostly case reports of vismodegib treating BCC in XP patients | Research Question |

- **Skin cancer:** There is no Phase 3 RCT, hence L2. This is probably an on-label use rather than true repurposing, and should be verified against the labeling.
- **Xeroderma pigmentosum:** The benefit is indirect. Vismodegib treats the BCC tumours, not the underlying DNA-repair defect.
- **Remaining candidates:** The seven lower-ranked candidates (annular epidermolytic ichthyosis, epidermolysis bullosa simplex with mottled pigmentation, prostate cancer/brain cancer susceptibility, Brenner tumor, cutaneous adenocystic carcinoma, prostate leiomyoma, benign neoplasm of sweat gland) have no evidence and are on Hold. Their high scores are likely graph-proximity artifacts.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2409267 | ERIVEDGE |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Hedgehog/SMO pathway inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Teratogenicity:** The pack's rationale for the BCC indication lists teratogenicity as a known risk requiring guardrails.

Please refer to the package insert for other safety information. No drug interactions were found in the pack's DDI query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, but there are no trials or publications for this indication, and the evidence level is L5 (model prediction only). Response depends on SHH-subgroup status and downstream mutations, which cannot be assessed from the current data.

**To proceed, the following is needed:**
- A targeted literature search on SMO inhibitors in SHH-subgroup medulloblastoma, including the nodular subtype
- Tumour molecular profiling criteria (SHH subgroup; exclusion of SUFU and other downstream mutations)
- The Health Canada package insert (warnings, contraindications, original indication)
- Mechanism of action data from DrugBank
- Separately, a labeling check for the skin cancer (BCC) candidate, which has the strongest evidence in this pack

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

