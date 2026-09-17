---
layout: default
title: Posaconazole
parent: Moderate Evidence (L3-L4)
nav_order: 635
evidence_level: L4
indication_count: 1
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Posaconazole: From Invasive Fungal Infections to Pneumocystosis

## One-Sentence Summary

Posaconazole is a triazole antifungal whose established use targets invasive fungal infections such as aspergillosis and candidiasis. The TxGNN model predicts a possible link to **Pneumocystosis (Pneumocystis pneumonia)**, but this is currently supported only by **2 low-relevance clinical trials** and **5 indirect literature references**, with no evidence specific to posaconazole's efficacy against *Pneumocystis jirovecii*.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (no approved indications recorded for this drug in the data pack; posaconazole is clinically known as a triazole antifungal for mould-active prophylaxis/treatment) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for posaconazole is not available in this data pack (DG002, data gap). However, the repurposing rationale on file describes posaconazole as a triazole antifungal that inhibits 14α-demethylase, blocking ergosterol synthesis, giving it activity against *Aspergillus*, *Candida*, and other filamentous fungi.

This mechanism is the basis of the concern with the current prediction: *Pneumocystis jirovecii* has a cell membrane composed primarily of cholesterol rather than ergosterol, and its life cycle does not depend on ergosterol synthesis to the same degree as typical filamentous fungi. Triazole antifungals therefore lack a solid pharmacological rationale for activity against *Pneumocystis*, and none of the current standard therapies (TMP-SMX, atovaquone, pentamidine) belong to the azole class.

The high TxGNN score (99.98th percentile) most likely reflects a broad "antifungal drug – fungal infection" association learned from the knowledge graph, rather than a specific, mechanistically grounded signal for *Pneumocystis*. This should be treated as a weak or potentially mismatched association rather than confirmed biological plausibility.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform trial comparing GVHD prophylaxis regimens after mismatched unrelated donor stem cell transplant; posaconazole, if present, would appear only as part of broad-spectrum antifungal prophylaxis, not as a targeted pneumocystosis treatment/prevention arm (relevance grade C). |
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Active, not recruiting | 602 | Evaluates rezafungin (an echinocandin, not posaconazole) versus standard antimicrobial regimen to prevent invasive fungal disease after allogeneic transplant; echinocandins have no standard activity against *Pneumocystis*, so this trial is considered database noise for this indication pairing (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis, and *Pneumocystis* pneumonia; notes mould-active posaconazole prophylaxis has reduced invasive candidiasis in high-risk hemato-oncology patients, but does not report direct posaconazole efficacy against *Pneumocystis*. |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review | The Lancet Infectious Diseases | British Society for Medical Mycology 2025 best-practice update on diagnosis of serious fungal diseases; general diagnostic guidance, not posaconazole/pneumocystosis-specific efficacy data. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Review (Guideline) | Zhonghua Jie He He Hu Xi Za Zhi | 2025 Chinese clinical practice guideline for diagnosis/management of invasive pulmonary fungal disease; general guidance, no specific pneumocystosis efficacy data for posaconazole. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | Retrospective review of infectious complications of acute GVHD after liver transplantation; describes infection/antimicrobial management patterns broadly, not a posaconazole-pneumocystosis efficacy study. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Reviews pulmonary epithelial lining fluid penetration of anti-infective agents including antifungals; pharmacokinetic context only, no pneumocystosis efficacy data. |

## Canada Market Information

Posaconazole is not currently marketed in Canada under this data pack (0 licenses on file); no DIN authorizations are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for posaconazole activity against *Pneumocystis jirovecii* is weak — its ergosterol-targeting mechanism does not align well with *Pneumocystis*'s cholesterol-based membrane biology — and no identified clinical trial or literature evidence directly supports efficacy for this indication (both trials graded low relevance, and all literature is indirect/contextual). The high TxGNN score likely reflects a generic antifungal–fungal infection association rather than a validated signal.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (DG001, currently blocking safety review)
- Confirmed mechanism of action and original indication data from DrugBank (DG002)
- Dedicated in vitro or mechanistic studies evaluating posaconazole activity against *Pneumocystis jirovecii*
- A clinical trial specifically designed to test posaconazole for pneumocystosis prevention or treatment, rather than as an incidental component of broad-spectrum antifungal prophylaxis regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

