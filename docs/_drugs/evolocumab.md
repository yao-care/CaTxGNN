---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 280
evidence_level: L5
indication_count: 10
---

# Evolocumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Evolocumab: From Hypercholesterolemia to Symptomatic Hemophilia in Female Carriers

## One-Sentence Summary

Evolocumab is a PCSK9 inhibitor monoclonal antibody established for lowering LDL cholesterol and reducing cardiovascular risk in patients with hypercholesterolemia and atherosclerotic cardiovascular disease.
The TxGNN model ranks **symptomatic form of hemophilia in female carriers** as its top predicted new indication (score: 99.82%),
yet **0 clinical trials** and **0 publications** exist to support this direction — the prediction rests entirely on model inference with no empirical corroboration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypercholesterolemia / cardiovascular risk reduction (global approvals on record; not captured in this Evidence Pack) |
| Predicted New Indication | Symptomatic form of hemophilia in female carriers |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed (未上市) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on known pharmacology, Evolocumab is a fully human IgG2 monoclonal antibody that targets proprotein convertase subtilisin/kexin type 9 (PCSK9) — a serine protease secreted by the liver that degrades LDL receptors on hepatocyte surfaces. By blocking PCSK9 from binding to and downregulating LDL receptors, Evolocumab preserves receptor availability, enabling greater clearance of circulating LDL-C. The result is a 50–60% reduction in LDL-C on top of statin therapy, with demonstrated reduction in major adverse cardiovascular events.

The top-ranked predicted indication — **symptomatic hemophilia in female carriers** — involves an entirely different biological domain: reduced activity of coagulation factor VIII (or IX), causing bleeding due to intrinsic clotting pathway dysfunction. The PCSK9–LDL receptor axis has no established direct intersection with coagulation factor synthesis, activity, or regulation. Emerging basic-science literature has explored whether PCSK9 may exert indirect effects on platelet biology or the hemostatic system, but these findings are preliminary, inconsistent, and remote from clinical applicability. Current standard of care for symptomatic female carriers centers on coagulation factor replacement or emicizumab prophylaxis — pathways Evolocumab does not address.

The high TxGNN score almost certainly reflects ontological proximity in the knowledge graph (e.g., shared "hematologic/vascular" node connections) rather than genuine mechanistic plausibility. All 10 predicted indications in this Evidence Pack involve coagulation disorders, rare metabolic diseases, or broad ontological categories — none with a credible direct link to PCSK9 inhibition. This pattern is a recognized failure mode in graph-based repurposing models when a hub drug (Evolocumab has rich lipid-metabolism node connectivity) generates spurious high-scoring edges to loosely related disease clusters.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

No DIN data is on file for Evolocumab in this Evidence Pack (0 licenses recorded, not marketed). Note that Evolocumab (Repatha®, Amgen) holds regulatory approvals in the United States (FDA, 2015), European Union (EMA, 2015), and other major markets; however, no Health Canada authorization data was successfully captured in the current evidence retrieval cycle.

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields (key warnings, contraindications, drug-drug interactions) were not captured in this Evidence Pack and remain pending remediation via TFDA/Health Canada product monograph retrieval (Data Gap DG001).

---

## All Predicted Indications — Summary Assessment

The Evidence Pack contains 10 predicted indications, all assigned **L5 / Hold**. For reference:

| Rank | Disease | TxGNN Score | Mechanistic Plausibility | Note |
|------|---------|-------------|--------------------------|------|
| 1 | Symptomatic hemophilia in female carriers | 99.82% | Very low | No PCSK9–coagulation factor link |
| 2 | Familial apolipoprotein C-II deficiency | 99.50% | Low | TG/VLDL axis, not LDL axis |
| 3 | Thrombocytopenic purpura | 99.42% | Very low | Autoimmune/TMA, not lipid-mediated |
| 4 | Factor XI deficiency | 99.29% | Very low | Intrinsic coagulation pathway defect |
| 5 | Hemophilia A with vascular abnormality | 99.22% | Indirect only | LDL lowering may reduce CV risk in this subgroup — but this is an extension of existing indication, not true repurposing |
| 6 | Disease of catalytic activity | 99.08% | None (ontological artifact) | PCSK9 is a serine protease; KG mis-links |
| 7 | Hemorrhagic disease of newborn | 98.89% | Very low | Vitamin K-dependent clotting, unrelated to PCSK9 |
| 8 | X-linked ichthyosis (without STS deficiency) | 98.84% | Very low | Cholesterol sulfate pathway ≠ systemic LDL-R regulation |
| 9 | Inherited thrombophilia | 98.82% | Low–moderate (theoretical) | Highest relative biological rationale among the 10; high LDL can potentiate thrombotic risk, but no Evolocumab-specific trial evidence |
| 10 | Disorder of vitamins/cofactors metabolism | 98.80% | Very low (ontological) | LDL carries fat-soluble vitamins — highly speculative |

Of these, **Rank 9 (inherited thrombophilia)** has the highest relative theoretical rationale: the interaction between hyperlipidemia and prothrombotic states is biologically recognized, and PCSK9 inhibition has been speculatively proposed as having antithrombotic properties. However, no Evolocumab clinical trial data exists for this indication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Evolocumab in this Evidence Pack are unsupported by any registered clinical trials or published literature (L5). The dominant predicted indications involve coagulation and rare hematologic disorders that have no established mechanistic connection to PCSK9 inhibition; the high model scores are likely driven by knowledge graph artifacts rather than true drug–disease biological proximity.

**To proceed, the following is needed:**

- **Remediate Data Gap DG001**: Retrieve Health Canada / TFDA product monograph to establish baseline safety profile before any further evaluation.
- **Remediate Data Gap DG002**: Confirm Evolocumab's MOA and approved indications from DrugBank API to properly populate the Evidence Pack.
- **Re-run TxGNN with disease ontology filtering**: Apply a constraint to exclude diseases with no plausible pathway connection to lipid metabolism or PCSK9 biology, to reduce false-positive predictions.
- **Consider Rank 9 (inherited thrombophilia) for deeper investigation**: This is the only predicted indication with any theoretical biological rationale. A focused literature search on PCSK9 inhibition and thrombosis biomarkers is warranted before dismissal.
- **Verify global market status**: Cross-reference Health Canada Drug Product Database directly to confirm Evolocumab's Canadian authorization status and approved indications, given the drug's known global approvals.

---

> **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. YMYL content — consult a qualified healthcare professional for individual patient management decisions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

