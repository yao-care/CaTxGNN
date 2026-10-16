---
layout: default
title: Amikacin
parent: Moderate Evidence (L3-L4)
nav_order: 49
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Amikacin: predicted new indication Paratyphoid fever (evidence level L4). Approved use: Bacterial pneumonia, Pseudomonas aeruginosa infection…"
---

# Amikacin
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

# Amikacin: From Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Amikacin is an aminoglycoside antibiotic originally used for serious gram-negative bacterial infections such as bacterial pneumonia, Pseudomonas aeruginosa infection and bacterial meningitis.
The TxGNN model predicts it may be effective for **paratyphoid fever**, but **no clinical trials** and only **8 publications** (mostly epidemiology, antibiogram and case reports) are available, and none provides controlled evidence for amikacin.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, Pseudomonas aeruginosa infection, bacterial meningitis and other gram-negative infections (Health Canada indication text is not available) |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amikacin is an aminoglycoside antibiotic that binds the 30S ribosomal subunit and is active against many gram-negative Enterobacterales, including Salmonella. Its efficacy in gram-negative infections is established, so the prediction has some biological plausibility for paratyphoid fever, which is caused by *Salmonella* Paratyphi.

There are important limits. Aminoglycosides penetrate cells poorly, and *Salmonella* Paratyphi is an intracellular pathogen. Aminoglycosides are generally not considered effective for enteric fever in vivo, even when the isolate is susceptible in vitro. For typhoid fever, a related condition, one small study (PMID 2598731) reported a clinical effective rate of 36.4% with amikacin (11 patients) versus 100% with ofloxacin. No amikacin-specific clinical data for paratyphoid fever are available.

Other predictions in the list (for example typhoid fever, salmonellosis and meningococcemia) have a similar pattern: antibacterial plausibility but only indirect evidence. Several (diffuse scleroderma, congenital analbuminemia, polyclonal hyperviscosity syndrome, hyperamylasemia) have no plausible mechanistic link and no evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case report | Pediatr Hematol Oncol | Child with leukemia and *S.* Paratyphi B acalculous cholecystitis, treated successfully with cefepime, amikacin and G-CSF (combination therapy) |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Cohort | Mikrobiyol Bul | 48 paratyphoid B patients; antibiotic options for strains resistant to classical therapy |
| [8354556](https://pubmed.ncbi.nlm.nih.gov/8354556/) | 1993 | Epidemiology | Indian J Pathol Microbiol | Multidrug-resistant *S.* Typhi remained sensitive to aminoglycosides, including amikacin, in vitro |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Cohort | Med J Armed Forces India | Susceptibility patterns of *S.* Typhi and Paratyphi A in northern India |
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Cohort | J Indian Med Assoc | 145 children with enteric fever; clinical profile and antibiotic sensitivity |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiology | New Microbiol | Occurrence of *S.* Typhi and Paratyphi in Jordan, 1988–2000 |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Epidemiology | Pak J Biol Sci | Isolation and identification of *S.* Paratyphi from enteric fever patients in Quetta |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Cohort | JNMA | Blood culture isolates and antibiograms in a teaching hospital |

For the closely related typhoid fever prediction, the most relevant paper is an in vitro study ([19554971](https://pubmed.ncbi.nlm.nih.gov/19554971/), 2009), in which 464 *S.* Typhi isolates were sensitive to gentamicin and amikacin.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02242971 | Amikacin Sulfate Injection USP | Injection | Not available |
| 02486717 | Amikacin Sulfate Injection | Injection | Not available |
| 02529459 | Amikacin Sulfate Injection | Injection | Not available |
| 02481073 | Amikacin Sulfate Injection USP | Injection | Not available |
| 02525909 | Amikacin Sulfate Injection | Injection | Not available |

---

## Safety Considerations

- **Contraindication signals (from knowledge-graph drug-disease links, not label text)**: kidney disease, pyoureter, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, central nervous system vertigo, myasthenia gravis (including adult-onset), neuromuscular junction disease, parkinsonian disorders and Parkinson disease.
- **Drug Interactions** (100 interactions recorded; examples):
  - **Major**: magnesium sulfate, mannitol
  - **Moderate**: amphotericin B (including lipid complex, liposomal and cholesteryl sulfate forms), other aminoglycosides (kanamycin, neomycin), proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, pantoprazole, rabeprazole, dexlansoprazole), aspirin, mesalazine and related agents (balsalazide, olsalazine), exenatide

Please refer to the package insert for warnings and full contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there are no clinical trials, and the literature is mostly epidemiology, susceptibility data and case reports. Aminoglycosides penetrate cells poorly and are not recommended for enteric fever, and the available clinical signal for amikacin in typhoid fever was weak. Effective, established alternatives exist for enteric fever.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clinical evidence specific to amikacin in paratyphoid or enteric fever, including intracellular activity and comparison with standard therapy
- A nephrotoxicity, ototoxicity and neuromuscular monitoring plan, given the kidney, neuromuscular and vestibular signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

