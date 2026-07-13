---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 2
---

# Misoprostol
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

# Misoprostol: From Gastric Ulcer & Obstetric Use to Amenorrhea

## One-Sentence Summary

Misoprostol is a synthetic prostaglandin E1 (PGE1) analogue with established use in gastric ulcer prevention, medical abortion (combined with mifepristone), cervical ripening, and postpartum haemorrhage management.
The TxGNN model predicts it may have potential benefit for **Amenorrhea**, with **0 registered clinical trials** and **7 publications** available — though these studies address abortion and retained products of conception rather than amenorrhea as a direct therapeutic target.
Evidence is currently classified as **L4 (mechanistic/indirect)**, and no standalone misoprostol product holds a DIN in Canada.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada (no DIN on record); known internationally for gastric ulcer prevention and obstetric indications |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Misoprostol acts as a synthetic PGE1 analogue that binds prostaglandin EP receptors on uterine smooth muscle, triggering myometrial contractions and promoting cervical softening and dilation. This uterotonic mechanism is biologically relevant to certain subtypes of secondary amenorrhea: when menstruation fails to resume because of retained uterine contents (incomplete miscarriage, missed abortion) or mild intrauterine adhesions (early Asherman's syndrome), misoprostol's ability to stimulate contractions and mechanically open the uterine cavity could theoretically restore cyclical bleeding. The BMJ case series (PMID 1486304) and the body of missed-abortion literature offer indirect support for this pathway.

However, amenorrhea is not a single disease. Misoprostol's mechanism would only be plausible for etiology-specific cases — retained-tissue or mild-adhesion types of secondary amenorrhea — and would have no rationale for amenorrhea driven by hypothalamic-pituitary dysfunction, premature ovarian insufficiency, polycystic ovary syndrome, or other endocrine causes. This etiological heterogeneity sharply limits the scope of any potential repurposing claim.

The available literature does not treat amenorrhea as a therapeutic endpoint. Instead, amenorrhea duration is used as a gestational dating criterion for enrolling participants in medical abortion trials (e.g., "amenorrhea ≤35 days"). There is no study in which restoring menstruation in an amenorrhoeic patient was the primary outcome. This gap — high TxGNN mechanistic score, zero direct clinical evidence — explains the L4 classification and the Hold recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for misoprostol in amenorrhea.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | Dose-ranging RCT (n=2,500); mifepristone 50–150 mg + misoprostol 200 µg for ultra-early pregnancy termination; amenorrhea ≤35 days used as eligibility criterion, not a treatment endpoint |
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | RCT (n=744); low-dose mifepristone + self-administered misoprostol for ultra-early medical abortion; demonstrates comparable efficacy between hospital and home administration |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | RCT | J Obstet Gynaecol Res | RCT on self-administered low-dose mifepristone + misoprostol for early pregnancy termination; evaluates safety and tolerability of home protocols |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Prospective Observational | Human Reproduction | Prospective study of mifepristone + misoprostol given before expected menstruation to prevent unintended pregnancy; amenorrhea used for gestational dating |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Case Series | BMJ | Foundational report on misoprostol for medical management of missed abortion and anembryonic pregnancy; earliest evidence for uterotonic application in retained intrauterine contents — the subtype most relevant to the amenorrhea hypothesis |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | JOGC | Canadian Society of Obstetrics & Gynaecology guideline on endometrial ablation for abnormal uterine bleeding; misoprostol cited as a cervical priming agent prior to procedures, not as a treatment for amenorrhea |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case Report | Cureus | Case report of acute fatty liver of pregnancy with HELLP syndrome; amenorrhea appears as a presenting complaint in context of unrecognised pregnancy, unrelated to misoprostol use |

---

## Canada Market Information

No DINs are registered for misoprostol as a standalone product in this dataset.

> **Note:** Misoprostol is available in Canada as a component of **Mifegymiso®** (mifepristone 200 mg + misoprostol 200 µg), approved by Health Canada for medical termination of intrauterine pregnancy up to 63 days gestational age. Historical standalone misoprostol products (Cytotec®) may warrant a direct search of the current Health Canada Drug Product Database to confirm current market status.

---

## Safety Considerations

Safety data (warnings, contraindications, drug–drug interactions) is not available in this Evidence Pack.

> Please refer to the Health Canada product monograph and package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.64%), the mechanistic link between misoprostol and amenorrhea is etiology-dependent and indirect — all available literature uses amenorrhea only as a gestational dating criterion in abortion trials, not as a treatment target. Zero registered clinical trials exist for this indication, and the safety profile required for a formal repurposing assessment is currently unavailable (Blocking data gap: TFDA/Health Canada package insert).

**To proceed, the following is needed:**

- **Resolve Blocking data gap (DG001):** Retrieve Health Canada product monograph for misoprostol/Mifegymiso to complete the S1 safety screen (contraindications, warnings)
- **Resolve High data gap (DG002):** Query DrugBank API for full MOA details — receptor subtype specificity (EP1–EP4), uterine vs. vascular selectivity, and duration of action
- **Etiology-specific evidence search:** Narrow the research question to secondary amenorrhea due to retained products of conception or intrauterine adhesions; search for misoprostol use in Asherman's syndrome management as an adjunct post-adhesiolysis
- **Differentiate from alprostadil:** Clarify and document the distinction between misoprostol (oral/vaginal PGE1 analogue) and alprostadil (IV PGE1) to ensure the second-ranked prediction (atypical coarctation of aorta, L5/Hold) is not conflating the two agents in the knowledge graph
- **Standalone DIN verification:** Confirm current Health Canada Drug Product Database status for misoprostol as a standalone product before any regulatory pathway analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

