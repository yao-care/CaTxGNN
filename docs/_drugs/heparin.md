---
layout: default
title: Heparin
parent: Model Prediction Only (L5)
nav_order: 449
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Heparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
monitor_inn: "HEPARIN"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
---

# Heparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Heparin: From Pulmonary Embolism to Thrombophilia Due to Protein C Deficiency

## One-Sentence Summary

Heparin is an injectable anticoagulant originally used for pulmonary embolism, disseminated intravascular coagulation and purpura fulminans.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency (autosomal recessive)**,
but **no clinical trials and no publications** currently support this specific direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans, acquired purpura fulminans (licence indication text is not available in the data compiled for this report) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacological knowledge, heparin enhances antithrombin-mediated inhibition of thrombin and factor Xa, which reduces clot formation.

Protein C deficiency removes a natural brake on coagulation, leaving patients prone to thrombosis. Heparin's anticoagulant action could plausibly offset this hypercoagulable state. This is consistent with its existing use in purpura fulminans, a severe manifestation of homozygous or severe protein C deficiency.

However, this link is theoretical. No trials or publications for this indication were found. Standard care (protein C concentrate, with anticoagulation as a bridge or adjunct) was not assessed in the data, so no conclusion about added benefit can be drawn. The high score is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication (protein C deficiency).

For context, the second-ranked prediction (primary release disorder of platelets, score 99.06%) returned 20 publications, but they are tangential (heparin-induced thrombocytopenia, cirrhosis coagulation, cancer-associated VTE) and none evaluates heparin as a treatment for that condition. The mechanism there is arguably contradictory: heparin would be expected to worsen, not treat, a bleeding-prone platelet function defect. This second prediction is not recommended for pursuit.

## Canada Market Information

Heparin is marketed in Canada as single-ingredient injectables. Dosage form and approved indication text are not available in the compiled data. Five of the 14 authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 02456958 | Heparin Sodium Injection USP |
| 00727520 | Heparin Leo 100 unit/mL |
| 00453811 | Heparin Leo Inj 1000 unit/mL |
| 02303086 | Heparin Sodium Injection USP (multidose vial with preservative) |
| 01990748 | Heparin Sodium in 0.9% Sodium Chloride Injection |

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for authoritative safety information.

- **Contraindications suggested by the knowledge graph (not label text):** liver failure, thrombocytopenia (including heparin-induced thrombocytopenia), haemophilia and other blood coagulation diseases, antithrombin III deficiency, intracranial or intracerebral haemorrhage, active peptic ulcer disease, ulcerative colitis and inflammatory bowel disease, infective endocarditis, retinal disease (including diabetic and hypertensive retinopathy), placental abruption, Glanzmann thrombasthenia and qualitative platelet defects, osteoporosis, biliary tract disease and obstructive jaundice.
- **Drug interactions:** 100 interactions were identified. Moderate-level interactions listed include acetylsalicylic acid (aspirin), several sulfonylurea and glinide antidiabetics (chlorpropamide, glimepiride, glipizide, glyburide, tolbutamide, tolazamide, acetohexamide, repaglinide, nateglinide), and the weight-loss agents fenfluramine, dexfenfluramine and sibutramine. Others (e.g., levocarnitine, mannitol, calcitriol, vitamin A, pantoprazole, mesalazine, doxycycline) have an unknown severity level.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible and aligns with heparin's existing use in purpura fulminans. However, it has no clinical trials or literature behind it (L5), and the established standard of care for protein C deficiency was not evaluated.

**To proceed, the following is needed:**
- A targeted literature and trial search on heparin in severe congenital protein C deficiency and purpura fulminans
- Comparison with standard care (protein C concentrate, warfarin or other anticoagulation)
- Mechanism of action data and Health Canada package insert warnings and contraindications
- Review of the bleeding-risk profile and the knowledge-graph contraindications in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

