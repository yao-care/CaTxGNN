---
layout: default
title: Bumetanide
parent: Moderate Evidence (L3-L4)
nav_order: 133
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-13
description: "Bumetanide: predicted new indication Acute pulmonary heart disease (evidence level L4). Approved use: Congestive heart failure"
monitor_inn: "BUMETANIDE"
predicted_indications: ["acute pulmonary heart disease"]
---

# Bumetanide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

## Bumetanide: From Congestive Heart Failure to Acute Pulmonary Heart Disease
{: .text-alpha }

## One-Sentence Summary

Bumetanide is a loop diuretic originally used to treat congestive heart failure.
The TxGNN model predicts it may be useful for **acute pulmonary heart disease**,
but the evidence is thin: **0 clinical trials** and **5 publications**, none of which studies this specific condition directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Congestive heart failure |
| Predicted New Indication | Acute pulmonary heart disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Bumetanide is a loop diuretic. It blocks the Na-K-2Cl cotransporter (NKCC2) in the thick ascending limb of the loop of Henle. This causes rapid loss of sodium and water, which lowers preload and relieves venous and pulmonary congestion. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on the known pharmacology of the drug class.

Acute pulmonary heart disease (acute cor pulmonale, for example after a massive pulmonary embolism) involves pressure overload and dilation of the right ventricle, with systemic venous congestion. Decongestive diuresis is therefore plausible as supportive care for right-sided volume overload. This is an extension of the existing heart failure use, not a new mechanism.

There are important limits. Bumetanide does not treat the underlying cause, such as a blocked pulmonary vessel or high pulmonary vascular resistance. In a right ventricle that depends on preload, aggressive diuresis may lower cardiac output and cause harm. The very high TxGNN score most likely reflects the drug's established heart failure indication and its closeness to related cardiac conditions in the knowledge graph, not evidence specific to this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Small clinical haemodynamic study | Br J Clin Pharmacol | In 24 patients with coronary artery disease and acute or chronic heart failure, IV bumetanide lowered cardiac index and pulmonary artery occluded pressure, while raising blood pressure and vascular resistance |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Review | Drugs | Bumetanide is a potent loop diuretic for oedema from heart failure, hepatic and renal disease, and acute pulmonary congestion |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Review | Am J Ther | Reviews treatment of acute heart failure; most patients can be managed effectively with diuretics |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Review | Ann Pharmacother | Compares the pharmacokinetics, safety, efficacy and cost of loop diuretics, asking whether furosemide should be first line |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Cohort | Am J Emerg Med | Describes heart failure presentations to US emergency departments from 2016 to 2023; not specific to bumetanide |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00728284 | BURINEX | Not specified | Not specified |
| 00728276 | BURINEX | Not specified | Not specified |

## Safety Considerations

- **Contraindications or disease associations flagged in the knowledge graph** (these come from network data, not from label text): liver disease, hepatic coma and encephalopathy, gallbladder disease, thrombocytopenia, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, hyperuricaemia, anuria, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, and hearing or auditory system disorders.
- **Drug interactions:** 100 interactions were found. Most of the 20 listed are of moderate severity, including acarbose, metformin, alogliptin, albiglutide, acetohexamide, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone). Others are omeprazole, rabeprazole, bupropion, morphine, bisacodyl and several amphotericin B formulations. Doxycycline and acetylsalicylic acid are minor.
- **Disease-specific concern:** Over-diuresis may reduce right ventricular preload and cardiac output in acute cor pulmonale.

Please refer to the package insert for warnings and full contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and mechanistic plausibility alone. No clinical trials exist, and none of the available literature studies bumetanide in acute pulmonary heart disease. Diuresis could also be harmful in preload-dependent right ventricular failure.

**To proceed, the following is needed:**
- Retrieve and review the Health Canada package insert for warnings and contraindications (a blocking gap for safety screening)
- Obtain detailed mechanism-of-action data from DrugBank
- Search for disease-specific evidence on loop diuretics in acute cor pulmonale or right ventricular failure
- Seek clinical expert input on the risk of reduced right ventricular preload before any further evaluation
- Confirm the approved indications and dosage forms for the two BURINEX DINs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

