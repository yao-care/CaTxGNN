---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 364
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a progestin used in hormonal contraceptives (the Nexplanon implant and vaginal rings such as NuvaRing). The TxGNN model predicts it may be effective for **amenorrhea**, but this is most likely a drug-effect association rather than a treatment use. Only **1 clinical trial** and **2 publications** were retrieved, and none tests amenorrhea as a treatment target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Contraception (inferred from the product names and the retrieved trial; the licence indication text was not provided) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 (the pack lists L4, but no preclinical or mechanistic study was retrieved, so L5 fits the level rules) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Etonogestrel is a progestin that suppresses ovulation and thins the endometrium. Its efficacy in contraception is well established.

The link to amenorrhea is weak. Amenorrhea and altered bleeding patterns are well-known effects of the implant. The high TxGNN score most likely reflects this class-level drug-phenotype association rather than a therapeutic use. Using an ovulation-suppressing implant to treat amenorrhea is mechanistically counterintuitive, and no evidence supports it as a treatment.

The original indication and mechanism data are also missing, so the prediction could not be cross-checked.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Open-label, single-arm study of contraceptive efficacy and safety of the etonogestrel implant (MK-8415) in years 4-5 of use, in females 35 or younger. Amenorrhea is not a treatment target and would appear only as a bleeding-pattern or safety outcome. |

The single-arm design and the different endpoint mean this cannot count as direct Phase 3 RCT evidence for the predicted indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Randomized multicenter study (n=200, China) comparing the single-rod implant (Implanon) with the six-capsule Norplant implant. No pregnancies occurred. Bleeding patterns were compared, but this is contraceptive efficacy and tolerability, not amenorrhea treatment. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT protocol | Trials | Protocol for BIO101 in COVID-19 pneumonia. Unrelated to etonogestrel or amenorrhea; likely a retrieval artifact. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2499509 | NEXPLANON |
| 2253186 | NUVARING |
| 2520028 | HALOETTE |

Dosage form and approved indication text were not provided for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. The one completed Phase 3 trial is a single-arm contraceptive study that does not test amenorrhea as a treatment target. Amenorrhea is a known effect of the drug, so a therapeutic use is mechanistically counterintuitive.

The other predicted indications (breast fibrocystic disease, blunt duct adenosis, apocrine adenosis, benign mammary dysplasia) are also L5. They have no retrieved trials or literature and are largely duplicates of one another through the knowledge graph.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (DrugBank) and the original indication text for each authorization
- Evidence that etonogestrel treats amenorrhea, rather than causing it, before any further evaluation
- Confirmation that the amenorrhea prediction is not simply a drug-effect association
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

