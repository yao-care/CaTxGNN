---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 191
evidence_level: L5
indication_count: 5
monitor_inn: "CICLESONIDE"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis"]
last_modified_at: 2026-10-28
description: "Ciclesonide: predicted new indication atopic eczema (evidence level L5). Approved use: Not recorded in the local data"
---

# Ciclesonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ciclesonide: Inhaled corticosteroid prodrug → Atopic eczema (atopic eczema)
{: .text-alpha }

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid prodrug that is converted in the body to an active glucocorticoid.
The TxGNN model predicts it may be effective for **atopic eczema**,
but **no clinical trials and no publications** directly studying this disease were found, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | atopic eczema |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ciclesonide is not available in the data compiled for this report. Based on its drug class, ciclesonide is a prodrug that is activated to des-ciclesonide, a glucocorticoid receptor agonist with anti-inflammatory effects.

Corticosteroids are an established treatment class for atopic eczema, an inflammatory skin disease. This makes the prediction mechanistically plausible. However, this reasoning is by class analogy only. No study of ciclesonide itself in atopic eczema was supplied.

Ciclesonide is an inhaled product. Use on the skin, or systemically, would need separate formulation, route and safety evaluation. Route compatibility has not yet been assessed.

Two other model outputs, "dermatitis, atopic" and "2-hydroxyethyl methacrylate sensitization", also have no supporting studies. The "dermatitis, atopic" entry is essentially the same condition as the main prediction and should be consolidated with it in later review.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for atopic eczema.

Two items were found for other conditions. They do not study atopic eczema and do not raise the evidence level:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline/Review | Basic & Clinical Pharmacology & Toxicology | Finnish guideline on diagnosis and drug treatment of stable COPD. Indirect; it does not test ciclesonide. |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Case report | Contact Dermatitis | Systemic allergic dermatitis caused by inhaled budesonide, with cross-reactivity in patch tests to ciclesonide. This is a hypersensitivity signal, not evidence of benefit. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02285614 | ALVESCO | Not recorded | Not recorded |
| 02285606 | ALVESCO | Not recorded | Not recorded |
| 02303671 | OMNARIS | Not recorded | Not recorded |

## Safety Considerations

**Drug interactions:** 63 interactions were identified. Examples of the main ones:
- **Major:** Cladribine
- **Moderate:** Clarithromycin, Miconazole, Cobicistat, Atazanavir, Fosamprenavir, Amprenavir, Boceprevir, Ceritinib, Conivaptan, Fostamatinib, inhaled rapid-acting human insulin, topical Abametapir
- **Minor:** Formoterol, Salbutamol, Arformoterol

Several of the moderate interactions involve strong CYP3A4 inhibitors (for example clarithromycin, cobicistat and the HIV protease inhibitors). These can raise corticosteroid exposure.

**Conditions of concern for corticosteroids as a class** (not taken from the product label): herpes simplex keratitis, adrenocortical insufficiency, Addison disease, osteoporosis, fungal and parasitic infections, dermatophytosis, ocular hypertension and glaucoma.

**Hypersensitivity:** A published case report describes cross-reactivity between inhaled budesonide and ciclesonide in patch testing, so allergic contact reactions should be considered.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9996), and corticosteroids are mechanistically relevant to atopic eczema. However, no trial or publication studies ciclesonide in this disease, so the evidence level is L5. The available literature includes a hypersensitivity signal.

**To proceed, the following is needed:**
- Studies or trials of ciclesonide, or its active metabolite, in atopic eczema
- Mechanism-of-action data from DrugBank
- Health Canada package insert warnings and contraindications
- Assessment of route and formulation, since the marketed products are inhaled or nasal
- Review of the comparative benefit of established topical corticosteroids already used in atopic eczema
- Consolidation of the duplicate "atopic eczema" and "dermatitis, atopic" predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

