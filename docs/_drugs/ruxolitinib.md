---
layout: default
title: Ruxolitinib
parent: Model Prediction Only (L5)
nav_order: 829
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "RUXOLITINIB"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease"]
description: "Ruxolitinib: predicted new indication Uterine corpus perivascular epithelioid cell tumor (evidence level L5). Approved use: Not recorded in the local data"
---

# Ruxolitinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Ruxolitinib: Uterine corpus perivascular epithelioid cell tumor
{: .text-alpha }

## One-Sentence Summary

Ruxolitinib is a JAK1/2 inhibitor originally used for myeloproliferative neoplasms, including polycythemia vera and myelofibrosis.
The TxGNN model's top-ranked prediction is **uterine corpus perivascular epithelioid cell tumor (PEComa)**, but that prediction has no supporting studies. The best-supported prediction is **hemophagocytic syndrome associated with an infection**, backed by **20 publications** (no registered clinical trials), mostly retrospective studies, case series and preclinical work.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Uterine corpus perivascular epithelioid cell tumor |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 5 of 5) |
| Number of DINs | 5 (valid: 5) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ruxolitinib is not available in the data compiled for this report. Ruxolitinib is known as a JAK1/2 inhibitor, and its efficacy in myeloproliferative neoplasms is established. Mechanistically, it may be applicable to diseases driven by JAK/STAT signaling.

Hemophagocytic lymphohistiocytosis (HLH) is a life-threatening hyperinflammatory disorder driven by interferon-gamma and other cytokines that signal through JAK/STAT. Blocking JAK1/2 can dampen T-cell activation and cytokine signaling. Murine HLH models (PMID 31015190) and laboratory work (PMID 32530039) support this mechanism. The link to the original indication is the shared reliance on dysregulated JAK/STAT signaling in blood and immune cells.

Other predictions are weaker. For myxoid liposarcoma, two preclinical papers show that JAK-STAT signaling controls cancer stem cell properties and chemotherapy resistance, which is biologically plausible but indirect. For malignancy-associated HLH, the linked papers are a general ICU management article and an unrelated case report, so the evidence is indirect. For the remaining predictions (PEComa variants, lymphangioleiomyomatosis, rhabdoid tumor), no evidence was provided.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. Some publications cite trial registrations (for example ChiCTR2000031702 in PMID 35344583), but no trial records were supplied in the data compiled for this report.

---

## Literature Evidence

Selected publications for hemophagocytic syndrome associated with an infection (the best-supported prediction):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35344583](https://pubmed.ncbi.nlm.nih.gov/35344583/) | 2022 | Clinical study | Blood | Ruxolitinib as first-line agent in pediatric HLH, with treatment stratified by early response |
| [31879790](https://pubmed.ncbi.nlm.nih.gov/31879790/) | 2020 | Retrospective cohort | Ann Hematol | Ruxolitinib for steroid-refractory acute GVHD in 12 patients with EBV-HLH after transplant |
| [33523540](https://pubmed.ncbi.nlm.nih.gov/33523540/) | 2021 | Case series | Eur J Haematol | Ruxolitinib as adjunctive therapy for secondary HLH, with a favorable safety profile |
| [37787838](https://pubmed.ncbi.nlm.nih.gov/37787838/) | 2023 | Case series | Ann Hematol | Sintilimab plus ruxolitinib as compassionate therapy in 12 adults with EBV-HLH |
| [40665481](https://pubmed.ncbi.nlm.nih.gov/40665481/) | 2025 | Retrospective cohort | Br J Haematol | Ruxolitinib-based regimen (n=53) compared with adjusted HLH-94 chemotherapy (n=42) in pediatric EBV-HLH |
| [41934358](https://pubmed.ncbi.nlm.nih.gov/41934358/) | 2026 | Retrospective survey | Pediatr Hematol Oncol | Nationwide Japanese survey of ruxolitinib in 17 children with HLH |
| [31015190](https://pubmed.ncbi.nlm.nih.gov/31015190/) | 2019 | Preclinical | Blood | Mechanisms of ruxolitinib action in murine HLH models |
| [32530039](https://pubmed.ncbi.nlm.nih.gov/32530039/) | 2020 | Preclinical | Blood | JAK/STAT inhibition sensitizes CD8 T cells to dexamethasone-induced apoptosis in hyperinflammation |
| [38691058](https://pubmed.ncbi.nlm.nih.gov/38691058/) | 2024 | Case report | J Pediatr Hematol Oncol | Emapalumab with ruxolitinib and dexamethasone in complicated EBV-HLH |
| [36263041](https://pubmed.ncbi.nlm.nih.gov/36263041/) | 2022 | Case report | Front Immunol | Ruxolitinib as first-line therapy for secondary HLH in patients with AIDS |

Preclinical support for liposarcoma: [35186752](https://pubmed.ncbi.nlm.nih.gov/35186752/) (2022, Front Oncol) and [30650179](https://pubmed.ncbi.nlm.nih.gov/30650179/) (2019, Int J Cancer) link JAK-STAT signaling to cancer stem cell properties and chemotherapy resistance in myxoid liposarcoma.

No randomized controlled trials were identified. Study-type classifications are provisional because some records were truncated.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02552434 | OPZELURA | Not specified | Not specified |
| 02388022 | JAKAVI | Not specified | Not specified |
| 02388014 | JAKAVI | Not specified | Not specified |
| 02434814 | JAKAVI | Not specified | Not specified |
| 02388006 | JAKAVI | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count; infection surveillance (also noted in the HLH guardrails) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions** (100 interactions were recorded; selected examples):
- **Major**: Clarithromycin, Cobicistat, Deferasirox, Deferiprone, Ibritumomab tiuxetan, Tositumomab (including I-131), Samarium (153Sm) lexidronam
- **Moderate**: Dexamethasone, Rosuvastatin, Fenfluramine, Dexfenfluramine, Sibutramine, Troglitazone, Palifermin, Strontium chloride Sr-89
- **Minor**: Aprepitant, Cimetidine, Miconazole, Clotrimazole

Dexamethasone is a standard part of HLH therapy, so that interaction deserves attention in this setting.

Literature on HLH use suggests monitoring for infection and cytopenias. Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For hemophagocytic syndrome associated with an infection, there is a plausible JAK/STAT mechanism, supportive murine data, and multiple clinical series, mostly in EBV-associated HLH. The evidence is retrospective or case-based, with no RCTs or registered trials supplied. The top-scoring predictions (PEComa variants, lymphangioleiomyomatosis) have no supporting evidence and should stay on Hold. Liposarcoma and malignancy-associated HLH are research questions only.

**To proceed, the following is needed:**
- Prospective controlled trials in HLH (and clinical trial registration data)
- Health Canada package insert warnings, contraindications and approved indication text (currently unavailable)
- Detailed mechanism-of-action data
- A safety monitoring plan (infection, cytopenias, interactions such as clarithromycin and cobicistat) for specialist-supervised use
- Further review of the truncated literature records to confirm study classifications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

