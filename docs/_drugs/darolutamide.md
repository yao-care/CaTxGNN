---
layout: default
title: Darolutamide
parent: Model Prediction Only (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Darolutamide
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

# Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Darolutamide is an androgen receptor (AR) antagonist marketed in Canada as NUBEQA, used in prostate cancer.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)** with a high score, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on the model output alone, so we recommend holding it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (based on general drug knowledge; the Canadian label indication text was not supplied) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Darolutamide is an androgen receptor antagonist, and its efficacy in prostate cancer is established through that mechanism.

We could not find a mechanistic link to HoFH. HoFH is caused by loss-of-function variants in LDLR, APOB, PCSK9 or LDLRAP1, which impair LDL cholesterol clearance, and AR antagonism does not act on these pathways. Androgen deprivation is known to shift lipid profiles in prostate cancer patients, but this is an adverse metabolic effect, not a therapeutic one.

The high score (0.991, rank 14,849) is best read as a knowledge-graph proximity signal. No trial or publication supports it, so the prediction has not been validated.

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
| 2496348 | NUBEQA |

Dosage form and approved indication text were not supplied for this license.

---

## Cytotoxicity

Darolutamide is treated as an antineoplastic drug because its original indication is a cancer.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (androgen receptor antagonist), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were retrieved for this drug.

One point relevant to this prediction: androgen-pathway inhibition in prostate cancer is generally associated with cardiovascular and thromboembolic risk. For a lipid disorder such as HoFH, that concern would need to be addressed as a safety question.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HoFH prediction has no clinical trials, no literature and no plausible mechanistic link, so it stands at L5 (model prediction only). The other nine predicted indications also carry a Hold recommendation. The only trial found among them was a terminated Phase 1 platform study (NCT03878524, 2 participants, multiple endocrine neoplasia), which is not specific to darolutamide.

**To proceed, the following is needed:**
- The Health Canada package insert, for warnings, contraindications and the approved indication text
- Mechanism of action data for darolutamide (for example from DrugBank)
- Preclinical or mechanistic evidence showing that AR antagonism can affect LDL metabolism in HoFH
- A cardiovascular and lipid safety assessment, given the known metabolic effects of androgen-pathway inhibition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

