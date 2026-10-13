---
layout: default
title: Enoxaparin
parent: Model Prediction Only (L5)
nav_order: 330
evidence_level: L5
indication_count: 1
---

# Enoxaparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Enoxaparin: From Pulmonary Embolism and Disseminated Intravascular Coagulation to Protein C Deficiency Thrombophilia

## One-Sentence Summary

Enoxaparin is a low-molecular-weight heparin originally used for conditions of excessive clotting, including pulmonary embolism, disseminated intravascular coagulation (DIC) and purpura fulminans.
The TxGNN model predicts it may be useful for **autosomal recessive thrombophilia due to protein C deficiency**,
but **no clinical trials and no publications** have been identified for this specific indication, so the prediction rests on mechanistic reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans, acquired purpura fulminans (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (no trials or literature; the data compiled for this report labels it L4 on the basis of mechanistic reasoning, but no preclinical or mechanism studies were actually found) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. The following explanation is based on general pharmacological knowledge. Enoxaparin enhances the activity of antithrombin III, which mainly inhibits factor Xa and, to a lesser degree, thrombin.

In severe (homozygous or compound heterozygous) protein C deficiency, the body's natural protein C anticoagulant pathway is impaired. This pathway normally switches off factors Va and VIIIa. Without it, thrombin generation goes unchecked, which can cause thrombosis and neonatal purpura fulminans. Enoxaparin works through a separate, antithrombin-dependent pathway, so it could in principle make up for the missing anticoagulant activity.

The original indications (pulmonary embolism, DIC, purpura fulminans) share this underlying problem of uncontrolled clotting. The model's high score likely reflects this closeness in the knowledge graph. However, this is a computational prediction supported by mechanistic reasoning. It is not direct clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Twenty valid single-ingredient licences are on record. Dosage form and approved indication text are not available for any of them. The five main entries are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242692 | LOVENOX HP | Not available | Not available |
| 02378469 | LOVENOX HP | Not available | Not available |
| 02507536 | INCLUNOX | Not available | Not available |
| 02506483 | NOROMBY | Not available | Not available |
| 02509083 | REDESCA | Not available | Not available |

The remaining licences are for other brands of the same drug: AXBERI, ELONOX, INCLUNOX HP, NOROMBY HP, REDESCA HP and further strengths.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for the official safety information.

- **Contraindication-related conditions from the knowledge graph** (these come from a computational drug-disease network, not from label text): 
  - Bleeding or bleeding-risk conditions: intracranial or intracerebral haemorrhage, placental abruption, haemophilia, blood coagulation disease, Glanzmann thrombasthenia, qualitative platelet defect
  - Platelet and blood disorders: thrombocytopenia, heparin-induced thrombocytopenia, haematologic disease, antithrombin III deficiency
  - Gastrointestinal and liver or biliary conditions: active peptic ulcer disease, ulcerative colitis, inflammatory bowel disease, liver failure, biliary tract disease, obstructive jaundice
  - Eye and vascular conditions: diabetic retinopathy, hypertensive retinopathy, diabetic cataract, retinal disease, retinitis, arteriosclerosis obliterans
  - Infection and bone: infective endocarditis (including subacute bacterial endocarditis), osteoporosis, postmenopausal osteoporosis

- **Drug interactions**: A total of 100 interactions were found. Examples of major-level interactions:
  - Antiplatelet and anti-inflammatory drugs: acetylsalicylic acid, ibuprofen, ketorolac, abciximab
  - Thrombolytic: alteplase
  - Other: deferasirox, acalabrutinib, trastuzumab emtansine, radioimmunotherapies (ibritumomab tiuxetan, tositumomab)

  Moderate-level examples include fenfluramine, dexfenfluramine, sibutramine, aliskiren, sugammadex, radioactive iodide, and topical diclofenac.

For this particular indication, the bleeding-related items above matter because the patients are often neonates or have severe clotting disorders. The anticoagulant effect would also add to that of the interacting drugs listed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high and the mechanism is plausible, but there are no clinical trials or publications for this indication. Package insert safety data is also missing. The case currently remains a research question rather than a candidate for action.

**To proceed, the following is needed:**
- A systematic literature search on low-molecular-weight heparin in severe protein C deficiency, including case reports and the neonatal purpura fulminans setting
- Comparison with established treatments for this condition, such as protein C concentrate and warfarin
- Official mechanism-of-action data from DrugBank
- Health Canada package insert warnings and contraindications, together with dosage form and approved indication text for the licences
- A bleeding-risk and dosing assessment for neonatal and paediatric patients
- Confirmation of whether the available product forms suit the intended route and population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

