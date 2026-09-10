---
layout: default
title: Nitroglycerin
parent: 僅模型預測 (L5)
nav_order: 557
evidence_level: L5
indication_count: 5
---

# Nitroglycerin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Nitroglycerin: From Angina Pectoris to Pulmonary Hypertension

## One-Sentence Summary

Nitroglycerin is a nitric oxide (NO) donor classically used to relieve angina pectoris and acute coronary vasospasm.
The TxGNN model predicts it may also be effective for **Pulmonary Hypertension**,
with **13 clinical trials** and **20 publications** currently identified in support of this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris / acute coronary vasospasm (classic vasodilator use; no license record found in this data pack) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (flagged as a High-severity data gap, DG002). Based on known pharmacology, nitroglycerin is a nitric oxide (NO) donor that activates guanylate cyclase, raising cGMP levels and relaxing vascular smooth muscle — the same mechanism it uses to relieve coronary vasospasm in angina pectoris.

This mechanism is not vessel-specific: the pulmonary vascular bed responds to NO-mediated vasodilation through the identical guanylate cyclase/cGMP pathway used by established pulmonary vasodilators such as inhaled nitric oxide (iNO) and prostacyclin (PGI2) analogs. This mechanistic overlap is why nitroglycerin (particularly nebulized or inhaled formulations) is already used clinically as an acute pulmonary vasoreactivity testing agent in pulmonary arterial hypertension.

The evidence base, however, is drawn mostly from small, perioperative, or pediatric/congenital heart disease settings rather than large trials in chronic idiopathic pulmonary arterial hypertension, so applicability to the broader PH population still needs confirmation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07214129](https://clinicaltrials.gov/study/NCT07214129) | N/A | Completed | 20 | Nebulized nitroglycerin evaluated as a vaso-reactive agent for pulmonary arterial hypertension per 6th World Symposium on PH criteria |
| [NCT04594629](https://clinicaltrials.gov/study/NCT04594629) | Phase 1 | Unknown | 120 | Nebulized PGI2 (epoprostenol) vs. nebulized nitroglycerin for pulmonary hypertension after valve replacement surgery |
| [NCT05741229](https://clinicaltrials.gov/study/NCT05741229) | N/A | Completed | 80 | Nebulized nitroglycerin as adjuvant therapy for persistent pulmonary hypertension of the newborn (PPHN), assessed by echocardiographic and clinical parameters |
| [NCT03259165](https://clinicaltrials.gov/study/NCT03259165) | Phase 2 | Terminated | 52 | Nitroglycerin vs. furosemide guided by lung ultrasound in acute heart failure/pulmonary congestion (N-FURIOUS pilot) |
| [NCT06107465](https://clinicaltrials.gov/study/NCT06107465) | Phase 2/3 | Unknown | 60 | High- vs. low-dose nitroglycerin for sympathetic crashing acute pulmonary edema |
| [NCT00449059](https://clinicaltrials.gov/study/NCT00449059) | Phase 4 | Completed | 20 | Acute effect of nitroglycerin infusion on cyclosporine-induced hypertension after cardiac transplantation |
| [NCT02018497](https://clinicaltrials.gov/study/NCT02018497) | N/A | Unknown | 5000 | Essential arterial hypotension and allostasis registry — limited direct relevance to PH |
| [NCT05373108](https://clinicaltrials.gov/study/NCT05373108) | Phase 4 | Completed | 19 | Endothelin-1 and cardiac allograft vasculopathy in heart transplant recipients (not a direct NTG treatment trial) |
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular function and exercise rehabilitation in systemic hypertension |
| [NCT05172739](https://clinicaltrials.gov/study/NCT05172739) | Phase 4 | Recruiting | 70 | Opioid-free anesthesia strategy in lobectomy for NSCLC — no direct PH treatment link |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34082850](https://pubmed.ncbi.nlm.nih.gov/34082850/) | 2021 | Cohort (Tier 1) | Cardiology in the Young | Review/analysis of nitroglycerin inhalation for acute PAH treatment in children with congenital heart disease |
| [40888971](https://pubmed.ncbi.nlm.nih.gov/40888971/) | 2025 | Cohort (Tier 1) | European Journal of Pediatrics | Randomized controlled trial of nebulized nitroglycerin as adjuvant therapy in 80 newborns with persistent pulmonary hypertension |
| [29880427](https://pubmed.ncbi.nlm.nih.gov/29880427/) | 2018 | Cohort (Tier 2) | J Cardiothoracic Vasc Anesth | Randomized controlled study comparing dobutamine+nitroglycerin vs. milrinone for perioperative PH management in mitral valve surgery |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Cohort (Tier 2) | Bull Eur Physiopathol Respir | Sublingual nitroglycerin/isosorbide dinitrate reduced pulmonary vascular resistance in COPD-related pulmonary hypertension (54 patients) |
| [31425404](https://pubmed.ncbi.nlm.nih.gov/31425404/) | 2020 | Cohort (Tier 2) | Shock | Comparison of nitroglycerin vs. novel NO donor for acute pulmonary hypertension after aortic cross-clamping in anesthetized pigs |
| [6407380](https://pubmed.ncbi.nlm.nih.gov/6407380/) | 1983 | Cohort (Tier 2) | Annals of Internal Medicine | Nitroglycerin increased cardiac index and reduced pulmonary vascular resistance and mean pulmonary artery pressure in 9 patients with chronic PH |
| [39799613](https://pubmed.ncbi.nlm.nih.gov/39799613/) | 2025 | Review (Tier 3) | Am J Emergency Medicine | Review of sympathetic crashing acute pulmonary edema management, including nitrate therapy |
| [32246442](https://pubmed.ncbi.nlm.nih.gov/32246442/) | 2020 | Review (Tier 3) | Adv Exp Med Biol | General review of coronary artery disease mechanisms and treatment |
| [16429888](https://pubmed.ncbi.nlm.nih.gov/16429888/) | 2005 | Review (Tier 3) | Texas Heart Institute Journal | Review of pharmacologic management of systemic and pulmonary hypertension in cardiac surgery patients |
| [8689279](https://pubmed.ncbi.nlm.nih.gov/8689279/) | 1996 | Review (Tier 3) | New Horizons | Review of calcium blockade in pulmonary hypertension and hypoxic vasoconstriction |

---

## Canada Market Information

Nitroglycerin currently has **no active Drug Identification Numbers (DINs)** on record in this data pack (market status: Not Marketed, total licenses: 0). No product-level licensing data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale (NO donor → guanylate cyclase/cGMP-mediated pulmonary vasodilation) is well established and already reflected in clinical use of nitroglycerin for acute PH vasoreactivity testing. However, most supporting trials are small, perioperative, or pediatric/congenital-heart-disease studies rather than confirmatory trials in the general chronic PH population, placing the evidence at L2 rather than L1.

**To proceed, the following is needed:**
- TFDA/Health Canada package insert warnings and contraindications (currently a Blocking data gap — required before safety screening)
- Detailed DrugBank mechanism-of-action record (currently a High-severity data gap)
- Clarification of regulatory pathway given the drug has 0 active DINs and is not currently marketed in Canada
- Larger, prospective trials specifically in chronic (non-perioperative) pulmonary arterial hypertension populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

