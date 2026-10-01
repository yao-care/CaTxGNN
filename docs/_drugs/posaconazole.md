---
layout: default
title: Posaconazole
parent: Model Prediction Only (L5)
nav_order: 747
evidence_level: L5
indication_count: 1
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Posaconazole: From Antifungal Use to Pneumocystosis

## One-Sentence Summary

Posaconazole is a marketed azole antifungal, but the Canadian license records available here do not list its approved indications.
The TxGNN model predicts it may be effective for **pneumocystosis** (score 99.77%), yet **none of the 2 related clinical trials and 5 publications** tests posaconazole against this disease.
The prediction is not supported by a plausible mechanism, so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available license records (azole antifungal class) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only; no study evaluates posaconazole for this disease) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Posaconazole is an azole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which depletes ergosterol in the fungal cell membrane. It is used in high-risk haemato-oncology patients as mould-active prophylaxis against invasive fungal disease. This is consistent with the overview in PMID 26901377.

Pneumocystosis is a fungal-type lung infection, so the model's link to a general antifungal is easy to see. The mechanism, however, argues against the prediction. *Pneumocystis jirovecii* has little or no ergosterol in its membranes and uses cholesterol-like sterols instead. Azoles are generally considered inactive against it. First-line treatment and prophylaxis is trimethoprim-sulfamethoxazole. The high score probably reflects the drug's antifungal class links in the knowledge graph rather than *Pneumocystis*-specific activity.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform protocol comparing post-transplant cyclophosphamide-based GVHD prophylaxis combinations in mismatched unrelated donor stem cell transplant. Posaconazole and *Pneumocystis* are likely only part of supportive care, so there is no direct efficacy evidence (relevance grade C). |
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, not recruiting | 602 | ReSPECT: randomized, double-blind trial of rezafungin versus the standard antimicrobial regimen to prevent invasive fungal disease after allogeneic transplant. Posaconazole is most likely part of the comparator arm, and the trial does not test it against pneumocystosis (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Med Wkly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and *Pneumocystis* pneumonia. Fluconazole and later mould-active posaconazole prophylaxis markedly reduced invasive candidiasis and aspergillosis in high-risk haemato-oncology patients. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | Review of antifungal and other anti-infective penetration into pulmonary epithelial lining fluid. It provides pharmacokinetic context, not evidence of efficacy against pneumocystosis. |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Guideline | Lancet Infect Dis | British Society for Medical Mycology 2025 update on diagnosing serious fungal diseases. It covers diagnostic methods, not posaconazole treatment. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Zhonghua Jie He He Hu Xi Za Zhi | 2025 Chinese guidelines for diagnosing and managing invasive pulmonary fungal disease, aimed especially at non-immunosuppressed patients. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transpl Infect Dis | Retrospective Mayo Clinic cohort of infectious complications in acute GVHD after liver transplantation. It describes infection and antimicrobial patterns, not posaconazole efficacy for pneumocystosis. |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2496259 | SANDOZ POSACONAZOLE |
| 2542021 | GLN-POSACONAZOLE |
| 2530333 | JAMP POSACONAZOLE |
| 2544644 | MINT-POSACONAZOLE |
| 2432676 | POSANOL |

The records list 8 licenses in total, and the 5 above are the main ones shown. Dosage forms and approved indication text are not included in the available records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score has no direct clinical support. The two related trials only involve posaconazole as supportive care or a comparator. The literature is general guidelines and reviews. *Pneumocystis* lacks the ergosterol target that posaconazole acts on, and trimethoprim-sulfamethoxazole is the established standard of care.

**To proceed, the following is needed:**
- Direct evidence, such as in vitro, animal or clinical data, showing posaconazole activity against *Pneumocystis*
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Complete mechanism of action data from DrugBank
- Approved indication text, dosage forms and route information for the Canadian products
- A comparison with trimethoprim-sulfamethoxazole to define any niche, such as patients intolerant of it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

