---
layout: default
title: Pseudoephedrine
parent: Moderate Evidence (L3-L4)
nav_order: 783
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Pseudoephedrine: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis (also vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Pseudoephedrine"
predicted_indications: ["allergic urticaria"]
---

# Pseudoephedrine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Pseudoephedrine: From Allergic Rhinitis to Nasal Cavity Disease

## One-Sentence Summary

Pseudoephedrine is a nasal decongestant originally used for allergic rhinitis, vasomotor rhinitis, the common cold and related upper-airway conditions.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but this is mostly a broader version of its existing uses.
Currently there are **0 registered clinical trials** and **7 publications** (2 human or review papers, 5 animal-model studies) for this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (also vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis and others). Health Canada indication text is not available. |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, pseudoephedrine is an indirect sympathomimetic with alpha-adrenergic activity. It constricts blood vessels in the nasal lining and reduces congestion.

The original indications (allergic rhinitis, vasomotor rhinitis, rhinitis, common cold) already cover most nasal conditions. "Nasal cavity disease" is a broad category, so this prediction is largely a generalization of existing use, not a true repurposing. The very high score is consistent with this overlap.

The other two predictions are weaker:
- **Acute laryngopharyngitis** (score 99.73%, L5): the score probably reflects proximity to approved indications such as pharyngitis and the common cold. There is no direct mechanistic evidence, no trials and no literature.
- **Allergic urticaria** (score 99.14%, L5): pseudoephedrine has no antihistaminic activity. The retrieved papers are about antihistamines, and pseudoephedrine appears only as a combination partner or analytical context.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Clinical study (human) | Am J Rhinol | Compared oral and topical decongestant effects of phenylpropanolamine and d-pseudoephedrine on nasal cavity dimensions, measured by acoustic rhinometry |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy Asthma Proc | Overview of nonallergic rhinitis (inflammatory and noninflammatory causes) with nasal congestion as a shared symptom |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Animal model (cat) | Am J Rhinol Allergy | Loratadine plus montelukast produced decongestion; d-pseudoephedrine was also studied with and without desloratadine |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Animal model | J Pharmacol Exp Ther | Selective α2c-adrenergic agonists were evaluated in nasal congestion models |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Animal model (dog) | Am J Rhinol | Allergic nasal congestion model in ragweed-sensitized dogs using acoustic rhinometry |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Animal model (dog) | J Pharmacol Toxicol Methods | Pharmacological characterization of a chronic dog model of nasal congestion |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Animal model (dog) | Am J Rhinol | Acoustic rhinometry dog model of nasal congestion induced by mast cell degranulation |

---

## Canada Market Information

Pseudoephedrine is marketed in Canada under 20 valid single-ingredient licences. Dosage form and approved indication text are not available in the data compiled for this report. The first 5 are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242217 | SUDAFED SINUS ADVANCE | Not available | Not available |
| 01938371 | EXTRA STRENGTH SINUTAB SINUS DAYTIME | Not available | Not available |
| 02478110 | EXTRA STRENGTH TYLENOL COLD & SINUS PLUS | Not available | Not available |
| 02352281 | COLD + SINUS | Not available | Not available |
| 02246162 | REACTINE COMPLETE | Not available | Not available |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are model-derived links, not label text): hypertension, coronary artery disease, congestive heart failure, stroke and cerebrovascular disorder, diabetes mellitus and diabetic ketoacidosis, hypothyroidism, benign prostatic hyperplasia, epilepsy, liver and kidney disease, peptic ulcer disease, inflammatory bowel disease, severe COPD, pancreatitis and substance abuse/dependence, among others.
- **Drug interactions**: 100 interactions were found in total. The 20 shown are mostly Moderate and involve antidiabetic agents: sulfonylureas (chlorpropamide, glimepiride, glipizide, glyburide, acetohexamide), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), GLP-1 agonists (albiglutide, dulaglutide, exenatide), DPP-4 inhibitor alogliptin, acarbose and insulins. Diethylpropion is also Moderate. Ascorbic acid is Minor.

Official warnings and contraindications from the Health Canada package insert were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction score is high, but the evidence is thin: there are no registered trials, and most literature comes from animal models. "Nasal cavity disease" largely restates indications pseudoephedrine already has, so a repurposing study would add little. The other two predictions are supported only by the model score.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian products
- A defined, specific nasal condition beyond the existing indications, ideally with human trial data
- A cardiovascular and metabolic safety plan, given the knowledge-graph contraindications and the interactions with antidiabetic drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

