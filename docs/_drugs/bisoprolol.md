---
layout: default
title: Bisoprolol
parent: Model Prediction Only (L5)
nav_order: 119
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Bisoprolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Bisoprolol"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Bisoprolol
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

# Bisoprolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Bisoprolol is a beta-1 selective blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Based on known pharmacology, bisoprolol is a beta-1 selective blocker whose efficacy in hypertension is established. Beta-1 blockade lowers heart rate and cardiac output and reduces renin release from the kidney.

Malignant hypertensive renal disease is a severe kidney complication of very high blood pressure. The link to the original indication is therefore plausible: the underlying problem is the same (raised blood pressure), and reduced renin release could in theory help. The high score likely reflects how close this disease sits to hypertension in the knowledge graph, not independent evidence.

There is an important caution. Malignant hypertension is normally treated in acute care with intravenous agents, not oral beta-blockers, so the practical role of bisoprolol would be limited to long-term maintenance at most.

Other predictions in the same list were also reviewed:
- **Malignant renovascular hypertension** (score 99.94%): a theoretical rationale through renin suppression, but no trials or literature.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.93%): 8 publications were retrieved, but they are preclinical or cardiac-focused and show no efficacy signal. Beta-blockers may impair right ventricular function in pulmonary hypertension.
- **Pulmonary hypertension with unclear multifactorial mechanism** (score 99.93%): no supporting evidence, and low biological plausibility.
- **Braddock syndrome** (score 99.91%): a very rare condition with no mechanistic or clinical link to bisoprolol.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction (malignant hypertensive renal disease).

For reference, the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia) has indirect literature only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | Beta-blocker effects on lung function in heart failure; the older view that they are unsuitable with impaired lung function is being challenged |
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Clinical comparative study | Int J Cardiol | Carvedilol vs nebivolol vs bisoprolol in moderate heart failure (CARNEBI) |
| [23706341](https://pubmed.ncbi.nlm.nih.gov/23706341/) | 2013 | Physiological study | J Am Soc Echocardiogr | Left ventricular adaptation to acute hypoxia, with and without beta-1 blockade |
| [18845967](https://pubmed.ncbi.nlm.nih.gov/18845967/) | 2008 | Physiological study | Med Sci Sports Exerc | Beta-adrenergic blockade and chemoreflex contributions to exercise capacity |
| [32363697](https://pubmed.ncbi.nlm.nih.gov/32363697/) | 2020 | Preclinical (in vitro/in vivo) | Fundam Clin Pharmacol | Bisoprolol protected heart cells from ischemia-reperfusion injury via the PI3K/AKT/GSK3β pathway |
| [27687650](https://pubmed.ncbi.nlm.nih.gov/27687650/) | 2016 | Preclinical (in vitro) | Nan Fang Yi Ke Da Xue Xue Bao | Bisoprolol pretreatment and hypoxia/reoxygenation injury in cardiomyocytes |
| [39088923](https://pubmed.ncbi.nlm.nih.gov/39088923/) | 2024 | Preclinical (animal) | Int Immunopharmacol | Diosmin plus bisoprolol reduced cobalt chloride-induced cardiotoxicity in rats |
| [12887136](https://pubmed.ncbi.nlm.nih.gov/12887136/) | 2003 | Case report | Hypertens Res | Two cases of pheochromocytoma with tetralogy of Fallot |

None of these test bisoprolol in patients with pulmonary hypertension.

---

## Canada Market Information

Bisoprolol is marketed in Canada as 20 valid single-ingredient authorizations. Dosage form and approved indication text were not available in the data compiled for this report. Five of the authorizations are listed below.

| DIN | Product Name |
|---------|------|
| 02465620 | MINT-BISOPROLOL |
| 02518805 | JAMP BISOPROLOL |
| 02267489 | TEVA-BISOPROLOL |
| 02256134 | APO-BISOPROLOL |
| 02544245 | SANDOZ BISOPROLOL TABLETS |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (model-derived, not label text): anxiety disorder, kidney disease, liver disease, pancreatitis, gallbladder disease, asthma (including intrinsic and allergic), diabetes mellitus and diabetic ketoacidosis, systemic lupus erythematosus, psoriasis, gout, myasthenia gravis, hepatic coma/encephalopathy, anuria, and several metabolic conditions (potassium deficiency, hypercalcemia, hyperparathyroidism, phosphorus metabolism disease). Kidney disease appears on this list, which is relevant to the proposed renal indication and needs careful review.
- **Drug Interactions**: 100 interactions were found in total. Most of those listed are Moderate, including epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, acetohexamide, and calcium salts. Minor interactions include acetylsalicylic acid, aluminum hydroxide and attapulgite.
- **Disease-specific concern**: beta-blockers may impair right ventricular function and exercise capacity in pulmonary hypertension.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (evidence level L5), with no clinical trials or publications for the top-ranked indication. Malignant hypertension is managed with intravenous agents in acute care, and the knowledge graph itself lists kidney disease as a contraindication.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank) to support the mechanistic link
- A targeted literature search on beta-blockers in malignant or renovascular hypertension and hypertensive nephropathy
- Clinical evidence in the target population, and a clear role for oral bisoprolol compared with standard acute and long-term therapy
- Assessment of whether pulmonary hypertension predictions are worth pursuing at all, given the safety concern
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

