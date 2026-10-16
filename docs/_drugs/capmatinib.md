---
layout: default
title: Capmatinib
parent: Model Prediction Only (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Capmatinib: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not available in the compiled data (Health Canada indication text is…"
---

# Capmatinib
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

# Capmatinib: From an Unspecified Original Indication to Rheumatoid Arthritis

## One-Sentence Summary

Capmatinib is a selective MET tyrosine kinase inhibitor marketed in Canada as TABRECTA. The approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 clinical trials** and only **1 general review article** behind this prediction, so it is currently a computational hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (Health Canada indication text is empty) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on the drug's known class, capmatinib is a selective inhibitor of the MET receptor tyrosine kinase.

MET signaling has been implicated in synovial inflammation and angiogenesis in rheumatoid arthritis, so a biologically plausible link exists. However, it is unproven. The only linked publication is a general review of FDA-approved kinase inhibitors, and it contains no RA-specific data. The high TxGNN score reflects a computational prediction, not clinical or experimental confirmation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | 2021 update on the properties of FDA-approved small-molecule protein kinase inhibitors; general overview with no RA-specific data |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02527405 | TABRECTA | Not specified | Not specified |
| 02527391 | TABRECTA | Not specified | Not specified |

---

## Cytotoxicity

Capmatinib is a targeted anticancer therapy (MET kinase inhibitor), but no cytotoxicity data are available in the compiled data. Please refer to the package insert warnings and precautions.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the DDInter database; 20 are listed in the compiled data. Notable ones:
  - **Major**: Dexamethasone, Clarithromycin
  - **Moderate**: Metformin, Alosetron, Loperamide, Aprepitant, Empagliflozin, Glycerol phenylbutyrate, Methylnaltrexone, Metreleptin, Naldemedine, Naltrexone
  - **Minor**: Rabeprazole, Dexlansoprazole, Esomeprazole, Fidaxomicin, Lansoprazole, Naloxegol, Omeprazole, Pantoprazole

Warnings and contraindications from the package insert were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, and the single linked publication is a general kinase inhibitor review with no RA-specific data. Package insert safety data and mechanism of action data are also missing.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications, and approved indications (currently blocking safety screening)
- Mechanism of action data to support the MET–RA link
- Preclinical studies of MET inhibition in RA models (e.g., synovial inflammation, angiogenesis)
- A safety assessment for use in a non-oncology chronic inflammatory setting

---

### Other Predictions (for reference)

Of the other nine predictions, only **heart disease** (score 98.64%, evidence level L4) has any supporting literature. A 2020 mouse study (PMID [32333917](https://pubmed.ncbi.nlm.nih.gov/32333917/)) suggested capmatinib may offset doxorubicin cardiotoxicity and cisplatin nephrotoxicity. This is indirect preclinical evidence in a drug-toxicity setting, not evidence for treating established heart disease. It is best treated as a research question. The remaining eight predictions (mostly rare congenital syndromes and hyperthyroidism) have no identifiable mechanistic rationale or supporting evidence and are likely knowledge-graph artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

