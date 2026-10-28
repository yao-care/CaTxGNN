---
layout: default
title: Letrozole
parent: High Evidence (L1-L2)
nav_order: 538
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "LETROZOLE"
predicted_indications: ["nipple carcinoma", "Ehrlich tumor carcinoma", "breast fibrocystic disease", "benign mammary dysplasia"]
description: "Letrozole: predicted new indication Nipple carcinoma (evidence level L1). Approved use: Not recorded in the local data"
---

# Letrozole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Letrozole: Nipple carcinoma
{: .text-alpha }

## One-Sentence Summary

Letrozole is a nonsteroidal aromatase inhibitor, marketed in Canada and used for hormone receptor-positive breast cancer.
Because this is already an established use, the prediction is better read as a confirmation than as true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nipple carcinoma |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L1 |
| Canada Market Status | Marketed (valid licenses: 20 of 20) |
| Number of DINs | 20 (valid: 20) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on the published literature, letrozole is a third-generation nonsteroidal aromatase inhibitor. It blocks the conversion of androgens to oestrogens, which lowers oestrogen-driven tumour growth in hormone receptor-positive breast cancer.

The predicted indication sits very close to the drug's established use. Large Phase 3 trials pair letrozole with CDK4/6 inhibitors (for example MONALEESA-2 with ribociclib and PALOMA-2 with palbociclib) in hormone receptor-positive, HER2-negative breast cancer. Since letrozole is already marketed for this setting, the high score reflects confirmation of an existing use rather than a new therapeutic direction.

The other nine predictions in the ranked list vary widely in strength:
- **Estrogen-receptor positive breast cancer** (L1): also an established use, with extensive Phase 3 evidence.
- **Hormone-resistant breast carcinoma** (L2) and **bilateral breast carcinoma** (L2): research questions. Letrozole serves as the endocrine backbone in combination studies, and the evidence is mostly early-phase.
- **Breast carcinoma by gene expression profile** (L3): biomarker-related evidence rather than a distinct indication.
- **Nipple carcinoma** (L4): only case reports are available.
- **Estrogen-receptor negative breast cancer** (L4): mechanistically unlikely, since letrozole works by depleting oestrogen. The high score appears to reflect disease-ontology proximity rather than specific evidence.
- **Ehrlich tumour carcinoma** (L5): a single mouse-model study.
- **Breast fibrocystic disease and benign mammary dysplasia** (L5): no trials or literature; benefit-risk is unfavourable for benign conditions.

---

## Clinical Trial Evidence

