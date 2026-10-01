---
layout: default
title: Arsenic Trioxide
parent: Model Prediction Only (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Arsenic Trioxide
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

# Arsenic Trioxide: From Acute Promyelocytic Leukemia to Unclassified Myelodysplastic Syndrome

## One-Sentence Summary

Arsenic trioxide is an intravenous anticancer drug best known for treating acute promyelocytic leukemia (APL). The TxGNN model predicts it may be effective for **unclassified myelodysplastic syndrome (MDS)**, with a very high score of 99.93%. No clinical trials or publications are linked to this exact term, so the prediction currently rests on the model alone. The broader MDS category has **24 linked trials** and **20 linked publications**, which give only indirect support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute promyelocytic leukemia (from published literature; the Canadian license text supplied contains no indication) |
| Predicted New Indication | Unclassified myelodysplastic syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Arsenic trioxide's efficacy in APL is well established. The literature in the pack describes it as pro-apoptotic and antiproliferative, and it may be mechanistically applicable to MDS.

MDS is a group of clonal bone marrow disorders that can progress to acute myeloid leukemia (AML). Arsenic trioxide is already used in a related blood cancer, which makes the prediction plausible. Preclinical and ex-vivo work in MDS supports this in three ways:
- It induces apoptosis through NF-kB/FLIP signalling and BCL2-family genes.
- It shows synergy with decitabine in MDS cell lines.
- In one ex-vivo study, MDS patients treated with arsenic trioxide plus ascorbic acid showed changes in apoptotic gene expression.

"Unclassified MDS" is a subtype of MDS. Evidence for the parent MDS entry is therefore indirect support for this prediction, not direct evidence. That parent entry includes small Phase 1/2 studies, a 2023 systematic review and network meta-analysis, and recent oral arsenic trials. Most MDS trials were single-arm, small, or terminated early. The only Phase 3 trial was withdrawn with no participants enrolled, so efficacy is not established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this exact indication.

---

## Literature Evidence

Currently no related literature available for this exact indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2554364 | Arsenic Trioxide for Injection | Injection (per product name) | Not listed in supplied data |
| 2487357 | Arsenic Trioxide Solution for Injection | Injection (per product name) | Not listed in supplied data |
| 2513420 | Arsenic Trioxide for Injection | Injection (per product name) | Not listed in supplied data |
| 2492768 | Arsenic Trioxide for Injection | Injection (per product name) | Not listed in supplied data |

---

## Cytotoxicity

The pack contains no toxicity data for this drug, so the entries below are general class-level expectations. Please refer to the package insert warnings and precautions for authoritative details.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antineoplastic; differentiation-inducing and pro-apoptotic agent |
| Myelosuppression Risk | Medium (blood counts need monitoring, particularly in patients with MDS who already have cytopenias) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, ECG/QTc, electrolytes (potassium, magnesium), liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no trials or publications are linked to this exact term, so the evidence level is L5. The related MDS evidence is mostly small, single-arm, or terminated studies, and the only Phase 3 trial was withdrawn. It is indirect support and not enough to move this specific subtype forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications. This is currently a blocking gap for safety screening.
- Mechanism of action data (for example, from the DrugBank API) to support the mechanistic-link analysis.
- The approved indication text for the four Canadian DINs.
- An assessment of whether MDS-level evidence can be applied to the unclassified subtype. This should include follow-up on the recruiting oral arsenic trials (NCT06670222, NCT06778187) and the 2023 systematic review (PMID 37908176).
- Randomized, disease-specific confirmatory data.

*This report is for research reference only and does not constitute medical advice. Predicted repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

