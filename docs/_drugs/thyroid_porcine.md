---
layout: default
title: Thyroid Porcine
parent: Model Prediction Only (L5)
nav_order: 910
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Thyroid Porcine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the available licence data"
---

# Thyroid Porcine
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

# Thyroid, porcine: From Thyroid Hormone Replacement to Migraine Disorder

## One-Sentence Summary

Porcine thyroid is a natural thyroid hormone preparation (containing T3/T4) that is marketed in Canada under three licences. The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, porcine thyroid is a source of exogenous thyroid hormones (T3/T4) and is used to replace deficient thyroid hormone. Its mechanistic link to migraine is therefore indirect.

The only plausible connection is epidemiological: hypothyroidism has been reported as a comorbidity or risk factor for migraine and other headache disorders. Correcting thyroid deficiency might help in that subgroup, but no trial or publication in the data compiled for this report supports this. The high score (0.999) is a model-based prediction and likely reflects proximity in the knowledge graph.

Other top predictions show the same pattern:

- **Migraine with brainstem aura** and **migraine with or without aura, susceptibility to**: these inherit the general migraine prediction. The second is a genetic susceptibility entry rather than a treatable condition.
- **Raynaud disease** (99.45%): hypothyroidism can cause cold intolerance and vasospasm, but the link is indirect.
- **Atrophoderma vermiculata** and **ulerythema ophryogenesis**: rare follicular skin disorders with no plausible thyroid hormone mechanism. These appear to be knowledge-graph artifacts.
- **Prinzmetal angina** (99.10%): thyroid hormone raises heart rate, oxygen demand and adrenergic sensitivity, so it could worsen coronary vasospasm. This is a safety concern.
- **Sciatic neuropathy** and **lesion of sciatic nerve**: hypothyroidism can contribute to neuropathy, and preclinical work suggests a role for thyroid hormone in nerve myelination and regeneration, but there is no clinical evidence.
- **Hyperthyroidism** (98.18%): pharmacologically implausible and contraindicated, since exogenous T3/T4 would worsen it or cause thyrotoxicosis. It is most likely a model artifact and should not be pursued.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00023949 | THYROID | Not stated | Not stated |
| 00023957 | THYROID | Not stated | Not stated |
| 00023965 | THYROID | Not stated | Not stated |

## Safety Considerations

- **Drug Interactions**: The interaction screening found 99 interacting drugs. The 20 listed in the data are all rated Moderate. They include:
  - Antidiabetic agents: acarbose, metformin, pioglitazone, alogliptin, albiglutide, dulaglutide, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide and acetohexamide
  - Acid-suppressing drugs: omeprazole, rabeprazole and dexlansoprazole
  - Minerals and antacids: calcium phosphate, calcium acetate and magnesium oxide
  - Sympathomimetic agents: epinephrine, isometheptene and diethylpropion
- **Disease-specific cautions** (from the mechanistic review above):
  - Hyperthyroidism: exogenous thyroid hormone is contraindicated.
  - Coronary vasospasm and ischaemic disease: thyroid hormone may worsen these and needs careful dosing.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions are supported by model output only, with no clinical trials or publications (Evidence Level L5). The migraine link is indirect, and several other predictions are implausible or carry safety concerns (hyperthyroidism, Prinzmetal angina).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication, dosage form and manufacturer details for the three licences
- Mechanism of action data
- A literature and trial search on thyroid status and migraine, to test whether any benefit is limited to patients with hypothyroidism
- A cardiovascular and drug-interaction risk assessment before any new-indication study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

