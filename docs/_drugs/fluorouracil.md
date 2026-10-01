---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: From Antimetabolite Chemotherapy to Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil is a thymidylate synthase-inhibiting antimetabolite chemotherapy that is marketed in Canada.
The TxGNN model predicts it may be effective for **botryoid-type embryonal rhabdomyosarcoma of the vagina**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Fluorouracil is known as an antimetabolite that inhibits thymidylate synthase, giving it broad cytotoxic activity against rapidly dividing tumour cells. Mechanistically, it could be applicable to a fast-growing sarcoma such as rhabdomyosarcoma.

This prediction should be read cautiously. The score most likely reflects graph proximity among rhabdomyosarcoma subtypes rather than independent evidence. Standard rhabdomyosarcoma regimens do not centre on fluorouracil, and this rare vaginal subtype has no supporting trials or literature.

The same pattern appears in the other top-ranked predictions:
- **Rhabdomyosarcoma subtypes** (parameningeal, prostate, extrahepatic bile duct): scores of about 99.7%, with no direct evidence. They appear to be graph-adjacent duplicates of the parent rhabdomyosarcoma prediction.
- **Rhabdomyosarcoma (parent term)**: five retrieved papers from 1973–1991, all indirect (general paediatric sarcoma chemotherapy, nasopharyngeal carcinoma, head and neck intra-arterial chemotherapy). None shows a fluorouracil-specific benefit.
- **Liver sarcoma**: five matched trials, but all concern colorectal cancer, hepatocellular carcinoma or general solid tumours, not sarcoma of the liver.
- **Sickle cell syndromes** (three predictions, identical scores): likely a knowledge-graph artefact from hydroxyurea-like antimetabolite similarity. Fluorouracil's myelosuppression is a safety concern in these patients.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 12882 | FLUOROURACIL INJECTION |
| 330582 | EFUDEX |
| 2485346 | TOLAK |
| 2473763 | FLUOROURACIL INJECTION |
| 2473771 | FLUOROURACIL INJECTION |

Seven authorizations are recorded in total; the five above are shown. Dosage form and approved indication text are not available in the records provided.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium to high, depending on regimen (neutropenia and thrombocytopenia are common with systemic use) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes |
| Handling Protection | Follow cytotoxic drug handling regulations. Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score (99.75%) that likely reflects graph proximity among rhabdomyosarcoma subtypes. There are no trials or publications for this rare vaginal subtype, and fluorouracil is not a standard rhabdomyosarcoma agent.

**To proceed, the following is needed:**
- Full-text review of the rhabdomyosarcoma literature to confirm whether fluorouracil was actually studied in rhabdomyosarcoma patients
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmed mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian licenses, to assess route compatibility
- Any registered or published evidence specific to embryonal rhabdomyosarcoma, or a decision to focus on the parent rhabdomyosarcoma prediction instead

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

