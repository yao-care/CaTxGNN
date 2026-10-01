---
layout: default
title: Hydroxyzine
parent: Moderate Evidence (L3-L4)
nav_order: 456
evidence_level: L4
indication_count: 5
---

# Hydroxyzine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Hydroxyzine: From First-Generation Antihistamine to Allergic Urticaria

## One-Sentence Summary

Hydroxyzine is a first-generation H1 antihistamine that is marketed in Canada. The TxGNN model predicts it may be effective for **allergic urticaria**, with a very high graph score (99.77%). Only **1 clinical trial** (a pilot study of cetirizine, hydroxyzine's active metabolite) and **20 publications** were retrieved, and none directly tests hydroxyzine in this condition, so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Hydroxyzine is a first-generation H1 histamine receptor inverse agonist. Histamine released from mast cells drives the wheal-and-flare reaction of urticaria, so blocking H1 receptors is biologically coherent for this condition.

Its active metabolite is cetirizine, which has been studied extensively in urticaria. Cetirizine data therefore support the mechanism, but they are not direct evidence for hydroxyzine.

Guideline-level literature also tempers the prediction. A 2019 Canadian position statement (CSACI) recommends newer-generation H1 antihistamines over first-generation agents such as hydroxyzine. The reasons are sedation, cognitive impairment and other safety concerns. This is a question of positioning, not of mechanism.

Among the other predictions, cold urticaria has the most supporting evidence. It includes a 1984 randomized double-blind comparison that included hydroxyzine, which is the only hydroxyzine-specific study in the pack. Rosacea conjunctivitis, recalcitrant atopic dermatitis and atopic IgE responsiveness have no supporting evidence and remain at model-prediction level.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Pilot feasibility study comparing IV cetirizine 10 mg with IV diphenhydramine 50 mg in acute urticaria. It does not test hydroxyzine and is not an efficacy trial, so relevance is indirect. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position statement | Allergy Asthma Clin Immunol | Names hydroxyzine among first-generation antihistamines with significant sedation, cognitive and cardiac safety concerns. Newer-generation agents are recommended first-line for allergic rhinitis and urticaria. |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Antihistamines are the first step in chronic spontaneous urticaria. Hydroxyzine was used in the past, and second-generation agents are now preferred, at higher doses. |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Reviews the efficacy and safety of first- and newer-generation antihistamines in allergic rhinitis and chronic idiopathic urticaria. |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review | Clin Exp Allergy | Discusses how to choose the best H1 antihistamine for urticaria and how to compare agents. |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Cetirizine, the carboxylated metabolite of hydroxyzine, is a potent H1 antagonist with clinical potential in chronic urticaria and lacks the CNS depressant effects of standard antihistamines. |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine, a second-generation antihistamine, in allergic rhinitis and urticaria. Indirect. |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Review | Allergy Asthma Proc | Levocetirizine in allergic rhinitis and chronic idiopathic urticaria. Indirect. |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Review | Clin Ther | Levocetirizine for allergic rhinitis and chronic idiopathic urticaria in adults and children. Indirect. |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | H1 antihistamines in children, with strong evidence for allergic rhinoconjunctivitis. |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case report | J Clin Gastroenterol | Cetirizine-induced cholestasis. It is a safety signal for the metabolite, not efficacy evidence. |

## Canada Market Information

| DIN / License No. | Product Name |
|---------|------|
| 646024 | HYDROXYZINE |
| 646016 | HYDROXYZINE |
| 646059 | HYDROXYZINE |
| 742813 | HYDROXYZINE HYDROCHLORIDE INJECTION USP |
| 24694 | ATARAX |

## Safety Considerations

- **Class-level concerns (CSACI 2019):** First-generation antihistamines such as hydroxyzine commonly cause sedation, impaired cognition, poor sleep quality, dry mouth, dizziness and orthostatic hypotension. They have also been linked to accidents, overdoses and sudden cardiac death.

Please refer to the package insert for drug-specific warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the model score is high, but no supplied study tests hydroxyzine in allergic urticaria. The only trial involves cetirizine and is a feasibility pilot. Current guidance also favors newer-generation antihistamines on safety grounds. The Canadian package insert warnings and contraindications are missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking)
- Mechanism of action data from DrugBank
- Approved indication text for each Canadian license, to confirm whether urticaria or pruritus is already labeled
- Hydroxyzine-specific comparative or controlled data in urticaria, ideally against second-generation antihistamines
- Verification of the arms and population of NCT01940393 (five antihistamines, n=150) to see whether hydroxyzine is included
- A full-text review of the 1984 cold urticaria comparison (PMID 6480953), which would be the first step if cold urticaria is prioritized

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

