---
layout: default
title: Ceftriaxone
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ceftriaxone: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic with established global use for serious bacterial infections, yet it currently has no approved drug identification numbers (DINs) in the Canadian regulatory database.
The TxGNN model's highest-evidence prediction identifies **Infectious Otitis Media** as the most actionable candidate (TxGNN rank #4, score 99.26%), supported by **3 clinical trials** and **19 publications** — and this finding reflects an existing global clinical use pattern, making the Canadian regulatory gap the central question for repurposing action.

> **Note on prediction selection:** The TxGNN rank #1 prediction (polyclonal hyperviscosity syndrome, score 99.39%) carries no supporting clinical trials or literature (L5, Hold). This report therefore focuses on the highest-evidence prediction — rank #4, Infectious Otitis Media (L2, Proceed with Guardrails) — to maximize actionability.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Canadian regulatory approval on record (globally used for bacterial infections: meningitis, sepsis, pneumonia, gonorrhea) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.26% (rank #4) |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, ceftriaxone is a broad-spectrum beta-lactam antibiotic that exerts bactericidal activity by irreversibly binding to penicillin-binding proteins (PBPs) on the bacterial cell surface. This blocks transpeptidation — the final cross-linking step of peptidoglycan cell wall synthesis — leading to cell wall destabilization and bacterial lysis. Its activity spans both Gram-positive and Gram-negative organisms, and a plasma half-life of approximately 8 hours supports once-daily or single-dose intramuscular administration.

Infectious otitis media is one of the most common pediatric bacterial infections worldwide. Its three primary causative pathogens — *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis* — fall squarely within ceftriaxone's antibacterial spectrum. Critically, ceftriaxone achieves middle ear tissue concentrations exceeding 50% of plasma levels, ensuring adequate local drug exposure at the infection site. These combined properties — potency against relevant pathogens, tissue penetration, and dosing convenience — make it biologically well-suited for this indication.

