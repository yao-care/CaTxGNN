---
layout: default
title: Bleomycin
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Bleomycin: predicted new indication Cauda equina neoplasm . Best-supported: reticulum cell sarcoma… (evidence level L5). Approved use: Hodgkin lymphoma, non-Hodgkin lymphoma, head and neck cancer…"
monitor_inn: "BLEOMYCIN"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "reticulum cell sarcoma", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
---

# Bleomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Bleomycin: From Lymphoma to Reticulum Cell Sarcoma

## One-Sentence Summary

Bleomycin is a cytotoxic antibiotic originally used to treat Hodgkin and non-Hodgkin lymphomas and head and neck cancer.
The TxGNN model's top-ranked prediction is cauda equina neoplasm, but it has no clinical support. The best-supported prediction is **reticulum cell sarcoma** (an obsolete term for diffuse large B-cell lymphoma and related non-Hodgkin lymphomas), with **11 clinical trials** and **20 publications** behind it. This is largely within the existing lymphoma label, so it is closer to indication confirmation than novel repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma, non-Hodgkin lymphoma, head and neck cancer, and other lymphoid neoplasms (the Canadian license records contain no indication text, so these come from the knowledge-graph indication list) |
| Predicted New Indication | Cauda equina neoplasm (rank 1, score-based; no clinical support). Best-supported: reticulum cell sarcoma (rank 3), covered in detail below |
| TxGNN Prediction Score | 99.30% (cauda equina neoplasm); 99.14% (reticulum cell sarcoma) |
| Evidence Level | L1 (reticulum cell sarcoma); L5 (cauda equina neoplasm) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails (reticulum cell sarcoma); Hold for cauda equina neoplasm |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Bleomycin is a cytotoxic agent that breaks DNA strands. Its efficacy in lymphoma is established, and it is a component of several multi-drug regimens.

Reticulum cell sarcoma is an obsolete name for diffuse large B-cell lymphoma and related non-Hodgkin lymphomas, which overlaps with bleomycin's existing lymphoma uses. Bleomycin already appears in regimens such as VACOP-B, MACOP-B, PMitCEBO and PROMACE-CytaBOM. A 1972 report described bleomycin alone in 22 patients with reticulum cell sarcoma, along with Hodgkin disease and lymphosarcoma.

The top-ranked prediction, cauda equina neoplasm, is much weaker. The only linked paper concerns radiotherapy for relapsed CNS germinoma and does not show bleomycin activity in cauda equina tumours. Blood-CNS barrier penetration is also a concern. Other predictions include adult astrocytic tumour (L3, older small studies, no established regimen), primary pulmonary lymphoma (L4, indirect evidence), pulmonary blastoma (L4, two case reports) and well-differentiated fetal adenocarcinoma of the lung (L5, prediction only).

---

## Clinical Trial Evidence

