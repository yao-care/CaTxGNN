---
layout: default
title: Bepotastine
parent: High Evidence (L1-L2)
nav_order: 107
evidence_level: L2
indication_count: 1
last_modified_at: 2026-10-13
description: "Bepotastine: predicted new indication Allergic urticaria (evidence level L2). Approved use: Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis"
---

# Bepotastine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **1** 
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

# Bepotastine: From Atopic Conjunctivitis to Allergic Urticaria

## One-Sentence Summary

Bepotastine is a second-generation antihistamine, originally used for allergic eye conditions such as atopic, papillary and vernal conjunctivitis.
The TxGNN model predicts it may be effective for **allergic urticaria**,
with **1 clinical trial** (a Phase 1 pharmacokinetic study, not an efficacy trial) and **12 publications** currently supporting this direction, including one randomised comparative trial in chronic spontaneous urticaria.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic conjunctivitis, papillary conjunctivitis, vernal conjunctivitis |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. The following is based on general pharmacological knowledge, not on the supplied data. Bepotastine is a selective histamine H1 receptor antagonist. It also stabilises mast cells and inhibits eosinophil migration and some inflammatory mediators (such as leukotriene B4 and IL-5).

Histamine released from mast cells is the main driver of wheals, flare and itching in urticaria. Blocking H1 receptors is therefore a direct and well-established treatment approach. The same mechanism underlies its use in allergic conjunctivitis, so the original and predicted indications share one pathway: histamine-mediated allergic reactions.

Published reviews report that oral bepotastine besilate is approved in Japan and Korea for urticaria and pruritus. The high TxGNN score is consistent with this biological plausibility, but it is a computational prediction and not clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01897428](https://clinicaltrials.gov/study/NCT01897428) | Phase 1 | Completed | 26 | Compared the pharmacokinetics of two bepotastine formulations (salicylate vs besilate) in healthy volunteers. It provides exposure and safety data only, with no urticaria patients and no efficacy endpoints. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37067147](https://pubmed.ncbi.nlm.nih.gov/37067147/) | 2023 | RCT | Indian J Dermatol Venereol Leprol | Randomised, open-label, parallel study comparing bepotastine besilate with levocetirizine in chronic spontaneous urticaria |
| [20687621](https://pubmed.ncbi.nlm.nih.gov/20687621/) | 2010 | Review | Drugs | Oral bepotastine is a second-generation H1 antagonist. Trials and surveillance studies show it is effective and generally well tolerated in allergic rhinitis, chronic urticaria and skin-related pruritus. |
| [24191914](https://pubmed.ncbi.nlm.nih.gov/24191914/) | 2013 | Review | Expert Opin Pharmacother | Topical bepotastine 1.5% is approved for allergic conjunctival itching. The oral form is approved in Japan for allergic rhinitis and urticaria. |
| [30208284](https://pubmed.ncbi.nlm.nih.gov/30208284/) | 2018 | Review | Expert Opin Pharmacother | Oral bepotastine is widely used outside the US for allergic rhinitis, urticaria and chronic pruritus, with results similar to other drugs of its class. |
| [22035879](https://pubmed.ncbi.nlm.nih.gov/22035879/) | 2011 | Review | J Allergy Clin Immunol | Review of histamine and H1-antihistamines, which act as inverse agonists. |
| [38543228](https://pubmed.ncbi.nlm.nih.gov/38543228/) | 2024 | PK modelling | Pharmaceutics | Population and physiologically based PK modelling to propose paediatric dosing for allergic rhinitis or urticaria, where use is currently off-label. |
| [24105252](https://pubmed.ncbi.nlm.nih.gov/24105252/) | 2013 | PK study | Clin Drug Investig | Compared the pharmacokinetics of bepotastine besilate and salicylate in healthy subjects. |
| [24656153](https://pubmed.ncbi.nlm.nih.gov/24656153/) | 2014 | PK study | Clin Ther | Bioavailability of two bepotastine formulations in healthy Chinese volunteers. |
| [27803886](https://pubmed.ncbi.nlm.nih.gov/27803886/) | 2016 | Case report | Asia Pac Allergy | Hypersensitivity (urticaria) to bepotastine, cross-reactive with other antihistamines, in a teenage patient. |
| [19348661](https://pubmed.ncbi.nlm.nih.gov/19348661/) | 2009 | Case report | J Dermatol | Urticaria induced by multiple H1-antihistamines, a rare phenomenon. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02456532 | BEPREVE | Not specified | Not specified |

## Safety Considerations

- **Hypersensitivity**: Rare case reports describe urticaria triggered by bepotastine itself, with cross-reactivity to other antihistamines. Patients with a history of antihistamine-induced urticaria need careful assessment.
- **Sedation**: Large-scale surveillance of H1-antihistamines identifies sedation as the most frequent side effect of the class.

Please refer to the package insert for full warnings, contraindications and drug interaction information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is biologically direct, and the literature includes a randomised comparison with levocetirizine in chronic spontaneous urticaria. Reviews also report that oral bepotastine is approved for urticaria in other countries. However, the only registered trial is a Phase 1 pharmacokinetic study, the supporting efficacy evidence is limited to one open-label RCT, and the Canadian product (BEPREVE) is an ophthalmic brand, so the route differs from the oral form used for urticaria.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmation of the dosage form and approved indication for DIN 02456532, and of whether an oral formulation is available or planned in Canada
- Mechanism of action data from DrugBank to replace the general pharmacology used here
- Efficacy data from completed Phase 2/3 trials in urticaria patients
- Dosing guidance for special populations, including children
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

