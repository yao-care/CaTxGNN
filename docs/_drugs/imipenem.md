---
layout: default
title: Imipenem
parent: Model Prediction Only (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Imipenem: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Bacterial pneumonia, peritonitis, endocarditis, bacterial arthritis…"
monitor_inn: "IMIPENEM"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "staphylococcus aureus infection", "eosinophilia-myalgia syndrome"]
---

# Imipenem
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

## Imipenem: From Bacterial Pneumonia to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Imipenem is a carbapenem antibiotic, originally used for serious bacterial infections such as bacterial pneumonia, peritonitis and endocarditis.
The TxGNN model's top-ranked prediction is **diffuse scleroderma**, but this has **no clinical trials and no publications** behind it. The best-supported candidate in the data compiled for this report is instead **Staphylococcus aureus infection**, with **2 clinical trials** and **19 publications**. The remaining predictions are mostly extensions of imipenem's antibacterial use, supported by susceptibility and surveillance studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, peritonitis, endocarditis, bacterial arthritis, endometritis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Diffuse scleroderma (rank 1); Staphylococcus aureus infection is the best-supported candidate (rank 9) |
| TxGNN Prediction Score | 0.9999 (diffuse scleroderma) |
| Evidence Level | L5 for diffuse scleroderma (model prediction only); L2 for Staphylococcus aureus infection |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold (diffuse scleroderma); Staphylococcus aureus infection is flagged as a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, imipenem is a carbapenem antibacterial that inhibits bacterial cell wall synthesis and has broad activity against Gram-positive, Gram-negative and anaerobic bacteria.

**Diffuse scleroderma (top-ranked prediction):** No mechanistic link is supported. Diffuse scleroderma is an autoimmune fibrotic disease, and an antibacterial has no established action on it. The very high score is a computational prediction only, with no trials or literature behind it.

**Infectious predictions (paratyphoid fever, salmonellosis, typhoid fever, sinusitis, chronic rhinosinusitis, chronic ethmoidal sinusitis):** These are biologically plausible, because imipenem covers Enterobacterales such as Salmonella and many pathogens found in sinus infections. The supporting literature is largely resistance surveillance and susceptibility studies, which is indirect evidence. Carbapenem use for routine sinusitis would also conflict with antimicrobial stewardship, and chronic rhinosinusitis is often inflammatory rather than primarily infectious.

**Staphylococcus aureus infection:** Imipenem inhibits penicillin-binding proteins and is active against methicillin-susceptible *S. aureus*. MRSA is intrinsically resistant, but combinations such as fosfomycin plus imipenem, or a carbapenem plus linezolid, may act synergistically. This is the only prediction with registered clinical trials.

**Paranasal sinus neoplasm and eosinophilia-myalgia syndrome:** No mechanistic link is supported, and there are no trials or literature. The scores are computational predictions only.

---

## Clinical Trial Evidence

Only Staphylococcus aureus infection has registered trials. The other nine predicted indications have none.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Phase 4 | Completed | 50 | Fosfomycin plus imipenem versus vancomycin (standard therapy) for MRSA infective endocarditis. Results are not available. |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Unknown | 60 | Linezolid alone or combined with a carbapenem against MRSA in ventilator-associated pneumonia. The carbapenem may not be imipenem, and no results are available. |

---

## Literature Evidence

Evidence for Staphylococcus aureus infection (the best-supported candidate):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Cohort | Antimicrob Agents Chemother | Imipenem-cilastatin evaluated in 23 patients with MSSA and MRSA infections (soft tissue, endovascular, skeletal). |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Case report | Antimicrob Agents Chemother | Commentary on imipenem/cilastatin plus fosfomycin as a combination for refractory MRSA infection. |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | Animal study | J Antimicrob Chemother | Imipenem was highly active in vitro against *S. aureus* endocarditis isolates and was tested in a rabbit endocarditis model. |
| [7928812](https://pubmed.ncbi.nlm.nih.gov/7928812/) | 1994 | Animal study | J Antimicrob Chemother | Imipenem compared with oxacillin and vancomycin in a rat chronic foreign-body infection model. |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | Not classified | J Antimicrob Chemother | Vancomycin plus imipenem was synergistic against 34 of 36 MRSA isolates, with in vivo mouse thigh model data. |

Evidence for infectious predictions (selected):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) | 2025 | Not classified | Cureus | Carbapenems as the final line of defence in MDR/XDR typhoid fever (Peshawar). |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | Case report | J Med Liban | Typhoid-associated rhabdomyolysis and renal failure successfully treated with imipenem/cilastatin and haemodialysis. |
| [19208884](https://pubmed.ncbi.nlm.nih.gov/19208884/) | 2009 | Not classified | J Med Microbiol | MIC of carbapenems and tigecycline against 210 Salmonella isolates. |
| [22204180](https://pubmed.ncbi.nlm.nih.gov/22204180/) | 2011 | In vitro | J Pak Med Assoc | In vitro MICs, including imipenem, against typhoidal Salmonellae. |
| [16918048](https://pubmed.ncbi.nlm.nih.gov/16918048/) | 2006 | Review | Folia Med | Review of antimicrobial therapy of salmonelloses. |
| [16200963](https://pubmed.ncbi.nlm.nih.gov/16200963/) | 2005 | Cohort | Zhonghua Er Bi Yan Hou Tou Jing Wai Ke Za Zhi | Bacteriology and antibiotic resistance in chronic sinusitis. |
| [9044641](https://pubmed.ncbi.nlm.nih.gov/9044641/) | 1996 | Not classified | Enferm Infecc Microbiol Clin | Severe orbital cellulitis in 9 patients, with imipenem noted as a valid therapeutic choice. |

No publications were found for diffuse scleroderma, paranasal sinus neoplasm or eosinophilia-myalgia syndrome.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02351706 | TARO-IMIPENEM-CILASTATIN | Not recorded | Not recorded |
| 02358344 | IMIPENEM AND CILASTATIN FOR INJECTION USP | Not recorded | Not recorded |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** epilepsy, kidney disease, pyoureter, *Clostridium difficile* colitis, and perinatal necrotizing enterocolitis.
- **Drug Interactions:** 15 interactions were identified.
  - **Major:** bupropion, iohexol, iopamidol.
  - **Moderate:** polyethylene glycol (3350 with electrolytes), dicoumarol, warfarin, lindane, aminophylline, dyphylline, oxtriphylline, theophylline, cyclosporine, ethinylestradiol, mycophenolic acid, pemetrexed.

Please refer to the package insert for warnings and contraindications from the approved labelling.

---

## Conclusion and Next Steps

**Decision: Hold** (for all predictions except Staphylococcus aureus infection, which is flagged as a research question)

**Rationale:**
- The top-ranked prediction, diffuse scleroderma, has no trials, no literature and no plausible mechanism, so the high score alone does not justify progression.
- Most infectious predictions rest on susceptibility and surveillance data, which do not show clinical outcomes.
- Staphylococcus aureus infection has two small Phase 4 trials (n=50 and n=60) and older clinical and animal studies. This supports further investigation, but not approval-level conclusions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening).
- Mechanism of action data from DrugBank.
- Results and design details (including randomization) for NCT00871104 and NCT01356472.
- Clinical outcome data for imipenem in typhoid and paratyphoid fever, ideally from controlled studies.
- A review of stewardship considerations, since carbapenem use in sinusitis and rhinosinusitis conflicts with antimicrobial stewardship.
- A safety plan covering seizure risk and renal impairment, and the interactions listed above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

