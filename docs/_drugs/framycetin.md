---
layout: default
title: Framycetin
parent: Model Prediction Only (L5)
nav_order: 414
evidence_level: L5
indication_count: 7
---

# Framycetin
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

# Framycetin: From Aminoglycoside Antibacterial to Sclerosing Cholangitis

## One-Sentence Summary

Framycetin (neomycin B) is a poorly absorbed aminoglycoside antibiotic, and it is marketed in Canada in nasal, ointment and suppository products.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

The approved indication text is not available in the Canadian licence records, so the original indication is not listed here.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Framycetin is an aminoglycoside antibacterial (neomycin B) with minimal systemic absorption when given topically or orally. Its antibacterial activity is established, but no mechanism specific to sclerosing cholangitis is documented.

The only conceivable link is a gut-microbiome or enteric-antibacterial hypothesis. Under it, reducing gut bacterial load could influence a bile-duct inflammatory disease. Nothing in the supplied data tests or supports this. The 99.66% score is a graph-based prediction, and the link cannot be verified with the information available.

The other predicted indications are also unsupported:
- **Urinary tract infection** (99.42%): plausible at the aminoglycoside class level, but framycetin's urinary exposure is doubtful. The one retrieved paper (PMID 816047, 1976) concerns Actihaemyl in chronic bladder inflammation and does not appear to study framycetin.
- **Congenital prothrombin deficiency** (99.41%): no plausible pharmacological mechanism, so this is likely a graph artifact.
- **Ureaplasma urethritis, gonococcal urethritis, uterine inflammatory disease and xanthogranulomatous pyelonephritis** (99.17–99.28%): class-level plausibility at most, with no supplied clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2224860 | SOFRAMYCIN NASAL SPRAY |
| 2224623 | SOFRACORT |
| 2247322 | PROCTOL OINTMENT |
| 2226383 | TEVA-PROCTOSONE |
| 2247882 | PROCTOL SUPPOSITORIES |

Dosage form and approved indication text were not provided in the licence records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no clinical trials, no literature and no verified mechanism (Evidence Level L5). Framycetin's poor systemic absorption also makes a therapeutic role in a hepatobiliary disease hard to justify without supporting data.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are needed before any safety screening
- Mechanism of action data, for example from DrugBank
- A targeted literature search on framycetin or neomycin in sclerosing cholangitis and the gut-liver axis
- A check of ClinicalTrials.gov and ICTRP for related trials
- Approved indication text and dosage forms for the five Canadian DINs, so route compatibility can be assessed

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

