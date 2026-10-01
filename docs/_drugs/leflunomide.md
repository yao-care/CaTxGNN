---
layout: default
title: Leflunomide
parent: Model Prediction Only (L5)
nav_order: 528
evidence_level: L5
indication_count: 2
---

# Leflunomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Leflunomide: From Rheumatoid Arthritis to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Leflunomide is an immunomodulating drug originally used to treat rheumatoid arthritis.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation.
The prediction currently has **0 clinical trials** and **0 publications** behind it, and the drug's known mechanism suggests possible harm rather than benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (general drug knowledge; the Canadian license records supplied contain no indication text) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 18 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Leflunomide's active metabolite, teriflunomide, is known to inhibit dihydroorotate dehydrogenase (DHODH). This blocks pyrimidine synthesis and dampens the proliferation of activated lymphocytes. That mechanism explains its efficacy in autoimmune disease.

The predicted indication is a congenital limb malformation, which has no autoimmune or inflammatory basis. DHODH and pyrimidine inhibition therefore have no plausible therapeutic role in it. Loss of DHODH function is known to cause limb malformations (Miller syndrome), and leflunomide is teratogenic and contraindicated in pregnancy. The mechanism points toward harm rather than benefit.

The very high score most likely reflects a knowledge-graph artifact. Rare diseases with sparse graph connectivity can score high through proximity alone. The second predicted indication, colobomatous microphthalmia-rhizomelic dysplasia syndrome (score 99.93%), is another rare congenital syndrome with the same weaknesses: no evidence and no mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Leflunomide has 18 licenses in Canada. The records supplied do not include dosage form or approved indication text. The first 5 authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 02478862 | ACCEL-LEFLUNOMIDE |
| 02351676 | LEFLUNOMIDE |
| 02478870 | ACCEL-LEFLUNOMIDE |
| 02256495 | APO-LEFLUNOMIDE |
| 02261278 | TEVA-LEFLUNOMIDE |

---

## Safety Considerations

- **Key Warnings**: Leflunomide is teratogenic, which is a particular concern for a congenital developmental disorder.
- **Contraindications**: Pregnancy.

Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a model score, with no trials or literature. The known mechanism (DHODH inhibition) and the drug's teratogenicity argue against benefit in a congenital limb malformation. The score does not justify further investigation without independent mechanistic support.

**To proceed, the following is needed:**
- Independent mechanistic evidence linking DHODH or pyrimidine-pathway modulation to therapeutic benefit in brachydactyly-syndactyly syndrome
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Complete mechanism of action data from DrugBank
- Any preclinical or clinical evidence, since none currently exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

