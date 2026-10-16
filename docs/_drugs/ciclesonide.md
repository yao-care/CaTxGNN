---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 191
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Ciclesonide: predicted new indication Atopic eczema (evidence level L5). Approved use: Asthma (including intrinsic and allergic asthma), allergic rhinitis…"
monitor_inn: "CICLESONIDE"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis", "asthma-related traits, susceptibility to"]
---

# Ciclesonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid originally used for asthma and allergic or vasomotor rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific direction, so the prediction rests on the model and mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (including intrinsic and allergic asthma), allergic rhinitis, vasomotor rhinitis (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ciclesonide was not available in the data compiled for this report. Based on known pharmacology, ciclesonide is an inhaled corticosteroid prodrug. It is activated to des-ciclesonide, a glucocorticoid receptor agonist with anti-inflammatory effects.

Asthma, allergic rhinitis and atopic eczema are all allergic (atopic) inflammatory conditions. Corticosteroids are an established treatment class for atopic eczema, so a glucocorticoid anti-inflammatory mechanism could plausibly apply.

There are important caveats. No clinical trials or publications were found for ciclesonide in atopic eczema. Ciclesonide is formulated for inhalation and nasal use, so a topical or systemic version would need separate formulation, route and safety work. The model also lists "dermatitis, atopic" (score 99.73%) as a separate prediction. It is essentially the same condition and should be merged with atopic eczema in later review.

### Other Predictions Reviewed

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| 2-Hydroxyethyl methacrylate sensitization | 99.76% | L5 | Computational prediction only. Sensitization to a specific hapten is not a typical treatment target. |
| Dermatitis, atopic | 99.73% | L5 | Duplicate of atopic eczema. |
| Bronchitis | 99.70% | L4 | Only indirect evidence (a Finnish COPD guideline). Mechanistically relevant to airway inflammation. |
| Contact dermatitis | 99.25% | L4 | The only publication is a case report of an allergic reaction, so it is a safety signal rather than evidence of benefit. |
| Asthma-related traits, susceptibility to | 99.13% | L5 | A genetic susceptibility trait, not a treatable condition. Likely reflects proximity to the approved asthma indication. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for atopic eczema.

Literature found for other predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline/Review | Basic & Clinical Pharmacology & Toxicology | Finnish national guideline on diagnosis and drug treatment of stable COPD. Indirect evidence for bronchitis, as it does not test ciclesonide specifically. |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Case report | Contact Dermatitis | Systemic allergic dermatitis caused by inhaled budesonide, with cross-reactivity in patch tests to ciclesonide. This is a hypersensitivity safety signal, not evidence of benefit. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02285614 | ALVESCO | Not listed | Not listed |
| 02285606 | ALVESCO | Not listed | Not listed |
| 02303671 | OMNARIS | Not listed | Not listed |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (derived from drug–disease contraindication links, not from label text): herpes simplex virus keratitis, adrenocortical insufficiency, Addison disease, osteoporosis (including postmenopausal), fungal infections (including dermatophytosis), ocular hypertension, glaucoma, and parasitic infection.
- **Hypersensitivity**: A published case report describes cross-reactivity between inhaled budesonide and ciclesonide in patch testing.
- **Drug Interactions**: 63 interactions were identified. The main ones are listed below.
  - **Major**: Cladribine
  - **Moderate**: Clarithromycin, Miconazole, Cobicistat, Atazanavir, Fosamprenavir, Amprenavir, Boceprevir, Ceritinib, Conivaptan, Fostamatinib, Abametapir (topical), inhaled rapid-acting human insulin
  - **Minor**: Formoterol, Salbutamol, Arformoterol

  Several of the moderate interactions involve strong CYP3A4 inhibitors, which would be expected to raise corticosteroid exposure. Interactions with omeprazole, lansoprazole, prednisolone and famotidine are of unknown severity.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.96%), and the glucocorticoid mechanism is plausible for atopic eczema. However, there are no clinical trials or publications for this use, so evidence is at the lowest level (L5). Ciclesonide's current Canadian products are inhaled and nasal, and no route of administration suitable for skin disease has been established.

**To proceed, the following is needed:**
- The Health Canada package insert, to confirm approved indications, warnings and contraindications. This is a blocking gap for safety screening.
- Mechanism-of-action data from DrugBank.
- A literature and trial search for ciclesonide in atopic eczema, including topical or alternative formulations.
- An assessment of route and formulation feasibility, since current products are not designed for skin application.
- Consolidation of the duplicate "atopic eczema" and "dermatitis, atopic" predictions.
- Review of the hypersensitivity cross-reactivity signal and CYP3A4 interaction risks if development proceeds.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

