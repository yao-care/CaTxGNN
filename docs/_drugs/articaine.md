---
layout: default
title: Articaine
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Articaine: predicted new indication Gout (evidence level L5). Approved use: Not specified in the available license data (the products are markete…"
monitor_inn: "Articaine"
predicted_indications: ["gout", "exostosis", "allergic asthma", "intrinsic asthma"]
---

# Articaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Articaine: From Local Dental Anesthesia to Gout
{: .text-alpha }

## One-Sentence Summary

Articaine is an amide-type local anesthetic marketed in Canada in dental injection products, combined with epinephrine.
The TxGNN model predicts it may be effective for **gout**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no supporting studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available license data (the products are marketed as dental local anesthetics) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 12 of 12) |
| Number of DINs | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, articaine is an amide-type local anesthetic that blocks voltage-gated sodium channels. Its efficacy as a local anesthetic is established, but this has no recognized connection to gout.

Gout is driven by urate metabolism and inflammation (for example, xanthine oxidase activity and NLRP3 inflammasome signaling). Articaine has no known effect on these pathways. The high score (0.9958) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No clinical trial or publication backs it.

For this reason, the prediction should be treated as a computational hypothesis, not as a mechanistically supported candidate.

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Exostosis | 0.9942 | L5 | No credible mechanistic link. Articaine could only serve as procedural anesthesia in surgery. |
| 3 | Allergic asthma | 0.9938 | L5 | The two retrieved papers concern allergy *to* local anesthetics, so they are a safety signal, not efficacy evidence. |
| 4 | Intrinsic asthma | 0.9934 | L5 | No articaine data. Caution is warranted because of possible sulfite excipients in epinephrine-containing products. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for gout.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02248489 | 4% Astracaine Dental with Epinephrine 1:200,000 (0.005 mg/mL) | Not listed | Not listed |
| 02123371 | Septanest N | Not listed | Not listed |
| 02339544 | Articaine Hydrochloride and Epinephrine Bitartrate Injection | Not listed | Not listed |
| 02248488 | 4% Astracaine Dental with Epinephrine Forte 1:100,000 (0.01 mg/mL) | Not listed | Not listed |
| 02381338 | Posicaine SP | Not listed | Not listed |

Twelve valid single-ingredient licenses exist in total; the five above are shown.

## Safety Considerations

- **Drug Interactions** (10 recorded interactions):
  - **Major**: Nitrous acid
  - **Moderate**: Morphine (liposomal), benzocaine (topical), lidocaine (ophthalmic and topical), oxybuprocaine (ophthalmic), cinchocaine (topical), tetracaine (ophthalmic and topical)
  - **Minor**: Hyaluronidase
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): cardiovascular conditions (hypertension, coronary artery disease, myocardial infarction, heart conduction disease, cardiomyopathy), kidney and liver disease, diabetes and diabetic ketoacidosis, angle-closure glaucoma, myasthenia gravis and other neuromuscular junction disease, butyrylcholinesterase deficiency, hyperthyroidism, Parkinson disease and hemoglobinopathy. These should be verified against the official package insert.
- **Hypersensitivity**: the retrieved allergy literature suggests possible reactions to local anesthetics, though one case report found no cross-reactivity between prilocaine and articaine.

Please refer to the package insert for the official warnings and contraindications, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or relevant publications, and there is no plausible mechanistic link between a sodium channel–blocking local anesthetic and gout. The same holds for the other three predicted indications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or mechanistic evidence linking articaine to urate metabolism or gout-related inflammation
- Confirmation of the approved indications, dosage forms and routes for the Canadian products
- A route compatibility assessment, since articaine is an injectable dental anesthetic and the route required for gout treatment is undefined
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

