---
layout: default
title: Enfortumab Vedotin
parent: Model Prediction Only (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: From Its Approved Use to Leprosy (Top TxGNN Prediction)

## One-Sentence Summary

Enfortumab vedotin is a Nectin-4-directed antibody-drug conjugate (ADC) carrying an MMAE microtubule-disrupting payload. It is marketed in Canada as PADCEV, but the data compiled for this report do not list an approved indication text.
The TxGNN model's top prediction is **leprosy**, but there are **0 clinical trials** and **0 publications** for it, and no plausible mechanistic link exists.
The only prediction with any clinical-trial support is **HER2 positive breast carcinoma** (rank 10), with **1 Phase 2 trial** and **5 publications**, mostly reviews.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Leprosy (rank 1); HER2 positive breast carcinoma (rank 10) is the only prediction with trial evidence |
| TxGNN Prediction Score | 99.53% (leprosy); 98.99% (HER2 positive breast carcinoma) |
| Evidence Level | L5 (leprosy); L3 (HER2 positive breast carcinoma) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Enfortumab vedotin is known to be a Nectin-4-directed ADC: the antibody delivers the MMAE cytotoxic payload to Nectin-4-expressing cells, where it disrupts microtubules and kills them.

**Leprosy (rank 1):** There is no identifiable mechanistic link. Leprosy is a *Mycobacterium leprae* infection, and a cytotoxic ADC has no known role in treating it. The high score appears to be a knowledge-graph artifact. The same conclusion applies to the other top-ranked predictions with no evidence: multiple endocrine neoplasia, cerebral infarction, HIV infection, homozygous familial hypercholesterolemia, and the two veterinary diseases (infectious bovine rhinotracheitis and malignant catarrh).

**Cytomegalovirus infection and candidiasis (ranks 3-4):** The only publications are an adverse-event case report (severe ulcerative esophagitis after enfortumab vedotin plus pembrolizumab) and a pharmacovigilance study of ADC risk signals. These are safety observations, not efficacy evidence, and the drug has no known antiviral or antifungal activity.

**HER2 positive breast carcinoma (rank 10):** This is the only biologically plausible prediction, though indirect. Nectin-4 is expressed in a substantial fraction of breast cancers, particularly triple-negative and some HER2-positive subtypes, so an MMAE-based Nectin-4 ADC could have activity. The evidence does not yet show efficacy in HER2-positive disease specifically.

---

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction, leprosy. The only relevant trial was found for HER2 positive breast carcinoma (rank 10):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) | Phase 2 | Active, not recruiting | 329 | EV-202: open-label, multicohort study of enfortumab vedotin in locally advanced or metastatic solid tumors. The primary endpoint is confirmed objective response rate. It may include a breast cancer cohort, but is not specific to HER2-positive disease and is non-randomized. Estimated completion is March 2027. |

---

## Literature Evidence

No publications were found for leprosy. For the other predictions, the relevant items are below.

**HER2 positive breast carcinoma (rank 10):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41384708](https://pubmed.ncbi.nlm.nih.gov/41384708/) | 2026 | Review | Histopathology | Molecular pathology of bladder cancer; background on genetic drivers (KMT2D, KDM6A, TP53, PIK3CA, FGFR3, RB1) |
| [42480966](https://pubmed.ncbi.nlm.nih.gov/42480966/) | 2026 | Review | Cancer Letters | ADCs against multidrug-resistant cancers: biomarker-guided selection, payloads, linkers, bystander effects |
| [41654096](https://pubmed.ncbi.nlm.nih.gov/41654096/) | 2026 | Narrative review | Crit Rev Oncol Hematol | Real-world evidence synthesis for 10 recently approved oncology drugs |
| [32315240](https://pubmed.ncbi.nlm.nih.gov/32315240/) | 2020 | Review | ASCO Educational Book | Resurgence of ADCs in cancer therapy: novel targets and payloads |
| [40614854](https://pubmed.ncbi.nlm.nih.gov/40614854/) | 2025 | Preclinical study | Cancer Letters | Polyploid giant cancer cells mediate resistance to HER2-targeting ADCs; does not demonstrate enfortumab vedotin efficacy |

**Cytomegalovirus infection (rank 3) and candidiasis (rank 4):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42647281](https://pubmed.ncbi.nlm.nih.gov/42647281/) | 2026 | Case report | Reports (MDPI) | Severe diffuse ulcerative esophagitis after enfortumab vedotin plus pembrolizumab in metastatic urothelial carcinoma; an adverse event, not evidence of efficacy |
| [41341429](https://pubmed.ncbi.nlm.nih.gov/41341429/) | 2025 | Pharmacovigilance (FAERS) | Clinical Epidemiology | Real-world risk signals of ADCs in bladder cancer; a safety signal, not efficacy |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02521903 | PADCEV | Not available | Not available |
| 02521911 | PADCEV | Not available | Not available |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (antibody-drug conjugate with MMAE, a microtubule-disrupting payload) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; typically CBC, liver and renal function, and blood glucose |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Drug Interactions:** The interaction screen returned 100 interactions in total. Of those listed, most are rated Moderate and mainly involve antidiabetic agents (for example metformin, pioglitazone, glimepiride, glipizide, glyburide, and the gliptin, gliflozin and GLP-1 agonist classes), plus aprepitant. **Clarithromycin** is the one Major interaction listed.
- **Clinical safety signals in the literature:** A case report describes severe ulcerative esophagitis with enfortumab vedotin plus pembrolizumab, and a pharmacovigilance study describes ADC risk signals in bladder cancer.

Please refer to the package insert for warnings and contraindications, which were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions, including leprosy, have no clinical or literature support and no plausible mechanism. They appear to be knowledge-graph artifacts. HER2 positive breast carcinoma is biologically plausible, but the evidence is one non-randomized Phase 2 multicohort trial, not specific to HER2-positive disease, plus reviews, so efficacy is unconfirmed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Approved indication text and dosage form for the two PADCEV DINs
- Mechanism of action data from DrugBank
- For HER2 positive breast carcinoma: confirmation of whether EV-202 includes a breast cancer cohort and its HER2 status, along with Nectin-4 expression data in HER2-positive tumours
- For any other prediction: target expression data and a plausible mechanistic rationale before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

