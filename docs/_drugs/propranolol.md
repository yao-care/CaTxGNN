---
layout: default
title: Propranolol
parent: Model Prediction Only (L5)
nav_order: 771
evidence_level: L5
indication_count: 6
---

# Propranolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Propranolol: From Established Beta-Blocker Use to Distal Myopathy, Tateyama Type

## One-Sentence Summary

Propranolol is a non-selective beta-blocker marketed in Canada, but the available licence records do not state its approved indications.
The TxGNN model predicts it may be effective for **distal myopathy, Tateyama type**, a rare muscle disease.
No clinical trials or publications currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available Canadian licence records |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 13 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Propranolol is a non-selective beta-adrenergic blocker, and it is widely marketed in Canada, including long-acting products.

For this specific prediction, the data do not support a mechanistic link. Beta-adrenergic blockade has no established connection to distal myopathy, Tateyama type. The high score most likely reflects proximity in the knowledge graph rather than a demonstrated biological rationale, so it should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications for Propranolol

Several lower-ranked predictions have more supporting evidence than the top-ranked one:

| Predicted Indication | TxGNN Score | Evidence Level | Evidence Summary | Recommendation |
|------|------|------|------|------|
| Cardiomyopathy | 99.12% | L2 | 3 registered trials (none testing efficacy) and about 20 publications, including a 1973 double-blind trial in hypertrophic cardiomyopathy ([PMID 4586631](https://pubmed.ncbi.nlm.nih.gov/4586631/)) | Proceed with Guardrails |
| Cirrhotic cardiomyopathy | 99.12% | L4 | 5 publications. One reports propranolol correcting prolonged QT in cirrhosis ([PMID 38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/)). Others raise safety concerns in advanced cirrhosis | Research Question |
| Congenital myopathy with excess of thin filaments | 99.30% | L5 | None | Hold |
| Hypertrophic cardiomyopathy due to intensive athletic training | 99.17% | L5 | None | Hold |
| Chondroma | 99.14% | L5 | None | Hold |

Key points on the cardiomyopathy signal:
- The support is mainly for hypertrophic obstructive cardiomyopathy and is subtype-specific.
- The trials found are deprescribing studies or address another condition.
- Beta-blockers may be poorly tolerated in transthyretin amyloid cardiomyopathy.
- Beta-blocker use in HCM may already be standard care, which limits repurposing novelty.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2491893 | LUPIN-PROPRANOLOL LA | Not listed | Not listed |
| 2491915 | LUPIN-PROPRANOLOL LA | Not listed | Not listed |
| 2550830 | PRZ-PROPRANOLOL | Not listed | Not listed |
| 2491907 | LUPIN-PROPRANOLOL LA | Not listed | Not listed |
| 740675 | TEVA-PROPRANOLOL | Not listed | Not listed |

These are 5 of the 13 authorisations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for distal myopathy, Tateyama type has no registered trials, no literature, and no plausible mechanistic link, so the evidence is model-only (L5). Among propranolol's other predicted indications, only cardiomyopathy reaches L2, and it should be limited to hypertrophic obstructive cardiomyopathy.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian licences
- Any disease-specific evidence for distal myopathy, Tateyama type, such as case series or preclinical data
- If advancing the cardiomyopathy candidate instead, a subtype-restricted review of HOCM evidence, with monitoring for bradycardia, hypotension and decompensation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

