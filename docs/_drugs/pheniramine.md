---
layout: default
title: Pheniramine
parent: Model Prediction Only (L5)
nav_order: 727
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "Pheniramine"
predicted_indications: ["nasal cavity disease"]
description: "Pheniramine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Pheniramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Pheniramine: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Pheniramine is a first-generation H1-antihistamine, originally used for allergic rhinitis, the common cold, conjunctivitis and urticaria.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9928 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 9 of 9) |
| Number of DINs | 9 (valid: 9) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pheniramine is a first-generation H1-receptor antagonist. Its efficacy in allergic and upper-airway conditions is established, and mechanistically it may be applicable to allergic urticaria through the same histamine H1 blockade.

Urticaria and angioedema are already among pheniramine's original indications. The retrieved literature gives no prospective efficacy evidence for pheniramine in allergic urticaria.

Another prediction shows the same pattern. **Nasal cavity disease** (score 0.9928) extends existing indications (rhinitis, common cold, pharyngitis). It has no trials or publications, so it rests on the model prediction and the mechanistic rationale alone (evidence level L5).

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

