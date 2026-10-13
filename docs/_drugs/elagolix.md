---
layout: default
title: Elagolix
parent: Moderate Evidence (L3-L4)
nav_order: 318
evidence_level: L4
indication_count: 1
---

# Elagolix
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Elagolix: From Endometriosis to Amenorrhea

## One-Sentence Summary

Elagolix is an oral GnRH receptor antagonist originally used to treat endometriosis.
The TxGNN model predicts it may be effective for **amenorrhea**, but there are **no registered clinical trials** and only **4 publications**, none of which study amenorrhea as a disease to be treated.
Amenorrhea appears in that literature as an expected on-treatment effect of menstrual suppression, not as a therapeutic target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (endometriosis of uterus) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, elagolix is a GnRH receptor antagonist. It suppresses pituitary release of LH and FSH, which lowers ovarian production of estradiol and progesterone. This hypoestrogenic state reduces endometrial proliferation and is the basis of its benefit in endometriosis.

The same mechanism commonly leads to markedly reduced menstrual bleeding or amenorrhea. This overlap probably explains the very high model score. However, amenorrhea here is a pharmacodynamic effect of the drug, not a condition it would treat. Elagolix would be expected to cause or worsen amenorrhea of hypoestrogenic origin. The prediction is therefore mechanistically understandable but does not support a valid therapeutic use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37769311](https://pubmed.ncbi.nlm.nih.gov/37769311/) | 2023 | Clinical study (RCT per title) | Obstetrics and Gynecology | Elagolix 150 mg once daily monotherapy for heavy menstrual bleeding in uterine leiomyomas |
| [32702363](https://pubmed.ncbi.nlm.nih.gov/32702363/) | 2021 | Post hoc analysis of RCT data | American Journal of Obstetrics and Gynecology | Predictors of response to elagolix with add-back therapy in heavy menstrual bleeding with fibroids |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Review | Obstetrics and Gynecology | Efficacy and safety of oral GnRH antagonists for uterine leiomyomas |
| [31695514](https://pubmed.ncbi.nlm.nih.gov/31695514/) | 2019 | Short report / Review | International Journal of Women's Health | Clinical utility and emerging efficacy data of elagolix in uterine fibroids |

None of these publications evaluate elagolix as a treatment for amenorrhea.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02481332 | ORILISSA | Not specified | Not specified |
| 02481340 | ORILISSA | Not specified | Not specified |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the drug-disease network, not label text): liver failure, osteoporosis, postmenopausal osteoporosis. Consistent with the hypoestrogenic mechanism, bone loss is a relevant concern.
- **Drug Interactions**: 100 interactions were identified. Examples shown here are:
  - **Major**: clarithromycin
  - **Moderate**: loperamide, aprepitant, dexamethasone, cimetidine, saxagliptin, clotrimazole, eliglustat, empagliflozin, linagliptin, repaglinide, rifaximin, naltrexone, among others
  - **Minor**: fidaxomicin, prucalopride

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high score probably reflects the drug's menstrual-suppressing effect rather than a therapeutic opportunity. Amenorrhea is an expected pharmacological effect of elagolix, so using it to treat amenorrhea is not supported. No clinical trials exist, and the literature does not address this indication.

**To proceed, the following is needed:**
- A clear clinical rationale showing a patient population in which inducing or treating amenorrhea would be a valid goal (for example, reframing toward heavy menstrual bleeding in uterine fibroids, which has actual literature support)
- Mechanism of action data from DrugBank
- Health Canada package insert warnings, contraindications, and approved indication text
- Bone-density and liver-safety risk assessment for any new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

