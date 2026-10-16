---
layout: default
title: Dutasteride
parent: Model Prediction Only (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Dutasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "DUTASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "familial isolated trichomegaly"]
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a 5-alpha-reductase inhibitor originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dutasteride inhibits type 1 and type 2 5-alpha-reductase, the enzymes that convert testosterone into dihydrotestosterone (DHT). Lowering DHT shrinks the prostate, which is why it is used for BPH. Detailed mechanism of action data was not available in the data compiled for this report, so this description reflects the drug's generally known pharmacology.

The link to the predicted indication is weak. Ambras syndrome is a genetic disorder (a chromosome 8q rearrangement affecting TRPS1 expression) and is not primarily driven by androgens. Reducing DHT is unlikely to correct the underlying defect. The very high model score probably reflects graph proximity to hair-related conditions rather than a true mechanistic fit.

Other top-ranked predictions are also of limited plausibility:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Hypertrichosis | 99.997% | L5 | Usually androgen-independent; weak fit |
| 3 | Malformation syndrome with dental/periodontal component | 99.997% | L5 | No plausible link; likely a graph artifact |
| 4 | Syndrome with Dandy-Walker malformation | 99.996% | L5 | No mechanistic rationale |
| 5 | Isolated genetic hair shaft abnormality | 99.996% | L5 | Structural defect; indirect link |
| 8 | Diffuse alopecia areata | 99.675% | L4 | Autoimmune; DHT suppression does not address it |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top prediction, currently no related literature available. The only publication retrieved across the top 10 predictions relates to diffuse alopecia areata (rank 8), and it addresses a different disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41714473](https://pubmed.ncbi.nlm.nih.gov/41714473/) | 2026 | Review | American Journal of Clinical Dermatology | Narrative review of the pathophysiology, evaluation and treatment of androgenetic alopecia in women. It covers a different condition from alopecia areata, so it is only indirect evidence. |

## Canada Market Information

Dutasteride has 16 valid single-ingredient authorizations in Canada. Dosage form and approved indication text were not available in the data compiled for this report. Five are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247813 | AVODART | Not available | Not available |
| 02408287 | TEVA-DUTASTERIDE | Not available | Not available |
| 02484870 | JAMP DUTASTERIDE | Not available | Not available |
| 02443058 | DUTASTERIDE | Not available | Not available |
| 02485672 | AG-DUTASTERIDE | Not available | Not available |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (model-derived, not label text): multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism, intraoperative floppy iris syndrome.
- **Fetal risk**: 5-alpha-reductase inhibitors can disrupt male external genital development, which argues against use in developmental disorders.
- **Drug Interactions**: 100 interactions were identified. The ones rated Moderate are aprepitant, cimetidine, clarithromycin, clotrimazole and miconazole. Others have an unknown severity level, including calcitriol, pantoprazole, glimepiride, metformin, omeprazole, simvastatin, morphine and prednisone.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials or literature. The mechanism is implausible for a genetic, largely androgen-independent condition, and the fetal developmental risk of 5-alpha-reductase inhibitors adds further concern. The evidence level is L5.

**To proceed, the following is needed:**
- A credible mechanistic rationale linking DHT suppression to TRPS1-related hypertrichosis
- Any preclinical or clinical evidence in Ambras syndrome or hypertrichosis
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data
- A benefit-risk review for use in a congenital, possibly pediatric, population
- Consideration of better-supported candidates, since the only retrieved paper concerns androgenetic alopecia, a different disease from the predicted alopecia areata
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

