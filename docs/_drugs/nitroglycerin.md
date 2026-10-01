---
layout: default
title: Nitroglycerin
parent: Model Prediction Only (L5)
nav_order: 655
evidence_level: L5
indication_count: 5
---

# Nitroglycerin
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

# Nitroglycerin: From Angina Pectoris to Pulmonary Hypertension

## One-Sentence Summary

Nitroglycerin is a nitric oxide (NO) donor vasodilator marketed in Canada as patches and a spray. The published literature describes its long-standing use in angina pectoris, but the pack contains no label indication text. The TxGNN model predicts it may be effective for **pulmonary hypertension**, supported by **13 registered trials (3 directly relevant, all small)** and **20 publications**, including one RCT in newborns.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris (taken from published literature; Health Canada indication text is not available in the pack) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L2 (assigned in the pack; see note under Clinical Trial Evidence) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 18 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Nitroglycerin is a well-known NO donor. NO raises cGMP in vascular smooth muscle and causes vasodilation. Its use as a vasodilator in angina has been established for a long time.

Pulmonary hypertension is driven partly by pulmonary vasoconstriction, so a vasodilator is biologically plausible. Delivering nitroglycerin by nebulizer or inhalation may target the lung vessels and limit systemic hypotension. Older haemodynamic studies, including intravenous, sublingual and transdermal use, reported lower pulmonary vascular resistance or pulmonary artery pressure. The high TxGNN score agrees with this pathway.

There are limits:
- Nitroglycerin is not pulmonary-selective.
- Tolerance can develop.
- Ventilation/perfusion mismatch is possible.
- Inhaled nitric oxide and PDE5 inhibitors are the established comparators.

The Canadian products in the pack are patches and a spray. No nebulized or inhaled product appears, so the route used in most of the supporting studies is not currently marketed here.

## Clinical Trial Evidence

