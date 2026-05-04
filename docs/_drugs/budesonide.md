---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Budesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Budesonide: From Asthma / Inflammatory Airway Disease to Atopic Eczema

## One-Sentence Summary

Budesonide is a potent synthetic glucocorticoid primarily used for inflammatory airway diseases (asthma, COPD) and gastrointestinal inflammatory conditions such as Crohn's disease; no Canadian regulatory license data is currently available in this dataset.
The TxGNN model predicts it may be effective for **Atopic Eczema**,
with **2 clinical trials** and **20 publications** currently identified in support of this direction — though the majority of evidence is indirect or safety-focused rather than efficacy-focused.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Canadian license data in current dataset) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacology, budesonide is a synthetic glucocorticoid with high topical potency and extensive first-pass hepatic metabolism, giving it a favorable local anti-inflammatory activity relative to systemic exposure. It suppresses pro-inflammatory gene transcription via glucocorticoid receptors, inhibiting Th2-associated cytokines (IL-4, IL-13, IL-31), reducing eosinophil infiltration, mast cell activation, and IgE-mediated responses — all of which are central to the immunopathology of atopic eczema.

Atopic eczema (atopic dermatitis) is driven by Th2-polarized immune dysregulation and skin barrier dysfunction. Because topical glucocorticosteroids are already the first-line treatment class for atopic dermatitis, budesonide's predicted efficacy is mechanistically plausible. A 2024 preclinical study (PMID 38275852) specifically explored pH-sensitive budesonide-loaded nanoparticles formulated into hydrogels for local atopic dermatitis therapy, capitalizing on the characteristic pH shift in atopic lesions to improve drug delivery — suggesting active pharmaceutical interest in novel budesonide delivery platforms for this indication.

However, there is a critical dual-edged concern that sets this prediction apart from straightforward repurposing candidates: budesonide itself is established as one of the more common corticosteroid contact allergens, included in the European Baseline Patch Test Series since 2000. Multiple publications in this evidence set document that patients with atopic dermatitis — who already have compromised skin barrier function and heightened sensitization risk — are at significant risk of developing contact hypersensitivity to budesonide. This "sensitizer paradox" (using a drug that can itself trigger or worsen dermatitis in atopic patients) is a primary safety concern requiring careful evaluation before any therapeutic development proceeds.

---

## Clinical Trial Evidence

Neither identified trial directly tests budesonide efficacy in atopic eczema. Both have only indirect relevance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy in atopic wheezing children at high risk for asthma; atopic background includes eczema, but the primary intervention is immunotherapy — budesonide is not the study drug |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | Unknown | 150 | Observational endotype characterization of severe paediatric asthma, including atopy and atopic dermatitis phenotyping; not an interventional budesonide trial |

> **Note:** No clinical trial in the current dataset directly evaluates budesonide as a treatment for atopic eczema in humans.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Pharmaceutical/Preclinical | Gels | Budesonide-loaded pH-sensitive Eudragit L 100 nanoparticles in hydrogel for topical atopic dermatitis therapy; exploits lesional skin pH to improve local drug release; most directly relevant study to this predicted indication |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | RCT (sub-group analysis) | Allergologia et Immunopathologia | Response to inhaled budesonide in atopic vs. non-atopic infants/preschoolers with recurrent wheezing; provides efficacy data in atopic paediatric population |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | RCT (veterinary) | J Vet Pharmacol Ther | Barazone (0.025% budesonide leave-on conditioner) in canine atopic dermatitis: significantly reduced skin lesions and pruritus vs. placebo in a crossover design |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Clinical Observation | Dermatology | Topical glucocorticosteroids in children with atopic dermatitis: documents systemic absorption and effects on IGF axis, bone and collagen turnover; raises growth suppression concern |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Clinical Study | Pediatric Dermatology | Knemometry in children with AD treated with topical budesonide; demonstrated measurable short-term lower leg growth suppression, confirming systemic absorption risk |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cross-sectional | Contact Dermatitis | Contact sensitization patterns in Asian AD patients; budesonide identified among key corticosteroid allergens, with comparable or higher sensitization rates versus the general population |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Retrospective Patch Test | Dermatitis | Contact hypersensitivity to European standard series and corticosteroid series (including budesonide) in adolescents/adults with atopic dermatitis |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Cross-sectional | J Am Acad Dermatol | Allergic contact dermatitis to topical medications in adults with AD; highlights the sensitization paradox of using topical corticosteroids in this population |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Patch Test Registry Study | Contact Dermatitis | Italian SIDAPA baseline series: budesonide patch test results 2018–2019; shows decreasing trend in budesonide contact allergy frequency over two decades, but sensitization remains clinically relevant |
| [40020933](https://pubmed.ncbi.nlm.nih.gov/40020933/) | 2025 | Translational Research | J Allergy Clin Immunol | Cutaneous ceramide synthesis dysregulation in paediatric eosinophilic esophagitis mirrors atopic dermatitis epithelial barrier dysfunction; provides mechanistic parallels relevant to budesonide's proposed role in barrier-compromised skin |

---

## Safety Considerations

**Additional evidence-derived safety signal:** Multiple publications in this evidence set consistently identify budesonide as a recognized contact allergen in the European Baseline Patch Test Series. Patients with atopic dermatitis — who have impaired skin barrier function and heightened sensitization risk — show similar or higher rates of positive patch-test reactions to budesonide compared with the general population. This creates a clinically significant "sensitizer paradox" for this specific indication. Two publications also document systemic glucocorticoid effects (growth suppression, HPA axis suppression) from topical budesonide in paediatric atopic dermatitis patients, underscoring the need for careful monitoring.

For complete prescribing safety information including contraindications and drug interactions, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While budesonide's glucocorticoid mechanism is theoretically aligned with the Th2-driven inflammation of atopic eczema, no human clinical trial directly demonstrates efficacy in this indication, and the drug is itself a documented contact allergen in the target patient population — creating a fundamental benefit-risk challenge that must be resolved before development can proceed.

**To proceed, the following is needed:**
- Prospective controlled clinical trials directly assessing budesonide topical formulations versus standard-of-care comparators (e.g., hydrocortisone, mometasone) in human atopic dermatitis
- Pre-screening assessment for budesonide contact sensitization in the target population prior to therapeutic exposure
- Pharmacokinetic evaluation of novel delivery systems (e.g., nanoparticle hydrogels per PMID 38275852) to establish local bioavailability and systemic exposure profiles
- Detailed MOA data retrieval from DrugBank (currently a data gap) to formally support mechanistic justification in regulatory submissions
- Health Canada pre-submission consultation given the drug's current zero-DIN status in Canada
- Pediatric safety assessment plan, given documented growth suppression signal in children with topical budesonide use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

