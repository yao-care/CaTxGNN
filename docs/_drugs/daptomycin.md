---
layout: default
title: Daptomycin
parent: Model Prediction Only (L5)
nav_order: 247
evidence_level: L5
indication_count: 10
---

# Daptomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis

## One-Sentence Summary

Daptomycin is an intravenous cyclic lipopeptide antibiotic, approved for Gram-positive infections such as skin infections, bacteremia and right-sided endocarditis.
The TxGNN model predicts it may be useful for **osteoarthritis**, but there are **0 clinical trials** and **10 publications**, none of which tests daptomycin as a treatment for osteoarthritis. The papers concern joint *infections* and appear to match on keywords only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (skin infections, bacteremia, right-sided endocarditis). The Canadian licence records provided contain no indication text. |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack. Daptomycin is known as a cyclic lipopeptide that disrupts Gram-positive bacterial membranes.

Osteoarthritis is a non-infectious, degenerative joint disease, so this antibacterial mechanism gives **no credible link** to it. All 10 retrieved papers concern osteoarticular or prosthetic joint infections. They match the word "osteoarticular" and do not test daptomycin in osteoarthritis. The high TxGNN score is therefore an unsupported prediction.

A more plausible signal appears for the second-ranked prediction, **rheumatoid arthritis** (score 99.84%, evidence level L4). Two 2025 preclinical papers report that daptomycin and related cyclic lipopeptides reduce inflammatory cytokines and NF-κB signalling and ease collagen-induced arthritis in mice. There is still no human efficacy data or registered trial. Practical barriers include IV-only administration, CK elevation and myopathy risk with prolonged dosing, and the cost of long-term use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the papers is an RCT or a review, and none tests daptomycin for osteoarthritis. Cohort studies are listed first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | Int Orthop | Safety and efficacy of high-dose daptomycin plus rifampicin in Gram-positive bone and joint *infections* |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Clinical experience with daptomycin in knee and hip periprosthetic joint *infections* |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) in complicated bone, joint and implant-associated *infections* |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin vs standard therapy for osteoarticular infections with *S. aureus* bacteraemia |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Cohort | Med Clin (Barc) | EU-CORE registry: routine daptomycin use in Spanish hospitals for Gram-positive infections |
| [25650692](https://pubmed.ncbi.nlm.nih.gov/25650692/) | 2015 | Observational | Surg Infect | Ten-year change in staphylococcal profile in osteoarticular infections |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | Antibiotic susceptibility of *S. aureus* and *S. epidermidis* from prosthetic joint infections |
| [23312602](https://pubmed.ncbi.nlm.nih.gov/23312602/) | 2013 | Survey | Int J Antimicrob Agents | Survey of current prosthetic joint infection management practices |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Rep Orthop | Chronic *Corynebacterium striatum* septic arthritis in a patient with known osteoarthritis |
| [41853106](https://pubmed.ncbi.nlm.nih.gov/41853106/) | 2026 | Case report | ASM Case Rep | *Corynebacterium propinquum* septic arthritis in a native joint |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2490463 | DAPTOMYCIN FOR INJECTION |
| 2490838 | DAPTOMYCIN FOR INJECTION |
| 2465493 | CUBICIN RF |

---

## Safety Considerations

Package insert warnings, contraindications and drug interaction data were not retrieved. Please refer to the package insert for safety information.

The literature does point to muscle-related risk. Daptomycin-induced rhabdomyolysis is well documented, and one case report described it triggering acute gouty arthritis ([PMID 36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/)). CK elevation and myopathy with prolonged dosing are also noted, which matters for any chronic-use scenario such as osteoarthritis.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction rests on the model score alone. Daptomycin's antibacterial mechanism has no link to degenerative joint disease, and the supporting papers are infection studies matched by keyword. Chronic use would also carry muscle toxicity risk with IV-only dosing.

**To proceed, the following is needed:**
- Any evidence that daptomycin has an anti-inflammatory or chondroprotective effect in osteoarthritis models. None exists in the current pack.
- Health Canada package insert warnings and contraindications (blocking gap).
- Mechanism of action data from DrugBank.
- Consideration of **rheumatoid arthritis** as the more promising research question. It needs replication of the 2025 mouse data and a safety assessment for long-term dosing before any human study.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

