---
layout: default
title: Cyproheptadine
parent: Moderate Evidence (L3-L4)
nav_order: 232
evidence_level: L4
indication_count: 4
---

# Cyproheptadine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Cyproheptadine: From an Unrecorded Original Indication to Allergic Urticaria

## One-Sentence Summary

Cyproheptadine is a first-generation H1 antihistamine, but the supplied record lists no original indication for it.
The TxGNN model predicts it may be effective for **allergic urticaria** with a very high score, yet only **2 clinical trials** and **19 publications** were retrieved, and none of the trials and only 1 of the publications actually tests cyproheptadine.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied record |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the supplied record. Based on class pharmacology, cyproheptadine is a first-generation H1 antihistamine with additional 5-HT2 antagonist and anticholinergic activity. Blocking H1 receptors is the accepted way to control the wheal and flare of histamine-mediated urticaria, so the link is biologically plausible.

This rationale rests on class knowledge, not on the supplied record, which lists neither an original indication nor a mechanism. The retrieved evidence mostly concerns other antihistamines (loratadine, desloratadine, rupatadine, bilastine, acrivastine) and does not test cyproheptadine in allergic urticaria.

A related signal is stronger. For **cold urticaria**, a mast-cell-driven physical urticaria, several older cyproheptadine studies exist (1971–1995), including double-blind comparisons. That subtype was ranked separately by the model and is discussed in the conclusion.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07101445](https://clinicaltrials.gov/study/NCT07101445) | Phase 4 | Recruiting | 94 | Methylprednisolone vs dexamethasone premedication to prevent allergic reactions to motixafortide in multiple myeloma stem cell mobilization. This is drug-hypersensitivity prophylaxis, not urticaria treatment, and cyproheptadine is not studied. |
| [NCT00762983](https://clinicaltrials.gov/study/NCT00762983) | N/A | Completed | 1003 | Post-marketing safety survey of loratadine (Claritin) in children. It is observational and concerns a different antihistamine. |

Neither trial supports cyproheptadine efficacy.

---

## Literature Evidence

Only 1 of the 19 retrieved publications involves cyproheptadine (it is listed first below). The other 9 shown are indirect evidence on other antihistamines.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Comparative study (double-blind crossover) | Asian Pac J Allergy Immunol | Cyproheptadine vs ketotifen in 6 Thai children with primary acquired cold urticaria. This is cold urticaria, not allergic urticaria in general. |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review | Clin Exp Allergy | Discusses how to choose the best H1-antihistamine for urticaria, especially chronic spontaneous urticaria. |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Bilastine, a second-generation antihistamine, in allergic rhinitis and urticaria. |
| [21162645](https://pubmed.ncbi.nlm.nih.gov/21162645/) | 2011 | Review | Expert Rev Clin Immunol | Rupatadine for allergic rhinitis and urticaria. Histamine is the key mediator and H1 antihistamines are the main therapy. |
| [18339040](https://pubmed.ncbi.nlm.nih.gov/18339040/) | 2008 | Review | Allergy | Rupatadine in allergic rhinitis and chronic urticaria. Histamine is the primary mediator, and a broader anti-inflammatory profile may add benefit. |
| [20067329](https://pubmed.ncbi.nlm.nih.gov/20067329/) | 2010 | Post-marketing studies | Clin Drug Investig | Safety and efficacy of desloratadine in seasonal allergic rhinitis or chronic urticaria. It does not involve cyproheptadine. |
| [33198523](https://pubmed.ncbi.nlm.nih.gov/33198523/) | 2021 | Review | Expert Opin Pharmacother | Second-generation H1-antihistamines in children over 2 years with allergic rhinitis and urticaria, focused on rupatadine. |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Acrivastine in allergic rhinitis, urticaria and related disorders. Double-blind trials show benefit in chronic urticaria. |
| [16259582](https://pubmed.ncbi.nlm.nih.gov/16259582/) | 2005 | Review | Expert Opin Pharmacother | Desloratadine for allergic rhinitis, chronic idiopathic urticaria and allergic inflammatory disorders. |
| [35396016](https://pubmed.ncbi.nlm.nih.gov/35396016/) | 2022 | Review | Profiles Drug Subst Excip Relat Methodol | Loratadine drug profile. It is widely used for allergic diseases including chronic urticaria. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2332248 | JAMP-CYPROHEPTADINE |
| 2533065 | MAR-CYPROHEPTADINE |
| 2466732 | EURO-CYPROHEPTADINE 2MG/5ML |

Dosage form and approved-indication text were not provided in the record. The third product appears to be an oral liquid (2 mg/5 mL).

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the supplied data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score for allergic urticaria is very high (99.96%), but none of the retrieved trials tests cyproheptadine, and the supporting literature concerns other antihistamines. The evidence is at L4, and the mechanism is plausible from class pharmacology only.

Two related predictions differ:
- **Cold urticaria** is a much stronger signal. It has several small, older cyproheptadine studies, including double-blind comparisons (e.g., PMID 334082, 6480953 and 2901993). A provisional read of that evidence supports **Proceed with Guardrails**, mainly for sedation and anticholinergic burden in children and older adults.
- **Nasal cavity disease** (Hold, L4) and **acute laryngopharyngitis** (Hold, L5, model prediction only) are not supported by cyproheptadine-specific evidence.

**To proceed, the following is needed:**
- The Health Canada product monograph (warnings, contraindications, approved indications) for the three marketed products
- Detailed mechanism-of-action data from DrugBank
- A cyproheptadine-specific study in urticaria, ideally compared against up-dosed second-generation antihistamines
- A sedation and anticholinergic safety plan for children and older adults
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

