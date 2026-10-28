---
layout: default
title: Natalizumab
parent: Model Prediction Only (L5)
nav_order: 644
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
monitor_inn: "NATALIZUMAB"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
description: "Natalizumab: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Natalizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Natalizumab: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Natalizumab is a monoclonal antibody originally used for multiple sclerosis and inflammatory bowel conditions, including Crohn's disease.
The TxGNN model predicts it may be effective for **bronchitis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, natalizumab is a monoclonal antibody that blocks alpha-4 integrin and so inhibits leukocyte trafficking into inflamed tissue. Its efficacy in multiple sclerosis and Crohn's disease is established, and mechanistically it might dampen leukocyte-driven inflammation in the airways.

The link to bronchitis is theoretical. The high TxGNN score (0.9904) is a prediction only, and no trials or literature were found to support it. Natalizumab's immunosuppressive effect may also raise the risk of respiratory infections, so the net direction of effect is unclear.

## Other Predicted Indications Reviewed

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Evidence Summary |
|------|------|------|------|------|
| 2 | Parapsoriasis | 0.9937 | L5 | One case report (PMID 32470781) of unusual skin adverse events with fingolimod and natalizumab. It suggests a drug-associated event rather than a benefit. |
| 3 | Psoriasis | 0.9919 | L4 | Mixed evidence. Several case reports describe natalizumab-induced or aggravated psoriasis, while one small case series reports improvement in 18 MS patients with comorbid psoriasis. |
| 4 | Severe nonproliferative diabetic retinopathy | 0.9918 | L5 | No trials or literature. The rationale is theoretical (leukocyte adhesion in retinal inflammation). |
| 5 | Acute lichenoid pityriasis | 0.9904 | L5 | The same single case report, which points to an adverse event rather than a therapeutic effect. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For bronchitis (the top prediction), currently no related literature is available.

The most substantial literature relates to the third-ranked prediction, psoriasis. It is summarised here because it is the only indication with a direct clinical signal.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33589543](https://pubmed.ncbi.nlm.nih.gov/33589543/) | 2021 | Cohort/Case series | Neurol Neuroimmunol Neuroinflamm | Natalizumab in 18 MS patients with comorbid psoriasis; psoriasis improvement observed |
| [30323758](https://pubmed.ncbi.nlm.nih.gov/30323758/) | 2018 | Case report/Review | Case Rep Neurol | Plaque psoriasis developed during natalizumab treatment; limited case-based evidence that it can induce or aggravate psoriasis |
| [28905124](https://pubmed.ncbi.nlm.nih.gov/28905124/) | 2018 | Case report/Review | Neurol Sci | Arthritic psoriasis during natalizumab treatment |
| [35646438](https://pubmed.ncbi.nlm.nih.gov/35646438/) | 2022 | Case report | Dermatol Pract Concept | Natalizumab-induced pustular psoriasis of palms and soles |
| [40526577](https://pubmed.ncbi.nlm.nih.gov/40526577/) | 2025 | Review | Dtsch Arztebl Int | Treatment options for MS comorbid with chronic inflammatory diseases, including psoriasis and IBD |
| [25448040](https://pubmed.ncbi.nlm.nih.gov/25448040/) | 2015 | Review | Pharmacol Ther | Leukocyte integrins as therapeutic targets in inflammatory disease |
| [18345706](https://pubmed.ncbi.nlm.nih.gov/18345706/) | 2008 | Review | BioDrugs | Cell adhesion antagonists: therapeutic potential in asthma and COPD (indirect, airway-related) |
| [20298966](https://pubmed.ncbi.nlm.nih.gov/20298966/) | 2010 | Review | Lancet Neurol | PML and other JC virus disorders; notes risk with natalizumab |
| [19647202](https://pubmed.ncbi.nlm.nih.gov/19647202/) | 2009 | Review | Lancet Oncol | PML associated with rituximab, natalizumab and efalizumab (RADAR project) |
| [32470781](https://pubmed.ncbi.nlm.nih.gov/32470781/) | 2020 | Case report | Clin Neurol Neurosurg | Unusual dermatologic adverse events with fingolimod and natalizumab in an MS patient |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02286386 | TYSABRI | Not specified | Not specified |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: progressive multifocal leukoencephalopathy (PML).
- **PML risk**: much of the literature compiled for this report concerns natalizumab-associated PML, a rare and often fatal brain infection caused by JC virus reactivation.
- **Drug interactions**: 100 interactions were identified. The main ones are:
  - **Major**: corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone), mercaptopurine, trimetrexate, levamisole, and radiopharmaceuticals/radioimmunotherapies (iobenguane I-131, ibritumomab tiuxetan, tositumomab).
  - **Moderate**: naltrexone.
  - **Minor**: zinc salts (sulfate, acetate, gluconate, chloride).

Label warnings and contraindications were not available for this report; please refer to the Health Canada package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All predicted indications rest on model scores with no clinical trials. The top prediction, bronchitis, has no supporting literature. For parapsoriasis, psoriasis and acute lichenoid pityriasis, the available reports lean toward adverse events rather than benefit. Systemic immunosuppression and PML risk are not justified without supporting evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Direct preclinical or clinical evidence for bronchitis, including whether the effect on respiratory infection risk is beneficial or harmful
- For psoriasis, a clearer determination of the direction of effect, since case reports of induced or worsened disease conflict with one small case series showing improvement
- Approved indication text and dosage form for the Canadian licence (DIN 02286386)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

