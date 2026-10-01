---
layout: default
title: Cysteine
parent: Model Prediction Only (L5)
nav_order: 235
evidence_level: L5
indication_count: 7
---

# Cysteine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cysteine: From Parenteral Amino Acid Nutrition to Dry Eye Syndrome

## One-Sentence Summary

Cysteine is an amino acid. The only Canadian product in the data is PRIMENE 10%, an amino acid infusion, and its license record gives no indication text.
The TxGNN model predicts it may be effective for **dry eye syndrome**.
The supporting evidence is **2 relevant randomized trials and 1 systematic review, all on N-acetylcysteine (NAC) rather than free cysteine**, plus several preclinical studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the license record. Likely amino acid supply in parenteral nutrition, inferred from the product name only. |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

*Evidence level note: the upstream pack labelled this L2. No completed Phase 2/3 RCT in the data actually targets dry eye (the only Phase 2/3 trial is terminated and concerns lung disease), so I rated it L3 under the stated rules. That rating rests on one systematic review and small RCTs of NAC.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Cysteine is a building block of glutathione, the body's main thiol antioxidant. Its acetylated form, NAC, is a mucolytic and antioxidant.

Dry eye involves oxidative stress on the ocular surface, inflammation, and abnormal mucin. Restoring glutathione and breaking disulfide bonds in mucus is therefore a plausible way to help. Preclinical work supports the oxidative-stress link, including ROS-activated NLRP3 inflammasome activity in dry eye patients (PMID 25701684).

There are three important caveats:
- Nearly all clinical data concern NAC, given as eye drops or orally, not free L-cysteine. Extrapolating to cysteine is indirect.
- The NAC RCTs are small, and no Phase 3 trial in dry eye was found.
- Topical NAC has also been used to create a mucin-deficient dry eye animal model (PMID 30025127), so its effect on the ocular surface depends on dose and formulation.

## Clinical Trial Evidence

Only two trials bear on this question. The rest surfaced through keyword matches and are unrelated to cysteine.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04793646](https://clinicaltrials.gov/study/NCT04793646) | N/A | Completed | 60 | Randomized, double-blind NAC study for dryness symptoms in primary Sjögren's syndrome. It is most relevant, but ocular-specific outcomes are unconfirmed. |
| [NCT04440280](https://clinicaltrials.gov/study/NCT04440280) | Phase 2 | Recruiting | 45 | Topical NAC eye drops for oxidative stress in Fuchs' endothelial corneal dystrophy. A different corneal disease with a shared mechanism. |
| [NCT01424033](https://clinicaltrials.gov/study/NCT01424033) | Phase 2/3 | Terminated | 5 | Oral NAC safety in connective-tissue-disease interstitial lung disease. Not an eye indication. |
| [NCT01064830](https://clinicaltrials.gov/study/NCT01064830) | Phase 2 | Completed | 21 | Topical cyclosporine 0.05% for brittle nails. Unrelated to cysteine. |
| [NCT04162210](https://clinicaltrials.gov/study/NCT04162210) | Phase 3 | Active, not recruiting | 325 | Belantamab mafodotin vs pomalidomide/dexamethasone in myeloma. Unrelated. |
| [NCT03525678](https://clinicaltrials.gov/study/NCT03525678) | Phase 2 | Completed | 221 | Belantamab mafodotin dose study in myeloma. Unrelated. |
| [NCT03544281](https://clinicaltrials.gov/study/NCT03544281) | Phase 1/2 | Completed | 153 | Belantamab mafodotin combinations in myeloma. Unrelated. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28441068](https://pubmed.ncbi.nlm.nih.gov/28441068/) | 2017 | RCT | J Ocul Pharmacol Ther | Double-blind trial of chitosan-NAC eye drops, measuring tear film thickness in dry eye patients. The abstract does not report results. |
| [39360368](https://pubmed.ncbi.nlm.nih.gov/39360368/) | 2024 | RCT | Clin Exp Rheumatol | Placebo-controlled, double-blind trial of NAC for dryness symptoms in Sjögren's disease. The abstract does not report results. |
| [16334742](https://pubmed.ncbi.nlm.nih.gov/16334742/) | 2005 | Comparative study | Acta Med Croatica | Compared topical acetylcysteine with artificial tears in dry eye. The rationale was mucus reduction. |
| [34339721](https://pubmed.ncbi.nlm.nih.gov/34339721/) | 2022 | Review | Surv Ophthalmol | Systematic review of topical NAC in eye disease (106 references), covering mucolysis, ROS scavenging and adverse effects. |
| [40123221](https://pubmed.ncbi.nlm.nih.gov/40123221/) | 2025 | Preclinical | Adv Mater | Catalase nanoparticle with cysteine-modified chitosan eye drops for dry eye. |
| [39842600](https://pubmed.ncbi.nlm.nih.gov/39842600/) | 2025 | Preclinical | Int J Biol Macromol | NAC-chitosan conjugate on dexamethasone lipid carriers improved corneal permeability and retention. |
| [36581034](https://pubmed.ncbi.nlm.nih.gov/36581034/) | 2023 | Preclinical | Int J Biol Macromol | Chondroitin sulfate-cysteine conjugate improved corneal retention of dexamethasone carriers. |
| [41485487](https://pubmed.ncbi.nlm.nih.gov/41485487/) | 2026 | Preclinical | J Control Release | Superoxide-responsive persulfide prodrug that eliminates ROS in dry eye. |
| [25701684](https://pubmed.ncbi.nlm.nih.gov/25701684/) | 2015 | Mechanistic | Exp Eye Res | ROS-activated NLRP3 inflammasomes drive inflammation in dry eye patients and hyperosmolar corneal cells. |
| [30025127](https://pubmed.ncbi.nlm.nih.gov/30025127/) | 2018 | Preclinical | Invest Ophthalmol Vis Sci | Topical NAC was used to create a mucin-deficient dry eye model, a caution on dose and formulation. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2236875 | PRIMENE 10% | Not listed | Not listed |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, and the mechanism is plausible for NAC. But the clinical evidence is small, and it concerns NAC, not free cysteine. No Phase 3 dry eye trial exists, and the Canadian product is an intravenous amino acid solution, not an eye formulation. The six other predicted indications are weaker still: pharyngitis, nasal cavity disease, acute laryngopharyngitis, both glaucoma entries and exercise-induced malignant hyperthermia have little or no supporting evidence. The two glaucoma entries are near-duplicates.

**To proceed, the following is needed:**
- Extract the actual results of the two NAC RCTs (PMIDs 28441068 and 39360368) and confirm NCT04793646's ocular outcomes.
- Decide whether the research target is cysteine or NAC, and justify any extrapolation between them.
- Obtain the PRIMENE 10% product monograph for indication, warnings and contraindications, and confirm a suitable ophthalmic route and formulation.
- Add the mechanism of action data from DrugBank.

*These results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

