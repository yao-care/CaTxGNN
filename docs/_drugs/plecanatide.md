---
layout: default
title: Plecanatide
parent: Model Prediction Only (L5)
nav_order: 745
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Plecanatide"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "syndrome with a Dandy-Walker malformation as major feature", "idiopathic spontaneous coronary artery dissection", "vascular disease", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "phaeochromocytoma"]
description: "Plecanatide: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Plecanatide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Plecanatide: Hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Plecanatide is a guanylate cyclase-C (GC-C) agonist, marketed in Canada as TRULANCE and used for gastrointestinal constipation disorders (chronic idiopathic constipation and IBS-C in other jurisdictions).
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Based on known pharmacology, plecanatide is a peptide agonist of guanylate cyclase-C (GUCY2C). It acts locally on intestinal epithelium, raising cGMP, and is minimally absorbed into the bloodstream.

On review, the predicted link is weak. Hair follicle biology is not known to depend on GC-C signalling, and the drug's gut-restricted action makes a systemic effect on hair growth unlikely. The very high TxGNN score (1.0000) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trials or literature back it up.

The other top-10 predictions are similarly unsupported: Ambras-type hypertrichosis, odontal/periodontal malformation syndromes, hair shaft abnormalities, Dandy-Walker malformation syndromes, spontaneous coronary artery dissection, vascular disease, thoracic outlet syndromes (venous and arterial) and phaeochromocytoma. Most are genetic, developmental or mechanical conditions with no plausible GC-C mechanism. The cGMP pathway does influence vascular tone in general, but this is speculative for a minimally absorbed drug.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02493012 | TRULANCE | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: Two entries were compiled.
  - Idelalisib: Moderate interaction (DDInter).
  - Guanylyl cyclase-C: this is the pharmacological target of plecanatide, not a drug-drug interaction.

For other safety information (warnings and contraindications), please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model (deep learning) score. There are no trials or publications, and the proposed mechanism is implausible given plecanatide's local intestinal action and minimal absorption. The 10 top-ranked predictions are all at Evidence Level L5.

**To proceed, the following is needed:**
- Retrieval of the Health Canada package insert, to confirm approved indications, warnings and contraindications
- Confirmed mechanism of action data
- A credible biological rationale linking GC-C/cGMP signalling to hair follicle biology, supported by preclinical evidence
- Any clinical or observational signal (such as case reports of altered hair growth) before further investment
- Review of other candidate indications that fit the gastrointestinal mechanism better
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

