---
layout: default
title: Eplerenone
parent: Moderate Evidence (L3-L4)
nav_order: 338
evidence_level: L4
indication_count: 5
---

# Eplerenone
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Eplerenone: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor antagonist, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**,
but there are currently **no registered clinical trials** and only **14 publications**, mostly preclinical or indirect, supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, eplerenone is a selective mineralocorticoid receptor (MR) antagonist. Its efficacy in hypertension is established, and mechanistically it may be applicable to pulmonary hypertension driven by hypoxia.

Preclinical studies link chronic intermittent hypoxia to MR activation, renal fibrosis and atrial remodelling, and eplerenone attenuated these effects in rodent models. Laboratory work also suggests hypoxia raises aldosterone production in pulmonary artery endothelial cells and promotes pulmonary vascular fibrosis. In rat models of pulmonary arterial hypertension, MR antagonists, including eplerenone, improved pulmonary vascular remodelling. A small clinical study in patients with obstructive sleep apnoea and resistant hypertension also suggests eplerenone may reduce apnoea severity and arterial stiffness.

Together these findings support a plausible hypoxia–MR–vascular remodelling axis. However, none of them directly measures pulmonary arterial pressure or pulmonary hypertension outcomes in humans. The high TxGNN score is a computational prediction, not clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27230560](https://pubmed.ncbi.nlm.nih.gov/27230560/) | 2016 | Clinical study | Pol Arch Med Wewn | Eplerenone in OSA with resistant hypertension; assessed effect on OSA severity and arterial stiffness (small study, indirect endpoints) |
| [41483355](https://pubmed.ncbi.nlm.nih.gov/41483355/) | 2026 | Review | Curr Hypertens Rep | Reviews OSA-driven hypertension and evidence for aldosterone blockade as a tailored treatment |
| [15199296](https://pubmed.ncbi.nlm.nih.gov/15199296/) | 2004 | Review | Curr Opin Nephrol Hypertens | Glucocorticoids can activate the mineralocorticoid receptor in non-epithelial cells, contributing to hypertension |
| [35043674](https://pubmed.ncbi.nlm.nih.gov/35043674/) | 2022 | Preclinical (rat) | Am J Physiol Lung Cell Mol Physiol | MR antagonists (eplerenone, spironolactone) in established PAH in the SU5416-hypoxia rat model; improved interventricular dependence |
| [29499691](https://pubmed.ncbi.nlm.nih.gov/29499691/) | 2018 | Preclinical | BMC Pulm Med | Eplerenone attenuated pulmonary vascular remodelling more than right ventricular remodelling in PAH |
| [25001622](https://pubmed.ncbi.nlm.nih.gov/25001622/) | 2014 | Preclinical | Circulation | Hypoxia upregulates StAR and aldosterone synthesis in pulmonary artery endothelial cells, promoting vascular fibrosis |
| [27006450](https://pubmed.ncbi.nlm.nih.gov/27006450/) | 2016 | Preclinical | FASEB J | Aldosterone raises Raptor (mTORC1) in pulmonary artery smooth muscle cells, promoting PAH |
| [35568141](https://pubmed.ncbi.nlm.nih.gov/35568141/) | 2022 | Preclinical (rat) | Cardiovasc Pathol | Eplerenone improved atrial remodelling induced by chronic intermittent hypoxia |
| [35346763](https://pubmed.ncbi.nlm.nih.gov/35346763/) | 2022 | Preclinical (rat) | Exp Gerontol | Chronic intermittent hypoxia induced renal fibrosis through MR activation |
| [39707386](https://pubmed.ncbi.nlm.nih.gov/39707386/) | 2024 | Preclinical | Cell Commun Signal | Eplerenone reduced cirrhosis-associated changes in hepatocyte glucose and lipid metabolism, with hypoxia-driven MR activation |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02543397 | JAMP EPLERENONE | Not specified | Not specified |
| 02323060 | INSPRA | Not specified | Not specified |
| 02323052 | INSPRA | Not specified | Not specified |
| 02471442 | MINT-EPLERENONE | Not specified | Not specified |
| 02543389 | JAMP EPLERENONE | Not specified | Not specified |

A sixth authorization, MINT-EPLERENONE (DIN 02471450), is also valid. All six are single-ingredient products.

---

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: liver disease, gallbladder disease, diabetic nephropathy, and impaired renal function disease.
- **Drug Interactions**: 100 interactions were identified. Major-level examples include:
  - Aprepitant
  - Clarithromycin
  - Clotrimazole
  - Potassium chloride, potassium citrate and potassium bicarbonate (hyperkalaemia risk)

  Moderate-level examples include corticosteroids (hydrocortisone, dexamethasone, prednisone, and others), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), acetylsalicylic acid, bupropion, and miconazole.
- **Other considerations**: Hyperkalaemia and renal-function risk would need careful assessment in any new patient population, particularly those with renal impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for pulmonary hypertension is indirect, consisting mainly of animal and cell studies plus a small sleep apnoea study with different endpoints. No clinical trials are registered. The high TxGNN score is a prediction only, so this remains a research question rather than a candidate ready for development.

**To proceed, the following is needed:**
- Human data measuring pulmonary arterial pressure or pulmonary hypertension outcomes, ideally from a pilot or Phase 2 trial
- Mechanism of action data compiled in a structured form
- Package insert warnings and contraindications from Health Canada, including approved indication text and dosage forms for each DIN
- A safety plan covering hyperkalaemia, renal impairment, and the major drug interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

