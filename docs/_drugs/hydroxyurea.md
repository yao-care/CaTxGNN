---
layout: default
title: Hydroxyurea
parent: Moderate Evidence (L3-L4)
nav_order: 460
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Hydroxyurea: predicted new indication Female breast carcinoma (evidence level L4). Approved use: Melanoma"
monitor_inn: "HYDROXYUREA"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin c disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
---

# Hydroxyurea
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Hydroxyurea: From Melanoma and Sickle Cell Anemia to Female Breast Carcinoma

## One-Sentence Summary

Hydroxyurea is an oral antimetabolite originally used for melanoma, ovarian cancer and sickle cell anemia.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but this is a model prediction only, with **no registered clinical trials** and only preclinical or indirect literature behind it.
The best-supported repurposing direction in the compiled data is a related one, **sickle cell-hemoglobin C disease**, which has **1 Phase 2 trial** and several clinical publications (see the Conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma; sickle cell anemia; ovarian cancer (the Canadian licence records contain no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the drug database records. Based on the literature compiled for this report, hydroxyurea inhibits ribonucleotide reductase, which depletes the pool of DNA building blocks (dNTPs) and causes replication stress in dividing cells. This is the basis of its use in cancer.

Several preclinical studies link this mechanism to breast cancer biology. They cover replication stress avoidance, RPA2 hyperphosphorylation-mediated DNA repair, and ATR inhibitor sensitization. One study showed that valproic acid sensitizes breast cancer cells to hydroxyurea. An in-silico study explored hydroxyurea–lipid conjugates for breast cancer.

However, hydroxyurea is not an established breast cancer therapy. The clinical literature consists of old Phase I combination regimens (5-FU, leucovorin, hydroxyurea, with or without cisplatin) in mixed solid tumours. The very high TxGNN score is therefore a computational prediction and is not backed by clinical efficacy data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for female breast carcinoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase I | Cancer Chemother Pharmacol | 5-FU, leucovorin, hydroxyurea and escalating cisplatin with radiotherapy in advanced solid tumours; dose-finding study |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I | Am J Clin Oncol | Allopurinol, 5-FU/leucovorin followed by hydroxyurea in 20 patients with advanced GI and breast cancer |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico/Preclinical | Drug Research | Hydroxyurea–lipid conjugates designed to improve uptake in breast cancer, targeting PI3K/AKT/mTOR |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitizes breast cancer cells to hydroxyurea by inhibiting RPA2-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | A valproic acid analogue as a potential breast carcinoma therapeutic acting on the same repair pathway |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | Preclinical | Mol Cancer | EYA4 promotes breast cancer progression through replication stress avoidance |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | Br J Cancer | ATR inhibitor NU6027 evaluated in breast and ovarian cancer cell lines |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Rep Hematol | Breast cancer coexisting with essential thrombocythemia; treatment challenges |
| [9060546](https://pubmed.ncbi.nlm.nih.gov/9060546/) | 1997 | Clinical series | J Clin Oncol | TPDC-FuHu combination (including hydroxyurea) in recurrent metastatic brain tumours; indirect |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclinical | Mol Pharmacol | RNR inhibitor COH29 inhibits DNA repair in BRCA1-defective breast cancer cells; hydroxyurea cited as a related RNR inhibitor |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247937 | APO-HYDROXYUREA | Not listed | Not listed |
| 00465283 | HYDREA | Not listed | Not listed |
| 02530260 | RIVA-HYDROXYUREA | Not listed | Not listed |
| 02242920 | MYLAN-HYDROXYUREA | Not listed | Not listed |

All four are valid single-ingredient licences.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | High. The literature reports thrombocytopenia as the main side effect in children with HbSC, and the knowledge graph links the drug to leukopenia, anemia and thrombocytopenia |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential and platelets, kidney function, liver function |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, pyoureter, thrombocytopenia, anemia, macrocytic anemia, leukopenia, cutaneous vasculitis.
- **Drug Interactions**: 100 interactions were found in the DDI query. Only the first 20 were retrieved. One is rated Minor (levofloxacin). The remainder, including doxycycline, amphotericin B, hydrocortisone, famotidine, acetylsalicylic acid, pantoprazole, metformin, omeprazole, morphine, vancomycin, prednisone and simvastatin, have no severity rating.

Please refer to the package insert for the official warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold** (for female breast carcinoma)

**Rationale:**
- The prediction score is very high, but there are no clinical trials and the literature is preclinical or old Phase I combination work. Hydroxyurea is not an established breast cancer treatment.
- Among the other predictions, **sickle cell-hemoglobin C disease** is the strongest (L2, Proceed with Guardrails). It has a terminated Phase 2 trial (NCT00532883, n=44), a 2025 NEJM Evidence study, observational cohorts, and Cochrane reviews on hydroxyurea in sickle cell disease. Sickle cell-beta-thalassemia has moderate support (L3), and the remaining predictions are L4–L5, "Hold" level.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block the safety screen
- Detailed mechanism-of-action data from DrugBank
- For breast cancer: well-designed preclinical validation, then a prospective trial before any clinical consideration
- For HbSC disease: confirmation in adequately powered prospective trials, myelosuppression monitoring, and selection of patients with severe disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

