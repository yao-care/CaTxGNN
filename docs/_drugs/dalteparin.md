---
layout: default
title: Dalteparin
parent: Model Prediction Only (L5)
nav_order: 244
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Dalteparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
monitor_inn: "Dalteparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets", "pseudo-von Willebrand disease", "atypical hemolytic-uremic syndrome with thrombomodulin anomaly", "neuropathy, painful"]
---

# Dalteparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dalteparin: Thrombophilia due to Protein C Deficiency, Autosomal Recessive
{: .text-alpha }

## One-Sentence Summary

Dalteparin is a low-molecular-weight heparin, originally used for conditions such as pulmonary embolism, disseminated intravascular coagulation and purpura fulminans.
The TxGNN model predicts it may be useful for **thrombophilia due to protein C deficiency, autosomal recessive**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific indication, so the prediction rests on the model score and mechanistic reasoning alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans (the Canadian licence records contain no approved indication text) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 10 of 10) |
| Number of DINs | 10 (valid: 10) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, dalteparin is a low-molecular-weight heparin that enhances antithrombin activity and inhibits factor Xa. This reduces clot formation.

Severe congenital protein C deficiency leaves the body without a key natural anticoagulant brake, creating a strongly clot-prone state. Purpura fulminans, one of dalteparin's original indications, is closely tied to severe protein C deficiency. Anticoagulation is therefore biologically plausible for this condition.

However, this link rests on the TxGNN prediction and mechanistic reasoning only. The data compiled for this report do not describe standard management of severe congenital protein C deficiency (such as protein C replacement), so dalteparin's role relative to established care cannot be judged.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

Note: one trial was linked to a lower-ranked prediction (painful neuropathy), [NCT00445328](https://clinicaltrials.gov/study/NCT00445328). It is a terminated Phase 4 comparison of dalteparin versus unfractionated heparin for VTE prevention (n=84) and is not relevant to protein C deficiency.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Dalteparin is marketed in Canada as FRAGMIN under 10 valid single-ingredient licences. The records do not include dosage form or approved indication text.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02352672 | FRAGMIN | Not listed | Not listed |
| 02132621 | FRAGMIN | Not listed | Not listed |
| 02231171 | FRAGMIN | Not listed | Not listed |
| 02352656 | FRAGMIN | Not listed | Not listed |
| 02352664 | FRAGMIN | Not listed | Not listed |

---

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):**
These come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. They should be verified against the product monograph. They include:
- Bleeding and coagulation disorders: hemophilia, blood coagulation disease, thrombocytopenia (including heparin-induced), Glanzmann thrombasthenia, qualitative platelet defect, antithrombin III deficiency
- Haemorrhage risk: intracranial and intracerebral haemorrhage, placental abruption, active peptic ulcer disease, ulcerative colitis and inflammatory bowel disease
- Other: liver failure, biliary tract disease, obstructive jaundice, osteoporosis, infective endocarditis, and retinal diseases (diabetic and hypertensive retinopathy, retinitis)

**Drug Interactions:**
The interaction query returned 100 interactions. The first 20 shown include:
- **Major:** acetylsalicylic acid, ibuprofen, ketorolac, fondaparinux, abciximab, acalabrutinib, deferasirox, trastuzumab emtansine, ibritumomab tiuxetan, tositumomab (including I-131)
- **Moderate:** fluvoxamine, fosinopril, sugammadex, fenfluramine, dexfenfluramine, sibutramine, iodide I-123 and I-131, ketorolac (ophthalmic)

Most of the major interactions involve additive bleeding risk with antiplatelet, NSAID or other anticoagulant drugs.

For other predicted indications, anticoagulation could worsen bleeding in platelet-function disorders (primary release disorder of platelets, pseudo-von Willebrand disease). It also requires caution in atypical haemolytic-uremic syndrome because of platelet consumption and renal impairment, which affects LMWH clearance.

Please also refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (0.9988) and a plausible mechanism, but there are no trials or publications for this indication (L5). Package insert safety data and the mechanism of action are missing, so the safety review cannot proceed. Treat this as a research question rather than an actionable candidate.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Detailed mechanism of action data
- A literature review of anticoagulant and LMWH use in severe congenital protein C deficiency and purpura fulminans, compared against protein C concentrate and other standard care
- Safety planning for bleeding risk, renal function and platelet monitoring, and interaction management with antiplatelet drugs and NSAIDs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

