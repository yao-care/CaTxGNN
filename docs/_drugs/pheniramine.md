---
layout: default
title: Pheniramine
parent: Moderate Evidence (L3-L4)
nav_order: 720
evidence_level: L4
indication_count: 3
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Pheniramine: From Allergy and Cold Symptom Relief to Allergic Urticaria

## One-Sentence Summary

Pheniramine is a first-generation H1 antihistamine. In Canada it is found in allergy eye drops and cold/sinus products, so its original use is inferred from product names because no indication text was supplied.
The TxGNN model predicts it may be effective for **allergic urticaria**, but only **1 loosely related clinical trial** and **20 retrieved publications** exist, and none is a pheniramine-specific efficacy study.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergy and cold symptom relief (inferred from product names; no approved indication text provided) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Pheniramine belongs to the first-generation H1 receptor antagonist class. Its use in allergy products is established, and mechanistically it may be applicable to allergic urticaria.

In allergic urticaria, histamine released from activated mast cells causes the wheal-and-flare response. Blocking the H1 receptor is a well-accepted way to relieve this, so the biological logic is sound and the high TxGNN score is understandable.

There is an important caveat. Because the original indications are unknown, this prediction may reflect a use that H1 antihistamines already carry (a class-labelled use) rather than true repurposing. The supporting literature concerns related drugs (chlorpheniramine, dexchlorpheniramine), not pheniramine itself.

TxGNN also ranked two other indications highly:
- **Nasal cavity disease** (99.28%): only animal-model and physiology studies, no clinical trials. The term is too broad and should be narrowed to allergic rhinitis.
- **Acute laryngopharyngitis** (99.25%): no trials and no literature. The prediction stands alone, and the anticholinergic drying effect could worsen throat dryness.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02082054](https://clinicaltrials.gov/study/NCT02082054) | Phase 2 | Unknown | 125 | Dose-ranging study of atropine added to pseudoephedrine/chlorpheniramine in seasonal allergic rhinitis. It does not involve pheniramine or urticaria, so it gives no direct support. |

---

## Literature Evidence

Of the 20 retrieved publications, the 10 most relevant are listed below. None is a controlled efficacy study of pheniramine in urticaria.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Review | Curr Rev Clin Exp Pharmacol | Review of chlorpheniramine (same class) covering uses including chronic urticaria; indirect, class-level support |
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Randomised phase I trial | Eur J Pharm Sci | Compared bilastine with parenteral dexchlorpheniramine on histamine-induced wheal and flare; related-drug evidence |
| [14709123](https://pubmed.ncbi.nlm.nih.gov/14709123/) | 2004 | Clinical study (type not classified) | Med J Aust | Hydrocortisone with or without chlorpheniramine to prevent antivenom reactions; indirect |
| [2859711](https://pubmed.ncbi.nlm.nih.gov/2859711/) | 1985 | Review | Z Hautkr | Astemizole was effective in chronic urticaria and was compared with older antihistamines including pheniramine |
| [15698856](https://pubmed.ncbi.nlm.nih.gov/15698856/) | 2005 | Preclinical | Life Sci | H1 blockade with chlorpheniramine attenuated mast-cell-driven skin permeability in guinea pigs |
| [18597008](https://pubmed.ncbi.nlm.nih.gov/18597008/) | 2008 | Surveillance study | Methods Find Exp Clin Pharmacol | Large survey of sedation from H1 antihistamines, which is the most frequent side effect |
| [12444322](https://pubmed.ncbi.nlm.nih.gov/12444322/) | 2002 | Clinical study (type not classified) | Int Arch Allergy Immunol | Single-dose oral tolerance testing with alternative compounds in drug adverse reactions |
| [40125237](https://pubmed.ncbi.nlm.nih.gov/40125237/) | 2025 | Case report | Cureus | Immediate hypersensitivity reaction to pheniramine in multiple drug hypersensitivity syndrome (safety signal) |
| [40324831](https://pubmed.ncbi.nlm.nih.gov/40324831/) | 2025 | Case report | Indian J Pharmacol | Loss of consciousness after IV pheniramine with hydrocortisone for an allergic reaction (safety signal) |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Case reports and pharmacovigilance review | Medicine | Chlorpheniramine-induced anaphylaxis (safety signal) |

---

## Canada Market Information

Dosage form, manufacturer and approved indication text were not provided for these authorizations. Five of the 9 licenses are listed.

| DIN | Product Name |
|---------|------|
| 2242764 | VISINE FOR ALLERGY WITH ANTIHISTAMINE |
| 750794 | SOOTHE ALLERGY |
| 481408 | NAPHCON A |
| 2456982 | NEOCITRAN EXTRA STRENGTH COLD & SINUS NIGHT - APPLE CINNAMON |
| 2215403 | NEOCITRAN EXTRA STRENGTH COLD & SINUS NIGHT |

Note that the listed products are eye drops and oral cold/sinus formulations, so route compatibility with an urticaria indication has not yet been assessed.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

The literature does flag possible signals to review:
- **Hypersensitivity and anaphylaxis**: case reports describe reactions to pheniramine and to the related chlorpheniramine.
- **Sedation**: this is the most frequent side effect of H1 antihistamines in a large surveillance study.
- **Anticholinergic effects**: drying effects are expected for a first-generation antihistamine.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is biologically coherent and the TxGNN score is very high. However, there is no pheniramine-specific controlled evidence for urticaria, the only trial is unrelated, and the supporting literature concerns related drugs. Safety data is also missing, which blocks progression to safety screening. This remains a research question rather than a candidate ready for development.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap)
- Original approved indications and mechanism of action (for example, from DrugBank)
- Confirmation of whether urticaria is already a labelled use of pheniramine or related antihistamines
- Pheniramine-specific efficacy data in urticaria, such as controlled trials or wheal-and-flare studies
- A review of hypersensitivity and sedation risk and an assessment of route and formulation compatibility

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