Of 13 registered trials, 3 are directly relevant. The others concern systemic hypertension, pulmonary edema, or are unrelated. The table lists the 3 direct trials and 3 indirect ones. No trial results are provided in the pack.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07214129](https://clinicaltrials.gov/study/NCT07214129) | Not phased | Completed | 20 | Nebulized nitroglycerin as a vasoreactive agent in pulmonary arterial hypertension. Direct match, but small and uncontrolled. |
| [NCT05741229](https://clinicaltrials.gov/study/NCT05741229) | Not phased | Completed | 80 | Nebulized nitroglycerin as an adjuvant in persistent pulmonary hypertension of the newborn, assessed by echocardiography and clinical parameters. Neonatal population. |
| [NCT04594629](https://clinicaltrials.gov/study/NCT04594629) | Phase 1 | Unknown | 120 | Randomized comparison of nebulized epoprostenol (PGI2) vs nebulized nitroglycerin for pulmonary hypertension after valve replacement surgery. Results may not be available. |
| [NCT06107465](https://clinicaltrials.gov/study/NCT06107465) | Phase 2/3 | Unknown | 60 | High vs low dose nitroglycerin in sympathetic crashing acute pulmonary edema. Cardiogenic pulmonary edema, so indirect. |
| [NCT03259165](https://clinicaltrials.gov/study/NCT03259165) | Phase 2 | Terminated | 52 | Nitroglycerin vs furosemide guided by lung ultrasound in acute heart failure congestion. Not pulmonary hypertension. |
| [NCT00449059](https://clinicaltrials.gov/study/NCT00449059) | Phase 4 | Completed | 20 | Acute effect of nitroglycerin infusion on cyclosporine-induced systemic hypertension after cardiac transplantation. Systemic, not pulmonary. |

The L2 level is the one assigned in the pack. It rests on the published RCT in newborns plus several small clinical studies. No completed Phase 2/3 trial in pulmonary hypertension is listed, so the level is at the lenient end.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40888971](https://pubmed.ncbi.nlm.nih.gov/40888971/) | 2025 | RCT | Eur J Pediatr | 80 full-term newborns with persistent pulmonary hypertension. Nebulized nitroglycerin vs no nitroglycerin, assessed by echocardiographic and clinical parameters. |
| [29880427](https://pubmed.ncbi.nlm.nih.gov/29880427/) | 2018 | RCT | J Cardiothorac Vasc Anesth | Dobutamine plus nitroglycerin vs milrinone in severe pulmonary hypertension during mitral valve replacement. |
| [39549131](https://pubmed.ncbi.nlm.nih.gov/39549131/) | 2024 | Network meta-analysis | Clin Drug Investig | Compares pulmonary vasodilators for perioperative pulmonary hypertension in mitral valve replacement. |
| [34082850](https://pubmed.ncbi.nlm.nih.gov/34082850/) | 2021 | Review | Cardiol Young | Reviews inhaled nitroglycerin as an alternative to inhaled nitric oxide in acute pulmonary hypertension in children with congenital heart disease. |
| [14508317](https://pubmed.ncbi.nlm.nih.gov/14508317/) | 2003 | Clinical study | Anesthesiology | Postoperative haemodynamic effects of inhaled nitroglycerin in pulmonary hypertension patients undergoing mitral valve replacement. |
| [16707530](https://pubmed.ncbi.nlm.nih.gov/16707530/) | 2006 | Clinical study | Br J Anaesth | Acute pulmonary and systemic haemodynamic effects of inhaled nitroglycerin in children with congenital heart disease and pulmonary hypertension. |
| [6407380](https://pubmed.ncbi.nlm.nih.gov/6407380/) | 1983 | Clinical study | Ann Intern Med | In 9 patients with chronic pulmonary hypertension, nitroglycerin raised cardiac index by 40% and lowered pulmonary vascular resistance by 40%. |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Clinical study | Bull Eur Physiopathol Respir | In COPD-associated pulmonary hypertension, sublingual nitroglycerin or isosorbide dinitrate lowered pulmonary pressure. Only nitroglycerin lowered pulmonary vascular resistance. |
| [3096761](https://pubmed.ncbi.nlm.nih.gov/3096761/) | 1986 | Clinical study | Eur J Respir Dis Suppl | Transdermal nitroglycerin lowered pulmonary artery pressure within 24 hours, and the effect persisted after 4 weeks. |
| [31250045](https://pubmed.ncbi.nlm.nih.gov/31250045/) | 2019 | Clinical study | Eur J Clin Pharmacol | Examined how the ALDH2 gene polymorphism affects nitroglycerin's vasodilatory effect in infants with congenital heart disease and pulmonary hypertension. |

## Canada Market Information

Dosage form and approved indication text are not available for these licenses. Five of the 18 DINs are listed.

| DIN | Product Name |
|---------|------|
| 2407469 | MYLAN-NITRO PATCH 0.6 |
| 2238998 | RHO-NITRO PUMPSPRAY |
| 2011271 | NITRO-DUR 0.8 |
| 2230733 | TRINIPATCH 0.4 |
| 2230732 | TRINIPATCH 0.2 |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the supporting studies are consistent. They include a recent RCT in newborns and several small haemodynamic studies, but all are small and the trials are mostly non-phased or early phase. Most of the studies used nebulized or inhaled nitroglycerin, a route not marketed in Canada. The Health Canada safety information is also missing, which blocks safety screening. This should be treated as a research question for now.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (the safety screening blocker).
- Mechanism of action data from DrugBank.
- Verification of the label indications, to confirm what is on-label and what is a true new use.
- A route and formulation assessment for nebulized or inhaled use.
- Results or status updates for NCT04594629 and NCT07214129.
- A comparison against inhaled nitric oxide and PDE5 inhibitors, including the tolerance and ventilation/perfusion mismatch risks.

Other predicted indications:
- **Prinzmetal angina** (L3) is probably an established use rather than a true repurposing. It needs a label check.
- **Kyphoscoliotic heart disease, primary hereditary glaucoma and congenital hypotrichosis milia** are model predictions only, with no trial or literature support. They should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