Trials for reticulum cell sarcoma (the other predicted indications have no registered trials):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005867](https://clinicaltrials.gov/study/NCT00005867) | Phase 3 | Completed | 310 | CHOP vs PMitCEBO in good-risk aggressive non-Hodgkin lymphoma |
| [NCT00002835](https://clinicaltrials.gov/study/NCT00002835) | Phase 3 | Completed | 116 | Early intensification vs alternating triple therapy in poor-prognosis lymphoma |
| [NCT00002565](https://clinicaltrials.gov/study/NCT00002565) | Phase 3 | Completed | 61 | Alternating triple therapy vs CHOP in intermediate-grade and immunoblastic lymphoma |
| [NCT00003815](https://clinicaltrials.gov/study/NCT00003815) | Phase 3 | Unknown | N/A | High-dose chemotherapy/radiotherapy with autologous transplant in high-grade NHL; bleomycin's role unclear |
| [NCT00002571](https://clinicaltrials.gov/study/NCT00002571) | Phase 2 | Completed | 52 | PROMACE-CytaBOM with supportive therapy in AIDS-related lymphoma |
| [NCT00002524](https://clinicaltrials.gov/study/NCT00002524) | Phase 2 | Completed | 46 | Combination chemotherapy pilot in AIDS-related lymphoma |
| [NCT00002657](https://clinicaltrials.gov/study/NCT00002657) | Phase 2 | Completed | 20 | PROMACE-CytaBOM with immunosuppression changes and interferon alpha in post-cardiac-transplant lymphoproliferation |
| [NCT00003110](https://clinicaltrials.gov/study/NCT00003110) | Phase 2 | Completed | 5 | 72-hour continuous infusion bleomycin as salvage therapy in NHL; very small |
| [NCT00032149](https://clinicaltrials.gov/study/NCT00032149) | Phase 1/2 | Unknown | 30 | PMitCEBO plus G-CSF in good-prognosis HIV-related lymphoma |
| [NCT00031902](https://clinicaltrials.gov/study/NCT00031902) | Phase 1 | Unknown | N/A | Rituximab plus PVB chemotherapy in HIV-related NHL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4109401](https://pubmed.ncbi.nlm.nih.gov/4109401/) | 1972 | Clinical study | Br Med J | Bleomycin alone in 54 Hodgkin, 17 lymphosarcoma, 22 reticulum cell sarcoma and 7 mycosis fungoides patients after prior therapy; 29% of Hodgkin patients remitted |
| [4107632](https://pubmed.ncbi.nlm.nih.gov/4107632/) | 1971 | Clinical study | Arch Dermatol | Bleomycin in mycosis fungoides and reticulum cell lymphoma |
| [14962711](https://pubmed.ncbi.nlm.nih.gov/14962711/) | 2004 | Trial analysis | Eur J Cancer | Long-term efficacy of the CHVmP/BV regimen (with bleomycin) in 936 patients across three randomised EORTC trials in aggressive NHL |
| [40030008](https://pubmed.ncbi.nlm.nih.gov/40030008/) | 2025 | Cohort | Blood Adv | Interim PET after 4 cycles predicts outcome in primary mediastinal B-cell lymphoma (post hoc analysis of the GAINED phase 3 trial; ACVBP arm includes bleomycin) |
| [24014242](https://pubmed.ncbi.nlm.nih.gov/24014242/) | 2013 | Pooled analysis | Blood | Treatment factors in HIV-associated NHL across 1,546 patients from 19 trials |
| [27888880](https://pubmed.ncbi.nlm.nih.gov/27888880/) | 2016 | Review | Hematol Oncol Clin North Am | Optimizing outcomes in primary mediastinal B-cell lymphoma |
| [15202521](https://pubmed.ncbi.nlm.nih.gov/15202521/) | 2003 | Review | Leuk Lymphoma | Pathobiology of PMBL; MACOP-B followed by radiotherapy suggested as a better induction strategy |
| [15934513](https://pubmed.ncbi.nlm.nih.gov/15934513/) | 2005 | Review | Oncology (Williston Park) | GELA studies in aggressive lymphoma; CHOP alone is not sufficient to cure many patients |
| [6187214](https://pubmed.ncbi.nlm.nih.gov/6187214/) | 1983 | Case report | Am J Med | Fatal hyperpyrexia after bleomycin in a lymphoma patient |
| [11785838](https://pubmed.ncbi.nlm.nih.gov/11785838/) | 2002 | Review | Recent Results Cancer Res | Prognostic factors in HIV-associated NHL, including m-BACOD regimens |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02131692 | BLEOMYCIN FOR INJECTION USP | Not specified | Not specified |
| 02265982 | BLEOMYCIN FOR INJECTION | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-strand-breaking antibiotic) |
| Myelosuppression Risk | Generally low; the 1972 report described bleomycin as marrow-sparing, but it is usually combined with myelosuppressive agents |
| Emetogenicity Classification | Low to moderate; please refer to the package insert |
| Monitoring Items | Pulmonary function and chest imaging, CBC, liver and renal function; watch for hyperpyrexic reactions after the first dose |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Pulmonary toxicity**: Bleomycin pulmonary toxicity and interstitial pneumonitis are well documented in the retrieved literature (PMIDs 4118423, 31668826, 27742539). Risk may rise with age and with combined mediastinal radiotherapy. This is a particular concern for lung-localised diseases such as primary pulmonary lymphoma, pulmonary blastoma and fetal adenocarcinoma of the lung.
- **Hyperpyrexia**: A fatal acute hyperpyrexic reaction has been reported in a lymphoma patient (PMID 6187214), and a test dose is recommended before therapy.
- **CNS delivery**: Systemic delivery to CNS tumours is limited by the blood-brain barrier.
- **Drug interactions**: The interaction screen returned 100 records. The ones available for review are mostly of unknown severity, including pantoprazole, omeprazole, lansoprazole, ondansetron, granisetron, palonosetron, aprepitant, morphine, prednisone, hydrocortisone and vancomycin. Levofloxacin is the only one rated Minor. Please check each against the package insert.

The package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for the full safety profile.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (reticulum cell sarcoma / aggressive non-Hodgkin lymphoma); Hold (cauda equina neoplasm and the other predicted indications)**

**Rationale:**
- Three completed Phase 3 trials and several Phase 2 trials involve bleomycin-containing regimens in aggressive NHL, which supports reticulum cell sarcoma. However, the trials are small, the regimens are older and largely superseded by rituximab-based therapy, and bleomycin's individual contribution cannot be isolated.
- The top-ranked cauda equina neoplasm rests on a model score alone, and the glioma, lung and other predictions have only dated, early-phase or case-level evidence, with pulmonary toxicity as a significant concern.

**To proceed, the following is needed:**
- The Health Canada package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Mechanism-of-action data from DrugBank
- Comparison with current rituximab-based standard of care to establish bleomycin's added value
- A pulmonary function monitoring plan and dose-limit safeguards
- For the CNS and lung predictions, targeted evidence on drug delivery and pulmonary risk before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

