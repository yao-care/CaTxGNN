---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: From Endometriosis to Amenorrhea

## One-Sentence Summary

Dienogest is a fourth-generation synthetic progestin internationally approved for the treatment of endometriosis (brand name: Visanne®), though it currently holds no Health Canada approval and is not marketed in Canada.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **4 clinical trials** and **6 publications** available to assess this direction.
However, a critical mechanistic paradox exists: amenorrhea is a well-documented **pharmacological consequence** of Dienogest therapy — the drug reliably induces amenorrhea as part of its mechanism in endometriosis — rather than a condition it is designed to treat.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Endometriosis (established internationally; not approved in Canada) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the formal database record for Dienogest. Based on known information from the clinical trial literature, Dienogest belongs to the fourth-generation progestin class with selective progesterone receptor agonist activity and minimal androgenic or estrogenic effects. Its efficacy in endometriosis has been well established across multiple Phase 3 trials and real-world studies. The drug works primarily by suppressing ovulation, reducing systemic and local estradiol levels, and inhibiting endometrial cell proliferation — collectively creating a hypoestrogenic, amenorrheic state that starves ectopic endometrial implants of the hormonal stimulation they require.

The mechanistic link between endometriosis treatment and amenorrhea is therefore direct and established: the entire therapeutic strategy of Dienogest in endometriosis is to induce amenorrhea as a desired pharmacological effect. A 2026 pharmacological study (PMID: 41329046) explicitly states that the objective of endometriosis treatment with Dienogest is "inducing amenorrhea and a hypoestrogenic environment." In this sense, TxGNN has correctly identified the drug–amenorrhea connection.

However, this connection presents a fundamental repurposing paradox. When amenorrhea is treated as the **target disease** rather than the **intended pharmacological tool**, the therapeutic logic inverts. Pathological amenorrhea — whether hypothalamic, pituitary, ovarian, or uterine in origin — requires identifying and correcting the underlying cause. A progestin that induces amenorrhea does not treat its pathological absence in secondary amenorrhea (e.g., hypothalamic dysfunction, PCOS-related anovulation) and is contraindicated in primary amenorrhea caused by hormonal insufficiency. The TxGNN model likely captured the mechanistic overlap in its knowledge graph without distinguishing between "causes amenorrhea" and "treats amenorrhea" — a distinction critical for clinical translation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | Recruiting | 290 | Non-inferiority RCT comparing Indinol Forto® 200 mg vs Visanne® (Dienogest 2 mg) in endometriosis; amenorrhea induction rate available as secondary endpoint data |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Completed | 968 | Real-world observational study (VISANNE OS) of Dienogest for endometriosis; amenorrhea documented as a treatment-related outcome, not the study's primary therapeutic target |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Completed | 895 | Prospective observational cohort in Asian women with endometriosis; characterized quality of life, long-term safety, and menstrual pattern changes including amenorrhea rates |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Active, Not Recruiting | 138 | Compares Dienogest + transdermal estradiol vs drospirenone for endometriosis; evaluates patient satisfaction and tolerability including bleeding pattern changes |

> **Note:** None of the identified trials were designed to treat pathological amenorrhea as a primary indication. Amenorrhea appears as a secondary outcome, adverse event record, or expected pharmacological effect within endometriosis studies.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review + Bayesian Analysis | BMC Pharmacology & Toxicology | Comprehensive summary of adverse events from Dienogest in endometriosis/adenomyosis; abnormal uterine bleeding and amenorrhea among the most prevalent treatment-related events |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Narrative Review | Reviews in Endocrine & Metabolic Disorders | Reviews hormonal treatment landscape for endometriosis; estrogen-dependency and progesterone-resistance identified as key pathogenetic mechanisms; supports progestin-induced amenorrhea as the core therapeutic strategy |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Pharmacological/Translational Study | European Journal of Contraception & Reproductive Health Care | Reports high inhibition ratio and transformation index for Dienogest 2 mg; the stated treatment objective is explicitly "inducing amenorrhea and a hypoestrogenic environment" |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Prospective Cohort | Reproductive Sciences | Long-term efficacy and safety of Dienogest in ovarian endometrioma (n=514, ≥12 months); documents amenorrhea rates longitudinally and recurrence prevention |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Clinical Review | Journal of Pediatric & Adolescent Gynecology | Discusses advanced visualization for obstructive Müllerian anomalies; Dienogest used as bridging medical management for amenorrhea caused by outflow tract obstruction (indirect relevance only) |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case Report | Medicine | Ovarian granulosa cell tumor in a patient with PCOS; hormonal background relates to anovulation/amenorrhea but has no direct relevance to Dienogest repurposing |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.71%), but it reflects a mechanistic artefact rather than a genuine repurposing opportunity: Dienogest reliably *causes* amenorrhea as part of its established mechanism of action in endometriosis, and no clinical evidence exists for its use in treating pathological amenorrhea as a primary condition. The evidence package (L4) documents this drug–amenorrhea association only as a pharmacological side effect or desired treatment outcome within endometriosis studies, not as a new therapeutic indication.

**To proceed, the following is needed:**
- Define the specific type of amenorrhea being considered (hypothalamic, pituitary, ovarian, or uterine) — each subtype requires a fundamentally different therapeutic approach, and Dienogest may be inappropriate or contraindicated for most
- Clarify whether the clinical question is "therapeutic amenorrhea induction" (e.g., in adolescents with severe dysmenorrhea or endometriosis who lack a formal endometriosis diagnosis) — if so, this is better framed as an expanded use of the existing endometriosis indication rather than true repurposing
- Obtain full pharmacokinetic and MOA data from DrugBank to complete mechanistic analysis
- Download and review the originator product (Visanne®) package insert for warnings and contraindications, particularly regarding amenorrhea-related endocrine effects
- Before any advancement, conduct a structured literature review specifically targeting "Dienogest AND amenorrhea treatment" (not endometriosis) to confirm the absence of any prospective clinical evidence supporting this as a therapeutic target

> ⚠️ **Research Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

