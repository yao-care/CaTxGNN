---
layout: default
title: Cilastatin
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
---

# Cilastatin
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

# Cilastatin: From Imipenem Renal Adjunct to Staphylococcus Aureus Infection

## One-Sentence Summary

Cilastatin is a renal dehydropeptidase-I (DHP-I) inhibitor co-formulated with imipenem in the widely used combination antibiotic imipenem/cilastatin, where its established role is to prevent enzymatic degradation of imipenem in the renal tubules — not to exert direct antibacterial activity.
The TxGNN model predicts it may be effective for **Staphylococcus Aureus Infection**, with **3 clinical trials** and **20 publications** currently supporting this direction — although virtually all available evidence pertains to the imipenem/cilastatin combination rather than cilastatin as a standalone agent.
A central unresolved question drives this entire evaluation: does cilastatin possess independent antimicrobial or immunomodulatory activity beyond its pharmacokinetic support role for imipenem?

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal DHP-I inhibitor; co-administered with imipenem to prevent its degradation by renal tubular dehydropeptidase-I |
| Predicted New Indication | Staphylococcus Aureus Infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not retrieved during this evaluation. Based on well-established pharmacology, cilastatin is a specific, competitive inhibitor of renal dehydropeptidase-I (DHP-I) — a brush-border enzyme located on the luminal surface of proximal renal tubular cells. When imipenem is administered alone, DHP-I hydrolyses it rapidly in the kidney, reducing urinary drug concentrations and generating nephrotoxic metabolites. Cilastatin blocks this process, preserving imipenem bioavailability and preventing renal toxicity. Critically, cilastatin carries **no intrinsic antibacterial activity** against *Staphylococcus aureus* or any other pathogen.

The TxGNN prediction most likely arises from knowledge graph topology rather than direct biology. Imipenem/cilastatin is a well-documented broad-spectrum antibiotic combination used for severe bacterial infections, including those caused by *S. aureus* — particularly methicillin-susceptible strains (MSSA), where imipenem achieves low MICs (MIC₉₀ ≤ 0.5 mg/L). Against methicillin-resistant *S. aureus* (MRSA), however, imipenem/cilastatin shows limited effectiveness (MIC₉₀ 6.25–8 mg/L), and clinical data confirm inferior outcomes compared to vancomycin. Because cilastatin is inseparably documented alongside imipenem in the literature, the model likely attributed the combination's antimicrobial signal to cilastatin as an independent node.

