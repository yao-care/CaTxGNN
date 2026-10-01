---
layout: default
title: Tobramycin
parent: Moderate Evidence (L3-L4)
nav_order: 913
evidence_level: L4
indication_count: 10
---

# Tobramycin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tobramycin: From Antibacterial Use to Exposure Keratitis

## One-Sentence Summary

Tobramycin is an aminoglycoside antibiotic, and the Evidence Pack does not list its original approved indications.
The TxGNN model predicts it may be effective for **exposure keratitis**, but only **2 clinical trials** and **7 publications** were retrieved, and none directly tests tobramycin for this condition.
The high score appears to reflect proximity to bacterial keratitis in the knowledge graph rather than direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Exposure keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Tobramycin is an aminoglycoside antibiotic that is bactericidal through 30S ribosomal binding. This suits Gram-negative organisms such as *Pseudomonas aeruginosa*.

Exposure keratitis is mainly a desiccation and lagophthalmos problem (the eyelids do not close fully), not a primary infection. Tobramycin could plausibly help only when a secondary bacterial infection develops on the damaged cornea. One retrieved case report, a patient who could not close his eyes, fits this scenario.

There is also a counter-signal. An in vitro study (PMID 2707046) found that aminoglycosides, including tobramycin, are toxic to corneal epithelial cells. This argues against use on an ocular surface that is already compromised.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Compares treatment modalities for dendritic (herpes simplex) corneal ulcer. Tobramycin is not identified as the studied intervention. |
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Unknown | 170 | Platelet-rich fibrin membrane in ophthalmic diseases, including corneal ulcer. Unrelated to tobramycin. |

Both trials were graded C for relevance. No trial tests tobramycin in exposure keratitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Bacterial keratitis from multidrug-resistant *Shewanella algae* in a patient in a vegetative state who could not close his eyes. |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related *Bacillus cereus* keratitis traced to a contaminated lens case. |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis after photorefractive keratectomy. |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro study | Current Eye Research | Compared corneal epithelial cytotoxicity of neomycin, gentamicin, tobramycin and amikacin in rabbit corneal cell culture, showing a toxicity concern. |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | In vitro / microbiology | Nippon Ganka Gakkai Zasshi | Compared MIC and post-antibiotic effect of antibiotic eyedrops against isolates from infectious keratitis in Japan. |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Veterinary case series | Polish Journal of Veterinary Sciences | Feline ocular toxoplasmosis: seroprevalence, diagnosis and treatment outcome in 60 cats. Not relevant to exposure keratitis in humans. |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report | Yan Ke Xue Bao (Eye Science) | Paracentral corneal dellen as a rare sign of Graves ophthalmopathy. |

No randomized trials were found. The evidence is case reports, in vitro work and veterinary data.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2230640 | TOBRAMYCIN INJECTION |
| 2239630 | TOBI |
| 2533103 | TOBRAMYCIN INJECTION USP |
| 513962 | TOBREX |
| 2241209 | TOBRAMYCIN INJECTION USP |

Dosage forms and approved indication text were not provided for these licenses. Route compatibility with ocular use has not been assessed.

---

## Safety Considerations

- **Ocular surface toxicity:** In vitro data (PMID 2707046) show that tobramycin and other aminoglycosides are toxic to corneal epithelial cells. This is a concern for an already damaged corneal surface.

Please refer to the package insert for warnings, contraindications and drug interaction information. No drug interaction records were found in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is L4. No retrieved trial or publication tests tobramycin for exposure keratitis, and the one mechanistic study points to possible epithelial harm. The high TxGNN score most likely reflects graph proximity to bacterial keratitis, so any benefit would be limited to secondary infection.

**To proceed, the following is needed:**
- Canadian package insert warnings, contraindications and approved indications. Safety screening cannot proceed without them.
- Mechanism of action data from DrugBank.
- Dosage forms and routes for the 14 DINs, to check whether an ophthalmic product is available.
- Clinical data on tobramycin for infected exposure keratitis, and a review of whether corneal epithelial toxicity is clinically significant.
- Consider prioritizing other predictions for this drug. Otitis externa (L3) has more supporting literature, though it may already be an established use and should be checked against labeled indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

