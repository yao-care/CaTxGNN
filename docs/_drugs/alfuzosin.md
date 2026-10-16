---
layout: default
title: Alfuzosin
parent: Model Prediction Only (L5)
nav_order: 32
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Alfuzosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is an alpha-1 adrenergic blocker originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but **no clinical trials and no publications** currently support this prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, alfuzosin is a uroselective alpha-1 adrenergic antagonist. Its efficacy in BPH is established, but no mechanistic route to the predicted new indication is known.

Ambras syndrome is a rare genetic disorder caused by chromosomal rearrangements that affect regulation of the TRPS1 gene. No plausible pathway links alpha-1 blockade to this condition. The very high TxGNN score (about 0.99999) most likely reflects graph-topology artifacts shared across a cluster of hypertrichosis and hair-disorder diseases, rather than a true pharmacological signal.

The other top predictions (hypertrichosis, dental/periodontal malformation syndromes, Dandy-Walker–type syndromes, hair shaft abnormalities, trichomegaly, allergic urticaria, persistent fetal circulation syndrome, hypotrichosis simplex of the scalp, and congenital hypotrichosis milia) also have no supporting trials or literature. Persistent fetal circulation syndrome has only a loose vasodilation rationale, and it carries a serious hypotension risk in neonates.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02245565 | XATRAL | Not specified | Not specified |
| 02447576 | ALFUZOSIN | Not specified | Not specified |
| 02443201 | AURO-ALFUZOSIN | Not specified | Not specified |
| 02519844 | ALFUZOSIN | Not specified | Not specified |
| 02304678 | SANDOZ ALFUZOSIN | Not specified | Not specified |

A sixth valid authorization (DIN 02315866, APO-ALFUZOSIN) is also marketed. All six are single-ingredient products.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, hypotensive disorder, long QT syndrome (including familial), torsades de pointes, liver failure, liver disease, gallbladder disease, and intraoperative floppy iris syndrome.
- **Drug Interactions**: 100 interactions were identified. Examples:
  - **Major**: cisapride, clarithromycin, dolasetron
  - **Moderate**: famotidine, aprepitant, bupropion, levofloxacin, granisetron, dronabinol, the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), and several laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose)
  - **Minor**: cimetidine

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and no plausible mechanism links alpha-1 blockade to Ambras-type hypertrichosis, which is a genetic disorder. The high score probably reflects similarity within a disease cluster in the knowledge graph.

**To proceed, the following is needed:**
- Mechanism of action data, to allow a proper mechanistic analysis
- Package insert warnings and contraindications from Health Canada, to complete safety screening
- Any preclinical or clinical evidence linking alpha-1 blockade to hair growth or TRPS1-related biology
- A review of the other ranked predictions for any with a more credible pharmacological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

