---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 289
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

# Dipyridamole: From Antiplatelet Therapy to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is an antiplatelet and vasodilating drug, and its injection form is also used as a pharmacologic stress agent for cardiac imaging. The TxGNN model predicts it may be useful for **Prinzmetal angina** (score 99.99%), but there are **0 clinical trials** for this indication and only **15 mostly older publications**, none showing therapeutic benefit. The evidence does not support moving this candidate forward at this time.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records. Dipyridamole is generally known as an antiplatelet agent, and the injection form is used for stress imaging. |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (mechanism and observational literature only, no trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dipyridamole blocks adenosine reuptake, which raises adenosine levels and causes coronary vasodilation. It also inhibits platelet aggregation. A drug that dilates coronary vessels could plausibly be considered for vasospastic angina. Detailed mechanism-of-action data are not available in the Evidence Pack, so this reasoning comes from the rationale notes rather than a curated MOA record.

The link is weak. Most of the retrieved literature describes dipyridamole as a **stress-testing agent** for detecting coronary disease, not as a treatment for vasospasm. One report (PMID 3421166) describes coronary vasospasm triggered in variant angina patients when dipyridamole stress was terminated with aminophylline. That is a **safety or provocation signal**, not a benefit. Vasodilator-induced coronary steal is also a theoretical concern in vasospastic disease. The high model score therefore looks more like a knowledge-graph association than a clinical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Ten of the 15 retrieved publications are shown, selected from the list provided. No RCTs were retrieved, so reviews and clinical studies were prioritized.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Clinical observation | Jpn Circ J | 26 patients with rest angina (13 with Prinzmetal's variant) received several drugs, including dipyridamole 50 mg. Propranolol did not suppress attacks and tended to aggravate them. The dipyridamole result is not visible in the abstract provided. |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Case report / in-hospital study | Am J Cardiol | Ending dipyridamole stress with aminophylline can trigger coronary vasospasm in variant angina. This is a safety signal, not a therapeutic effect. |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Cohort | Br Heart J | 25 patients with exercise-induced ST elevation underwent dipyridamole echocardiography. The study assessed test reproducibility and diagnostic responses, not treatment. |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | Pathophysiology of noninvasive functional testing for coronary stenosis, including dipyridamole as a stress stimulus. |
| [6125623](https://pubmed.ncbi.nlm.nih.gov/6125623/) | 1982 | Review | Kardiologiia | Review of diagnostic and treatment problems in angina. No abstract available. |
| [3915223](https://pubmed.ncbi.nlm.nih.gov/3915223/) | 1985 | Review | Cardiologia (Rome) | Review of provocation tests and their effects on cardiovascular function. No abstract available. |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Diagnostic study | Jpn Circ J | Dipyridamole-loading thallium-201 imaging in 38 CAD patients had 66% diagnostic accuracy. Combined with exercise, sensitivity rose from 71% to 87%. |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Diagnostic study | J Am Coll Cardiol | Increased echodensity of transiently asynergic myocardium was proposed as an echocardiographic sign of ischemia, including dipyridamole-induced ischemia. |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Case series | Zhonghua Xin Xue Guan Bing Za Zhi | Compares clinical features of typical and atypical coronary artery spasm. No therapeutic conclusion about dipyridamole. |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Case report | Clin Nucl Med | Patient with migraine, asthma and documented variant angina who had scintigraphic ischemia during exercise and pharmacologic stress. Descriptive only. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2244475 | DIPYRIDAMOLE INJECTION, USP |
| 637734 | PERSANTINE |

Dosage form and approved indication text are not recorded for these licences.

---

## Safety Considerations

- **Literature safety signal**: Coronary vasospasm was reported when dipyridamole stress was terminated with aminophylline in variant angina (PMID 3421166). Coronary steal is a theoretical concern in vasospastic disease.

Please refer to the package insert for warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no registered clinical trials and no literature showing therapeutic benefit. The available papers are mostly about diagnostic stress testing, and one reports a vasospasm-triggering risk. The high model score is not supported by clinical evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Evidence that dipyridamole has a therapeutic effect in vasospastic angina, rather than only a diagnostic or provocation role
- Review of the 5 retrieved publications not shown above

**Note:** Other predicted indications for this drug, stroke and transient ischemic attack, have much stronger evidence (L1, including Phase 3/4 RCTs and meta-analyses). Those are established uses of aspirin plus dipyridamole, not new repurposing findings.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

