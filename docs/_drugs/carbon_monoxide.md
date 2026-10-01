---
layout: default
title: Carbon Monoxide
parent: Model Prediction Only (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Carbon Monoxide
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

# Carbon Monoxide: From Lung Diffusion Test Gas to Sclerosing Cholangitis

## One-Sentence Summary

Carbon monoxide (CO) is marketed in Canada only as components of gas mixtures whose product names indicate lung diffusion testing. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model's graph-based score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the regulatory data. Product names suggest diagnostic lung diffusion testing (inferred) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug. CO is not a conventional therapeutic drug in Canada. The listed products are multi-gas mixtures (CO with helium, neon, oxygen and nitrogen) whose names point to lung diffusion testing rather than treatment.

The only plausible link is speculative. The body produces CO through the heme oxygenase-1 (HO-1) pathway, and this pathway has anti-inflammatory and cytoprotective effects. This could in theory apply to inflammatory bile duct disease. However, no trials or publications retrieved for this indication support the idea. The 99.75% score reflects proximity in the knowledge graph, not clinical validation.

Inhaled CO is also toxic because it forms carboxyhemoglobin and reduces oxygen delivery. Any therapeutic use would need strict dose control.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for sclerosing cholangitis.

---

## Literature Evidence

Currently no related literature available for sclerosing cholangitis.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2154773 | CO-HE-O2-N2 MIXTURE |
| 2014424 | CARBON MONOX, HELIUM, OXYGEN, NITROGEN L.D.M. |
| 2182238 | CO-NE-O2-N2 MIXTURE |
| 588075 | LUNG DIFFUSION TEST MIX NO NE CO |

Dosage form and approved indication text are not available in the source data.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found for this drug.

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no supporting trials or literature. CO's known toxicity and the absence of a therapeutic product in Canada argue against advancing it for sclerosing cholangitis.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data (for example, from DrugBank)
- Preclinical evidence that CO or CO-releasing molecules affect cholangiopathy models
- A clear route, dose and delivery approach that addresses carboxyhemoglobin toxicity

**Other candidates worth a look:**
The pulmonary hypertension prediction (score 99.15%) has more support at L4, rated "Research Question". It rests on preclinical work (for example PMID 16908624, CO reversing established pulmonary hypertension) and a small phase 1 inhaled-CO neonatal trial (NCT01818843, status unknown, 24 participants). Most other retrieved records concern DLCO as a diagnostic test, not CO as a therapy. The ventricular tachycardia and glaucoma hits point toward harm, not benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

