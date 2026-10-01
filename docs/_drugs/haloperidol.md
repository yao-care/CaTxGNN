---
layout: default
title: Haloperidol
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Antipsychotic Therapy to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Haloperidol is a dopamine D2-antagonist antipsychotic that is already marketed in Canada. The TxGNN model ranks **congenital disorder of glycosylation with defective fucosylation** as its top new-indication prediction. There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the graph model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records provided |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Haloperidol is known to be a high-affinity dopamine D2 receptor antagonist, and its efficacy as an antipsychotic is well established.

We found no plausible link between D2 antagonism and fucosylation pathways. The disease is a rare inherited defect in protein glycosylation, and nothing in the available data suggests haloperidol would alter it. The very high score (99.91%) reflects the knowledge-graph structure and is not evidence of biological plausibility. This prediction should be treated as a model artifact unless independent evidence emerges.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 363669 | TEVA-HALOPERIDOL | — | — |
| 713449 | TEVA-HALOPERIDOL | — | — |
| 2366010 | HALOPERIDOL INJECTION | — | — |
| 363677 | TEVA-HALOPERIDOL | — | — |
| 363685 | TEVA-HALOPERIDOL | — | — |

The dosage form and approved-indication fields are blank in the records provided. Only 5 of the 9 licences are listed.

## Safety Considerations

Please refer to the package insert for safety information.

## Other Predicted Indications Worth Noting

Only one of the ten predictions has real supporting evidence: **manic bipolar affective disorder** (rank 10, TxGNN score 99.83%, evidence level L1). The other nine, including the top-ranked one above, have no trials and no relevant literature. Several of the retrieved papers, such as those on the orbit and extraocular muscles for rank 2, look like keyword matches.

The mania evidence comes mainly from trials in which haloperidol was a comparator arm:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone vs placebo vs haloperidol as add-on to mood stabilizers in bipolar mania |
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Flexible-dose risperidone vs placebo or haloperidol in manic episodes of bipolar I |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Placebo- and haloperidol-controlled olanzapine trial in manic or mixed episodes |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate-amisulpride vs valproate-haloperidol in bipolar I mania |

Supporting literature includes a 2022 network meta-analysis of double-blind RCTs in bipolar mania ([34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/), *Molecular Psychiatry*) and a Japanese placebo- and haloperidol-controlled olanzapine RCT ([22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/), *Journal of Affective Disorders*).

This is largely an already-recognized antimanic use and not a novel repurposing signal. Also, haloperidol is the comparator in these trials, not the primary study drug.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, congenital disorder of glycosylation with defective fucosylation)

**Rationale:**
The prediction has no clinical, literature or mechanistic support, and it sits at evidence level L5. The high TxGNN score alone does not justify further investment. The mania indication is better supported (Proceed with Guardrails), but it is not a new use.

**To proceed, the following is needed:**
- For the glycosylation disorder: a credible mechanistic hypothesis and preclinical data. Without these, the prediction should be deprioritized.
- For mania: confirmation of Canadian labeling status. The original-indication fields are empty in the current records.
- Health Canada package insert warnings and contraindications, which are missing and block safety screening.
- Mechanism of action data from DrugBank.
- A safety plan covering extrapyramidal symptoms, QT prolongation and tardive dyskinesia, using guideline-based dosing.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

