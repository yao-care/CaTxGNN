---
layout: default
title: Posaconazole
parent: Moderate Evidence (L3-L4)
nav_order: 754
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-13
description: "Posaconazole: predicted new indication Pneumocystosis (evidence level L4). Approved use: Chromomycosis, coccidioidomycosis, aspergillosis, sporotrichosis…"
monitor_inn: "POSACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

## Posaconazole: From Invasive Fungal Infections to Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Posaconazole is a triazole antifungal, originally used for fungal infections such as aspergillosis, candidiasis, histoplasmosis and sporotrichosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but the supporting evidence is weak: **1 clinical trial** (which tests a different drug) and **5 publications** (guidelines, reviews and a cohort study, none showing direct efficacy) are currently linked to this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chromomycosis, coccidioidomycosis, aspergillosis, sporotrichosis, histoplasmosis, fusariosis, mycetoma, candidiasis, oral candidiasis and other fungal infections (no approved indication text is available from the Canadian licence records) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, posaconazole is a triazole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis in the fungal cell membrane. Its efficacy in a range of invasive fungal diseases is established, and this is probably why the knowledge graph links it to pneumocystosis.

The mechanistic link is weak, however. *Pneumocystis jirovecii* has no ergosterol in its cell membrane and uses cholesterol and other sterols instead, so the azole mechanism has no clear target in this organism. The very high TxGNN score (0.998) most likely reflects posaconazole's broad association with invasive fungal diseases in the knowledge graph, not a validated mechanism.

The literature gathered so far is indirect. It consists of guidelines and reviews on invasive fungal disease, a study of antifungal penetration into lung epithelial lining fluid, and a cohort study of infections after liver transplantation. None of it shows posaconazole efficacy against Pneumocystis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Rezafungin versus the standard antimicrobial regimen for preventing invasive fungal disease after allogeneic blood and marrow transplantation (ReSPECT). The study tests rezafungin, not posaconazole, so it gives no direct evidence for posaconazole in pneumocystosis. The comparator and endpoints should be verified. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guideline | The Lancet Infectious Diseases | British Society for Medical Mycology 2025 update on best-practice recommendations for diagnosing serious fungal diseases; diagnosis-focused |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Zhonghua Jie He He Hu Xi Za Zhi | 2025 Chinese guidelines for diagnosing and managing invasive pulmonary fungal disease |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis and Pneumocystis pneumonia; notes that mould-active posaconazole prophylaxis reduced invasive fungal disease in high-risk haemato-oncology patients |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Infectious complications and antimicrobial management in acute graft-versus-host disease after liver transplantation |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02496259 | SANDOZ POSACONAZOLE | Not specified | Not specified |
| 02542021 | GLN-POSACONAZOLE | Not specified | Not specified |
| 02530333 | JAMP POSACONAZOLE | Not specified | Not specified |
| 02544644 | MINT-POSACONAZOLE | Not specified | Not specified |
| 02432676 | POSANOL | Not specified | Not specified |

Eight single-ingredient authorizations are currently valid in total; the table lists the first five.

---

## Safety Considerations

**Drug Interactions:** The interaction screening returned 100 interacting drugs in total. The records examined here include the following:

- **Major:** loperamide, triamcinolone, budesonide
- **Moderate:** famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, hydrocortisone, dexamethasone, betamethasone, aprepitant, clarithromycin, saxagliptin, bisacodyl, picosulfuric acid, polyethylene glycol (3350 with electrolytes)

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it rests on posaconazole's general link to fungal diseases. Pneumocystis lacks the ergosterol target of azoles, and no study shows posaconazole efficacy against pneumocystosis. The only registered trial tests a different drug. The evidence is at the model-prediction and indirect-literature level (L4).

**To proceed, the following is needed:**
- Mechanism of action data, plus an explanation of how an azole could act on an organism that lacks ergosterol
- Direct preclinical or clinical studies of posaconazole in Pneumocystis infection, including comparison with the standard treatment (trimethoprim-sulfamethoxazole)
- Package insert warnings and contraindications from Health Canada
- Approved indication text and dosage form for the Canadian licences
- A review of the major drug interactions, especially with corticosteroids, which are often co-prescribed in pneumocystosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

