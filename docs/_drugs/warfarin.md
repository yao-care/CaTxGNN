---
layout: default
title: Warfarin
parent: Moderate Evidence (L3-L4)
nav_order: 978
evidence_level: L4
indication_count: 7
---

# Warfarin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Warfarin: From Thromboembolic Disorders to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Warfarin is a long-established oral anticoagulant used to prevent and treat blood clots. The TxGNN model predicts it may be useful for **heparin cofactor 2 deficiency**, an inherited clotting disorder. Support is thin: **0 clinical trials** and **5 publications**, all case reports, a general review or laboratory-methods papers.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation for thromboembolic disorders (general drug knowledge; the Canadian licence records provided contain no indication text) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not retrieved from DrugBank. The pack's rationale text describes warfarin as a vitamin K antagonist that reduces the synthesis of clotting factors II, VII, IX and X.

Heparin cofactor II normally helps neutralise thrombin. When it is deficient, thrombin activity is less restrained and clotting risk rises. Warfarin lowers the supply of clotting factors, including prothrombin (factor II, the precursor of thrombin). It could therefore plausibly offset this loss of thrombin inhibition. This is why the case reports describe patients with thrombosis being treated with warfarin.

The link is a plausible mechanism, not a clinically validated one. The available evidence cannot show that warfarin works in this specific deficiency, and it is far weaker than the evidence for warfarin's established uses. The high model score reflects knowledge-graph association, not trial results.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11177584](https://pubmed.ncbi.nlm.nih.gov/11177584/) | 2001 | Review | AIDS Patient Care and STDs | Review of thrombosis in HIV infection, covering hypercoagulable abnormalities such as antiphospholipid antibodies and deficiencies of natural anticoagulant proteins |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case report (family) | Journal of UOEH | A family with multiple thromboses, including an infant death. A sibling developed recurrent deep vein thrombosis despite warfarin; known hereditary thrombophilias were ruled out |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case report | Nihon Kyobu Shikkan Gakkai Zasshi | Woman with congenital antithrombin deficiency and pulmonary infarction who had taken warfarin for 7 years; switched to low-dose heparin after admission |
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case report | Kyobu Geka | A 14-year-old girl with familial heparin cofactor II deficiency had a right ventricular thrombus that mimicked a tumour; it was removed surgically |
| [3778142](https://pubmed.ncbi.nlm.nih.gov/3778142/) | 1986 | Laboratory methods | Archives of Pathology & Laboratory Medicine | Laboratory assay for heparin cofactor II; low levels were seen in liver disease, consumptive coagulopathy and preeclampsia |

None of these papers tests warfarin's efficacy in heparin cofactor 2 deficiency.

---

## Canada Market Information

Warfarin has 16 Health Canada authorisations (DINs). The records provided list no dosage form or approved-indication text. Five are shown below.

| DIN | Product Name |
|---------|------|
| 2242925 | APO-WARFARIN |
| 2242697 | TARO-WARFARIN |
| 2242680 | TARO-WARFARIN |
| 2242684 | TARO-WARFARIN |
| 2242685 | TARO-WARFARIN |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a plausible mechanism and a handful of case reports, with no clinical trials. The Canadian package-insert safety review is also incomplete. This cannot support moving forward.

For context, the same evidence pack ranks **thrombophilia** (a broader hypercoagulable-state indication) as the better-supported candidate. That prediction carries Evidence Level L2 and a "Proceed with Guardrails" recommendation, and its guardrails include confirming the thrombophilia subtype, close INR monitoring and watching for warfarin-induced skin necrosis in protein C or S deficiency. It is worth evaluating separately.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Mechanism-of-action data from DrugBank
- Controlled or cohort studies of warfarin specifically in heparin cofactor 2 deficiency
- Approved-indication and dosage-form details for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

