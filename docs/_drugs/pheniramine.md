---
layout: default
title: Pheniramine
parent: Moderate Evidence (L3-L4)
nav_order: 727
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Pheniramine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Pheniramine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis"]
---

# Pheniramine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Pheniramine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Pheniramine is a first-generation H1-antihistamine, originally used for allergic rhinitis, the common cold, conjunctivitis and urticaria.
The TxGNN model predicts it may be effective for **allergic urticaria**, but there are **0 registered clinical trials** and only **4 publications** (3 case reports and 1 review) supporting this direction.
Allergic urticaria largely overlaps with its existing indications, so this is not a true repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, atopic/papillary/vernal conjunctivitis, urticaria, angioedema, among others (the Health Canada indication text was not available) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pheniramine is a first-generation H1-receptor antagonist. Its efficacy in allergic and upper-airway conditions is established, and mechanistically it may be applicable to allergic urticaria through the same histamine H1 blockade.

Urticaria and angioedema are already among pheniramine's original indications. The high TxGNN score (99.67%) most likely reflects this overlap rather than a new therapeutic direction. The retrieved literature gives no prospective efficacy evidence for pheniramine in allergic urticaria.

Two other predictions show the same pattern. **Nasal cavity disease** (score 99.28%) and **acute laryngopharyngitis** (score 99.25%) both extend existing indications (rhinitis, common cold, pharyngitis). Neither has any trials or publications, so both rest on the model prediction and the mechanistic rationale alone (evidence level L5).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2859711](https://pubmed.ncbi.nlm.nih.gov/2859711/) | 1985 | Review | Zeitschrift fur Hautkrankheiten | Worldwide review of astemizole trials (39 trials, over 2,300 patients) in hay fever, allergic rhinitis, conjunctivitis and chronic urticaria. Pheniramine appears only as one of the older comparator antihistamines. |
| [40324831](https://pubmed.ncbi.nlm.nih.gov/40324831/) | 2025 | Case report | Indian Journal of Pharmacology | Loss of consciousness after concurrent intravenous pheniramine and hydrocortisone given for an anaphylactic reaction. |
| [40125237](https://pubmed.ncbi.nlm.nih.gov/40125237/) | 2025 | Case report | Cureus | Immediate hypersensitivity reaction to pheniramine in a patient with multiple drug hypersensitivity syndrome. |
| [16854350](https://pubmed.ncbi.nlm.nih.gov/16854350/) | 2006 | Case report | Allergologia et Immunopathologia | Life-threatening facial edema in a child after ingesting a pine processionary caterpillar, which mimicked an allergic event. |

None of these publications provides prospective efficacy evidence for pheniramine in allergic urticaria. The case reports mostly concern adverse events.

---

## Canada Market Information

All 9 licences below are valid single-ingredient products. Dosage form and approved indication text were not available.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242764 | VISINE FOR ALLERGY WITH ANTIHISTAMINE | Not available | Not available |
| 00750794 | SOOTHE ALLERGY | Not available | Not available |
| 00481408 | NAPHCON A | Not available | Not available |
| 02456982 | NEOCITRAN EXTRA STRENGTH COLD & SINUS NIGHT - APPLE CINNAMON | Not available | Not available |
| 02215403 | NEOCITRAN EXTRA STRENGTH COLD & SINUS NIGHT | Not available | Not available |

Four more licences are valid: CALMYLIN ACE (02198630), NEOCITRAN COLD & SORE THROAT NIGHT (02246602), HOT LEMON RELIEF FOR SYMPTOMS OF COLD AND FLU EXTRA STRENGTH (02238890) and HOT LEMON RELIEF FOR SYMPTOMS OF COLD AND FLU REGULAR STRENGTH (02047349).

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease relationships in the TxGNN knowledge graph, not from package insert text):
  - Cardiovascular and respiratory: hypertension, chronic obstructive pulmonary disease, bronchitis
  - Neurological and psychiatric: epilepsy, insomnia, psychotic disorders (including schizophreniform and schizoaffective disorders)
  - Hepatic and renal: liver disease and liver failure, kidney disease, pyoureter
  - Gastrointestinal: gastric ulcer and peptic ulcer disease, gastritis, inflammatory bowel disease, pancreatitis, gallbladder disease
  - Endocrine and metabolic: diabetes mellitus, hyperglycemia, diabetic ketoacidosis, hypothyroidism (including myxedema and congenital hypothyroidism)
  - Other: benign prostatic hyperplasia, thrombocytopenia, dermatitis herpetiformis
- **Reported hypersensitivity**: A recent case report describes an immediate hypersensitivity reaction to pheniramine itself (PMID 40125237). A second case report describes loss of consciousness after concurrent intravenous pheniramine and hydrocortisone (PMID 40324831).

Please refer to the package insert for the full label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Allergic urticaria largely overlaps with pheniramine's existing indications (urticaria, angioedema, allergic rhinitis), so the high prediction score does not indicate a new repurposing opportunity. No clinical trials exist, and the literature contains only case reports and an older comparative review. The other two predictions (nasal cavity disease and acute laryngopharyngitis) are supported by the model prediction alone.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (the safety screening cannot proceed without them)
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the 9 Canadian licences
- Prospective or controlled efficacy data in allergic urticaria, or confirmation that this is already a labeled use, in which case it is not a repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

