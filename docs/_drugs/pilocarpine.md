---
layout: default
title: Pilocarpine
parent: Model Prediction Only (L5)
nav_order: 728
evidence_level: L5
indication_count: 1
---

# Pilocarpine
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

# Pilocarpine: From Its Currently Marketed Uses in Canada to Primary Hereditary Glaucoma

## One-Sentence Summary

Pilocarpine is marketed in Canada under five licences, but the supplied data does not state its approved indications.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, with **0 clinical trials** and **0 publications** currently supporting this direction.
The prediction rests on the model score alone, and it may simply rediscover a use that is already labelled.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. The following comes from general pharmacology, not from the Evidence Pack. Pilocarpine is a muscarinic M3 receptor agonist. It contracts the ciliary muscle and the iris sphincter, which opens the trabecular meshwork and increases aqueous humour outflow, lowering intraocular pressure. Topical pilocarpine is widely known as a miotic for open-angle and angle-closure glaucoma, so the very high TxGNN score is plausible.

This also raises a caution. Because the original indications are missing from the record, the prediction may be a rediscovery of an existing labelled use and not true repurposing. Nothing in the input supports a hereditary or genetic mechanism specific to primary hereditary glaucoma. The labelled indications should be checked against the regulatory record before this is classed as repurposing.

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
| 868 | ISOPTO CARPINE |
| 2496119 | M-PILOCARPINE |
| 2148463 | MINIMS PILOCARPINE NITRATE |
| 2216345 | SALAGEN |
| 2509571 | JAMP PILOCARPINE |

Dosage forms and approved indication text were not supplied for these products.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is the model score (evidence level L5), with no registered trials or publications. The Canadian labelled indications are unknown, so it cannot yet be determined whether this is new repurposing or an already approved use. The missing Health Canada safety information blocks progression to safety screening.

**To proceed, the following is needed:**
- Health Canada package insert or product monograph for each of the five licences, to confirm the approved indications (including whether glaucoma is already labelled), dosage forms, warnings and contraindications
- Mechanism-of-action data from DrugBank to replace the general-pharmacology reasoning above
- Evidence specific to primary hereditary glaucoma (trials or literature), if the indication proves not to be already labelled
- Route-of-administration compatibility between the marketed products and the proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

