---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Aztreonam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Aztreonam: From Gram-Negative Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

Aztreonam is a monobactam beta-lactam antibiotic used to treat serious gram-negative bacterial infections by inhibiting bacterial cell wall synthesis. The TxGNN model predicts it may be effective for **Gonococcal Urethritis**, with **1 completed Phase 2/3 clinical trial** and **8 publications** currently supporting this direction. Among the top 10 predicted indications, gonococcal urethritis is selected as the primary focus because it carries the strongest mechanistic rationale and clinical evidence (Evidence Level L2); several other higher-ranked predictions (e.g., polyclonal hyperviscosity syndrome, congenital analbuminemia) lack biological plausibility and are assessed as knowledge-graph noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-negative bacterial infections (monobactam antibiotic class) |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on information embedded in the repurposing rationale, aztreonam is a monobactam beta-lactam antibiotic that acts by binding specifically to penicillin-binding protein 3 (PBP3) on gram-negative bacteria, thereby inhibiting the final cross-linking step of peptidoglycan cell wall synthesis and causing bacterial lysis. Uniquely among beta-lactams, aztreonam has activity exclusively against gram-negative organisms and carries no cross-reactivity with most penicillin allergies.

Gonococcal urethritis is caused by *Neisseria gonorrhoeae*, a gram-negative diplococcus — precisely the bacterial class within aztreonam's spectrum of activity. Inhibition of PBP3-mediated cell wall synthesis in *N. gonorrhoeae* is mechanistically direct and well-supported. This prediction is therefore not a distant model extrapolation, but rather a mechanistically coherent repurposing opportunity.

The clinical urgency is further reinforced by the global antimicrobial resistance (AMR) crisis in gonorrhea. The CDC has designated AMR *N. gonorrhoeae* as one of the top three most urgent AMR threats in the United States. As *N. gonorrhoeae* has successively acquired resistance to penicillins, tetracyclines, fluoroquinolones, and increasingly cephalosporins, parenteral third-generation cephalosporins are now the last reliable front-line option. Aztreonam — a monobactam not conventionally used for gonorrhea — represents a viable salvage candidate against resistant strains, as evidenced by both laboratory susceptibility data and clinical trial results spanning four decades.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | Completed | 32 | Open-label, single-arm demonstration study of single-dose intramuscular aztreonam (2 g) for pharyngeal gonorrhea in men. Designed in response to urgent AMR gonorrhea threat; evaluated aztreonam as a repurposed older antibiotic. Pharyngeal eradication was the primary endpoint; urethral gonorrhea efficacy requires site-specific confirmation in a dedicated trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Non-randomized Clinical Trial | Antimicrobial Agents and Chemotherapy | Single-arm trial (the published report of NCT03867734); single-dose IM aztreonam 2 g evaluated for *N. gonorrhoeae*; supports repurposing against ceftriaxone-resistant gonorrhea and provides proof-of-concept efficacy and tolerability data |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical Study | Antimicrobial Agents and Chemotherapy | Aztreonam 1 g IM vs. spectinomycin 2 g IM for uncomplicated gonorrhea; no treatment failures in either arm; aztreonam showed efficacy at urethral, rectal, and endocervical sites |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical Trial | Genitourinary Medicine | Single 1 g IM injection of aztreonam cleared *N. gonorrhoeae* in 61 men and 26 women at all anatomical sites (one pharyngeal failure noted); effective against both penicillin-sensitive and penicillin-resistant strains |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Clinical Study | Journal of Infectious Diseases | Early evidence of aztreonam activity against penicillinase-producing *N. gonorrhoeae* (PPNG) strains at a time when PPNG resistance was emerging globally; established feasibility as an alternative to spectinomycin |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | Clinical Study | Japanese Journal of Antibiotics | 30 male patients with gonococcal urethritis treated with aztreonam; bacteriological evaluation of 61 *N. gonorrhoeae* strains (15% PPNG); clinical and microbiological cure demonstrated for both PPNG and non-PPNG strains |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiologic/Therapeutic Study | Acta Urologica Japonica | One-shot aztreonam therapy for gonococcal infections; epidemiological analysis of 244 clinical isolates (17.2% PPNG); demonstrated broad effectiveness across resistance phenotypes |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | Clinical Study | Giornale Italiano di Dermatologia e Venereologia | Clinical evaluation of aztreonam in acute gonococcal urethritis; early European evidence supporting efficacy |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Surveillance/Microbiological Study | Journal of Infection and Chemotherapy | Reports emergence of *N. gonorrhoeae* strains with high-level aztreonam resistance (non-beta-lactamase-mediated); important resistance surveillance data that should inform any clinical deployment of aztreonam for gonorrhea |

---

## Canada Market Information

Aztreonam currently has **no Health Canada-approved products** in Canada. There are zero Drug Identification Numbers (DINs) on record, meaning aztreonam is not commercially available through standard Canadian regulatory channels. Any clinical use in Canada would require a Special Access Programme (SAP) application or a new regulatory submission.

---

## Safety Considerations

Please refer to the package insert for safety information. Safety data (key warnings, contraindications, and drug interactions) were not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2/3 clinical trial (NCT03867734) and eight supporting publications spanning 1983–2020 demonstrate aztreonam's direct antibacterial activity against *Neisseria gonorrhoeae*, with a mechanistically sound rationale (beta-lactam PBP3 inhibition against a gram-negative pathogen) and a compelling public health justification rooted in the global AMR gonorrhea crisis. Evidence is graded L2; the primary limitations are small sample sizes and a focus on pharyngeal rather than urethral disease.

**To proceed, the following is needed:**
- Formal mechanism of action data from DrugBank to complete mechanistic scoring
- A larger, randomized controlled trial comparing aztreonam to current standard-of-care (ceftriaxone ± azithromycin) specifically for urethral gonorrhea
- Site-specific efficacy data for rectal and endocervical gonorrhea beyond the existing pharyngeal trial
- Up-to-date resistance surveillance: the 2001 literature (PMID 11406757) flagged emerging aztreonam resistance in *N. gonorrhoeae*; current minimum inhibitory concentration (MIC) distributions must be characterized before any deployment
- Full safety profile review including Canadian package insert warnings, contraindications, and relevant drug interactions
- Health Canada regulatory pathway assessment (Special Access Programme or new drug submission), given that aztreonam is not currently marketed in Canada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