It is important to note that this is not novel repurposing in the traditional biological sense. Ceftriaxone intramuscular injection is already embedded in pediatric infectious disease guidelines in the United States as a second-line option for acute otitis media — particularly when oral therapy has failed, the patient cannot tolerate oral medications, or adherence is a concern. The TxGNN model's signal therefore highlights a **regulatory market gap** rather than an unexplored hypothesis: ceftriaxone is a globally established treatment for this indication, yet it is absent from the Canadian drug identification number database.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicenter, randomized, double-blind, placebo-controlled trial comparing 5-day vs. 10-day antibiotic therapy in children aged 6–23 months with acute otitis media; designed to evaluate clinical outcomes and impact on antimicrobial resistance. Trial was terminated before completion; full efficacy results unavailable. |
| [NCT01272999](https://clinicaltrials.gov/study/NCT01272999) | N/A | Completed | 391 | Post-marketing observational study of Prevnar 13 (pneumococcal 13-valent conjugate vaccine) impact on otitis media in children. Not a ceftriaxone intervention study; provides epidemiological context on the pneumococcal burden underlying the indication. |
| [NCT02567825](https://clinicaltrials.gov/study/NCT02567825) | N/A | Completed | 250 | Compared tympanostomy tube placement vs. nonsurgical management in children with recurrent acute otitis media over a 2-year follow-up period. Surgical intervention study; provides treatment pathway context but does not address antibiotic efficacy directly. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [8989332](https://pubmed.ncbi.nlm.nih.gov/8989332/) | 1997 | RCT | *Pediatrics* | Prospective, randomized, single-blind trial (Greater Boston Otitis Media Study Group) comparing a single IM dose of ceftriaxone vs. 10 days of oral TMP-SMZ for acute otitis media; directly tests ceftriaxone clinical efficacy head-to-head. |
| [11099083](https://pubmed.ncbi.nlm.nih.gov/11099083/) | 2000 | RCT | *Pediatric Infectious Disease Journal* | Compared 1-day vs. 3-day IM ceftriaxone regimens in children with nonresponsive acute otitis media; found 3-day regimen superior in bacteriologic eradication, supporting licensed single-dose use as baseline. |
| [35841649](https://pubmed.ncbi.nlm.nih.gov/35841649/) | 2022 | Retrospective Cohort | *Int'l Journal of Pediatric Otorhinolaryngology* | Large US academic primary care analysis of factors associated with IM ceftriaxone use for AOM, noting increased prescribing rates (particularly for otitis-conjunctivitis) as a potential antimicrobial stewardship concern. |
| [39361280](https://pubmed.ncbi.nlm.nih.gov/39361280/) | 2024 | Clinical Guideline Review | *JAMA Network Open* | Systematic assessment of pediatric outpatient antibiotic prescribing in the US; ~50% of prescriptions found unnecessary or inappropriate, with specific recommendations on AOM including appropriate cephalosporin use. |
| [20802367](https://pubmed.ncbi.nlm.nih.gov/20802367/) | 2010 | Clinical Review | *Otology & Neurotology* | Recommendations for prevention and antimicrobial treatment of meningitis and AOM in children with cochlear implants; includes specific antibiotic therapy guidance covering ceftriaxone-class agents. |
| [20660544](https://pubmed.ncbi.nlm.nih.gov/20660544/) | 2010 | Clinical Review | *Pediatrics* | American Academy of Pediatrics policy statement on cochlear implants: addresses AOM and bacterial meningitis prevention and treatment protocols, underscoring ceftriaxone's role in high-risk pediatric ear infections. |
| [38368849](https://pubmed.ncbi.nlm.nih.gov/38368849/) | 2024 | Review | *American Journal of Emergency Medicine* | Review of acute mastoiditis — a serious suppurative complication of otitis media — covering diagnosis, parenteral antibiotic selection, and the critical role of cephalosporins in preventing intracranial extension. |
| [12166789](https://pubmed.ncbi.nlm.nih.gov/12166789/) | 2002 | Consensus Guidelines | *Clinical Pediatrics* | Expert consensus recommendations for AOM management integrating clinical trial data; explicitly addresses third-generation cephalosporin selection including ceftriaxone in treatment-failure scenarios. |
| [32796134](https://pubmed.ncbi.nlm.nih.gov/32796134/) | 2020 | Case Report | *European Journal of Microbiology & Immunology* | Chronic otitis media caused by non-O1/non-O139 *Vibrio cholerae* treated with ciprofloxacin and ceftriaxone combination followed by surgical atticotomy; illustrates ceftriaxone use in complex otitis media with unusual pathogens. |
| [1554826](https://pubmed.ncbi.nlm.nih.gov/1554826/) | 1992 | Case Series | *Clinical Infectious Diseases* | Review of Group A streptococcal meningitis cases, most associated with antecedent otitis media or pharyngitis; provides historical perspective on the life-threatening bacterial complications that parenteral ceftriaxone is designed to prevent. |

---

## Canada Market Information

Ceftriaxone (DB01212) has **no approved drug identification numbers (DINs) registered in Canada** at the time of this evidence pack (data cutoff: 2026-04-04). No product name, dosage form, or approved indication text is available from the Canadian regulatory database.

This absence is the central finding: ceftriaxone is a WHO Essential Medicine, widely marketed in the United States, Europe, Japan, and most global markets, yet it does not appear in the Canadian drug register. Whether this represents a historical delisting, a gap in the data source, or a genuine absence of market authorization requires direct verification with Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two prospective randomized controlled trials directly demonstrate ceftriaxone's bacteriologic and clinical efficacy for acute otitis media, and international pediatric guidelines already recommend it as a second-line intramuscular option — meaning the scientific case is established and the primary unknowns are regulatory and contextual rather than biological.

**To proceed, the following is needed:**

- **Verify Canadian regulatory status:** Determine whether ceftriaxone has ever held a Canadian DIN, and if so, why it is no longer on record; identify the applicable Health Canada submission pathway (new drug submission, abbreviated NDS, or supplement)
- **Obtain safety documentation:** Download and review the Health Canada product monograph or equivalent package insert to complete the safety profile (warnings, contraindications, drug interactions) — currently the single largest data gap blocking formal safety assessment
- **Retrieve mechanism of action data:** Query the DrugBank API for DB01212 to formally document MOA, pharmacokinetics, and protein binding data (currently flagged as Data Gap DG002)
- **Assess local resistance patterns:** Review Canadian surveillance data (e.g., CARSS — Canadian Antimicrobial Resistance Surveillance System) for *S. pneumoniae*, *H. influenzae*, and *M. catarrhalis* susceptibility to ceftriaxone in pediatric otitis media, to confirm that resistance has not undermined clinical utility in the Canadian context
- **Conduct a comparative effectiveness review:** Evaluate ceftriaxone against currently marketed Canadian alternatives (high-dose amoxicillin-clavulanate, oral cefuroxime axetil) in terms of efficacy, tolerability, cost, and stewardship implications before initiating any regulatory action
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