The most relevant trials for the top-ranked prediction are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02941926](https://clinicaltrials.gov/study/NCT02941926) | Phase 3 | Completed | 3246 | COMPLEEMENT-1: safety and efficacy of ribociclib plus letrozole in HR+/HER2- advanced breast cancer with no prior hormonal therapy |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | Completed | 131 | Palbociclib plus letrozole in postmenopausal women with HR+/HER2- advanced breast cancer (access study in Latin America) |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | Completed | 666 | PALOMA-2: palbociclib plus letrozole versus placebo plus letrozole as first-line therapy |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Phase 3 | Active, not recruiting | 1050 | SONIA: aromatase inhibitor plus CDK4/6 inhibitor first-line versus second-line sequencing |
| [NCT00382070](https://clinicaltrials.gov/study/NCT00382070) | Phase 3 | Unknown | 3966 | Five years of extended letrozole versus placebo after prior hormonal therapy |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | Terminated | 123 | Four months of preoperative letrozole versus surgery first in postmenopausal HR+ disease |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Phase 2 | Active, not recruiting | 84 | Pre-operative endocrine window in older women to inform radiation decisions |
| [NCT00728949](https://clinicaltrials.gov/study/NCT00728949) | Phase 2 | Completed | 93 | IMC-A12 alone or with antiestrogens after progression on antiestrogen therapy |
| [NCT01439711](https://clinicaltrials.gov/study/NCT01439711) | Phase 2 | Completed | 108 | Neoadjuvant letrozole in ER+ ductal carcinoma in situ |
| [NCT02344550](https://clinicaltrials.gov/study/NCT02344550) | Phase 2 | Completed | 137 | Ovarian suppression plus letrozole plus everolimus in premenopausal metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35263519](https://pubmed.ncbi.nlm.nih.gov/35263519/) | 2022 | RCT | N Engl J Med | Overall survival analysis of ribociclib plus letrozole in advanced breast cancer, following earlier progression-free survival gains |
| [29718092](https://pubmed.ncbi.nlm.nih.gov/29718092/) | 2018 | RCT | Ann Oncol | Updated MONALEESA-2 efficacy, safety and biomarker results for ribociclib plus letrozole |
| [30632023](https://pubmed.ncbi.nlm.nih.gov/30632023/) | 2019 | RCT | Breast Cancer Res Treat | PALOMA-2 extended follow-up: palbociclib plus letrozole prolonged progression-free survival (HR 0.58) |
| [15001182](https://pubmed.ncbi.nlm.nih.gov/15001182/) | 2004 | RCT | Womens Health Issues | Commentary on the Letrozole Breast Cancer Trial and remaining questions |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sci | Pharmacology, toxicity and potential therapeutic effects of letrozole |
| [17912633](https://pubmed.ncbi.nlm.nih.gov/17912633/) | 2007 | Review | Breast Cancer Res Treat | Discovery and mechanism of action of letrozole as an aromatase inhibitor |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Pharmacodynamics, pharmacokinetics, efficacy and safety of letrozole |
| [19250202](https://pubmed.ncbi.nlm.nih.gov/19250202/) | 2009 | Review | Ann N Y Acad Sci | Intratumoral aromatase model: letrozole sustained growth inhibition longer than tamoxifen |
| [27235140](https://pubmed.ncbi.nlm.nih.gov/27235140/) | 2016 | Preclinical | Med Oncol | Letrozole-induced changes in carcinoma-associated fibroblasts and their effect on breast cancer cells |
| [29229198](https://pubmed.ncbi.nlm.nih.gov/29229198/) | 2017 | Clinical study | Arch Med Res | Combined raloxifene and letrozole in breast cancer cell lines, aimed at offsetting bone adverse effects |

---

## Canada Market Information

Letrozole holds 20 valid single-ingredient authorisations in Canada, with no cancelled licences. The records compiled for this report do not include dosage form or approved indication text. The first five licences are shown below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02231384 | FEMARA | Not listed | Not listed |
| 02309114 | PMS-LETROZOLE | Not listed | Not listed |
| 02343657 | TEVA-LETROZOLE | Not listed | Not listed |
| 02358514 | APO-LETROZOLE | Not listed | Not listed |
| 02344815 | SANDOZ LETROZOLE | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted endocrine therapy (aromatase inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low as a single agent; haematological toxicity in combinations is driven mainly by the partner drug (for example CDK4/6 inhibitors) |
| Emetogenicity Classification | Low |
| Monitoring Items | Please refer to the package insert warnings and precautions; bone density and liver function are commonly followed (see Safety Considerations) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

The package insert warnings and contraindications were not available in the data compiled for this report, so label-based safety review could not be completed.

- **Disease associations flagged by the knowledge graph** (not label text): liver failure, cirrhosis of the liver, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), osteoporosis (including postmenopausal osteoporosis) and cerebrovascular disorder. These should be checked against the official label.
- **Drug interactions**: 100 interactions were identified. The only one graded in the data shown is **aprepitant (Moderate)**. Others listed with an unknown severity level include calcitriol, glimepiride, lansoprazole, dolasetron, granisetron, famotidine, acetylsalicylic acid, pantoprazole, morphine, metformin, omeprazole, rosiglitazone, simvastatin and prednisone.
- Literature reports include bone loss, arthralgia and rare cases of maculopathy during letrozole therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Multiple completed Phase 3 trials (PALOMA-2, MONALEESA-2 and related studies) and a large body of publications support letrozole in hormone receptor-positive breast cancer. This is an established, marketed use, so it is not a true repurposing opportunity.
- Safety data from the label are incomplete, and the nine other predicted indications range from well supported (ER-positive disease) to unsupported (ER-negative disease, benign breast conditions, a mouse tumour model).

**To proceed, the following is needed:**
- Download and review the Health Canada package insert for warnings and contraindications (a blocking gap for safety screening).
- Obtain mechanism of action data from DrugBank.
- Confirm the approved indication text for the Canadian licences.
- Review the liver, bone and cerebrovascular flags and the moderate aprepitant interaction.
- Treat ER-negative, benign breast and Ehrlich tumour predictions as Hold, since they lack supporting clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

