---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Amlodipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a dihydropyridine calcium channel blocker (CCB) established in clinical practice for hypertension and chronic stable angina pectoris.
The TxGNN model ranks **Brain Stem Infarction** as its top predicted new indication with a score of 99.94%; however, **no clinical trials** and **no publications** currently support this specific direction.
Importantly, Amlodipine's cerebrovascular evidence is considerably stronger for related indications — particularly **intracerebral hemorrhage** (rank 10), which is supported by a completed Phase 3 RCT with 1,671 participants.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Chronic stable angina (globally recognised; no Canadian DIN records found in current dataset) |
| Predicted New Indication | Brain Stem Infarction |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed (per current dataset — verification recommended) |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Amlodipine is a dihydropyridine-class CCB that inhibits voltage-gated L-type calcium channels in vascular smooth muscle cells, causing vasodilation, lowering peripheral resistance, and reducing blood pressure. Its efficacy in hypertension and angina pectoris has been extensively proven across decades of clinical use worldwide.

Brain stem infarction is an ischaemic stroke involving the posterior circulation (vertebrobasilar territory), for which hypertension is the single most important modifiable risk factor. By providing sustained blood pressure reduction, Amlodipine could theoretically reduce haemodynamic stress on the small perforating arteries supplying the brain stem, thereby lowering infarction risk. This mechanistic pathway is broadly applicable to all cerebrovascular stroke subtypes, not uniquely to brain stem infarction.

Beyond blood pressure control, animal models of cerebral ischaemia (primarily middle cerebral artery occlusion studies, see Cerebral Artery Occlusion — rank 6 below) suggest that Amlodipine may provide direct neuroprotection through blockade of calcium overload following ischaemic depolarisation and through antioxidative properties. However, no targeted preclinical or clinical studies in brain stem infarction specifically have been identified. The TxGNN high score most likely reflects knowledge-graph proximity between CCB pharmacological nodes and brain stem infarction disease nodes rather than direct experimental validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for brain stem infarction specifically.

---

## Literature Evidence

Currently no related literature available for brain stem infarction specifically.

---

## Other Predicted Indications with Stronger Evidence

The TxGNN model generated predictions across 10 ranked indications. The following carry substantially stronger evidence than top-ranked brain stem infarction and offer more actionable repurposing opportunities:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Key Evidence |
|------|----------------------|-------------|----------------|----------------|--------------|
| 10 | Intracerebral Hemorrhage | 99.79% | **L2** | **Proceed with Guardrails** | TRIDENT Phase 3 completed (n=1,671); NCT07458880 recruiting (n=140) |
| 6 | Cerebral Artery Occlusion | 99.89% | L3 | Research Question | 5 animal studies; 5 indirect clinical trials |
| 8 | MRI Defined Brain Infarct | 99.86% | L4 | Research Question | STEP trial (n=8,000; intensive BP control) |
| 4 | Malignant Renovascular Hypertension | 99.90% | L4 | Research Question | 2 paediatric case reports; strong mechanistic rationale |
| 2 | Pulmonary Hypertension (Lung Disease/Hypoxia) | 99.91% | L5 | **Hold** | Non-specific literature; known safety concern (see Safety section) |

### Intracerebral Hemorrhage — Most Actionable Prediction (Rank 10)

**Clinical Trials:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT: fixed-dose triple antihypertensive pill (CCB/Amlodipine component) vs standard care for prevention of recurrent stroke after intracerebral haemorrhage — primary efficacy trial |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | — | Recruiting | 140 | Triple antihypertensive therapy (including Amlodipine) for blood pressure control after ICH, guided by TRICH scoring — directly targets post-ICH BP management |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1,000 | CASE-J: ARB monotherapy vs ARB + CCB combination in high-cardiovascular-risk Japanese hypertensive patients — indirect evidence comparing CCB-inclusive strategies |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11,414 | IPAD: antihypertensives in T2DM patients with high-normal BP — large BP-intervention trial with ICH as secondary endpoint |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT Cognitive Sub-Study — terminated early, no usable data |

**Literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial Protocol | Int J Stroke | TRIDENT rationale and design: single-pill combination BP therapy (including Amlodipine) to prevent recurrent ICH in high-risk patients |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT Design | Hypertension Res | CASE-J design: ARB vs ARB+CCB strategy in high-risk hypertensive patients — cardiovascular event endpoints including stroke |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Review | Neurol Sci | β-blocker vs CCB comparison in acute ICH blood pressure management; contextualises CCB role in acute cerebrovascular haemorrhage |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Calcium antagonist mechanisms in hypertension and cerebrovascular disease — foundational pharmacology review |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case Report | Ann Pharmacother | Amlodipine-associated angioedema in a right thalamic haemorrhagic stroke patient — safety signal worth noting |

### Cerebral Artery Occlusion — Strongest Preclinical Evidence (Rank 6)

**Literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Animal Study | J Neurosci Res | Amlodipine + atorvastatin reduce infarct size and neuronal apoptosis after transient MCAO in metabolic syndrome rats — antiapoptotic and antiautophagic protection |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | Animal Study | Brain Res | Synergistic neuroprotection with amlodipine + atorvastatin in Zucker rat MCAO model — additive effect on infarct volume reduction |
| [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/) | 2011 | Animal Study | Brain Res | Combination therapy with amlodipine + atorvastatin protects against ischaemic stroke damage in metabolic syndrome model |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Animal Study | Am J Hypertens | Amlodipine reduces stroke size in ApoE-deficient mice after focal cerebral ischaemia — L-type CCB mechanism |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | Animal Study | Brain Res | CCBs with antioxidative effects prevent neuronal damage after focal ischaemia in rats; Amlodipine's antioxidative properties implicated in neuroprotection |

---

## Canada Market Information

No Canadian Drug Identification Number (DIN) records were identified for Amlodipine in the current dataset. This finding is inconsistent with Amlodipine's well-established global availability as a first-line antihypertensive (Norvasc® and numerous generics are known to be approved and marketed in Canada). A verification query against Health Canada's Drug Product Database is strongly recommended before drawing any regulatory conclusions from this data.

---

## Safety Considerations

**Key Safety Note — Pulmonary Hypertension Group 3 (Rank 2 Prediction):**
The mechanistic analysis in this Evidence Pack flags a clinically important contraindication. In WHO Group 3 pulmonary hypertension (arising from lung disease and/or hypoxia), CCBs such as Amlodipine may cause systemic vasodilation without selective pulmonary vasodilation, worsening ventilation-perfusion (V/Q) mismatch and aggravating hypoxaemia. Current guidelines restrict CCB use in pulmonary hypertension to WHO Group 1 patients with demonstrated acute vasoreactivity. This rank 2 prediction should therefore be considered a **safety contraindication** rather than a repurposing opportunity.

For all other indications, please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold** *(for brain stem infarction — TxGNN rank 1 prediction)*

**Rationale:**
The L5 evidence level for brain stem infarction reflects a model prediction only — no clinical trials, observational studies, or targeted preclinical data have been identified for this specific anatomical stroke subtype. Advancing a repurposing programme without any supporting evidence is not warranted at this time.

**To proceed, the following is needed:**
- Targeted literature review specifically for Amlodipine or dihydropyridine CCBs in posterior circulation stroke and vertebrobasilar ischaemia
- Mechanism of action (MOA) data retrieval from DrugBank (DB00381) to formalise the pharmacological rationale
- Verification of Canada DIN status via Health Canada's Drug Product Database — the 0-DIN result likely reflects a data pipeline issue rather than actual non-availability
- Safety data retrieval from the drug monograph (TFDA/Health Canada package insert) to complete the S1 safety screening
- **Priority recommendation: Redirect primary evaluation to intracerebral hemorrhage (rank 10)**, where the completed TRIDENT Phase 3 RCT (n=1,671) establishes an L2 evidence level and supports a **"Proceed with Guardrails"** recommendation — this is the most actionable finding in the current Evidence Pack

---

> **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application. All findings should be interpreted in conjunction with full regulatory review and clinical expert assessment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

