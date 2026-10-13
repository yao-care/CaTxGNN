---
layout: default
title: Nadolol
parent: Model Prediction Only (L5)
nav_order: 639
evidence_level: L5
indication_count: 5
---

# Nadolol
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

# Nadolol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Nadolol is a non-selective beta-blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, nadolol is a non-selective beta-blocker. Its efficacy in hypertension is established, and it is mechanistically plausible that it also applies to renovascular hypertension.

Beta-1 blockade reduces renin release from the juxtaglomerular apparatus. Renovascular hypertension is driven largely by the renin-angiotensin system, so this link is reasonable.

However, malignant renovascular hypertension is essentially a severe subtype of the already-approved hypertension indication, so this is not true repurposing. Malignant hypertension also usually needs acute parenteral treatment rather than oral nadolol.

**Other predictions (all Hold):**

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant hypertensive renal disease | 99.59% | L5 | No trials or literature. Nadolol is renally cleared, so dose adjustment would be needed in renal impairment. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.53% | L4 | Only indirect preclinical literature. Non-selective beta-blockers carry bronchoconstriction risk in chronic lung disease. |
| Pulmonary hypertension with unclear multifactorial mechanism | 99.53% | L5 | No evidence. Beta-blockers are generally not recommended in pulmonary hypertension. |
| Braddock syndrome | 99.43% | L5 | No mechanistic rationale. The disease annotation should be verified. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

For the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), only indirect and preclinical papers were retrieved. None tests nadolol in pulmonary hypertension in humans:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6488695](https://pubmed.ncbi.nlm.nih.gov/6488695/) | 1984 | Animal study (dog) | Clin Physiol Biochem | Chronic propranolol lowered pulmonary artery pressure in conscious dogs. Nadolol, a structurally different beta-blocker, had a similar effect on pulmonary vascular resistance. |
| [25350545](https://pubmed.ncbi.nlm.nih.gov/25350545/) | 2014 | Preclinical | PLoS One | β2-adrenergic receptor-dependent attenuation of hypoxic pulmonary vasoconstriction in intermittent hypoxic rats. |
| [24795691](https://pubmed.ncbi.nlm.nih.gov/24795691/) | 2014 | Preclinical | Front Neurol | β1-blockers lower norepinephrine release by inhibiting presynaptic β1-adrenoceptors in rats. |
| [2566504](https://pubmed.ncbi.nlm.nih.gov/2566504/) | 1989 | Preclinical | Eur J Pharmacol | Cardioprotective effect of beta-blockers against anoxia in isolated guinea pig hearts. |
| [8729060](https://pubmed.ncbi.nlm.nih.gov/8729060/) | 1996 | Preclinical | J Mol Cell Cardiol | Nadolol and chloride-current blockers studied in action potential shortening in hypoxic rabbit hearts. |

The remaining retrieved papers concern myocardial ischemia, arrhythmia, ischemic stroke, or non-mammalian species (goldfish, turtle), and are not relevant to this indication.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00782467 | APO-NADOLOL | Not specified | Not specified |
| 02496399 | MINT-NADOLOL | Not specified | Not specified |
| 00782475 | APO-NADOLOL | Not specified | Not specified |
| 00782505 | APO-NADOLOL | Not specified | Not specified |
| 02496380 | MINT-NADOLOL | Not specified | Not specified |

All 5 licences are valid single-ingredient products.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** anxiety and neurotic disorders, dysthymic disorder, kidney disease, anuria, liver disease, hepatic coma and encephalopathy, pancreatitis, gallbladder disease, systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, gout and hyperuricaemia, hyperparathyroidism, hypercalcaemia, nephrocalcinosis, potassium deficiency, phosphorus metabolism disease, myasthenia gravis and other neuromuscular junction disease, atrioventricular block, pulmonary emphysema, and bronchial disease.
- **Drug Interactions:** 100 interactions were found in total. The list reviewed here shows:
  - **Major:** epinephrine.
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), anticholinergics (atropine, hyoscyamine, methscopolamine), bupropion, morphine, cimetidine, canagliflozin, dapagliflozin, chlorpropamide, calcium acetate and calcium phosphate.
  - **Minor:** acetylsalicylic acid, clarithromycin, magnesium oxide.
- **Predicted-indication cautions:** Non-selective beta-blockers can cause bronchoconstriction in chronic lung disease, and beta-blockers are generally cautioned against in pulmonary hypertension.

Please also refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model output alone (L5 for the top indication), with no supporting trials or literature. The top two predictions are subtypes of the already-approved hypertension indication, and the pulmonary hypertension predictions carry safety concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- Clinical or observational evidence of nadolol in renovascular hypertension, if this indication is pursued
- Clarification of whether the malignant hypertension predictions add value beyond the existing hypertension indication
- Verification of the Braddock syndrome disease annotation before any further work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

