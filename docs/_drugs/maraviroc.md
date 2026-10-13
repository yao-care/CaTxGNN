---
layout: default
title: Maraviroc
parent: Model Prediction Only (L5)
nav_order: 573
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: From an Unspecified Original Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a CCR5 antagonist marketed in Canada as CELSENTRI, but the data compiled for this report do not include the text of its approved indication.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia** (score 99.8%), yet there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the Canadian licence records contain no indication text) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, maraviroc is a CCR5 antagonist, a class that blocks the chemokine receptor CCR5 on immune cells. This is the mechanism behind its use in HIV infection, but the Canadian licence records here do not state its approved indication.

For multiple endocrine neoplasia (MEN), the analysis found **no direct mechanistic link**. MEN is driven mainly by MEN1 and RET alterations, and nothing in the data shows that CCR5 plays a role in these pathways. The high TxGNN score is a computational prediction only and should not be read as evidence of efficacy.

Other predictions for this drug are somewhat better grounded biologically, though still unproven:
- **HER2-positive breast carcinoma** (score 99.2%): a 2020 preclinical study reported that autocrine CCL5 drives trastuzumab resistance through ERK pathway activation. Blocking CCR5 could theoretically reverse this, making it the most biologically grounded candidate. It remains hypothesis-generating, with no clinical trials.
- **Primary cutaneous T-cell lymphoma** (score 99.7%): chemokine receptors are implicated in skin-homing T-cell trafficking, but the only literature is an indirect 2023 review on ACKR1.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02299852 | CELSENTRI | Not listed | Not listed |
| 02299844 | CELSENTRI | Not listed | Not listed |

Both authorizations are valid single-ingredient products.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these come from drug-disease links in a computational knowledge graph, not from label text): orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, liver disease (including drug-induced liver injury, chronic hepatitis B and hepatitis C infection), kidney disease (including chronic and end-stage renal failure), coronary artery disease, myocardial infarction and ischemia, gallbladder disease, and hemoglobinopathy.
- **Drug Interactions**: 93 interactions were recorded. The only **Major** interaction among the 20 listed is with **clarithromycin**. Most others are Moderate, including aprepitant, dexamethasone, cimetidine, cobicistat, clotrimazole, miconazole, eliglustat, naltrexone, promethazine, rolapitant and deferasirox. Maraviroc is generally understood to be metabolised via CYP3A, so strong CYP3A inhibitors and inducers deserve particular attention.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (evidence level L5), and no mechanistic link between CCR5 antagonism and multiple endocrine neoplasia was identified. A high model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications and approved indication), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- A defined mechanistic hypothesis linking CCR5 to MEN pathogenesis, or a switch in focus to a better-supported candidate such as HER2-positive breast carcinoma (preclinical CCL5–CCR5 evidence)
- Preclinical or early exploratory studies before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

