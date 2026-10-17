---
layout: default
title: Carboplatin
parent: High Evidence (L1-L2)
nav_order: 159
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-13
description: "Carboplatin: predicted new indication Female breast carcinoma (evidence level L2). Approved use: Ovarian cancer"
monitor_inn: "CARBOPLATIN"
predicted_indications: ["rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "adult germ cell tumor", "cervical mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma", "endometrial mixed adenocarcinoma", "villoglandular endometrial endometrioid adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
---

# Carboplatin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based chemotherapy drug originally used to treat ovarian cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **41 clinical trials** and **20 publications** currently supporting this direction, including several randomized trials in triple-negative and HER2-positive disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

Note: The Canadian licence records compiled for this report do not include approved indication text. The original indication is therefore taken from the knowledge-graph indication list (ovarian cancer and its subtypes).

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carboplatin is a platinum agent that forms DNA crosslinks, causing DNA damage and cell death. Its efficacy in ovarian cancer is established.

Its activity is greatest in tumours with homologous recombination deficiency, such as BRCA-mutated or triple-negative breast cancer. This is the same DNA-repair vulnerability seen in ovarian cancer, which is the mechanistic bridge between the original and predicted indications. The high TxGNN score (0.9986) is consistent with this shared mechanism.

Several randomized neoadjuvant studies (GeparSixto, CALGB 40603, BrighTNess) support its use, mainly in triple-negative disease. Carboplatin is already used clinically in this setting, so this is not a de novo repurposing signal. Phase 3 evidence in the supplied list tests regimens that contain carboplatin (for example TCH in HER2-positive disease) rather than a clean carboplatin versus no-carboplatin comparison, so the evidence level is capped at L2.

---

## Clinical Trial Evidence

The data include 41 trials for this indication. The most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Carboplatin vs docetaxel in metastatic BRCA-related breast cancer |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Phase 2 | Active, not recruiting | 68 | Carboplatin + nab-paclitaxel ± vorinostat as preoperative therapy in HER2-negative breast cancer |
| [NCT05020860](https://clinicaltrials.gov/study/NCT05020860) | Phase 2 | Recruiting | 185 | Clinical vs pathologic response after neoadjuvant systemic therapy in early breast cancer |
| [NCT00535119](https://clinicaltrials.gov/study/NCT00535119) | Phase 1 | Completed | 107 | Veliparib + carboplatin + paclitaxel in advanced solid tumours (not breast-specific) |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Completed | 3222 | AC-T vs AC-TH vs TCH (docetaxel, carboplatin, trastuzumab) in adjuvant HER2-positive breast cancer |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel + trastuzumab with or without carboplatin in advanced HER2-positive breast cancer |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: two dose-dense neoadjuvant strategies, one including carboplatin, in high-risk early breast cancer |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | Completed | 45 | Neoadjuvant bevacizumab, docetaxel and carboplatin in triple-negative breast cancer |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Completed | 92 | Paclitaxel, carboplatin and trastuzumab first-line in HER2-overexpressing metastatic breast cancer |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | Epirubicin/cyclophosphamide then docetaxel + carboplatin in triple-negative breast cancer (Nigeria) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT | Lancet Oncol | GeparSixto: adding carboplatin to neoadjuvant therapy in triple-negative and HER2-positive early breast cancer |
| [29501363](https://pubmed.ncbi.nlm.nih.gov/29501363/) | 2018 | RCT | Lancet Oncol | BrighTNess: veliparib + carboplatin or carboplatin alone added to neoadjuvant chemotherapy in triple-negative breast cancer |
| [35044810](https://pubmed.ncbi.nlm.nih.gov/35044810/) | 2022 | RCT | J Clin Oncol | CALGB 40603: long-term outcomes of adding carboplatin or bevacizumab in triple-negative breast cancer |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT | Clin Cancer Res | NeoSTOP: anthracycline-free vs anthracycline-containing carboplatin regimens in triple-negative breast cancer |
| [41436191](https://pubmed.ncbi.nlm.nih.gov/41436191/) | 2025 | RCT | BMJ | CITRINE: adjuvant carboplatin-intensified chemotherapy vs standard chemotherapy in high-risk early triple-negative breast cancer |
| [41115255](https://pubmed.ncbi.nlm.nih.gov/41115255/) | 2026 | Phase 3 trial | J Clin Oncol | Adding carboplatin to sequential taxane-anthracycline neoadjuvant chemotherapy in triple-negative breast cancer |
| [38492276](https://pubmed.ncbi.nlm.nih.gov/38492276/) | 2024 | Review | Breast | Platinum chemotherapy for early triple-negative breast cancer |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | Phase 2 RCT | Breast Cancer Res Treat | Carboplatin vs carboplatin + everolimus in advanced triple-negative breast cancer |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | Paclitaxel-carboplatin combination in advanced breast cancer: evidence for synergy, efficacy and safety |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | Targeted and cytotoxic inhibitors used in breast cancer |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02126680 | Carboplatin Injection BP | Injection | Not specified in the available records |
| 02125439 | Carboplatin Injection | Injection | Not specified in the available records |
| 02320371 | Carboplatin Injection BP | Injection | Not specified in the available records |

All three licences are valid single-ingredient products. The dosage form is listed as "Injection" on the basis of the product names; the licence records themselves left this field empty.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum, DNA-crosslinking agent) |
| Myelosuppression Risk | High (thrombocytopenia, neutropenia, leukopenia and anaemia are listed among the drug's knowledge-graph contraindicated conditions) |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential and platelets, renal and liver function, electrolytes, hearing and neurological assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text):** The drug is linked to contraindications in kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anaemia (including macrocytic), blood coagulation disorders, peripheral neuropathy and other peripheral nervous system disease, hearing and auditory disorders, and functional visual loss.
- **Drug Interactions:** 100 interactions were found. Most listed are moderate, including:
  - Proton pump inhibitors: omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole and rabeprazole
  - Aminoglycosides and related antibiotics: kanamycin, neomycin, streptomycin and vancomycin
  - Statins: rosuvastatin and simvastatin
  - Nitroimidazoles: metronidazole and tinidazole

  Levofloxacin is a minor interaction. Calcitriol, glimepiride, mesalazine, doxycycline and clotrimazole have an unknown severity level.

Label-based warnings and contraindications were not available. Please refer to the Canadian package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple randomized Phase 2 and neoadjuvant trials, together with several Phase 3 regimens that contain carboplatin, support its activity in breast cancer, especially triple-negative and HER2-positive disease. Carboplatin is already used in this setting and has three valid Canadian licences. Evidence for carboplatin alone, as opposed to carboplatin-containing combinations, is still limited, and label safety data are missing.

**To proceed, the following is needed:**
- Canadian package insert warnings and contraindications, which were not available for this report
- Mechanism of action data to support the mechanistic analysis
- Confirmation of the approved indication wording for the three DINs
- Subtype-specific evidence review (triple-negative, BRCA-related, HER2-positive), with attention to survival outcomes and not only pathologic complete response
- A haematologic, renal, and neuro/ototoxicity monitoring plan

---

### Other Predicted Indications (Brief)

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|
| Endometrial mixed adenocarcinoma | 99.20% | L1 | Proceed with Guardrails. Carboplatin/paclitaxel is the standard backbone; the Phase 3 trials test add-on agents |
| Adult germ cell tumour | 99.24% | L2 | Research Question. Phase 1/2 high-dose regimens and a systematic review; carboplatin is generally considered less effective than cisplatin in metastatic non-seminoma |
| Cervical mucinous adenocarcinoma | 99.24% | L3 | Research Question. One Phase 1 study and mostly case reports |
| Endometrial mucinous adenocarcinoma | 99.20% | L3 | Research Question. Two Phase 1 studies in mixed gynaecologic populations |
| Rectum, colon, gallbladder and extrahepatic bile duct mucinous adenocarcinoma; villoglandular endometrial endometrioid adenocarcinoma | 99.18–99.28% | L5 | Hold. Prediction based on the model score only, with no supporting trials or relevant literature |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

