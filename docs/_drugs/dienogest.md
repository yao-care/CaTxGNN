---
layout: default
title: Dienogest
parent: Model Prediction Only (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Dienogest
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

# Dienogest: From Endometriosis to Amenorrhea

## One-Sentence Summary

Dienogest is a progestin used to treat endometriosis. The Canadian licence records in the Evidence Pack contain no indication text, so this is inferred from the linked trials and literature. The TxGNN model predicts it may be effective for **amenorrhea**, but **none of the 4 linked clinical trials and none of the 6 linked publications tests dienogest as a treatment for amenorrhea**. Amenorrhea is a known effect of dienogest, not a therapeutic target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (inferred from linked studies; licence indication text is empty) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (the Evidence Pack lists L4, but only indirect endometriosis studies are linked) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, dienogest is a progestin that suppresses ovulation and thins the endometrium. Its efficacy in endometriosis is established.

This is also why the prediction is doubtful. Amenorrhea is an expected effect of dienogest treatment and is often reported as an adverse effect in endometriosis patients. It is not a condition the drug treats. The high TxGNN score most likely reflects a drug-disease association in the knowledge graph (the drug causes or is linked to amenorrhea) rather than a therapeutic link.

Mechanistically, there is no evidence that suppressing menstruation would help a patient who already has amenorrhea. The prediction should be treated as a graph artifact until proven otherwise.

---

## Clinical Trial Evidence

All four linked trials study endometriosis, not amenorrhea.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A (observational) | Completed | 968 | Real-world dienogest (Visanne) treatment of endometriosis; amenorrhea is not the target |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A (observational) | Completed | 895 | Quality-of-life and long-term safety of dienogest in Asian women with endometriosis |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | Recruiting | 290 | Non-inferiority RCT of Indinol Forto vs Visanne 2 mg in endometriosis; no results yet |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Active, not recruiting | 138 | Compares two progestin regimens including transdermal estradiol-dienogest in endometriosis, focused on patient satisfaction |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematic Review | BMC Pharmacol Toxicol | Bayesian analysis of adverse events with dienogest in endometriosis and adenomyosis |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Review | Rev Endocr Metab Disord | Endocrine background of hormonal treatments for endometriosis |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Retrospective cohort | Reprod Sci | Long-term efficacy and safety of dienogest in 514 women with ovarian endometrioma |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Other | Eur J Contracept Reprod Health Care | Supports 2 mg dienogest for endometriosis; notes treatment aims to induce amenorrhoea and a hypoestrogenic state |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Review | J Pediatr Adolesc Gynecol | 3-D and VR visualization for Müllerian anomalies; not about dienogest treatment |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Case report | Medicine | Ovarian granulosa cell tumor in a patient with PCOS; not about dienogest treatment |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2374900 | VISANNE |
| 2493055 | ASPEN-DIENOGEST |
| 2498189 | JAMP DIENOGEST |
| 2543613 | M-DIENOGEST |
| 2551683 | MAR-DIENOGEST |

Dosage form and approved indication text were not provided for these authorizations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study tests dienogest as a treatment for amenorrhea, and amenorrhea is a known effect of the drug. The high TxGNN score most likely reflects a knowledge-graph association rather than a therapeutic link. The other nine predictions (primary ovarian failure, breast fibrocystic disease, isolated growth hormone deficiency, and others) are also Hold, with no supporting evidence or a contradictory mechanism.

**To proceed, the following is needed:**
- Confirmation of the approved indication from Health Canada product monographs, since the licence records are empty
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Any clinical evidence that dienogest treats amenorrhea, without which this candidate should not advance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

