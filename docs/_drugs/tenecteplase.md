---
layout: default
title: Tenecteplase
parent: Model Prediction Only (L5)
nav_order: 884
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: From Unspecified Original Indication to Posterolateral Myocardial Infarction

## One-Sentence Summary

Tenecteplase is a fibrin-specific clot-dissolving (thrombolytic) drug marketed in Canada under the brand TNKASE, but no original indication is recorded in the input data.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but **0 clinical trials** and **0 publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available licence data |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tenecteplase is a variant of tissue plasminogen activator that acts on fibrin, so it can dissolve the blood clots that block coronary arteries during a heart attack.

Posterolateral myocardial infarction is an anatomical subtype of acute myocardial infarction, not a distinct disease target. Because the clot-dissolving mechanism applies to any acute infarction caused by a coronary clot, the prediction is mechanistically plausible. However, the input lists no original indication, so whether the existing Canadian label already covers myocardial infarction must be verified separately. No trials or literature specific to this subtype were provided.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2244826 | TNKASE | Not listed | Not listed |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the available data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials or publications for this subtype, and the pack gives no original indication or safety data to check it against. The mechanism is plausible, but because the subtype is part of the broader myocardial infarction category, the question is better judged against the existing label than as a new repurposing target.

**To proceed, the following is needed:**
- The approved indication text, dosage form and manufacturer for DIN 2244826 from Health Canada, to confirm whether myocardial infarction is already covered
- Package insert warnings and contraindications, which are required before any safety screening (this is currently a blocking gap)
- Mechanism of action data from DrugBank
- Subtype-specific clinical evidence for posterolateral myocardial infarction, if the subtype is to be pursued as a separate target

**Other candidates in the same prediction set:**
- **Coronary stenosis** has the strongest evidence among the ten predictions (Evidence Level L2, Research Question). It is supported by a completed Phase 2 randomized trial of low-dose intracoronary tenecteplase during primary PCI, [NCT00604695](https://clinicaltrials.gov/study/NCT00604695) (n=40), and a related feasibility and safety report, [PMID 31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/). The trial population is acute heart attack patients undergoing PCI, so the fit to the stated indication is only partial.
- **Congenital coronary artery anomaly** has only a case report in which fibrinolysis was unsuccessful, which is mildly negative evidence.
- **Septal myocardial infarction** has only indirect evidence, from pulmonary embolism papers.
- Five predictions have no plausible mechanism and no evidence: partial deletion of the short arm of chromosome 16, beta-thalassemia, glucophosphate isomerase deficiency hemolytic anemia, hereditary pyropoikilocytosis and pyruvate kinase deficiency. Their high scores are likely network artifacts.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

