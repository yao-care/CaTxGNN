---
layout: default
title: Ribociclib
parent: Moderate Evidence (L3-L4)
nav_order: 797
evidence_level: L4
indication_count: 4
---

# Ribociclib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Ribociclib: From HR+/HER2- Breast Cancer to Myeloid Leukemia

## One-Sentence Summary

Ribociclib (marketed in Canada as KISQALI) is a CDK4/6 inhibitor used to treat hormone receptor-positive, HER2-negative breast cancer.
The TxGNN model predicts it may be effective for **myeloid leukemia**, but **no clinical trials** and only **one preclinical paper** support this direction.
A case report even raises a possible safety signal: AML arising after CDK4/6 inhibitor treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2- breast cancer (taken from the trials and literature; the license record has no indication text) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Ribociclib is known as a CDK4/6 inhibitor. CDK4/6 drives cells from G1 into S phase of the cell cycle, so blocking it slows proliferation. In breast cancer, this has been proven effective.

CDK4/6 dependence has been described in AML cell models, which is the basis for the prediction. The only mechanistic paper is an in vitro study of pharmacokinetic drug resistance (ABCB1 and ABCG2 transporters) in AML cells treated with CDK4/6 inhibitors.

The prediction is therefore biologically plausible but unproven. The 99.35% score is a graph-based prediction only. It has not been confirmed by any trial in myeloid leukemia.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclinical (in vitro) | Cancers | CDK4/6 inhibitors studied against pharmacokinetic drug resistance (ABCB1/ABCG2 transporters) in AML cells |
| [30575100](https://pubmed.ncbi.nlm.nih.gov/30575100/) | 2019 | Case report | Am J Hematol | AML with eosinophilia after CDK4/6 inhibitor treatment, linked to underlying clonal hematopoiesis. A possible safety signal, not therapeutic evidence |
| [41641105](https://pubmed.ncbi.nlm.nih.gov/41641105/) | 2026 | Case report | Front Oncol | Vulvar adenocarcinoma in a breast cancer patient. Not relevant to myeloid leukemia |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2473569 | KISQALI |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) |
| Myelosuppression Risk | Myelosuppression is a known class effect of CDK4/6 inhibitors. Neutropenia and thrombocytopenia are reported in the literature, and hematologic toxicity was a dose-limiting concern in the phase 1 combination studies |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count (with differential). For other items, refer to the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Secondary malignancy signal**: One case report describes AML with eosinophilia after CDK4/6 inhibitor treatment, associated with underlying clonal hematopoiesis. This is a single case and does not establish causality, but it needs attention before any use in myeloid disease.

Please refer to the package insert for other safety information, including warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence stays at the model-prediction and preclinical level (L4). There are no clinical trials, and the only myeloid-specific clinical report is a possible adverse event rather than a benefit. This remains a research question, not a development candidate.

Other predicted indications are no stronger. The thrombocytopenia prediction most likely reflects ribociclib causing thrombocytopenia as a side effect, which is the opposite of a therapeutic effect. The two rare hereditary thrombocytopenia predictions have no trials, no literature and no plausible mechanism.

**To proceed, the following is needed:**
- The package insert for safety review (warnings, contraindications, interactions)
- Detailed mechanism of action data (MOA) to support the mechanistic-link analysis
- Further preclinical studies in AML and myeloid leukemia models, beyond the single in vitro paper
- Assessment of the clonal hematopoiesis and secondary-AML safety signal
- At least early-phase clinical data in myeloid leukemia before reconsidering the decision

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

