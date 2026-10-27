---
layout: default
title: Cefuroxime
parent: Model Prediction Only (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Cefuroxime: predicted new indication Hyperamylasemia . The best-supported candidate is urinary tract infec… (evidence level L5). Approved use: Bacterial infections (otitis media…"
monitor_inn: "CEFUROXIME"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Peptostreptococcus infectious disease", "blood group incompatibility", "urinary tract infection (disease)", "premalignant hematological system disease", "monoclonal gammopathy", "suppurative otitis media", "hematological disease associated with an acquired peripheral neuropathy"]
---

# Cefuroxime
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Cefuroxime: From Bacterial Infections to Urinary Tract Infection
{: .text-alpha }

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic, originally used for infections such as otitis media, pneumonia, meningitis, gonorrhea and Lyme disease.
The TxGNN model's top-ranked predictions were mostly implausible, and the best-supported candidate is **urinary tract infection (UTI)**, with **5 registered clinical trials** and **20 publications**.
That candidate largely extends cefuroxime's existing anti-infective use rather than representing a novel repurposing target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (otitis media, streptococcal and staphylococcal infections, pneumonia, meningitis, gonorrhea, Lyme disease, among others) |
| Predicted New Indication | Hyperamylasemia (rank 1 by score; no supporting evidence). The best-supported candidate is urinary tract infection (rank 6). |
| TxGNN Prediction Score | 99.76% (hyperamylasemia); 99.62% (urinary tract infection) |
| Evidence Level | L5 (hyperamylasemia); L3 (urinary tract infection) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold (hyperamylasemia); Proceed with Guardrails for urinary tract infection as a research question only |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cefuroxime is a beta-lactam cephalosporin that inhibits bacterial cell-wall synthesis. Its efficacy in respiratory, ear and other bacterial infections is established.

**The top-scoring predictions lack a plausible mechanism.** Hyperamylasemia, polyclonal hyperviscosity syndrome, congenital analbuminemia, premalignant hematological disease, and hematological disease with peripheral neuropathy have no connection to cell-wall inhibition. Their high scores (99.5% to 99.8%) most likely reflect knowledge-graph topology rather than biology. None has any trial or literature support.

**Infection-type predictions are mechanistically sound but not novel.** Cefuroxime is active against common uropathogens (E. coli, Klebsiella, Proteus), so UTI is a reasonable extension. Suppurative otitis media and Peptostreptococcus infection likewise fall within existing anti-infective use. Otitis media is already a listed original indication.

**Some matches are spurious.** The only paper linked to blood group incompatibility concerns multidrug-resistant Salmonella in Kenya. The monoclonal gammopathy papers concern infections in neutropenic cancer patients, not the gammopathy itself.

---

## Clinical Trial Evidence

The only prediction with registered trials is urinary tract infection (rank 6).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | Completed | 973 | Outcomes of inappropriate cefuroxime therapy in hospitalized adults with pyelonephritis. Directly relevant, but observational in design. |
| [NCT02789579](https://clinicaltrials.gov/study/NCT02789579) | Early Phase 1 | Unknown | 150 | One-week antimicrobial prophylaxis before minimally invasive upper tract lithotomy. Cefuroxime's role is unclear. |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1000 | Antibiotic prophylaxis at urinary catheter removal. The antibiotic is not confirmed to be cefuroxime. |
| [NCT02009098](https://clinicaltrials.gov/study/NCT02009098) | Phase 4 | Withdrawn | 0 | Postpartum infection prophylaxis after cesarean section. Withdrawn with no enrollment. |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | Preventive antibiotics in puerperal women with recurrent UTI. Only partially relevant. |

No clinical trials are registered for the other nine predicted indications.

---

## Literature Evidence

Selected publications for the UTI prediction (rank 6):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2689345](https://pubmed.ncbi.nlm.nih.gov/2689345/) | 1989 | Randomized comparison | Infection | Aztreonam vs cefuroxime in gram-negative upper UTI; the only direct cefuroxime comparison |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | Randomized trial | Lancet Infect Dis | SIMPLIFY: de-escalation from antipseudomonal β-lactams in Enterobacterales bloodstream infection; indirect relevance |
| [41693075](https://pubmed.ncbi.nlm.nih.gov/41693075/) | 2026 | Systematic review | Pharmacotherapy | Oral β-lactams vs TMP/SMX and fluoroquinolones in complicated UTI |
| [8799689](https://pubmed.ncbi.nlm.nih.gov/8799689/) | 1996 | Review | Drugs | Cefuroxime axetil: antibacterial activity, pharmacokinetics and therapeutic efficacy |
| [6349019](https://pubmed.ncbi.nlm.nih.gov/6349019/) | 1983 | Review | Ther Drug Monit | Cefuroxime antimicrobial activity, pharmacology and clinical efficacy |
| [6344037](https://pubmed.ncbi.nlm.nih.gov/6344037/) | 1983 | Review | Pharmacotherapy | Cefuroxime mechanisms, spectrum, pharmacokinetics and adverse reactions |
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Review | Int J Antimicrob Agents | Cefuroxime axetil overview |
| [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/) | 2024 | Cohort | Infect Dis Clin Microbiol | Causative organisms and ESBL risk factors in community-acquired UTI |

Other predictions with literature:
- **Suppurative otitis media (rank 9):** Mostly reviews and susceptibility surveys, including [7142073](https://pubmed.ncbi.nlm.nih.gov/7142073/) (1982), which studied cefuroxime diffusion into middle ear effusions. No trials.
- **Peptostreptococcus infection (rank 4):** [19802974](https://pubmed.ncbi.nlm.nih.gov/19802974/) (1981), an in-vitro study in which cefuroxime inhibited 79% of anaerobic isolates at 16 mg/l. It focused on ceftazidime, so it is indirect evidence.
- **Blood group incompatibility (rank 5) and monoclonal gammopathy (rank 8):** The retrieved papers are irrelevant or only indirectly related, as described above.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02344831 | AURO-CEFUROXIME | Not specified | Not specified |
| 02241638 | CEFUROXIME FOR INJECTION, USP | Not specified | Not specified |
| 02244394 | APO-CEFUROXIME | Not specified | Not specified |
| 02344823 | AURO-CEFUROXIME | Not specified | Not specified |
| 02212307 | CEFTIN | Not specified | Not specified |

Nine DINs are valid, all single-ingredient products. The four others are 02547198 and 02547201 (JAMP CEFUROXIME), 02241639 (CEFUROXIME FOR INJECTION, USP) and 02244393 (APO-CEFUROXIME).

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, blood coagulation disease, Clostridium difficile colitis, perinatal necrotizing enterocolitis, and congenital prothrombin deficiency.
- **Drug Interactions:** 100 interactions were identified, and all those listed are Moderate severity. Main groups:
  - Acid-suppressing agents: famotidine, ranitidine, cimetidine, nizatidine, and the proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, rabeprazole, pantoprazole)
  - Antacids: aluminum hydroxide, calcium carbonate, magaldrate, and magnesium carbonate, hydroxide and oxide
  - Aminoglycosides: kanamycin, neomycin
  - Balsalazide

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the Health Canada package insert for them.

---

## Conclusion and Next Steps

**Decision: Hold** for the highest-scoring prediction (hyperamylasemia) and for the other predictions without evidence. **Proceed with Guardrails** applies only to UTI, and only as a research question.

**Rationale:**
- The highest-scoring predictions are computational artifacts with no mechanism, trials or literature (Evidence Level L5).
- UTI (L3) has the strongest support, but it comes from one observational study, prophylaxis trials in which cefuroxime is not clearly the tested agent, and reviews. No Phase 3 RCT is available.
- UTI, otitis media and Peptostreptococcus infection fall within the existing anti-infective profile, so none is a true repurposing opportunity.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved-indication text and dosage forms for the Canadian licenses
- For UTI, a review of current Canadian labeling to see whether it is already covered, and head-to-head comparative trial data against current standard therapy
- A safety plan covering renal and hepatic impairment, coagulation disorders and C. difficile risk, and the interaction groups above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

