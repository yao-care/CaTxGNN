---
layout: default
title: Anifrolumab
parent: Model Prediction Only (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Anifrolumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: The Canadian licence record contains no indication text. Publicly kno…"
---

# Anifrolumab
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

# Anifrolumab: From Systemic Lupus Erythematosus to Diabetic Cataract

## One-Sentence Summary

Anifrolumab (SAPHNELO) is a monoclonal antibody that blocks the type I interferon receptor. It is known to have been developed for systemic lupus erythematosus (SLE).
The TxGNN model predicts it may be effective for **diabetic cataract**, but there are currently **0 clinical trials** and **0 directly relevant publications** supporting this direction.
The prediction is purely computational and should be treated as a hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | The Canadian licence record contains no indication text. Publicly known indication: moderate to severe SLE in patients receiving standard therapy |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.50% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Anifrolumab is an antibody that targets IFNAR1, the receptor subunit for type I interferons. By blocking this receptor, it dampens interferon-driven immune activation, which is the rationale for its use in SLE. Detailed mechanism-of-action data are not currently available in the data compiled for this report. The description above is based on the target information in the interaction data (IFNAR1).

The link to diabetic cataract is weak. Diabetic cataract is mainly driven by polyol pathway activation, oxidative stress and glycation of lens proteins, none of which is an established interferon-mediated process. The high TxGNN score therefore reflects a computational association only, and no clinical or literature evidence supports it.

Other cataract-type predictions (tetanic, type 2 diabetes-associated, mature, immature, craniostenosis, nuclear senile, cortical and senile cataract) all have scores of about 98.3–98.4% and likewise lack a plausible mechanism. The most biologically plausible predicted indication is **diabetic retinopathy** (score 98.19%), where inflammation is involved and interferon signalling has been speculatively implicated in retinal inflammation. Even there, no trials or literature exist, and preclinical testing would be needed first.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly supports anifrolumab for diabetic cataract. One paper was retrieved for the related prediction "cortical cataract":

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41373894](https://pubmed.ncbi.nlm.nih.gov/41373894/) | 2025 | Review | International Journal of Molecular Sciences | Ophthalmological safety review of emerging and conventional SLE therapies. It addresses ocular adverse effects (such as cataract risk with long-term glucocorticoids), not a therapeutic benefit of anifrolumab for cataract |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02522845 | SAPHNELO | Not listed | Not listed |

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed and returned one pharmacology entry rather than a drug-drug interaction: anifrolumab's target is the interferon α/β receptor 1 (IFNAR1), where it acts as an antibody inhibitor. No clinically graded interactions were reported.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials, no supporting literature and no plausible mechanistic link to diabetic cataract. Cataract is also generally treated surgically, so an intravenous systemic antibody would be a difficult fit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data for anifrolumab
- Preclinical evidence that type I interferon signalling contributes to lens opacification or diabetic eye disease
- If an ocular direction is pursued, prioritise diabetic retinopathy over the cataract predictions, starting with preclinical hypothesis testing
- Assessment of route and formulation compatibility with an ocular indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

