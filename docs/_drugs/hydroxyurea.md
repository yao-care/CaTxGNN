---
layout: default
title: Hydroxyurea
parent: Model Prediction Only (L5)
nav_order: 460
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "HYDROXYUREA"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin E disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
description: "Hydroxyurea: predicted new indication Female breast carcinoma (evidence level L5). In Canada: 4 DINs (4 marketed)"
---

# Hydroxyurea
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Hydroxyurea: Female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Hydroxyurea is an oral antimetabolite originally used for melanoma, ovarian cancer and sickle cell anemia.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but this is a model prediction only, with **no registered clinical trials** and only preclinical or indirect literature behind it.
The best-supported repurposing direction in the compiled data is a related one, **sickle cell-hemoglobin C disease**, which has **1 Phase 2 trial** and several clinical publications (see the Conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 4 of 4) |
| Number of DINs | 4 (marketed: 4) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for hydroxyurea: "The precise mechanism by which hydroxyurea produces its cytotoxic and cytoreductive effects is not known. However, various studies support the hypothesis that hydroxyurea causes an immediate inhibition of DNA synthesis by acting as a ribonucleotide reductase inhibitor, without interfering with the synthesis of ribonucleic acid or of protein." ([DailyMed: Xromi (hydroxyurea) prescribing information, Nova Laboratories, Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4b37d336-86da-4363-aef1-34a7d3ba973b), label version 2026-02-02; accessed 2026-11-19.) Based on the literature compiled for this report, hydroxyurea inhibits ribonucleotide reductase, which depletes the pool of DNA building blocks (dNTPs) and causes replication stress in dividing cells. This is the basis of its use in cancer.

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

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00465283 | HYDREA | HYDROXYUREA | Marketed |
| 02242920 | MYLAN-HYDROXYUREA | HYDROXYUREA | Marketed |
| 02247937 | APO-HYDROXYUREA | HYDROXYUREA | Marketed |
| 02530260 | RIVA-HYDROXYUREA | HYDROXYUREA | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

All four are valid single-ingredient licences.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the drug database records" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xromi (hydroxyurea) prescribing information, Nova Laboratories, Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4b37d336-86da-4363-aef1-34a7d3ba973b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

