---
layout: default
title: Fluticasone Furoate
parent: Model Prediction Only (L5)
nav_order: 402
evidence_level: L5
indication_count: 8
---

# Fluticasone Furoate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Fluticasone Furoate: From Allergic Rhinitis and Asthma/COPD to Atopic Eczema

## One-Sentence Summary

Fluticasone furoate is a corticosteroid marketed in Canada as AVAMYS, ARNUITY ELLIPTA and BREO ELLIPTA, so its original uses are presumably nasal and inhaled treatment of allergic rhinitis, asthma and COPD.
The TxGNN model predicts it may be effective for **atopic eczema**, with **10 clinical trials** and **2 publications** matched to this indication.
All 10 trials test the related salt fluticasone propionate or are only loosely related, so the evidence supports a class effect, not direct proof for furoate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis and asthma/COPD (inferred from the marketed product names; no indication text in the Canadian licence records) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 (weak: the Phase 3 trial was terminated and tested propionate, not furoate) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fluticasone furoate is a high-potency glucocorticoid receptor agonist. It suppresses NF-kB/AP-1 signalling and Th2 cytokine output. Atopic skin inflammation is driven by the same pathways, so the biological rationale is coherent. Topical corticosteroids are already a standard treatment for atopic dermatitis.

The catch is that the supporting trials all use **fluticasone propionate**, a different salt, in topical or swallowed form. No topical dermatologic furoate product appears in the supplied data. The prediction therefore rests on the shared corticosteroid class, not on furoate-specific data.

Two other points affect how to read the prediction:
- "Atopic eczema" and "dermatitis, atopic" (rank 4) are the same disease concept with identical trials and literature. They should be merged, not counted twice.
- Other high-scoring predictions are weaker. Bronchitis has more trials, including furoate-containing products such as RELVAR/BREO, but they mostly cover COPD, bronchiectasis and bronchiolitis obliterans. Several skin-related predictions (HEMA sensitization, occupational dermatitis, phototoxic dermatitis) and "asthma-related traits, susceptibility to" have no trials or literature at all.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | Double-blind RCT of twice-weekly fluticasone propionate 0.05% cream to prevent relapse in children with mild to moderate atopic dermatitis. It is the closest design match, but it was stopped early and is small. |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Open-label randomized study of intermittent (twice-weekly) fluticasone propionate cream plus moisturizer in children with stabilized atopic dermatitis. |
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label, uncontrolled study of fluticasone propionate 0.05% lotion and its effect on the HPA axis in infants with atopic dermatitis. |
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | Tacrolimus 0.1% ointment versus fluticasone 0.005% ointment in adults with facial atopic dermatitis. Fluticasone is likely the comparator. |
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | Tacrolimus 0.03% ointment versus fluticasone 0.005% ointment in children with moderate to severe atopic dermatitis. Fluticasone is likely the comparator. |
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Exploratory vehicle-controlled paired study of Elidel 1% plus Cutivate 0.05% in severe atopic dermatitis. |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | Investigator-blind pilot comparing EpiCeram with mid-strength topical steroid (fluticasone propionate 0.05%) in children with moderate to severe atopic dermatitis. |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | SEAL study of skin-barrier care plus proactive fluticasone propionate cream to prevent food allergy in infants with early atopic dermatitis. The focus is prevention. |
| [NCT00426283](https://clinicaltrials.gov/study/NCT00426283) | Phase 2 | Completed | 42 | Placebo-controlled RCT of swallowed fluticasone propionate, most likely in eosinophilic esophagitis, so it is indirect for eczema. |
| [NCT03594565](https://clinicaltrials.gov/study/NCT03594565) | Early Phase 1 | Completed | 13 | Case series of nasal steroids for skin reactions to continuous glucose monitors in children with type 1 diabetes. It is device-related contact reaction, not eczema. |

One further matched trial, NCT04706559 (probiotics in children with atopic dermatitis), does not involve fluticasone and is omitted. It was matched only by disease term.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Intranasal corticosteroids in allergic rhinitis, which often coexists with asthma and atopic dermatitis. It reviews HPA-axis suppression as a measure of systemic steroid effect. |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case report | Indian J Otolaryngol Head Neck Surg | Allergen immunotherapy in a patient with autoimmune disease. Atopic dermatitis is mentioned only as an emerging use of immunotherapy, and fluticasone is not the subject. |

Neither publication tests fluticasone furoate in atopic eczema.

---

## Canada Market Information

Seven DINs are recorded. The five main authorizations are listed below. The records contain no dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 2298589 | AVAMYS |
| 2446588 | ARNUITY ELLIPTA |
| 2446561 | ARNUITY ELLIPTA |
| 2444186 | BREO ELLIPTA |
| 2408872 | BREO ELLIPTA |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.98%), and corticosteroids are a proven class for atopic dermatitis. However, every relevant trial used fluticasone propionate, the only Phase 3 RCT was terminated early with 54 patients, and no topical furoate product appears in the supplied data. The current evidence supports a class-level research question, not a furoate-specific repurposing case.

**To proceed, the following is needed:**
- Furoate-specific evidence in atopic dermatitis, such as a topical formulation, dermal pharmacology data, or a controlled trial
- Confirmation from the Health Canada package inserts of the approved indications, warnings and contraindications
- Detailed mechanism of action data from DrugBank
- A merged "atopic eczema" / "dermatitis, atopic" entry to avoid double counting
- A safety plan covering HPA-axis suppression and use in children, since several trials examine this
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

