---
layout: default
title: Cilastatin
parent: Moderate Evidence (L3-L4)
nav_order: 193
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-13
description: "Cilastatin: predicted new indication Staphylococcus aureus infection (evidence level L3). Approved use: Bacterial pneumonia (also peritonitis, streptococcal pneumonia…"
monitor_inn: "CILASTATIN"
predicted_indications: ["staphylococcus aureus infection", "chronic rhinosinusitis", "chronic ethmoidal sinusitis", "sinusitis", "paranasal sinus neoplasm (disease)", "paratyphoid fever", "bronchitis", "diffuse scleroderma", "salmonellosis"]
---

# Cilastatin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

## Cilastatin: From Bacterial Pneumonia to Staphylococcus aureus Infection
{: .text-alpha }

## One-Sentence Summary

Cilastatin is a dehydropeptidase-1 inhibitor co-formulated with the carbapenem antibiotic imipenem. It is used in bacterial and streptococcal pneumonia, endocarditis, peritonitis and related infections.
The TxGNN model predicts it may be effective for ***Staphylococcus aureus* infection**, with **1 clinical trial** and **20 publications** currently on record. The evidence is indirect, because any antibacterial effect comes from imipenem rather than cilastatin itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia (also peritonitis, streptococcal pneumonia, endocarditis, bacterial arthritis, endometritis) |
| Predicted New Indication | Staphylococcus aureus infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cilastatin inhibits dehydropeptidase-1 (DHP-1), a kidney enzyme that breaks down imipenem. It has no antibacterial activity of its own. By blocking DHP-1, it keeps imipenem active and raises the drug's exposure in the body. It is sold only in fixed-dose combination with imipenem.

*S. aureus* is a common cause of pneumonia, endocarditis, and skin, soft-tissue and bone infections. These are the same infection types already covered by the imipenem/cilastatin indications. That overlap likely explains the high model score. Older clinical reports describe imipenem/cilastatin in infections caused by methicillin-sensitive and methicillin-resistant *S. aureus* (MSSA and MRSA). They include combinations with fosfomycin, arbekacin or vancomycin.

The prediction therefore reflects the established imipenem/cilastatin combination, not an independent effect of cilastatin. Imipenem is also only bacteriostatic against many MRSA isolates in vitro, and one animal study found it less active than newer agents against MRSA.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Unknown | 60 | Linezolid alone or combined with a carbapenem against MRSA in ventilator-associated pneumonia. The carbapenem is not confirmed to be imipenem/cilastatin, so the evidence is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Clinical study | Antimicrob Agents Chemother | Imipenem-cilastatin evaluated in 23 patients with MSSA (12) or MRSA (11) infections, mainly soft tissue, endovascular and skeletal. |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Case commentary | Antimicrob Agents Chemother | Imipenem/cilastatin plus fosfomycin as a novel combination for refractory MRSA infection. |
| [3859210](https://pubmed.ncbi.nlm.nih.gov/3859210/) | 1985 | Clinical study | Am J Med | 17 patients with bacterial endocarditis (14 intravenous drug users) treated with imipenem/cilastatin 500 mg every 6 hours. |
| [3378959](https://pubmed.ncbi.nlm.nih.gov/3378959/) | 1988 | Animal study | J Antimicrob Chemother | In a rabbit model of MRSA aortic valve endocarditis, imipenem-cilastatin showed better efficacy than vancomycin on the study's criteria. |
| [8072190](https://pubmed.ncbi.nlm.nih.gov/8072190/) | 1994 | Clinical/in vitro study | Jpn J Antibiot | Arbekacin plus imipenem/cilastatin gave lower MICs against MRSA than the individual agents. |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In vitro / animal study | J Antimicrob Chemother | Vancomycin plus imipenem was synergistic or additive against all 36 MRSA isolates and was also tested in a neutropenic mouse model. |
| [22196394](https://pubmed.ncbi.nlm.nih.gov/22196394/) | 2012 | Review | Int J Antimicrob Agents | Review of MRSA pathogenesis, treatment trials and resistance. |
| [36804370](https://pubmed.ncbi.nlm.nih.gov/36804370/) | 2023 | Review | Int J Antimicrob Agents | Off-label versus recommended antibiotic use in multidrug-resistant infections, including MRSA. |
| [3890533](https://pubmed.ncbi.nlm.nih.gov/3890533/) | 1985 | Review | Am J Med | Pathogenesis and treatment of endocarditis, including the rabbit model and imipenem's broad spectrum. |
| [18649613](https://pubmed.ncbi.nlm.nih.gov/18649613/) | 2008 | Review | Am Fam Physician | Diabetic foot infection, in which *S. aureus* is a leading pathogen. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02351706 | TARO-IMIPENEM-CILASTATIN |
| 02358344 | IMIPENEM AND CILASTATIN FOR INJECTION USP |

Both are single-ingredient products with valid status.

---

## Safety Considerations

- **Disease-level contraindication signals:** The data compiled for this report flag epilepsy, kidney disease, pyoureter, *Clostridium difficile* colitis and perinatal necrotizing enterocolitis. These come from knowledge-graph associations rather than label text, so they need confirmation against the product monograph.
- **Reported adverse reaction:** One case report (PMID 9158321) describes imipenem-cilastatin-induced leukocytoclastic vasculitis with a maculopapular rash.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The *S. aureus* prediction rests on indirect evidence. The single trial does not isolate imipenem/cilastatin, and the supporting literature is mostly old small clinical series, case reports, animal work and reviews. Cilastatin has no antibacterial activity of its own, so this is not a true repurposing signal for cilastatin. The data compiled for this report show the stronger evidence is for pneumonia, which is already a labeled use. That evidence includes several completed Phase 3 trials of imipenem/cilastatin/relebactam in hospital-acquired and ventilator-associated pneumonia. Those results support the established combination, not a new indication for cilastatin.

**To proceed, the following is needed:**
- Product monograph warnings and contraindications for the Canadian products, which are currently missing
- Controlled clinical data on imipenem/cilastatin specifically in *S. aureus* (especially MRSA) infection
- Comparison with current standard anti-staphylococcal therapy, since imipenem is not a first-line anti-MRSA agent
- Clarification of whether the question concerns the imipenem/cilastatin combination or cilastatin alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

