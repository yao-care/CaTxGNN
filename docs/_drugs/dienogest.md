---
layout: default
title: Dienogest
parent: Moderate Evidence (L3-L4)
nav_order: 281
evidence_level: L4
indication_count: 10
---

# Dienogest
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Dienogest: From Endometriosis to Amenorrhea

## One-Sentence Summary

Dienogest is a progestin that is marketed in Canada as a single-ingredient product. The Health Canada records compiled for this report do not list an approved indication text, but the literature shows it is used mainly for endometriosis.
The TxGNN model predicts it may be effective for **amenorrhea**, with **no registered clinical trials** and **7 publications**, none of which directly tests this use.
Amenorrhea is better understood as an expected effect of dienogest than as a disease it treats, so the prediction is best treated as a research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records (the literature describes endometriosis as its main use) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on what is known, dienogest is a fourth-generation, 19-nortestosterone-derived progestin with strong progestogenic activity and minimal androgenic activity. It partially suppresses ovulation and lowers circulating estradiol.

The link to amenorrhea is therefore real but points the wrong way. Amenorrhea is a well-known result of dienogest treatment in endometriosis, where inducing amenorrhea and a low-estrogen environment is a treatment goal. It is an expected pharmacological effect, not a condition the drug is shown to cure.

Using dienogest to treat secondary amenorrhea is biologically uncertain. Progestins are used for withdrawal-bleed challenges and for endometrial protection when estrogen is present, but dienogest itself suppresses the cycle. The high TxGNN score most likely reflects the closeness of amenorrhea to sex-steroid pathways in the knowledge graph, not a demonstrated therapeutic benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic review/meta-analysis | BMC Pharmacol Toxicol | Bayesian summary of adverse events and their frequency during dienogest treatment for endometriosis and adenomyosis |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Retrospective cohort (514 women) | Reprod Sci | Long-term efficacy, safety and recurrence of ovarian endometrioma with dienogest 2 mg daily beyond 12 months |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | Endocrine background of hormonal treatments for endometriosis, including estrogen dependency and progesterone resistance |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Cohort/laboratory study | Eur J Contracept Reprod Health Care | Dienogest 2 mg shows a high inhibition ratio and transformation index, supporting its use in endometriosis |
| [42438810](https://pubmed.ncbi.nlm.nih.gov/42438810/) | 2026 | Case report | JCEM Case Rep | Primary hyperparathyroidism became overt about 6 months after starting dienogest for menorrhagia |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review | J Pediatr Adolesc Gynecol | 3-D and virtual-reality visualization for Müllerian anomalies; not directly about dienogest efficacy |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case report | Medicine | Ovarian granulosa cell tumour in a patient with polycystic ovarian syndrome; not directly relevant |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02374900 | VISANNE | Not listed | Not listed |
| 02493055 | ASPEN-DIENOGEST | Not listed | Not listed |
| 02498189 | JAMP DIENOGEST | Not listed | Not listed |
| 02543613 | M-DIENOGEST | Not listed | Not listed |
| 02551683 | MAR-DIENOGEST | Not listed | Not listed |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not from label text): hypertension, epilepsy, anxiety and neurotic disorders, porphyria, kidney disease, liver disease, gallbladder disease, hypothyroidism, systemic lupus erythematosus, asthma, diabetes mellitus and diabetic ketoacidosis, hypertriglyceridemia, hypercalcemia and related calcium or phosphorus disorders, female breast carcinoma, and thrombophlebitis.
- **Drug Interactions**: 37 interactions were identified. Of the 20 detailed entries, the **Major** ones are sugammadex, griseofulvin, bexarotene, brigatinib, dabrafenib and encorafenib. Most of the others are Moderate, including linaclotide, metreleptin, prucalopride, miltefosine, adalimumab, alefacept, anakinra, asparaginase, canakinumab, certolizumab pegol, cladribine, emapalumab and enasidenib. Ethanol is Minor.
- **Case report signal**: one 2026 report describes primary hyperparathyroidism becoming overt after dienogest-related estrogen changes, which suggests attention to calcium homeostasis.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist, and the literature covers only endometriosis and safety, with no direct support for treating amenorrhea. Amenorrhea is an expected effect of dienogest, so the prediction has little therapeutic logic and remains a research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text, which are required before any safety screening
- Mechanism of action data
- A clear clinical question, such as whether any form of amenorrhea could benefit from dienogest, supported by a literature review or a pilot study
- Review of the knowledge-graph contraindication signals against the official label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