An emerging — but entirely unvalidated — hypothesis proposes that cilastatin may modulate host immune responses independently of imipenem, through inhibition of megalin (LRP2)-mediated renal tubular uptake and potential secondary effects on neutrophil function and biofilm disruption. This is a speculative mechanistic hypothesis with no clinical trial data to date. The core repurposing question is therefore: **can cilastatin contribute independently to treatment outcomes in *S. aureus* infections, beyond its established pharmacokinetic support role for imipenem?** Current evidence cannot answer this question.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | Completed | 274 | Multinational, double-blind RCT comparing imipenem/cilastatin/relebactam (MK-7655A) vs. piperacillin/tazobactam in adults with hospital-acquired or ventilator-associated bacterial pneumonia (HABP/VABP); primary endpoint: 28-day all-cause mortality non-inferiority. Highest-quality indirect evidence; cilastatin is a combination component and its independent contribution cannot be isolated. |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Unknown | 60 | Investigates linezolid alone vs. combined with carbapenem (which includes cilastatin) against MRSA in ventilator-associated pneumonia patients, based on prior synergy data from in vitro and animal studies. Trial status unknown; data reliability uncertain. Cilastatin's role is indirect. |
| [NCT00707239](https://clinicaltrials.gov/study/NCT00707239) | Phase 2 | Terminated | 108 | Multicenter, double-blind RCT comparing two dose levels of tigecycline vs. imipenem/cilastatin for hospital-acquired pneumonia (≥70% VAP). Trial terminated prematurely; data are incomplete and statistical power insufficient for conclusions. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Clinical Case Series | Antimicrob Agents Chemother | Imipenem-cilastatin evaluated in 23 patients with MSSA (n=12) and MRSA (n=11) infections including soft tissue, endovascular, and skeletal sites; MIC₉₀ for MRSA was 6.25 mg/L (bacteriostatic), confirming the combination has limited anti-MRSA potency. |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Case Commentary | Antimicrob Agents Chemother | Commentary on a case of refractory MRSA bacteraemic osteomyelitis treated with imipenem/cilastatin + fosfomycin as a novel combination; highlights the need for individualized regimens when vancomycin/daptomycin fail, and advocates for collaborative clinician-microbiologist decision-making. |
| [8072190](https://pubmed.ncbi.nlm.nih.gov/8072190/) | 1994 | Clinical Case Series | Jpn J Antibiotics | Arbekacin (ABK) combined with imipenem/cilastatin showed synergistic in vitro activity against MRSA, with the combination achieving lower MICs than either drug alone; supports imipenem/cilastatin as a synergy partner rather than a primary anti-MRSA agent. |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In vitro / In vivo Study | J Antimicrob Chemother | Vancomycin + imipenem demonstrated synergistic or additive effects against 36 MRSA clinical isolates in vitro and confirmed efficacy in a neutropenic mouse thigh model; supports combination strategies for immunocompromised MRSA patients. |
| [8514648](https://pubmed.ncbi.nlm.nih.gov/8514648/) | 1993 | Animal Model | J Antimicrob Chemother | Imipenem/cilastatin + cefotiam showed synergistic bactericidal activity in a mouse bacteraemia model against both β-lactamase-producing and non-producing MRSA strains; staggered administration timing further enhanced in vitro pharmacokinetic synergy. |
| [3378959](https://pubmed.ncbi.nlm.nih.gov/3378959/) | 1988 | Animal Model | J Antimicrob Chemother | Compared imipenem-cilastatin vs. vancomycin in a rabbit model of MRSA aortic valve endocarditis; vancomycin was bactericidal in vitro (MIC₉₀ 2 mg/L), whereas imipenem was bacteriostatic (MIC₉₀ 8 mg/L); imipenem/cilastatin showed comparably favourable in vivo outcomes in this model. |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Review | Int J Antimicrob Agents | Comprehensive narrative review of MRSA virulence mechanisms, key clinical trials, and resistance implications; highlights carbapenems' limited role in MRSA management and summarises evidence for agents such as daptomycin, linezolid, and ceftaroline. |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Reviews off-label antibiotic use vs. formal guideline recommendations for MDR bacteria including MRSA; imipenem/cilastatin discussed as a component in combination regimens for XDR Gram-positive pathogens. |
| [12878512](https://pubmed.ncbi.nlm.nih.gov/12878512/) | 2003 | In vivo Animal Study | Antimicrob Agents Chemother | Evaluated novel cephalosporin S-3578 vs. imipenem-cilastatin and vancomycin in murine systemic MRSA infection; imipenem-cilastatin showed very limited anti-MRSA activity in vivo (ED₅₀ >100 mg/kg vs. vancomycin's effective dose), reinforcing that imipenem/cilastatin is not a reliable MRSA monotherapy. |
| [18649613](https://pubmed.ncbi.nlm.nih.gov/18649613/) | 2008 | Review / Clinical Guideline | Am Fam Physician | Clinical practice guideline for diabetic foot infections, in which *S. aureus* and β-haemolytic streptococci are cited as predominant pathogens; broad-spectrum agents including imipenem/cilastatin are recommended for severe or previously treated polymicrobial presentations. |

---

## Safety Considerations

Please refer to the package insert for safety information. Formal safety data — including key warnings, contraindications, and drug-drug interactions — were not retrieved during this evaluation cycle.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Cilastatin has no established independent antibacterial or immunomodulatory activity against *Staphylococcus aureus*; every piece of clinical evidence retrieved relates to the imipenem/cilastatin combination, in which cilastatin functions purely as a pharmacokinetic adjunct. The TxGNN high score (99.94%) most likely reflects knowledge graph proximity between cilastatin and broad-spectrum antibiotic indications rather than a direct biological signal. With the drug not marketed in Canada, no safety data on file, and no preclinical data demonstrating standalone anti-infective activity, the evidence base does not yet support moving to a formal repurposing pathway.

**To proceed, the following is needed:**

- **Preclinical mechanistic studies**: MIC assays, time-kill kinetics, and biofilm inhibition assays evaluating cilastatin as a standalone agent against *S. aureus* (MSSA and MRSA), independent of imipenem
- **Immunomodulatory hypothesis validation**: Controlled in vitro and animal studies examining cilastatin's hypothesised effects on neutrophil function, megalin-receptor-mediated mechanisms, and anti-biofilm potential in infection models
- **MOA documentation**: Formal retrieval of cilastatin's mechanism of action from DrugBank API and primary pharmacological literature
- **Safety data collection**: Retrieval and parsing of Health Canada or TFDA product monographs to document warnings, contraindications, and clinically significant drug interactions
- **Evidence gap resolution**: If preclinical data demonstrate a plausible independent mechanism, a hypothesis-generating pilot clinical study (e.g., cilastatin as adjunctive therapy in refractory MRSA bacteraemia) could be designed as the next translational step

> **Research disclaimer**: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

