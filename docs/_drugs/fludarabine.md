---
layout: default
title: Fludarabine
parent: Model Prediction Only (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fludarabine: predicted new indication Plasma cell myeloma (evidence level L5). Approved use: Not available in the data compiled for this report"
---

# Fludarabine
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

# Fludarabine: From Hematologic Malignancy Therapy to Plasma Cell Myeloma

## One-Sentence Summary

Fludarabine is a purine nucleoside analog chemotherapy drug that is marketed in Canada. The data compiled for this report do not include its approved indication text.
The TxGNN model predicts it may be effective for **plasma cell myeloma**, with **31 registered clinical trials** and **20 publications** in this direction. Nearly all of this evidence tests fludarabine as part of a regimen (transplant conditioning or CAR-T lymphodepletion), not as a stand-alone myeloma treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Plasma cell myeloma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 (conditioning and lymphodepletion use; mostly Phase 1–2 trials, with Phase 3 CAR-T trials in which fludarabine is only part of the lymphodepletion) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, fludarabine is a purine nucleoside analog that inhibits DNA synthesis and induces apoptosis in lymphoid cells.

In myeloma, it is used mainly in two ways:
- **Lymphodepletion** (usually with cyclophosphamide) before BCMA-directed CAR-T therapy.
- **Reduced-intensity conditioning** before allogeneic stem cell transplant, combined with busulfan, melphalan, or treosulfan.

Preclinical work (PMID 17976186) also shows some direct antimyeloma activity, including in a myeloma cell line (RPMI8226) and in vivo. Taken together, the prediction is plausible as a regimen component. It is not supported as a stand-alone antimyeloma agent.

---

## Clinical Trial Evidence

The 10 most relevant of the 31 trials are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03303950](https://clinicaltrials.gov/study/NCT03303950) | Phase 2 | Terminated | 6 | Busulfan/fludarabine/cyclophosphamide transplant conditioning in myeloma or myelofibrosis; stopped early |
| [NCT06045806](https://clinicaltrials.gov/study/NCT06045806) | Phase 3 | Active, not recruiting | 79 | Ide-cel plus lenalidomide maintenance vs lenalidomide alone (KarMMa-9); fludarabine is part of lymphodepletion only |
| [NCT07764978](https://clinicaltrials.gov/study/NCT07764978) | Phase 3 | Recruiting | 750 | AZD0120 BCMA/CD19 CAR-T consolidation in transplant-ineligible newly diagnosed myeloma (DURGA-5); fludarabine is likely in the lymphodepletion backbone |
| [NCT06413498](https://clinicaltrials.gov/study/NCT06413498) | Phase 3 | Active, not recruiting | 452 | Anitocabtagene autoleucel vs standard care in relapsed/refractory myeloma (iMMagine-3) |
| [NCT01658319](https://clinicaltrials.gov/study/NCT01658319) | Phase 1 | Completed | 20 | Fludarabine plus methoxyamine (TRC102) in relapsed/refractory hematologic malignancies; mixed population |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | Completed | 16 | Sequential autologous then nonmyeloablative haploidentical transplant in high-risk lymphoma, myeloma, or CLL |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Completed | 213 | Cord blood transplant with cyclophosphamide/fludarabine/TBI conditioning; mixed hematologic diseases |
| [NCT00014508](https://clinicaltrials.gov/study/NCT00014508) | Phase 2 | Completed | N/A | Autologous transplant followed by mini-allogeneic transplant for myeloma |
| [NCT05020444](https://clinicaltrials.gov/study/NCT05020444) | Phase 1 | Active, not recruiting | 16 | TriPRIL CAR-T in relapsed/refractory myeloma; fludarabine and cyclophosphamide used for lymphodepletion |
| [NCT05577000](https://clinicaltrials.gov/study/NCT05577000) | Phase 1b | Active, not recruiting | 5 | Anti-BCMA CAR-T in relapsed/refractory myeloma; fludarabine only as lymphodepletion |

---

## Literature Evidence

The 10 most relevant of the 20 publications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17976186](https://pubmed.ncbi.nlm.nih.gov/17976186/) | 2007 | Preclinical | Eur J Haematol | Fludarabine inhibited myeloma cells in vitro and in vivo |
| [38483213](https://pubmed.ncbi.nlm.nih.gov/38483213/) | 2024 | Phase 1 trial | Am J Clin Oncol | Bortezomib, fludarabine, and melphalan conditioning with or without total marrow irradiation before allogeneic transplant in high-risk myeloma |
| [17310135](https://pubmed.ncbi.nlm.nih.gov/17310135/) | 2007 | Cohort | Bone Marrow Transplant | Reduced-toxicity fludarabine/treosulfan conditioning in 34 myeloma patients |
| [37701906](https://pubmed.ncbi.nlm.nih.gov/37701906/) | 2023 | Phase 2 | Leuk Res Rep | Split-dose busulfan/fludarabine/cyclophosphamide allogeneic transplant (2 myeloma patients, 4 myelofibrosis); 33.3% non-relapse mortality at 1 year |
| [40972962](https://pubmed.ncbi.nlm.nih.gov/40972962/) | 2025 | Real-world study | Transplant Cell Ther | Fludarabine exposure during lymphodepletion was associated with toxicities after ide-cel |
| [39365257](https://pubmed.ncbi.nlm.nih.gov/39365257/) | 2025 | Cohort | Blood | Standard-of-care cilta-cel in 236 patients with relapsed/refractory myeloma |
| [38659046](https://pubmed.ncbi.nlm.nih.gov/38659046/) | 2024 | Cohort | J Hematol Oncol | 5-year follow-up of LEGEND-2 LCAR-B38M CAR-T |
| [35333600](https://pubmed.ncbi.nlm.nih.gov/35333600/) | 2022 | Cohort | J Clin Oncol | Long-term follow-up of combined BCMA and CD19 CAR-T in myeloma |
| [1415309](https://pubmed.ncbi.nlm.nih.gov/1415309/) | 1992 | Review | Am J Med | Parallels and contrasts between myeloma and CLL |
| [38576761](https://pubmed.ncbi.nlm.nih.gov/38576761/) | 2024 | Review | World J Transplant | Autologous transplant conditioning regimens and CAR-T across diseases |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02438577 | Fludarabine Phosphate Injection, USP | Not specified | Not specified |
| 02283859 | Fludarabine Phosphate for Injection | Not specified | Not specified |
| 02246226 | Fludara | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine nucleoside analog) |
| Myelosuppression Risk | High; significant myelosuppression and neurotoxicity at higher doses are documented in the literature (PMID 23787174, 7525188) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function (dose adjustment is needed in renal impairment) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 potential interactions; 20 are shown in the compiled data. Metronidazole, rosuvastatin, simvastatin, and tinidazole are rated Moderate. Levofloxacin is rated Minor. The remaining listed drugs (for example doxycycline, amphotericin B, omeprazole, and metformin) have no assigned severity (Unknown).
- **Other literature signals**: Therapy-related MDS/AML has been reported after fludarabine combination chemotherapy (PMID 20962860). Fludarabine exposure during CAR-T lymphodepletion has been associated with toxicities after ide-cel (PMID 40972962).

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Fludarabine is already an established component of lymphodepletion for BCMA CAR-T therapy and of reduced-intensity conditioning for allogeneic transplant in myeloma. Evidence is mostly Phase 1–2 and indirect, because fludarabine is a regimen component and not the tested variable. Evidence for stand-alone antimyeloma use is limited to preclinical work.

**To proceed, the following is needed:**
- Approved indication text and package insert warnings and contraindications from Health Canada
- Mechanism of action data
- Studies isolating fludarabine's contribution within conditioning and lymphodepletion regimens (for example, dose and exposure optimization)
- A safety monitoring plan covering myelosuppression, neurotoxicity, and dose adjustment in renal impairment

---

**Other predictions in the data:**
- **Indolent plasma cell myeloma** (score 99.76%, L1, Proceed with Guardrails): supported by Phase 3 conditioning and transplant trials, such as NCT00075478 (TBI vs fludarabine/TBI) and NCT01231412. Fludarabine is again a regimen component.
- **Myelodysplastic syndrome** (score 99.75%, L1, Proceed with Guardrails): supported by randomized evidence for treosulfan vs busulfan, each combined with fludarabine, in older patients with AML/MDS (PMID 31606445, 35617104).
- **Unclassified myelodysplastic syndrome** (L3, research question): a single non-randomized phase II study (PMID 21659356).
- **Hyperthyroidism, diabetic nephropathy, and several rare genetic disorders**: no plausible mechanistic link and no supporting evidence. Hold, since these are likely graph artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

