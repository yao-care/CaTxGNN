---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 189
evidence_level: L5
indication_count: 6
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

# Ciclesonide: From Asthma and Allergic Rhinitis to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled and intranasal corticosteroid marketed in Canada as ALVESCO and OMNARIS. The Canadian record does not list its approved indications, so this report uses asthma and allergic rhinitis from general knowledge of these products.
The TxGNN model predicts it may be effective for **atopic eczema** (score 99.96%), but there are currently **0 clinical trials** and **0 publications** for this indication, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence record (asthma and allergic rhinitis are assumed from general knowledge of the ALVESCO and OMNARIS products) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Ciclesonide is a glucocorticoid prodrug that is converted in the body to its active form, des-ciclesonide. Glucocorticoids suppress inflammation broadly, and inflammation drives the skin lesions of atopic eczema.

The high score most likely reflects class-level corticosteroid links in the knowledge graph rather than anything specific to ciclesonide. No ciclesonide-specific data, trials or literature support this indication. Ciclesonide is also formulated for inhalation and nasal use, and route compatibility with a skin indication has not been assessed. The prediction is therefore a plausible hypothesis, not evidence of benefit.

The same disease also appears as "dermatitis, atopic" (rank 3, score 99.73%). This is a duplicate ontology entry and should be merged during review so that no evidence is counted twice.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for atopic eczema.

Literature exists only for two other predicted indications, and neither supports atopic eczema:

| PMID | Year | Type | Journal | Related Prediction | Key Findings |
|------|-----|------|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline/Review | Basic & Clinical Pharmacology & Toxicology | Bronchitis | Finnish national guideline on diagnosis and pharmacotherapy of stable COPD. It is indirect evidence and not specific to ciclesonide. |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Case report | Contact Dermatitis | Contact dermatitis | Systemic allergic dermatitis from inhaled budesonide, with cross-reactivity to ciclesonide on patch testing. This is a hypersensitivity safety signal, not efficacy evidence. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2285614 | ALVESCO |
| 2285606 | ALVESCO |
| 2303671 | OMNARIS |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records.
- **Corticosteroid hypersensitivity**: A published case report describes allergic dermatitis from inhaled budesonide that cross-reacted with ciclesonide on patch testing (PMID 22957490). This suggests a possible cross-sensitivity concern in patients with corticosteroid allergy.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score and class-level corticosteroid reasoning. There are no ciclesonide-specific trials or publications for atopic eczema, and the available formulations are not designed for skin use.

**To proceed, the following is needed:**
- The Health Canada package insert, to confirm approved indications, warnings and contraindications
- Mechanism of action data from DrugBank
- A route-compatibility assessment, since only inhaled and nasal products are known and no topical route is available
- A targeted search for ciclesonide studies in atopic dermatitis, and merging of the duplicate "atopic eczema" and "dermatitis, atopic" entries
- Other predictions: bronchitis is a research question needing ciclesonide-specific COPD or chronic bronchitis data. The asthma-susceptibility prediction (rank 6) likely reflects an existing use and should be checked against the label. Contact dermatitis and 2-hydroxyethyl methacrylate sensitization remain on Hold, with no efficacy evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

