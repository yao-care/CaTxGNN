---
layout: default
title: Chlorpheniramine
parent: Moderate Evidence (L3-L4)
nav_order: 183
evidence_level: L3
indication_count: 4
---

# Chlorpheniramine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **4** 
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

# Chlorpheniramine: From Cough and Cold Symptom Relief to Allergic Urticaria

## One-Sentence Summary

Chlorpheniramine is a first-generation H1 antihistamine, sold in Canada mainly in cough and cold products. The TxGNN model predicts it may be effective for **allergic urticaria**. The supporting evidence is thin: **3 clinical trials** (none confirmed as testing chlorpheniramine in urticaria) and **20 publications** (mostly class-level reviews and case reports).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the record (all licence indication fields are empty). The marketed products are cough and cold combinations |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, chlorpheniramine is an alkylamine first-generation H1 antihistamine that has been used since the 1950s. It is commonly used for allergic conditions and for over-the-counter cough and cold relief.

Allergic urticaria is driven by histamine released from mast cells, which causes wheals, flare and itching. Blocking the H1 receptor is therefore a biologically direct mechanism, and H1 antihistamines are the standard first-line drug class for urticaria. The very high TxGNN score agrees with this.

The link comes from class pharmacology, not from a documented mechanism or original indication in the supplied record. Most of the supporting literature concerns other antihistamines (cetirizine, loratadine, acrivastine, ebastine) or chlorpheniramine in other conditions. Direct evidence for chlorpheniramine in allergic urticaria is limited.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completed | 75 | Randomised, double-blind trial of adding a short corticosteroid burst to conventional H1 antihistamine treatment. Plausibly relevant to urticaria, but chlorpheniramine is not confirmed as an intervention. Contextual evidence only |
| [NCT01293201](https://clinicaltrials.gov/study/NCT01293201) | Phase 3 | Completed | 290 | Placebo-controlled study of STAHIST (pseudoephedrine + chlorpheniramine + a small amount of atropine) in seasonal allergic rhinitis. It shows a chlorpheniramine combination in an allergic condition, not urticaria |
| [NCT02082054](https://clinicaltrials.gov/study/NCT02082054) | Phase 2 | Unknown | 125 | Dose-ranging study of atropine with pseudoephedrine 120 mg/chlorpheniramine 8 mg in seasonal allergic rhinitis. It targets rhinitis, not urticaria, and is likely a weak match |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Review | Curr Rev Clin Exp Pharmacol | Comprehensive review of chlorpheniramine. Lists chronic urticaria among its reported clinical uses, alongside asthma, plasma cell gingivitis and depression |
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Randomised phase I trial | Eur J Pharm Sci | Compared oral bilastine, parenteral dexchlorpheniramine and a new parenteral bilastine formulation on histamine-induced wheal and flare |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Loratadine was as effective as several antihistamines, including chlorpheniramine, in controlled comparative studies of allergic disorders |
| [1683523](https://pubmed.ncbi.nlm.nih.gov/1683523/) | 1991 | Review | Ann Allergy | Compares first- and second-generation H1 antagonists. Second-generation agents are less sedating and have little anticholinergic activity |
| [14977391](https://pubmed.ncbi.nlm.nih.gov/14977391/) | 2004 | Review | Drugs | Cetirizine is effective and well tolerated in allergic disorders. Useful as class context, not chlorpheniramine data |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Cetirizine review covering chronic urticaria. Class context only |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review | Drugs | Double-blind trials show acrivastine is effective in chronic urticaria and allergic rhinitis. Class context only |
| [8808167](https://pubmed.ncbi.nlm.nih.gov/8808167/) | 1996 | Review | Drugs | Ebastine improves symptoms in chronic idiopathic urticaria. Class context only |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Case reports + pharmacovigilance review | Medicine | Two cases of chlorpheniramine-induced anaphylaxis plus a pharmacovigilance database review. Notes chlorpheniramine is commonly used for urticaria and allergic rhinitis |
| [26240795](https://pubmed.ncbi.nlm.nih.gov/26240795/) | 2015 | Case report | Asia Pac Allergy | Chlorpheniramine-induced anaphylaxis diagnosed by basophil activation test. Notes chlorpheniramine is widely prescribed for urticaria |

## Canada Market Information

The record lists 20 licences; the first 5 are shown. Dosage form and approved indication text were not provided for any of them.

| DIN | Product Name |
|---------|------|
| 21288 | TEVA-PHENIRAM |
| 2309440 | COLDASIDE COUGH & COLD |
| 2273330 | NYQUIL KIDS COUGH & COLD |
| 2399733 | ADVIL COLD & SINUS CONVENIENCE PACK |
| 2551667 | NYQUIL COLD & FLU ALCOHOL FREE |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were available in the record.

One signal comes from the literature: rare chlorpheniramine hypersensitivity, including anaphylaxis, has been reported in case reports and a pharmacovigilance review (PMIDs 31852144, 26240795). This matters for a drug proposed to treat allergic conditions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is coherent and the TxGNN score is very high. However, no trial confirms chlorpheniramine in urticaria, and most literature concerns other antihistamines. The Health Canada safety data is also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- Verification of NCT01293201 and NCT03296358 (interventions and conditions), since NCT01293201 was completed Phase 3 but studied allergic rhinitis
- Chlorpheniramine-specific controlled studies in urticaria; a 1977 double-blind study in cold urticaria (PMID 334082) appears under a related predicted indication and could be assessed
- Confirmation of the original approved indications from the licence records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

