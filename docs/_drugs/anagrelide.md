---
layout: default
title: Anagrelide
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 2
---

# Anagrelide
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

# Anagrelide: From Essential Thrombocythemia to Reactive Thrombocytosis

## One-Sentence Summary

Anagrelide is a cytoreductive agent established in the management of essential thrombocythemia (ET), a myeloproliferative neoplasm defined by clonally driven platelet overproduction. The TxGNN model predicts it may be effective for **Reactive Thrombocytosis**, with **0 clinical trials** and **10 publications** identified — though the retrieved literature primarily discusses anagrelide in ET, and none directly studies its use as a treatment for reactive thrombocytosis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Essential Thrombocythemia (myeloproliferative neoplasm) |
| Predicted New Indication | Reactive Thrombocytosis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Anagrelide is known to reduce platelet counts by inhibiting phosphodiesterase 3 (PDE3) and interfering with megakaryocyte maturation and differentiation. This mechanism directly targets the platelet production pathway, and in principle it is pharmacologically agnostic to the *reason* platelets are elevated. Because reactive thrombocytosis, by definition, also involves an elevated platelet count, it is not surprising that a graph-based model would identify a potential connection.

However, the clinical reality creates a significant barrier to this prediction. Reactive thrombocytosis is a *secondary* phenomenon — the body's normal response to triggers such as infection, inflammation, iron deficiency, or post-splenectomy states — and is fundamentally different from the clonal, autonomous platelet overproduction seen in ET. Reactive thrombocytosis rarely causes the thrombohemorrhagic complications that justify cytoreductive therapy, and clinical guidelines consistently recommend treating the underlying cause rather than the platelet count itself. Anagrelide's known cardiovascular effects (tachycardia, palpitations, fluid retention) would represent an unfavorable risk–benefit profile in this generally benign condition.

None of the 10 retrieved publications contain a dedicated study design examining anagrelide as a therapeutic intervention for reactive thrombocytosis. Rather, the literature consistently uses reactive thrombocytosis as a *differential diagnosis to exclude* before starting anagrelide in ET. The mechanistic link proposed by TxGNN is theoretically traceable but runs counter to both the pathophysiology and the established treatment paradigm of reactive thrombocytosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Narrative Review | Expert Review of Anticancer Therapy | Comprehensive review of anagrelide's mechanism and clinical use; explicitly states reactive thrombocytosis does not require therapeutic intervention, whereas clonal thrombocytosis may require cytoreduction to prevent thrombohemorrhagic events |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Critical Review | Leukemia & Lymphoma | Critical appraisal of anagrelide in ET and related disorders; reinforces the clinical distinction between reactive and clonal thrombocytosis, with cytoreductive therapy reserved for the latter |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | Medical Journal of Australia | Overview of ET diagnosis and management; establishes that a diagnosis of ET requires active exclusion of reactive thrombocytosis before platelet-lowering therapy is initiated |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | American Journal of Medical Sciences | Characterises the full clinical spectrum of thrombocytosis; describes the cytokine regulatory network governing platelet production and distinguishes reactive from clonal forms |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case Report | European Journal of Case Reports in Internal Medicine | Documents acute myocardial infarction in an ET patient receiving anagrelide, illustrating the cardiovascular safety concerns relevant to any expansion of anagrelide's use |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leukemia Research | Reviews the role of thrombocytapheresis for extreme thrombocytosis in myeloproliferative neoplasms; anagrelide cited as standard cytoreductive therapy, with rapid mechanical reduction reserved for acute life-threatening events |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case Report | Srpski Arhiv Za Celokupno Lekarstvo | Reports a patient with concomitant ET and ankylosing spondylitis (a cause of reactive thrombocytosis); managed with anagrelide for the ET component alongside DMARDs for the inflammatory disease, illustrating the co-existence of both forms |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Retrospective Cohort | Pediatric Blood & Cancer | Retrospective analysis of 12 paediatric cases comparing ET vs. reactive thrombocythemia; underscores the clinical and molecular importance of distinguishing the two entities before treatment decisions are made |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Japanese Journal of Clinical Hematology | Reviews ET diagnosis and therapy including anagrelide; differential diagnosis from reactive thrombocytosis is presented as a prerequisite to treatment |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case Report | Medicine | Describes successful digital replantation in a post-splenectomy patient with reactive thrombocytosis; discusses platelet management strategies and highlights that thrombosis risk in reactive thrombocytosis demands careful, case-specific assessment |

---

## Canada Market Information

Anagrelide is not currently marketed in Canada and has no active Drug Identification Numbers (DINs) on file with Health Canada. Prescribers requiring access should consult Health Canada's Special Access Programme. For reference, anagrelide (brand name Agrylin®) holds U.S. FDA approval for the treatment of essential thrombocythemia.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No warnings, contraindications, or drug interaction data were available in this evidence pack. Clinicians should note that anagrelide carries known cardiovascular effects (tachycardia, palpitations, fluid retention, and QTc prolongation) that are especially relevant when evaluating any off-label use in populations who may not require cytoreductive therapy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Reactive thrombocytosis is a secondary, self-limiting condition whose treatment is directed at the underlying cause — not at platelet reduction — making anagrelide's cytoreductive mechanism both mechanistically misaligned and potentially harmful in this context. No clinical trials and no direct intervention studies support its use here, placing the evidence at L4 (mechanistic inference only).

**To proceed, the following is needed:**

- **Clarify the clinical subgroup**: Determine whether TxGNN's prediction targets a specific high-risk subpopulation (e.g., extreme post-splenectomy thrombocytosis with documented thrombotic events) where cytoreduction might be debated, rather than reactive thrombocytosis as a broad category
- **Retrieve full MOA data**: Obtain DrugBank pharmacology data to confirm whether any secondary pathway (e.g., anti-inflammatory effects) could theoretically justify use in reactive thrombocytosis independent of the platelet-lowering mechanism
- **Obtain full safety profile**: Contraindications, boxed warnings, and drug interaction data are currently unavailable and are required before any clinical feasibility assessment
- **Conduct an expert clinical review**: Seek input from a haematologist to evaluate whether any clinical scenario exists where anagrelide would be considered for reactive thrombocytosis, and under what conditions
- **Health Canada engagement**: If a research protocol is contemplated, regulatory consultation is required given that anagrelide is not currently marketed in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

