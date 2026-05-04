---
layout: default
title: Elagolix
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 1
---

# Elagolix
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Elagolix: From Heavy Menstrual Bleeding to Amenorrhea

## One-Sentence Summary

Elagolix is an oral GnRH receptor antagonist, studied primarily for heavy menstrual bleeding (HMB) associated with uterine fibroids and endometriosis pain management.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **3 clinical trials** and **4 publications** currently supporting this direction.
However, the mechanistic rationale reveals a critical conceptual tension: elagolix *induces* amenorrhea as a pharmacological effect, raising the question of whether treating pathological amenorrhea is a true therapeutic opportunity or a model artefact.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heavy Menstrual Bleeding (HMB) associated with Uterine Fibroids / Endometriosis (based on clinical trial context; no formal Health Canada DIN on file) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Elagolix is a competitive, oral GnRH receptor antagonist. By occupying pituitary GnRH receptors, it blocks the pulsatile GnRH signal, suppressing downstream secretion of LH and FSH. The resulting drop in gonadotropin drive causes the ovaries to markedly reduce estrogen and progesterone production, which in turn leads to endometrial atrophy and — at sufficient doses — complete amenorrhea. This is the intended pharmacodynamic mechanism exploited in HMB and endometriosis trials: controlling hormone-driven bleeding by inducing a reversible, medical menopause.

Because elagolix reliably produces amenorrhea as a measurable endpoint, a pattern-recognition model such as TxGNN will naturally associate the drug with the disease concept "amenorrhea." The drug–disease pair co-occurs frequently in clinical trial data, and the mechanistic pathway is unambiguous. In that narrow sense, the prediction is entirely coherent with the pharmacology.

However, the clinical interpretation requires an important caveat. The amenorrhea elagolix produces is a *drug-induced*, low-estrogen state that is therapeutically useful when the underlying problem is hormone-driven tissue growth (fibroids, endometriosis). In contrast, *pathological* amenorrhea — primary or secondary — often arises from a hypothalamic-pituitary-ovarian (HPO) axis that is already suppressed or dysfunctional. Administering a GnRH antagonist to a patient whose estrogen is already low would deepen HPO suppression, carry no therapeutic benefit, and accelerate bone mineral density loss. The mechanistic arrow points in the opposite direction from what treatment of pathological amenorrhea requires. This semantic gap is the central reason the recommendation is Hold rather than Proceed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Phase 2b | Completed | 571 | Randomized, double-blind, placebo-controlled RCT evaluating elagolix alone and in combination with add-back therapy vs. placebo for HMB in women with uterine fibroids. Amenorrhea rate was a secondary endpoint; study provides the largest Phase 2 quantitative dataset on elagolix-induced amenorrhea. |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2a | Completed | 271 | Proof-of-concept study assessing elagolix vs. placebo for uterine bleeding reduction and fibroid/uterine volume in premenopausal women. Amenorrhea served as a dose-response indicator; laid the groundwork for subsequent Phase 2b/3 development. |
| [NCT00797225](https://clinicaltrials.gov/study/NCT00797225) | Phase 2 | Completed | 174 | Randomized, double-blind, placebo- and active-controlled (vs. leuprorelin) trial in endometriosis over 6 months. Earliest rigorous head-to-head safety and efficacy dataset; amenorrhea rate monitored across dose arms. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37769311](https://pubmed.ncbi.nlm.nih.gov/37769311/) | 2023 | Clinical Study (RCT subgroup) | *Obstetrics and Gynecology* | Evaluated elagolix 150 mg once-daily monotherapy for HMB in uterine leiomyoma patients; provides efficacy and safety data at a lower dose with amenorrhea as an outcome measure. |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Systematic / Narrative Review | *Obstetrics and Gynecology* | Reviewed oral GnRH antagonists (including elagolix) co-administered with menopausal replacement hormones for uterine leiomyomas; summarises evidence on rapid bleeding suppression, amenorrhea induction, and bone protection strategies. |
| [32702363](https://pubmed.ncbi.nlm.nih.gov/32702363/) | 2021 | Retrospective Cohort / Post-hoc Analysis | *American Journal of Obstetrics and Gynecology* | Identified predictors of response to elagolix plus add-back therapy in HMB/fibroid patients; factors such as age, BMI, menstrual blood loss, and fibroid characteristics inform who is most likely to achieve amenorrhea. |
| [31695514](https://pubmed.ncbi.nlm.nih.gov/31695514/) | 2019 | Clinical Short Report / Narrative Review | *International Journal of Women's Health* | Early narrative overview of elagolix efficacy data in uterine fibroids; contextualises oral GnRH antagonism as an alternative to surgical intervention and existing hormonal therapies. |

---

## Canada Market Information

Elagolix currently holds **no Drug Identification Numbers (DINs)** in Canada. No Health Canada product licences are on file for this drug.

> For reference, elagolix is approved in the United States under the brand names **Orilissa** (endometriosis pain) and **Oriahnn** (HMB associated with uterine fibroids), both marketed by AbbVie. A Health Canada submission pathway would be required before any Canadian use.

---

## Safety Considerations

Detailed Canadian prescribing information (warnings, contraindications, and drug–drug interactions) is not available in this evidence pack.

> Please refer to the US prescribing information (Orilissa / Oriahnn package insert) and consult Health Canada's drug product database for the most current safety guidance. Key areas of known clinical concern for GnRH antagonists include: bone mineral density loss with prolonged use, hypoestrogenic symptoms (hot flashes, night sweats), mood changes, and teratogenicity risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model correctly identifies a strong pharmacological link between elagolix and amenorrhea — the drug reliably suppresses menstruation through HPO axis blockade — but this represents an *on-mechanism side effect* rather than a treatable disease. Applying elagolix to patients with pathological amenorrhea (where estrogen is already deficient) is mechanistically contraindicated and carries meaningful harm potential (accelerated bone loss, worsening hypo-oestrogenism). The prediction is a known model artefact arising from co-occurrence of drug and disease in clinical trial data.

**To proceed to a formal evaluation, the following would be needed:**

- **Reconceptualise the indication hypothesis:** Determine whether there is a *specific subtype* of amenorrhea (e.g., estrogen-excess-driven or adenomyosis-associated) where pharmacological HPO suppression could be beneficial, and reformulate the research question accordingly.
- **Retrieve Health Canada (or FDA) prescribing information:** Obtain the complete warnings, contraindications, and drug interaction profile from the Orilissa/Oriahnn package insert to complete the S1 safety assessment.
- **Confirm MOA data from DrugBank:** Formal MOA documentation (DrugBank DB11979) is flagged as a data gap; this should be retrieved to support any mechanistic analysis.
- **Pursue a Health Canada submission strategy:** Since elagolix is currently not marketed in Canada, any Canadian development path would require a New Drug Submission (NDS) with supporting Phase 3 data specific to the target indication.
- **Bone density risk management plan:** Any protocol involving elagolix for a population potentially at baseline low estrogen must include dual-energy X-ray absorptiometry (DEXA) monitoring and an add-back therapy framework.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

