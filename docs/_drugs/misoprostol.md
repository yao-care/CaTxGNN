---
layout: default
title: Misoprostol
parent: Model Prediction Only (L5)
nav_order: 618
evidence_level: L5
indication_count: 2
---

# Misoprostol
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

# Misoprostol: From Prostaglandin E1 Analog to Amenorrhea

## One-Sentence Summary

Misoprostol is a prostaglandin E1 analog. Its Canadian licence records in this pack contain no indication text, and the retrieved literature concerns pregnancy termination and missed abortion.
The TxGNN model predicts it may be effective for **amenorrhea** with a very high score (99.64%), but **0 clinical trials** and no publications that test misoprostol as a treatment for amenorrhea support this direction.
The literature mentions amenorrhea only as a sign of early pregnancy, so this prediction is most likely a graph-based artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence records |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 (as assigned in the Evidence Pack; no study directly tests this indication, so it is effectively close to L5) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Misoprostol is a prostaglandin E1 analog that causes uterine contractions and cervical ripening. In the retrieved literature it is used to terminate early pregnancy and to manage missed abortion, alone or combined with mifepristone.

In those papers, "amenorrhea" only means a missed period in early pregnancy, which is a symptom and not the disease being treated. No paper in the set shows misoprostol treating pathological amenorrhea, whether hypothalamic, PCOS-related or hypoestrogenic. A drug that stimulates uterine contraction would not be expected to restore menses in non-pregnant amenorrhea.

The high TxGNN score is probably driven by proximity in the knowledge graph to pregnancy and menstrual-regulation nodes, not by a therapeutic mechanism. On current evidence the prediction is not mechanistically credible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these papers evaluates misoprostol for treating amenorrhea. Most concern pregnancy termination.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | 744 women with ultra-early pregnancy (amenorrhea ≤35 days) compared hospital-administered and self-administered misoprostol after low-dose mifepristone for medical abortion. |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (dose-ranging) | Reproductive Sciences | 2,500 women with ultra-early pregnancy received mifepristone at 50–150 mg followed by 200 µg oral misoprostol. The primary endpoint was complete abortion without surgery. |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Clinical study | J Obstet Gynaecol Res | Safety and efficacy of low-dose mifepristone with self-administered misoprostol for early pregnancy termination. |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Clinical study | Human Reproduction | Low-dose mifepristone with misoprostol before expected menstruation, used to prevent unintended pregnancy. |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Clinical study | BMJ | Medical management of missed abortion and anembryonic pregnancy. |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrial ablation for abnormal uterine bleeding; not specific to misoprostol. |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Acute fatty liver of pregnancy, where amenorrhea appears only as a presenting symptom; unrelated to misoprostol treatment. |

---

## Canada Market Information

The Evidence Pack lists 10 licences in total and shows the 5 below. Dosage form and approved indication text are not recorded for these entries.

| DIN | Product Name |
|---------|------|
| 2244022 | MISOPROSTOL |
| 2244023 | MISOPROSTOL |
| 2413469 | PMS-DICLOFENAC-MISOPROSTOL |
| 2413477 | PMS-DICLOFENAC-MISOPROSTOL |
| 2229837 | ARTHROTEC 75 |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication supports misoprostol for treating amenorrhea. The retrieved literature concerns pregnancy termination, and the drug's uterotonic action gives no plausible way to restore menses in non-pregnant amenorrhea. The other top prediction, atypical coarctation of aorta (score 99.30%), has no supporting evidence or mechanism either, so neither prediction justifies further investment now.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data, for example from DrugBank
- Approved indication text for the Canadian licences, to confirm the original indication
- Expert review to decide whether the prediction should be dropped as a graph artifact, unless a credible mechanism for a specific amenorrhea subtype is identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

