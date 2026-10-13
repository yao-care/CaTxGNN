---
layout: default
title: Budesonide
parent: Model Prediction Only (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Budesonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Budesonide: From Crohn's Disease and Asthma to Atopic Eczema

## One-Sentence Summary

Budesonide is a glucocorticoid originally used for Crohn's disease, inflammatory bowel disease, asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema** (score 99.96%), but **no clinical trials** are registered for this indication.
The 20 publications retrieved are mostly indirect: contact allergy to corticosteroids, safety studies, and a preclinical formulation study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Crohn's disease, inflammatory bowel disease, Crohn's colitis, asthma, allergic rhinitis (the licence records compiled for this report contain no approved-indication text) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, budesonide is a glucocorticoid with broad anti-inflammatory and immunosuppressive activity. Its efficacy in inflammatory conditions of the gut and airways is established.

Atopic eczema is a Th2-driven inflammatory skin disease, so a corticosteroid mechanism is biologically plausible. Topical corticosteroids are already a mainstay of atopic dermatitis care.

However, the supporting literature does not test budesonide directly in patients with atopic eczema. It consists mainly of reviews, contact sensitization studies, and a preclinical nanoparticle-hydrogel formulation. The high TxGNN score is a computational prediction only. Corticosteroid contact allergy is a documented risk in atopic patients, which is a relevant caution.

Related predictions, listed for context:
- **Dermatitis, atopic** (score 99.81%): the same indirect evidence base and no clinical trials. Evidence level L5.
- **Bronchitis** (score 99.81%): the best-supported alternative, with 10 registered trials (evidence level L2). Most are small, and several concern bronchiolitis obliterans after transplant rather than classical bronchitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for atopic eczema.

---

## Literature Evidence

None of the publications below is a clinical trial of budesonide in atopic eczema. The study types are as classified in the data compiled for this report.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical formulation study | Gels | Budesonide-loaded pH-sensitive nanoparticles in hydrogels developed for local therapy of paediatric atopic dermatitis |
| [31705907](https://pubmed.ncbi.nlm.nih.gov/31705907/) | 2020 | Review | J Allergy Clin Immunol | Emerging therapies for eosinophilic esophagitis, including swallowed topical corticosteroids (indirect) |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Corticosteroid allergy in asthma: delayed contact allergy is frequent and immediate allergy occasional |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Case report | Cureus | Type I hypersensitivity (angioedema, urticaria) to a corticosteroid in a patient with atopic dermatitis |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Open longitudinal study | Pediatr Dermatol | Knemometry in 14 children with atopic dermatitis to assess the effect of topical budesonide on short-term growth |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | In vitro study | Int Immunopharmacol | Budesonide, but not tacrolimus, affected immune functions of normal human keratinocytes |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Patch-test series | Contact Dermatitis | Budesonide is a marker of corticosteroid hypersensitivity; allergy prevalence has been declining |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Intranasal corticosteroids and adrenal suppression in allergic rhinitis (indirect) |
| [9543750](https://pubmed.ncbi.nlm.nih.gov/9543750/) | 1997 | Review | Ned Tijdschr Geneeskd | Contact allergy to corticosteroids, with prevalence up to 6% in suspected contact dermatitis |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cross-sectional | Contact Dermatitis | Patterns of contact sensitization in patients with and without atopic dermatitis |

---

## Canada Market Information

Budesonide has 20 valid single-ingredient licences in Canada and none cancelled. Dosage form and approved-indication text are not available in the data compiled for this report.

| DIN | Product Name |
|---------|------|
| 02494264 | TARO-BUDESONIDE |
| 02241003 | MYLAN-BUDESONIDE AQ |
| 02229099 | PULMICORT NEBUAMP 0.125 MG/ML |
| 02231923 | RHINOCORT AQUA |
| 02052431 | ENTOCORT ENEMA |

Other licensed products include UCERIS, ENTOCORT, CORTIMENT, JORVEZA, PULMICORT TURBUHALER and TEVA-BUDESONIDE.

---

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):**
The model's knowledge graph links budesonide to the following conditions, among others:
- Hypertension and congestive heart failure
- Epilepsy
- Liver disease and gallbladder disease
- Hyperglycaemia
- Measles and herpes simplex virus keratitis
- Hypopituitarism and related pituitary or growth hormone deficiencies, including hypogonadotropic hypogonadism and Kallmann syndrome
- Urea cycle disorders (carbamoyl phosphate synthetase I deficiency, citrullinemia, hyperargininemia)

**Drug interactions:** 100 interactions were identified. Examples:
- **Major:** adalimumab, fosamprenavir
- **Moderate:** zidovudine, isotretinoin, nifedipine, ibuprofen, ketorolac, ethinylestradiol, fluvoxamine, aldesleukin, alemtuzumab
- **Minor:** formoterol, salbutamol

**Literature-based cautions for atopic patients:**
- Corticosteroid contact allergy
- Possible systemic effects, including adrenal suppression and short-term growth effects in children

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is not supported by any clinical trial or direct clinical publication for atopic eczema. Established topical corticosteroids already exist for this condition. The retrieved literature mainly highlights hypersensitivity risks in atopic patients.

**To proceed, the following is needed:**
- Mechanism-of-action data for budesonide
- Package insert warnings and contraindications from Health Canada
- A comparison against existing topical corticosteroids
- Evidence from controlled clinical studies of a dermal budesonide formulation in atopic eczema
- A review of route and formulation compatibility, since the licensed Canadian products are not topical dermal preparations
- Consideration of bronchitis as a better-supported alternative, once the disease definition is clarified (classical or eosinophilic bronchitis versus bronchiolitis obliterans)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

