---
layout: default
title: Hexaminolevulinate
parent: Model Prediction Only (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Hexaminolevulinate
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

# Hexaminolevulinate: From Bladder Cancer Detection to Bronchitis

## One-Sentence Summary

Hexaminolevulinate (marketed in Canada as CYSVIEW) is a photodiagnostic agent used for blue-light cystoscopy in bladder cancer.
The TxGNN model's top-ranked prediction is **bronchitis**, but **no clinical trials and no publications** support it, and no plausible mechanism links the drug to it.
The best-supported prediction is actually **colonic neoplasm** (rank 2), as a diagnostic imaging use backed by **3 early-phase trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Blue-light cystoscopy for bladder cancer (the licence indication text on file is empty; this comes from the drug's established use) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Hexaminolevulinate is a photodiagnostic prodrug. It is converted to protoporphyrin IX, which accumulates preferentially in neoplastic tissue and glows red under blue light. This selective fluorescence is what makes tumours easier to see during cystoscopy.

**For bronchitis, the prediction is not mechanistically supported.** Bronchitis is an inflammatory airway disease, and the drug's tumour-selective fluorescence has no evident relevance to it. The high score (0.991) is a model output only, with no trials or literature behind it.

**The more credible prediction is colonic neoplasm (rank 2, score 98.64%).** Protoporphyrin IX accumulation in neoplastic epithelium should also apply in the colon. This would be a diagnostic imaging use (fluorescence endoscopy), not a therapeutic one.

Other predictions in the top 10:
- **Indirect support, worth exploring:** cecum villous adenoma and rectosigmoid junction neoplasm are colonic epithelial lesions covered by the same fluorescence-imaging approach. No site-specific study exists.
- **Likely model artifacts:** severe nonproliferative diabetic retinopathy, cecum neuroendocrine tumor G1, colonic lymphangioma, lipoma of colon, cecal disease and cavernous hemangioma of colon. These are non-epithelial or benign non-neoplastic conditions with no supporting evidence.

---

## Clinical Trial Evidence

**Bronchitis (top prediction):** Currently no related clinical trials registered.

**Colonic neoplasm (best-supported alternative, rank 2):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00285701](https://clinicaltrials.gov/study/NCT00285701) | Phase 1/2 | Completed | 38 | Dose-finding study of fluorescence endoscopy with local and oral hexaminolevulinate for early detection of pre-malignant and malignant colon conditions; the strongest and most direct evidence, but early-phase and diagnostic |
| [NCT01344902](https://clinicaltrials.gov/study/NCT01344902) | Phase 1/2 | Terminated | 13 | Open dose-finding study of oral hexaminolevulinate imaging in patients with suspected or high-risk colon neoplasia; ended early, so evidence on safety and feasibility is limited |
| [NCT03272659](https://clinicaltrials.gov/study/NCT03272659) | Phase 2 | Withdrawn | 0 | Pilot study correlating fluorescence with colorectal cancer specimen pathology using an HAL enema; withdrawn with no participants, so it yields no data |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2436639 | CYSVIEW |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, bronchitis, is supported only by the model score (L5), with no trials, no literature and no mechanistic link. The colonic neoplasm prediction is biologically coherent and has some early-phase trial activity, but none of it is randomized or Phase 3, so it is best treated as a research question, not a go decision. Blocking safety data is also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For colonic neoplasm: published results from the completed Phase 1/2 study (NCT00285701) and any larger, controlled diagnostic-accuracy studies
- Confirmation of the dosage form, route and approved indication text for the Canadian licence, since route compatibility with colonic use (enema or oral) is still pending
- Drop bronchitis, diabetic retinopathy and the other non-neoplastic predictions from further evaluation unless new evidence appears
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

