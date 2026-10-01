---
layout: default
title: Sacubitril
parent: Model Prediction Only (L5)
nav_order: 824
evidence_level: L5
indication_count: 5
---

# Sacubitril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Sacubitril: From Heart Failure to Brain Small Vessel Disease 1 (With or Without Ocular Anomalies)

## One-Sentence Summary

Sacubitril is the neprilysin-inhibitor component of sacubitril/valsartan, a combination used for heart failure.
The TxGNN model predicts it may be effective for **brain small vessel disease 1 with or without ocular anomalies**, but there are **0 clinical trials** and **18 publications** on the disease, none of which study sacubitril.
This is a graph-based prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure (the Canadian license records contain no indication text, so this comes from the drug's known use as sacubitril/valsartan) |
| Predicted New Indication | Brain small vessel disease 1 with or without ocular anomalies |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Sacubitril is a prodrug of a neprilysin inhibitor. In sacubitril/valsartan it is combined with valsartan, an AT1 receptor blocker. Together they raise natriuretic peptides and reduce angiotensin II signalling, which is the basis of its use in heart failure.

The predicted disease is a monogenic (COL4A1-related) basement-membrane disorder. Neprilysin inhibition and AT1 blockade do not address that underlying defect, so no plausible mechanistic link was identified. The very high score (99.58%) reflects patterns in the knowledge graph, not biological or clinical support. This prediction should be treated as a weak signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The retrieved papers concern the disease area (congenital ocular anomalies and related syndromes). None evaluates sacubitril or sacubitril/valsartan. The papers below are a sample of the 18 retrieved, all reviews or case descriptions.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35882526](https://pubmed.ncbi.nlm.nih.gov/35882526/) | 2023 | Review | J Med Genet | Axenfeld-Rieger syndrome: anterior segment anomalies with variable systemic features |
| [39097141](https://pubmed.ncbi.nlm.nih.gov/39097141/) | 2024 | Review | Prog Retin Eye Res | Genotype-phenotype correlations in congenital anterior segment ocular disorders |
| [36926528](https://pubmed.ncbi.nlm.nih.gov/36926528/) | 2023 | Review | Clin Ophthalmol | Ocular manifestations of Axenfeld-Rieger syndrome (FOXC1/PITX2) |
| [37468646](https://pubmed.ncbi.nlm.nih.gov/37468646/) | 2024 | Review | Pediatr Nephrol | Ocular manifestations of congenital kidney and urinary tract anomalies |
| [30182440](https://pubmed.ncbi.nlm.nih.gov/30182440/) | 2018 | Review | Am J Med Genet C | Neuropathology of holoprosencephaly |
| [33870948](https://pubmed.ncbi.nlm.nih.gov/33870948/) | 2022 | Review | J Neuroophthalmol | Optic nerve aplasia: ophthalmologic, systemic and genetic findings |
| [11941259](https://pubmed.ncbi.nlm.nih.gov/11941259/) | 2002 | Review | J Fr Ophtalmol | Congenital megalocornea and its association with glaucoma |
| [10498002](https://pubmed.ncbi.nlm.nih.gov/10498002/) | 1999 | Review | Optom Vis Sci | Tilted disc syndrome: features and complications |

---

## Canada Market Information

Showing 5 of 9 authorizations. Dosage form and approved indication text are not populated in the records.

| DIN | Product Name |
|---------|------|
| 02446936 | ENTRESTO |
| 02446928 | ENTRESTO |
| 02564432 | PMS-SACUBITRIL-VALSARTAN |
| 02564440 | PMS-SACUBITRIL-VALSARTAN |
| 02549018 | SANDOZ SACUBITRIL-VALSARTAN |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no trials, no drug-specific literature, and no plausible mechanism linking neprilysin/AT1 blockade to this monogenic disorder. The high score is a graph-based prediction only.

**Other candidates in this pack:**
- **Diabetic nephropathy** (score 99.50%, L4, Research Question) is the strongest of the five predictions.
  - It has a plausible mechanism and consistent preclinical renal-protection data.
  - It has indirect clinical support: a PARADIGM-HF secondary analysis and a small BOLD-MRI study.
  - One Phase 4 trial, [NCT06501651](https://clinicaltrials.gov/study/NCT06501651), is not yet recruiting.
  - No Phase 3 RCT shows a renal outcome benefit.
- The other three candidates (autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome, rheumatoid arthritis, hemoglobinopathy) have no supporting evidence and are also on Hold.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block the safety screening step
- Detailed mechanism of action data from DrugBank
- A defensible mechanistic hypothesis and preclinical data for this disease before any further investment

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

