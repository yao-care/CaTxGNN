---
layout: default
title: Pseudoephedrine
parent: High Evidence (L1-L2)
nav_order: 776
evidence_level: L2
indication_count: 3
---

# Pseudoephedrine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **3** 
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

# Pseudoephedrine: From Established Decongestant Use to Nasal Cavity Disease

## One-Sentence Summary

Pseudoephedrine is an oral nasal decongestant found in many cold, sinus and allergy products marketed in Canada, but the data supplied does not record its approved indication text.
The TxGNN model predicts it may be effective for **nasal cavity disease**, with **18 retrieved clinical trials** (only a few directly relevant) and **7 publications** (one human comparative study, the rest mostly animal models and a review).
This prediction probably reflects an existing labeled use rather than true repurposing, so the label should be verified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied data (all Canadian licence entries have empty indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The mechanism of action field in the supplied data is empty, so the explanation below rests on general pharmacology and the model's rationale. Pseudoephedrine is an indirect sympathomimetic that also acts as a direct alpha-adrenergic agonist. It constricts blood vessels in the nasal mucosa, which reduces blood-volume congestion and swelling. This fits the nasal congestion seen in many nasal cavity conditions.

The original indication is not recorded in the data. The Canadian product names (for example "Sudafed Sinus Advance", "Cold + Sinus") suggest it is already used for cold, sinus and allergy congestion. The prediction therefore likely matches an established use, and the label should be checked before it is treated as a new indication.

Human data support the mechanism. A comparative study of oral and topical decongestant effects (PMID 11345158) measured nasal cavity dimensions with acoustic rhinometry. Several animal congestion models also use pseudoephedrine as a reference decongestant.

---

## Clinical Trial Evidence

Of the 18 trials retrieved for this prediction, most concern surgery, devices, probiotics or other drugs. The table lists those closest to pseudoephedrine or nasal decongestion.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00804687](https://clinicaltrials.gov/study/NCT00804687) | Phase 2 | Completed | 53 | Randomized, placebo-controlled, three-way crossover study comparing JNJ-39220675, pseudoephedrine and placebo in allergic rhinitis, using an environmental exposure chamber |
| [NCT03620513](https://clinicaltrials.gov/study/NCT03620513) | Phase 4 | Completed | 160 | Topical anesthesia vs decongestant pretreatment for pain and discomfort during fiberoptic nasal laryngoscopy. The endpoint is procedural comfort, and the specific agent is not confirmed |
| [NCT00517946](https://clinicaltrials.gov/study/NCT00517946) | N/A | Completed | 21 | MRI as a measure of anti-allergy drug effects on nasal dimensions after allergen challenge. A methodology study with no confirmed pseudoephedrine efficacy data |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | H3 receptor antagonist (PF-03654746) vs placebo for congestion after nasal allergen challenge. A different drug, but the same congestion endpoint |
| [NCT01886768](https://clinicaltrials.gov/study/NCT01886768) | N/A | Unknown | 212 | Double vs single pledget nasal anesthesia and decongestion for transnasal endoscopy |
| [NCT05494346](https://clinicaltrials.gov/study/NCT05494346) | N/A | Recruiting | 101 | Decongestant seawater spray with essential oils for acute rhinitis. A device study with no pseudoephedrine link |
| [NCT06580210](https://clinicaltrials.gov/study/NCT06580210) | N/A | Recruiting | 114 | Mechanical decongestant seawater spray for acute rhinitis with nasal obstruction. A device study with no pseudoephedrine link |

Only NCT00804687 directly includes pseudoephedrine as a comparator. Its title is truncated in the source data, so the intervention details should be confirmed.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Human comparative study | Am J Rhinol | Compared oral and topical decongestant effects of phenylpropanolamine and d-pseudoephedrine on nasal cavity dimensions using acoustic rhinometry |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy Asthma Proc | Overview of nonallergic rhinitis, whose shared symptoms include nasal congestion |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Animal study | Am J Rhinol Allergy | Feline congestion model testing loratadine and montelukast, and also d-pseudoephedrine with and without desloratadine |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Animal study | J Pharmacol Toxicol Methods | Pharmacological characterization of a dog model of nasal congestion for studying decongestant mechanisms |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Animal study | Am J Rhinol | Acoustic rhinometry in dogs as a large-animal model for nasal congestion |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Animal study | Am J Rhinol | Allergic nasal congestion model in ragweed-sensitized dogs |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Animal study | J Pharmacol Exp Ther | Selective α2c-adrenergic agonists in animal models of nasal congestion |

---

## Canada Market Information

Showing 5 of 20 authorizations. Dosage form and approved indication text were not recorded for these entries.

| DIN | Product Name |
|---------|------|
| 2242217 | SUDAFED SINUS ADVANCE |
| 1938371 | EXTRA STRENGTH SINUTAB SINUS DAYTIME |
| 2478110 | EXTRA STRENGTH TYLENOL COLD & SINUS PLUS |
| 2352281 | COLD + SINUS |
| 2246162 | REACTINE COMPLETE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism fits nasal congestion, one completed Phase 2 randomized trial includes pseudoephedrine as a comparator, and human and animal data support the decongestant effect. The prediction is probably an existing labeled use rather than a new one, and safety data is missing. Progress is therefore conditional on label and safety verification.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the Canadian products, to confirm whether nasal cavity disease is already labeled
- Mechanism of action data from DrugBank
- Confirmation of the intervention and results in NCT00804687
- Interaction data for pseudoephedrine, since the DDI query returned no results

**Other predicted indications (Hold):**
- **Acute laryngopharyngitis** (score 99.73%): no trials or literature, so the prediction is speculative.
- **Allergic urticaria** (score 99.14%): pseudoephedrine has no antihistamine activity. The literature concerns antihistamines, and the signal likely comes from co-formulation in allergic rhinitis products.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

