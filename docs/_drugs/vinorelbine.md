---
layout: default
title: Vinorelbine
parent: High Evidence (L1-L2)
nav_order: 978
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-13
description: "Vinorelbine: predicted new indication Ewing sarcoma (evidence level L2). Approved use: Non-small cell lung carcinoma"
monitor_inn: "VINORELBINE"
predicted_indications: ["Ewing sarcoma", "fibromatosis, gingival", "fibroma of lung", "pulmonary sulcus neoplasm", "lung germ cell tumor", "hamartoma of lung", "small cell lung carcinoma", "lung benign neoplasm", "lung hilum carcinoma", "pulmonary blastoma"]
---

# Vinorelbine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Vinorelbine: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

Vinorelbine is a vinca alkaloid chemotherapy drug, originally used to treat non-small cell lung cancer and lung cancer.
The TxGNN model predicts it may be effective for **Ewing sarcoma**, with **3 clinical trials** and **6 publications** currently supporting this direction.
The evidence is early-stage: the most relevant data are Phase 2 studies in children with relapsed or refractory solid tumours.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma; lung cancer (from the TxGNN knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, vinorelbine is a vinca alkaloid that inhibits microtubule polymerisation. This causes mitotic arrest and apoptosis in rapidly dividing cells.

Ewing sarcoma is an aggressive bone and soft tissue tumour with high relapse rates, especially in metastatic disease. Because vinorelbine acts on all rapidly dividing cells, its activity is not limited to lung cancer. Phase 2 studies have reported activity in relapsed or refractory paediatric solid tumours, including sarcomas. A metronomic combination with low-dose cyclophosphamide has shown activity in this setting. A 2026 review also describes the rationale for vinorelbine plus low-dose cyclophosphamide as maintenance therapy in the planned international INTER-EWING-1 trial. Preclinical work suggests synergy with PLK1 inhibitors in Ewing sarcoma cells.

Note that the link between the original and new indication is mechanistic (general cytotoxic activity) rather than based on shared disease biology. The clinical data so far come mostly from mixed tumour populations rather than Ewing sarcoma alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | Unknown | 210 | Vinorelbine plus cyclophosphamide in refractory or relapsed tumours, including Ewing tumours, rhabdomyosarcoma, osteosarcoma and neuroblastoma. Results are not available. |
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | Completed | 50 | Vinorelbine in children with recurrent or refractory malignancies. Mixed solid tumours, not Ewing sarcoma only. |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | Not applicable | Active, not recruiting | 100 | Prospective cohort of risk-stratified treatment in paediatric Ewing sarcoma in China. Gives outcome and safety context but does not test vinorelbine specifically. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase 2 trial | Eur J Cancer | Vinorelbine with continuous low-dose cyclophosphamide in children and young adults with relapsed or refractory solid tumours. Good tolerance, with efficacy noted in rhabdomyosarcoma. |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Phase 2 trial | Cancer | Vinorelbine in previously treated advanced childhood sarcomas. Activity seen in rhabdomyosarcoma. |
| [42561548](https://pubmed.ncbi.nlm.nih.gov/42561548/) | 2026 | Cohort / systematic review | Cancer Treat Rev | Rationale for vinorelbine plus low-dose cyclophosphamide as maintenance therapy in Ewing sarcoma (INTER-EWING-1 trial). |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Front Pharmacol | Review of chemotherapeutic drugs for soft tissue sarcomas. |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Preclinical | Int J Cancer | PLK1 inhibitor BI 6727 acted synergistically with microtubule-interfering drugs, including vinorelbine, to induce apoptosis in Ewing sarcoma cells. |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case report | BMC Urol | Extraosseous Ewing sarcoma of the kidney. Diagnostic focus, with little relevance to vinorelbine efficacy. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02271214 | Vinorelbine Tartrate for Injection | Not specified | Not specified |
| 02511347 | Vinorelbine Injection, USP | Not specified | Not specified |
| 02431130 | Vinorelbine Injection, USP | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, antimicrotubule agent) |
| Myelosuppression Risk | High. Neutropenia is the dose-limiting toxicity reported in the literature. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver function, signs of infection. Monitor for lung toxicity, given the knowledge graph contraindications listed below. |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindications / cautions (from the knowledge graph, not label text)**: liver failure, infectious disease, ileus, intestinal obstruction, interstitial lung disease, lung disease, rare pulmonary disease, leukopenia.
- **Drug Interactions**: 100 interactions were identified. The main ones listed are:
  - **Major**: clarithromycin.
  - **Moderate**: aprepitant, dexamethasone, metronidazole, eliglustat, miconazole, rolapitant, rosuvastatin, simvastatin, tinidazole, glycerol phenylbutyrate.
  - **Minor**: levofloxacin.
  - Several others, such as pantoprazole, omeprazole, morphine and metformin, are of unknown severity.
- Package insert warnings and contraindications for the Canadian products were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two Phase 2 trials and Phase 2 publications support vinorelbine, mostly with low-dose cyclophosphamide, in relapsed or refractory paediatric solid tumours. Ewing sarcoma is only one of several tumour types studied, and no Ewing-specific efficacy result is available in the data reviewed. The drug is already marketed in Canada, but it is a high-risk cytotoxic agent, so use should be limited to specialist oncology settings.

**To proceed, the following is needed:**
- Ewing sarcoma-specific efficacy data, for example subgroup results from NCT00180947 and NCT00003234, and the outcomes of the INTER-EWING-1 trial.
- Health Canada package insert warnings and contraindications, which are currently missing and block the safety screening.
- Detailed mechanism of action data.
- A safety monitoring plan covering myelosuppression, lung disease and major drug interactions such as clarithromycin.
- Confirmation of the approved indications and dosage forms for the three Canadian DINs.

---

### Other Predicted Indications (Brief Note)

Of the other predictions, small cell lung carcinoma has the highest evidence level (L1, with a Phase 3 trial). However, that evidence is in NSCLC, the original indication, and is not a new repurposing signal. The remaining predictions (gingival fibromatosis, lung fibroma, lung hamartoma, benign lung neoplasm, pulmonary blastoma, lung germ cell tumour, pulmonary sulcus neoplasm and lung hilum carcinoma) have no direct supporting evidence or only indirect evidence. Several of them are benign lesions, for which cytotoxic therapy is not appropriate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

