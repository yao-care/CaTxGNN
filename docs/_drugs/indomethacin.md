---
layout: default
title: Indomethacin
parent: Model Prediction Only (L5)
nav_order: 478
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Indomethacin: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Inflammatory arthritis and related musculoskeletal conditions (bursit…"
---

# Indomethacin
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

# Indomethacin: From Inflammatory Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Indomethacin is a nonsteroidal anti-inflammatory drug (NSAID) originally used for inflammatory joint and soft-tissue conditions such as rheumatoid arthritis, ankylosing spondylitis, gout and bursitis, and for closing patent ductus arteriosus.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation.
**No clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inflammatory arthritis and related musculoskeletal conditions (bursitis, synovitis, tenosynovitis, rheumatoid arthritis, ankylosing spondylitis, gout, osteoarthritis) and patent ductus arteriosus |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Indomethacin is generally understood to be a COX-1/COX-2 inhibitor. It reduces prostaglandin-mediated inflammation and pain, which is why it works in arthritis and other inflammatory joint conditions.

For this prediction, a reasonable mechanistic link could **not** be identified. Brachydactyly-syndactyly syndrome is a rare congenital skeletal malformation of the fingers and toes. It arises from abnormal limb development, not from ongoing inflammation. COX inhibition is not expected to correct a developmental defect.

The very high score most likely reflects the drug's closeness to musculoskeletal terms in the knowledge graph, not a true therapeutic relationship. The prediction should be treated as a computational signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Seven valid single-ingredient authorizations are on the Canadian market. Dosage form and approved-indication text were not available for them.

| DIN | Product Name |
|---------|------|
| 00337439 | TEVA-INDOMETHACIN |
| 00337420 | TEVA-INDOMETHACIN |
| 02231799 | ODAN-INDOMETHACIN |
| 02461811 | MINT-INDOMETHACIN |
| 02461536 | MINT-INDOMETHACIN |

Two further authorizations (02499223 AURO-INDOMETHACIN, 02231800 ODAN-INDOMETHACIN) are also valid but not listed here.

---

## Safety Considerations

Label-based warnings and contraindications were not available. Please refer to the package insert for safety information.

The following comes from drug-disease contraindication links in the knowledge graph, not from label text:

- **Contraindication-related conditions (knowledge graph):**
  - Cardiovascular: hypertension, myocardial infarction, coronary thrombosis, heart disease
  - Gastrointestinal: gastric, duodenal and active peptic ulcer, ulcerative colitis and inflammatory bowel disease, necrotizing enterocolitis, esophageal dyskinesia
  - Kidney and liver: kidney disease, liver disease, gallbladder disease
  - Bleeding and blood: blood coagulation disease, thrombocytopenia, intracerebral hemorrhage, hemoglobinopathy
  - Respiratory: asthma (intrinsic and allergic)
  - Neurological and psychiatric: epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
  - Other: infectious disease

- **Drug interactions:** The interaction screen returned 100 interacting drugs in total. The 20 shown in the compiled data are mostly Moderate, with a few Minor.
  - Moderate: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), metformin, glimepiride, chlorpropamide, aprepitant, mesalazine, balsalazide, potassium citrate, potassium bicarbonate, picosulfuric acid, polyethylene glycol with electrolytes
  - Minor: famotidine, ranitidine, cimetidine, linaclotide

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has the highest model score but no clinical, literature or mechanistic support. Indomethacin has no known biological reason to modify a congenital limb malformation, and its known risks (GI, renal, cardiovascular, bleeding) are not justified by evidence of benefit.

**To proceed, the following is needed:**
- A plausible biological mechanism linking COX inhibition to the developmental pathology of this syndrome
- Preclinical or case-level evidence of any benefit
- Mechanism of action data and label-based warnings and contraindications for the Canadian products
- Consideration of other candidates from the same prediction list. The most evidence-supported is **juvenile idiopathic arthritis** (TxGNN score 99.84%, Evidence Level L3, with a double-blind crossover trial against ketoprofen and several reviews). It is recommended as *Proceed with Guardrails*, but it largely extends existing arthritis use rather than being a new repurposing. Guardrails would be pediatric dosing, GI, renal and bleeding risk, and the availability of safer NSAIDs, DMARDs and biologics.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

