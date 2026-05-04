---
layout: default
title: Anti-Inhibitor Coagulant Complex
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 2
---

# Anti-Inhibitor Coagulant Complex
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Anti-Inhibitor Coagulant Complex: From Hemophilia with Inhibitors to Glanzmann Thrombasthenia

## One-Sentence Summary

Anti-Inhibitor Coagulant Complex (AICC, also known as FEIBA) is a plasma-derived activated coagulation factor concentrate classically used for the management of bleeding episodes in hemophilia A and B patients who have developed inhibitory antibodies against Factor VIII or IX.
The TxGNN model predicts it may be effective for **Glanzmann Thrombasthenia (GT)**, a rare inherited platelet function disorder,
with **no registered clinical trials** and **no indexed publications** currently supporting this specific repurposing direction — evidence is based on mechanistic rationale only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bleeding control in hemophilia patients with inhibitors (per drug class; no Canada regulatory record available) |
| Predicted New Indication | Glanzmann Thrombasthenia |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 (Mechanistic rationale; no clinical or preclinical studies identified) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Research Question (Hold pending mechanistic validation) |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the Evidence Pack. Based on the drug's name and class, AICC is a plasma-derived concentrate containing activated coagulation factors — most critically **Factor VIIa**, as well as Factors IIa, IXa, and Xa — that were originally developed to **bypass** the need for Factor VIII or IX in patients whose immune systems have neutralised these proteins (inhibitor hemophilia).

Glanzmann Thrombasthenia (GT) is caused by absent or non-functional **GPIIb/IIIa (αIIbβ3)** integrin on the platelet surface. Because GPIIb/IIIa is the final common pathway for platelet aggregation, patients with GT are unable to form a stable platelet plug regardless of platelet count. The proposed mechanistic bridge is compelling: AICC's activated Factor VIIa can **directly activate Factor X on the phospholipid surface of even non-aggregating platelets**, generating thrombin through a GPIIb/IIIa-independent route and thereby achieving haemostasis without requiring normal platelet aggregation. This bypassing mechanism closely mirrors that of recombinant FVIIa (NovoSeven/rFVIIa), which already has recognised off-label use in refractory GT, particularly in patients who have developed anti-platelet alloantibodies (anti-HLA-I or anti-GPIIb/IIIa) following repeated platelet transfusions.

The TxGNN model's high prediction score likely reflects the structural similarity between "platelet function disorder" phenotype clusters in the knowledge graph and AICC's mechanistic profile. While the prediction is biologically plausible and mechanistically analogous to an already-used agent (rFVIIa), direct clinical evidence for AICC specifically in GT is entirely absent in the current literature search, and this indication remains at the hypothesis-generating stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

This drug currently holds **no Drug Identification Numbers (DINs)** and is not marketed in Canada. No approved product information is available from the Canada regulatory record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** As AICC is not currently marketed in Canada, no local prescribing information is on file. Clinicians should consult international product monographs (e.g., FEIBA NF, Baxter) and standard plasma-derived coagulation concentrate safety guidelines, including risk of **thromboembolic events** (particularly at high doses), **disseminated intravascular coagulation (DIC)**, and **anamnestic inhibitor responses**.

---

## Conclusion and Next Steps

**Decision: Research Question (Hold)**

**Rationale:**
The mechanistic hypothesis linking AICC to Glanzmann Thrombasthenia is biologically coherent and draws a credible parallel to the established use of rFVIIa in refractory GT; however, no clinical trials, case series, or preclinical studies specific to AICC in this indication were identified, and the drug is entirely absent from the Canada market, making any near-term clinical translation premature.

**To proceed, the following is needed:**

- **MOA data gap resolution**: Obtain formal mechanism of action documentation from DrugBank (DB13151) to confirm activated factor content and coagulation cascade bypass activity
- **Literature re-search**: Expand PubMed search to include synonyms (FEIBA, factor eight inhibitor bypassing activity, aPCC) combined with "Glanzmann thrombasthenia" and "platelet function disorder"
- **Comparative positioning vs. rFVIIa**: Determine whether AICC offers any advantage over rFVIIa (NovoSeven) in GT given the latter's more established evidence base; a head-to-head mechanistic comparison report is recommended
- **Regulatory feasibility assessment**: Since AICC is not marketed in Canada, evaluate regulatory pathway for use in a rare/orphan disease context (e.g., Health Canada Special Access Programme)
- **Safety data retrieval**: Download and parse the international product monograph for FEIBA to complete the blocking DG001 data gap before any S1 safety evaluation can proceed
- **Expert consultation**: Engage a haematologist with expertise in rare platelet disorders to assess clinical unmet need and feasibility of a prospective case series or investigator-initiated trial

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. — TxGNN Evidence Pack v4 | Data cutoff: 2026-04-05*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

