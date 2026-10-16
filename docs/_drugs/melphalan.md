---
layout: default
title: Melphalan
parent: Model Prediction Only (L5)
nav_order: 582
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Melphalan: predicted new indication Gonadal germ cell tumor (evidence level L5). Approved use: Ovarian cancer (including ovarian adenocarcinoma and several ovarian…"
monitor_inn: "MELPHALAN"
predicted_indications: ["gonadal germ cell tumor", "ovarian primitive germ cell tumor", "choriocarcinoma of ovary", "female breast carcinoma", "malignant non-epithelial tumor of ovary", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "endometrial mucinous adenocarcinoma"]
---

# Melphalan
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

# Melphalan: From Ovarian Cancer to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is an alkylating chemotherapy drug, originally used to treat ovarian cancer.
The TxGNN model predicts it may be effective for **gonadal germ cell tumor**, a prediction supported by **7 clinical trials** (mostly small, early-phase, high-dose transplant-setting studies, of which only 2 are rated directly relevant) and **1 publication** of limited relevance.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (including ovarian adenocarcinoma and several ovarian histological subtypes) |
| Predicted New Indication | Gonadal germ cell tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 (as assessed in the data compiled for this report; see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

*Note on evidence level:* No trial for this indication is a randomized Phase 2/3 study. The strongest evidence is one completed Phase 2 study (n=64) of a multi-drug high-dose regimen. Under the stricter reading of the level rules, the evidence is closer to L3 to L4. The L2 label should be treated as an upper bound.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, melphalan is a DNA-alkylating agent. It forms interstrand crosslinks that block DNA replication and trigger cell death. Its efficacy in ovarian cancer is established.

Ovarian cancer and gonadal germ cell tumors are both gynaecological or gonadal malignancies, and germ cell tumors are typically chemosensitive. High-dose melphalan with autologous stem cell rescue is a rational salvage strategy for relapsed, poor-prognosis disease, which is the setting studied in the trials below.

Caveats: the TxGNN score is very high, but the model score alone does not show clinical benefit. Melphalan appears in the available trials mainly as one component of multi-drug regimens, so its individual contribution cannot be isolated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy (gemcitabine, docetaxel, melphalan, carboplatin, then ifosfamide, carboplatin, etoposide) for relapsed, poor-prognosis germ-cell tumors; results not summarized in the data |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine cytoprotection in cancer patients, including germ cell tumors |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens with autologous transplant across hematologic malignancies and selected solid tumors; germ cell tumors are a small subset |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan, melphalan and topotecan with autologous transplant in advanced or recurrent tumors; melphalan's contribution cannot be isolated |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | NA | Completed | 174 | Pilot of high-dose chemotherapy regimens with or without total-body irradiation before autologous transplant; mostly hematologic malignancies |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine as chemoprotectant with autologous transplant in pediatric solid and brain tumors; limited melphalan efficacy data |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis; different route and indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Preclinical/Other | Acta - Unio Internationalis Contra Cancrum | Early study of hormonal and alkylating drugs and pituitary follicle-stimulating function; no abstract, and little relevance to clinical efficacy in germ cell tumors |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00004715 | ALKERAN | Not specified | Not specified |
| 02087286 | ALKERAN | Not specified | Not specified |
| 02480026 | TARO-MELPHALAN | Not specified | Not specified |
| 02473348 | MELPHALAN FOR INJECTION | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High (the knowledge graph links melphalan with leukopenia, neutropenia, thrombocytopenia and anemia as contraindication-related conditions; high-dose use requires stem cell rescue) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** kidney disease, thrombocytopenia, anemia (including macrocytic and hemolytic anemia), leukopenia, agranulocytosis, neutropenia (including congenital and idiopathic forms), interstitial lung disease, pulmonary fibrosis, drug-induced liver injury, vasculitis, and pyoureter.
- **Drug Interactions:** 100 interactions were found. Moderate-level interactions include amphotericin B (conventional, lipid complex, cholesteryl sulfate and liposomal forms). Minor-level interactions include cimetidine, levofloxacin, zinc sulfate and zinc gluconate. Others, such as lansoprazole, omeprazole, pantoprazole, famotidine, metformin, prednisone, simvastatin, morphine, vancomycin, granisetron and dolasetron, have an unclassified interaction level.
- Official label warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting trials are small, early-phase, and mostly use melphalan in multi-drug high-dose regimens, so its independent effect cannot be assessed. The only literature is a 1964 non-clinical paper. Chemotherapy for germ cell tumors is well established with other agents, and this drug carries high myelosuppression risk. Other predicted indications (choriocarcinoma of ovary, malignant non-epithelial tumor of ovary, and the mucinous adenocarcinomas of rectum, colon, gallbladder, cervix and endometrium) rest on model prediction alone and are also on hold.

**To proceed, the following is needed:**
- Full results of NCT00936936 and NCT00003425, with germ-cell-specific outcomes
- Comparison against standard salvage regimens for relapsed germ cell tumors
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Approved indication text for each Canadian DIN
- A safety monitoring plan for high-dose use, including stem cell support, renal function and pulmonary toxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

