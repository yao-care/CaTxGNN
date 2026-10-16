---
layout: default
title: Anakinra
parent: Model Prediction Only (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Anakinra: predicted new indication Extracutaneous mastocytoma . Best-supported candidate: autosomal rece… (evidence level L5). Approved use: Rheumatoid arthritis, cryopyrin-associated periodic syndro…"
monitor_inn: "Anakinra"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "hepatic veno-occlusive disease", "peliosis hepatis", "oligoarticular juvenile idiopathic arthritis with anti-nuclear antibodies", "oligoarticular juvenile idiopathic arthritis without anti-nuclear antibodies", "pyogenic autoinflammatory syndrome", "unclassified autoinflammatory syndrome"]
---

# Anakinra
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

# Anakinra: From Rheumatoid Arthritis to Familial Mediterranean Fever

## One-Sentence Summary

Anakinra is an interleukin-1 (IL-1) receptor antagonist, originally used for rheumatoid arthritis and cryopyrin-associated periodic syndromes (including CINCA syndrome).
The TxGNN model's top-ranked prediction is **extracutaneous mastocytoma**, but it has no supporting evidence. The best-supported prediction is **autosomal recessive familial Mediterranean fever (FMF)**, with **0 registered clinical trials** and **20 publications** (mostly reviews and case reports) in the data compiled for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, cryopyrin-associated periodic syndrome, CINCA syndrome (the Health Canada licence record has no indication text) |
| Predicted New Indication | Extracutaneous mastocytoma (rank 1, no evidence). Best-supported candidate: autosomal recessive familial Mediterranean fever (rank 3) |
| TxGNN Prediction Score | 99.93% (extracutaneous mastocytoma); 99.89% (FMF) |
| Evidence Level | L5 (extracutaneous mastocytoma); L3 (FMF) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (extracutaneous mastocytoma); Proceed with Guardrails as a research question for FMF |

> Note: The top-ranked prediction has no trials or literature. This report therefore also evaluates the best-supported candidate, FMF, and briefly summarises the other predictions.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, anakinra is a recombinant IL-1 receptor antagonist. It blocks IL-1 signalling, and its efficacy in IL-1-driven conditions such as cryopyrin-associated periodic syndromes is established. Mechanistically, it may be applicable to other IL-1-driven autoinflammatory diseases.

**FMF (rank 3):** FMF is caused by mutations in the MEFV gene, which encodes pyrin. These mutations lead to inflammasome activation and excess IL-1β. Because anakinra directly blocks this pathway, the link is biologically plausible, and it is close to the original autoinflammatory indications (cryopyrin-associated syndromes). The literature includes IL-1-targeting case series and reviews, and case reports of anakinra in colchicine-resistant patients. This supports a class effect, but no trials were supplied.

**Extracutaneous mastocytoma (rank 1):** A speculative link would be IL-1 signalling in mast-cell-driven inflammation, but nothing in the data supports it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the top 10 predicted indications.

---

## Literature Evidence

No literature was available for the top-ranked prediction (extracutaneous mastocytoma). The table below covers the best-supported prediction, FMF.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Case series / Review | Semin Arthritis Rheum | Evaluates IL-1-targeting drugs in FMF; pyrin is implicated in IL-1 maturation and secretion |
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Review | Clin Rev Allergy Immunol | IL-1β biological treatment of FMF as an option beyond colchicine |
| [26572612](https://pubmed.ncbi.nlm.nih.gov/26572612/) | 2016 | Review | Curr Med Chem | Colchicine, biologic agents and other options for FMF |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Cohort | Rheumatol Int | Canakinumab (not anakinra) effective in FMF resistant or intolerant to colchicine and/or anakinra |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Case report | Nephrol Dial Transplant | Marked benefit of IL-1 inhibitor in FMF complicated by amyloidosis and renal failure |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Case report | Nephrol Dial Transplant | Successful anakinra treatment of FMF and outcome after renal transplantation |
| [20386914](https://pubmed.ncbi.nlm.nih.gov/20386914/) | 2012 | Case report | Rheumatol Int | Efficacy of anakinra in a patient with colchicine-resistant FMF |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Case report | Joint Bone Spine | Myositis in a patient with FMF and spondyloarthritis successfully treated with anakinra |
| [32655029](https://pubmed.ncbi.nlm.nih.gov/32655029/) | 2020 | Case report | Iran J Kidney Dis | Late acute cellular rejection after anakinra in a kidney transplant patient with FMF; possible safety signal |
| [28585601](https://pubmed.ncbi.nlm.nih.gov/28585601/) | 2017 | Case series | J Pak Med Assoc | Anakinra and canakinumab successful in four colchicine-resistant patients |

**Other predictions with limited evidence:**
- **Pyogenic autoinflammatory syndrome (rank 9, L3):** A scoping review of anakinra and canakinumab in PSTPIP1-associated diseases ([38259483](https://pubmed.ncbi.nlm.nih.gov/38259483/)) and an anakinra case report in PAPASH ([39006661](https://pubmed.ncbi.nlm.nih.gov/39006661/)). No trials.
- **Unclassified autoinflammatory syndrome (rank 10, L3):** A single-centre pediatric anakinra experience ([36589607](https://pubmed.ncbi.nlm.nih.gov/36589607/)) and a registry study ([37747561](https://pubmed.ncbi.nlm.nih.gov/37747561/)). Heterogeneous, retrospective evidence.
- **Oligoarticular juvenile idiopathic arthritis (ranks 7 and 8, L4):** Only a general review ([28418334](https://pubmed.ncbi.nlm.nih.gov/28418334/)), with no anakinra-specific data.
- **Aggressive systemic mastocytosis (rank 4, L5):** The two retrieved papers concern Schnitzler syndrome and do not support anakinra use in mastocytosis.
- **Hepatic infarction, hepatic veno-occlusive disease, peliosis hepatis (ranks 2, 5, 6, L5):** No evidence supplied.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02245913 | KINERET | Not specified | Not specified |

---

## Safety Considerations

**Drug Interactions:** 100 interactions were found in the interaction database. The entries shown include:
- **Major:** Deferiprone
- **Moderate:** Corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone, prednisolone, prednisone, triamcinolone), simvastatin, apixaban, rivaroxaban, dicoumarol, and radiopharmaceuticals such as ibritumomab tiuxetan, iobenguane (I-131) and tositumomab
- **Minor:** Zinc salts (acetate, gluconate, sulfate)

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report. One FMF case report (PMID 32655029) described late acute cellular rejection after anakinra in a kidney transplant patient; a causal link is unclear.

---

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction (extracutaneous mastocytoma); Proceed with Guardrails as a research question for FMF**

**Rationale:**
- The top-ranked prediction is based only on the model score, with no trials or literature. The best-supported candidate, FMF, has a clear IL-1 mechanistic basis and consistent case-level reports of benefit in colchicine-resistant disease. However, evidence consists of reviews, case reports and case series, with no registered trials.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Controlled or prospective studies of anakinra in colchicine-resistant FMF
- Approved indication text for the Canadian licence (DIN 02245913)
- For the other autoinflammatory candidates (PAPA/PAPASH spectrum, unclassified autoinflammatory syndromes), more rigorous clinical data before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

