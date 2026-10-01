---
layout: default
title: Atezolizumab
parent: Model Prediction Only (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Atezolizumab
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

# Atezolizumab: From PD-L1 Checkpoint Inhibitor to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab is a PD-L1-blocking antibody marketed in Canada as TECENTRIQ.
The TxGNN model predicts it may be effective for **prostatic urethra urothelial carcinoma**.
Support is indirect: **2 clinical trials** in related urothelial settings and **0 publications** specific to this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Prostatic urethra urothelial carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 (per the Evidence Pack; the supporting Phase 2 trial is single-arm, not randomized, and enrolled bladder rather than prostatic urethra patients) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Atezolizumab is a PD-L1 inhibitor, which is an immune checkpoint blockade approach. Blocking PD-L1 may help the immune system attack tumour cells.

Urothelial carcinoma of the prostatic urethra has the same histology as bladder urothelial carcinoma and shares its PD-1/PD-L1 axis biology, so checkpoint blockade is plausible. The main supporting trial enrolled patients with non-muscle invasive bladder cancer, not prostatic urethra disease. Extrapolation is therefore indirect, and the high TxGNN score is a prediction only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Single-arm trial of atezolizumab in BCG-unresponsive non-muscle invasive bladder cancer. Same tumour type (urothelial carcinoma) but a different anatomic site. Strongest clinical signal available (relevance grade B). |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 | Active, not recruiting | 914 | Phase 1b dose escalation of cabozantinib alone or with atezolizumab in multiple advanced solid tumours, including urothelial carcinoma of the urethra. No defined prostatic urethra cohort. Supports safety and combination feasibility only (relevance grade C). |

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2462990 | TECENTRIQ |
| 2492393 | TECENTRIQ |
| 2546310 | TECENTRIQ SC |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-L1 antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only relevant efficacy signal is a single-arm Phase 2 trial in bladder cancer, not prostatic urethra disease. There is no specific literature, and safety information from the Canadian package insert has not yet been reviewed. The other nine predicted indications have weaker evidence: Phase 1 data only for renal pelvis papillary urothelial carcinoma, one indirect review for endocervical carcinoma, and none for the rest. They are not more advanced candidates.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap for safety screening)
- Detailed mechanism of action data (from DrugBank)
- Approved indication text for the three Canadian licences
- Evidence specific to prostatic urethra or upper-tract urothelial carcinoma, for example subgroup analyses of bladder urothelial trials
- Route and formulation compatibility assessment (intravenous vs. subcutaneous)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

