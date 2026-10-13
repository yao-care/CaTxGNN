---
layout: default
title: Etonogestrel
parent: Model Prediction Only (L5)
nav_order: 366
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a progestin hormone marketed in Canada in a contraceptive implant and vaginal rings.
The TxGNN model predicts it may be relevant to **amenorrhea**, but there are **0 clinical trials** and **1 publication** (unrelated to this drug or indication) behind this prediction.
The prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian license records compiled for this report (the products NEXPLANON, NUVARING and HALOETTE are hormonal contraceptives) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on general pharmacology, etonogestrel is a progestin that suppresses ovulation and thins the endometrium.

Amenorrhea is a well-known effect of the implant, usually seen as a bleeding-pattern outcome of use. So a biological link exists. However, this is an expected pharmacologic effect, not a therapeutic goal that has been tested. The high score likely reflects hormone-pathway similarity in the knowledge graph rather than evidence that the drug treats amenorrhea.

Other predicted indications are all L5 and none has any trials or relevant literature:
- Breast fibrocystic disease (99.61%)
- Blunt duct adenosis of breast (99.29%)
- Apocrine adenosis of breast (99.29%)
- Benign mammary dysplasia (99.21%)

These are benign breast conditions where progestins might oppose estrogen-driven proliferation. This rationale is theoretical only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT protocol | Trials | Study protocol for BIO101 in preventing respiratory deterioration in COVID-19 pneumonia. Unrelated to etonogestrel or amenorrhea, so it gives no supporting evidence. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02499509 | NEXPLANON | Not listed | Not listed |
| 02253186 | NUVARING | Not listed | Not listed |
| 02520028 | HALOETTE | Not listed | Not listed |

---

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not from label text) include:
- Cardiovascular and metabolic: hypertension, coronary artery disease, thrombophlebitis, diabetes mellitus, diabetic ketoacidosis, hyperlipidemia, hypertriglyceridemia, obesity
- Liver, gallbladder and kidney disease
- Neurological: epilepsy, migraine
- Female breast carcinoma
- Others: porphyria, systemic lupus erythematosus, asthma, anxiety and related disorders

**Drug interactions:** 100 interactions were found. The 20 shown in the data are all rated Moderate. They fall mainly into these groups:
- Antidiabetic agents: acarbose, metformin, glimepiride, chlorpropamide, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, albiglutide, dulaglutide, semaglutide, and insulins (aspart, degludec, detemir, glargine, glulisine)
- Others: aprepitant, clarithromycin, linaclotide

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction only (L5). No trials exist, and the one linked publication is unrelated. Amenorrhea is an expected effect of etonogestrel rather than a treatment target, so it is hard to frame as a repurposing opportunity.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Approved indication text for each Canadian license
- Relevant clinical or observational studies of etonogestrel in amenorrhea or benign breast conditions
- A clear clinical rationale for whether amenorrhea would be a therapeutic goal rather than a side effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

