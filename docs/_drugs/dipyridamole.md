---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

# Dipyridamole: From Antiplatelet Therapy to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is a phosphodiesterase (PDE) inhibitor and adenosine reuptake blocker, historically used as an antiplatelet agent (combined with aspirin) and as a pharmacologic stressor in cardiac imaging.
The TxGNN model assigns its highest prediction score (99.99%) to **Prinzmetal Angina** — however, this association represents a **safety signal and potential contraindication**, not a therapeutic opportunity, as dipyridamole is known to *trigger* coronary vasospasm through the adenosine-mediated coronary steal phenomenon.
**0 clinical trials** and **15 publications** are retrieved; all document its diagnostic/provocative role, not a treatment relationship.

> **⚠️ Clinical Interpreter's Note:** The most evidence-supported repurposing indications in this Evidence Pack are **Rank #2 (Stroke disorder, L1)** and **Rank #5 (Transient Ischemic Attack, L1)**, both supported by multiple Phase 3/4 RCTs and Cochrane reviews. These are summarized at the end of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canadian regulatory database; globally known for antiplatelet use (with aspirin) and cardiac pharmacologic stress testing |
| Predicted New Indication (Rank #1) | Prinzmetal Angina |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 — Observational/mechanistic only; no interventional trials |
| Canada Market Status | Not marketed (0 DINs) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** — TxGNN captures diagnostic co-occurrence, not a treatment relationship |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on published pharmacology, dipyridamole exerts its effects through two complementary pathways: (1) inhibiting phosphodiesterase (PDE3/5), which prevents breakdown of cAMP and cGMP in platelets and vascular smooth muscle, and (2) blocking equilibrative nucleoside transporters to prevent cellular adenosine reuptake, resulting in elevated extracellular adenosine concentrations. Together, these effects produce vasodilation of coronary microvessels and inhibition of platelet aggregation.

The TxGNN model correctly identifies a strong biological relationship between dipyridamole and Prinzmetal angina — but the direction of that relationship is the opposite of therapeutic. In susceptible patients, dipyridamole-induced coronary vasodilation triggers a **coronary steal phenomenon**: blood is redistributed away from myocardial territories supplied by stenosed or spasm-prone arteries. PMID 3421166 (Picano et al., 1988) explicitly documents that dipyridamole stress testing can provoke coronary vasospasm in patients with variant angina, and that aminophylline (an adenosine receptor antagonist) is required to terminate the episode. PMID 633593 (Yasue et al., 1978) further confirms that dipyridamole not only failed to suppress attacks in 26 Prinzmetal angina patients but tended to **aggravate** them.

The high TxGNN score (99.99%) therefore reflects the model's accurate detection of a close pharmacological co-occurrence between dipyridamole and this disease — a co-occurrence arising from its role as a **diagnostic provocative agent and a potential contraindication**, not as a treatment candidate. This is a textbook example of why model scores must always be interpreted alongside mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for dipyridamole in the **treatment** of Prinzmetal angina.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Clinical observational | Am J Cardiology | Dipyridamole stress testing triggers coronary vasospasm via adenosine in variant angina patients; aminophylline reversal documented — establishes dipyridamole as a vasospasm trigger |
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Review | Jpn Circ J | In 26 rest angina patients (13 with Prinzmetal's), dipyridamole 50 mg failed to suppress attacks and tended to aggravate them — key early evidence of contraindication |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Clinical study | Br Heart J | Short-term reproducibility of exercise testing in patients with ST elevation; different responses to dipyridamole stress test used to characterize vasospastic vs. fixed-stenosis disease |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Clinical study | JACC | Increased myocardial echodensity during ischemic episodes of varying severity induced by different provocative mechanisms including dipyridamole — diagnostic utility context |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | Pathophysiological framework for noninvasive coronary stenosis evaluation; dipyridamole reviewed as one of several pharmacologic stressors |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Diagnostic study | Jpn Circ J | Dipyridamole-loading myocardial imaging in 38 CAD patients; diagnostic accuracy 66%, useful in patients unable to exercise — diagnostic (not therapeutic) role |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Prognostic study | Rev Port Cardiol | 3-year prognosis assessment using dipyridamole-thallium scintigraphy in suspected CAD — dipyridamole used as imaging stressor |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Case report | Clin Nucl Med | Patient with variant angina, migraine, and asthma developed inferior/posterior wall ischemia during dipyridamole stress — supports vasospasm-prone phenotype as a risk group |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Clinical study | Zhonghua Xin Xue Guan Bing Za Zhi | Comparison of typical vs. atypical coronary artery spasm clinical characteristics; dipyridamole stress testing context |
| [2221701](https://pubmed.ncbi.nlm.nih.gov/2221701/) | 1990 | Review | Ann NY Acad Sci | Sensitivity and specificity of ECG-based transient myocardial ischemia diagnosis; dipyridamole among provocative test modalities reviewed |

---

## Canada Market Information

No Canadian Drug Identification Numbers (DINs) are registered for dipyridamole as a standalone product in this dataset.

> **Note:** Dipyridamole is globally available as a combination product with aspirin (Aggrenox® — extended-release dipyridamole 200 mg + aspirin 25 mg). The absence of DINs in this dataset may reflect a data gap (DG001) or that the product is registered under a combination DIN not captured here. A manual review of the Health Canada Drug Product Database is recommended before concluding non-availability.

---

## Safety Considerations

**Key Warnings (derived from evidence and pharmacological rationale):**

- **Prinzmetal angina / vasospastic angina:** Dipyridamole is a known trigger of coronary vasospasm via the adenosine-mediated coronary steal mechanism. It should be considered **contraindicated** in this population (PMID 3421166, PMID 633593).
- **Sick sinus syndrome (Rank #4 prediction):** Dipyridamole blocks adenosine reuptake, raising local adenosine concentrations. Adenosine exerts negative chronotropic and dromotropic effects on the sinoatrial node. In patients with sick sinus syndrome, this may precipitate clinically significant bradycardia or conduction block — a potential contraindication.
- **Cardiac stress testing reversal:** Aminophylline should be readily available as an antidote when dipyridamole is used as a pharmacologic stress agent; it competitively blocks adenosine receptors and reverses vasodilation and vasospasm.

Please refer to the official prescribing information / Health Canada product monograph for complete warnings and contraindications (data gap DG001 — not resolved in this Evidence Pack).

---

## Additional High-Priority Repurposing Signals

The following indications from this Evidence Pack carry significantly stronger repurposing evidence and are recommended for prioritized evaluation:

| Rank | Indication | TxGNN Score | Evidence Level | Trials | Publications | Decision |
|------|-----------|-------------|----------------|--------|-------------|---------|
| 2 | Stroke disorder | 99.95% | **L1** | 31 | 18 | **Proceed with Guardrails** |
| 5 | Transient ischemic attack | 99.87% | **L1** | 15 | 20 | **Proceed with Guardrails** |
| 3 | Thrombotic disease | 99.94% | L3 | 2 | 20 | Research Question |

For **stroke disorder** and **TIA**, evidence includes ESPRIT (n=4,500, Phase 4 RCT), JASAP (n=1,295, Phase 3 RCT), EARLY (n=551, Phase 4 RCT), and multiple Cochrane systematic reviews (PMID 12535415, 17636684, 16625549) confirming that aspirin + dipyridamole (Aggrenox) reduces the risk of recurrent vascular events after ischemic stroke or TIA. These findings are endorsed by AHA/ASA and European stroke guidelines.

---

## Conclusion and Next Steps

**Decision: Hold (for Rank #1 — Prinzmetal Angina)**

**Rationale:**
The TxGNN Rank #1 prediction for Prinzmetal angina reflects a pharmacological co-occurrence rooted in a diagnostic and provocative relationship — not a therapeutic one. Dipyridamole-induced adenosine accumulation triggers rather than treats coronary vasospasm, making this a safety signal and likely contraindication rather than a repurposing opportunity. No interventional clinical trials exist, and all 15 retrieved publications document its use as a diagnostic stressor.

**To proceed with the overall dipyridamole program, the following is needed:**

- **Address DG001**: Obtain and parse the Health Canada product monograph / prescribing information for dipyridamole and Aggrenox to extract official warnings, contraindications, and approved indications
- **Address DG002**: Query DrugBank API for complete MOA, drug categories, and toxicity data for dipyridamole (DB00975)
- **Verify Canada regulatory status**: Confirm whether Aggrenox (dipyridamole + aspirin combination) holds a Canadian DIN — the current 0-DIN finding likely reflects a data gap, not true non-availability
- **Escalate Rank #2 (stroke) and Rank #5 (TIA)** to a full S3-stage evaluation given L1 evidence — these represent the genuine repurposing value in this Evidence Pack
- **Flag Rank #1 and Rank #4** as potential contraindication entries for the drug safety profile, not repurposing candidates
- Add YMYL disclaimer: *The predictions in this report are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

