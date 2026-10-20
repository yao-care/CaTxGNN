---
layout: default
title: Trandolapril
parent: Model Prediction Only (L5)
nav_order: 929
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Trandolapril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "TRANDOLAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Trandolapril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Trandolapril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Trandolapril is an ACE inhibitor originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trandolapril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension is established, and mechanistically, blocking the renin-angiotensin-aldosterone system (RAAS) may be applicable to malignant hypertensive renal disease.

Malignant hypertensive renal disease is a severe form of hypertension with kidney involvement. Because it is closely related to the original indication, the prediction is biologically plausible. It is better understood as an extension of the existing hypertension use than as true repurposing into a new disease area.

The other top-ranked predictions follow a similar pattern:
- **Malignant renovascular hypertension** (score 99.92%): driven by renin-angiotensin activation, so ACE inhibition is plausible. Caution is needed in bilateral renal artery stenosis, where ACE inhibitors can precipitate acute kidney injury.
- **Pulmonary hypertension (unclear multifactorial mechanism)** (99.92%): RAAS involvement in pulmonary vascular remodeling is only a theoretical rationale, and ACE inhibitors are not an established therapy for it.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (99.92%): only indirect preclinical support (see below).
- **Braddock syndrome** (99.88%): no mechanistic rationale can be established from the available data.
- **Chronic pulmonary heart disease** (99.19%): a single indirect rat study.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top prediction, or for any of the other predicted indications.

## Literature Evidence

Currently no related literature is available for the top prediction (malignant hypertensive renal disease). The literature below relates to lower-ranked predictions and is indirect, preclinical or non-relevant evidence only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8166049](https://pubmed.ncbi.nlm.nih.gov/8166049/) | 1994 | Review | Am J Cardiol | Molecular basis of regression of cardiac hypertrophy after reducing mechanical overload (pulmonary hypertension due to lung disease/hypoxia) |
| [7511729](https://pubmed.ncbi.nlm.nih.gov/7511729/) | 1994 | Preclinical (animal) | J Cardiovasc Pharmacol | Trandolapril for 3 months in old spontaneously hypertensive rats lowered blood pressure about 15% and was studied for effects on left ventricular stiffness and coronary resistance |
| [9218195](https://pubmed.ncbi.nlm.nih.gov/9218195/) | 1997 | Preclinical (animal) | J Hypertens Suppl | Preclinical rationale for combining verapamil and trandolapril in hypertension with cardiovascular or metabolic comorbidity |
| [8909991](https://pubmed.ncbi.nlm.nih.gov/8909991/) | 1996 | Preclinical (animal/ex vivo) | Gen Pharmacol | Trandolapril plus verapamil inhibited hypoxia-induced coronary vasospasm after ischemia-reperfusion injury in dogs |
| [8989645](https://pubmed.ncbi.nlm.nih.gov/8989645/) | 1996 | Preclinical (animal) | J Card Fail | Long-term trandolapril in rats with chronic heart failure was assessed for effects on augmented vasoconstriction (chronic pulmonary heart disease) |
| [17393952](https://pubmed.ncbi.nlm.nih.gov/17393952/) | 2007 | Case report (not directly relevant) | J Natl Med Assoc | Single patient with sickle cell pain whose pain resolved on trandolapril |

## Canada Market Information

Twenty single-ingredient licences are valid in Canada. Dosage form and approved indication text were not available in the data compiled for this report. Five main authorizations:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02239267 | MAVIK | Not available | Not available |
| 02231460 | MAVIK | Not available | Not available |
| 02325756 | SANDOZ TRANDOLAPRIL | Not available | Not available |
| 02471868 | AURO-TRANDOLAPRIL | Not available | Not available |
| 02357798 | PMS-TRANDOLAPRIL | Not available | Not available |

## Safety Considerations

**Contraindication-related diseases (from the knowledge graph, not label text):**
Note that these are graph-derived associations and should be verified against the package insert. They include:
- Angioedema (including hereditary, acquired, and RAAS-blocker-induced forms)
- Kidney disease, renal artery obstruction, and liver disease
- Neutropenia and agranulocytosis
- Aortic stenosis and aortic valve disease
- Hypotensive disorder
- Hypertrophic cardiomyopathy
- Ventricular tachycardia and atrioventricular block
- Heart failure
- Connective tissue, bone, and cartilage disease
- Myasthenia gravis and neuromuscular junction disease
- Gallbladder disease

**Drug Interactions:** 100 interactions were identified. Those listed include:
- **Major:** potassium citrate and potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, glimepiride, chlorpropamide), bupropion, morphine, acetylsalicylic acid, dronabinol, picosulfuric acid, and polyethylene glycol with electrolytes

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.92%), but evidence is at L5, with no clinical trials or literature for malignant hypertensive renal disease. The indication is also close to the existing hypertension use, so the prediction adds little new. Official label warnings and contraindications are not yet available, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- Literature and clinical evidence specific to malignant hypertensive renal disease
- Review of renal-risk considerations (renal artery obstruction, kidney disease) and hyperkalaemia-related interactions
- Approved indication text and dosage forms for the Canadian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

