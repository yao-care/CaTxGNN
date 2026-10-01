---
layout: default
title: Cefprozil
parent: Model Prediction Only (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Cefprozil
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

# Cefprozil: From Bacterial Infections to Urinary Tract Infection

## One-Sentence Summary

Cefprozil is an oral second-generation cephalosporin antibiotic, used mainly for respiratory tract, skin and soft tissue infections.
The TxGNN model predicts it may be effective for **urinary tract infection (UTI)**.
Currently **3 randomized trials** and **6 other publications** support this direction, and no clinical trials are registered.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence records. The literature describes use in respiratory tract, skin and soft tissue infections |
| Predicted New Indication | Urinary tract infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (3 published randomized comparative trials, all from 1991-1992; no registered Phase 3 trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on known pharmacology, cefprozil is a second-generation oral cephalosporin. It inhibits bacterial cell wall synthesis by binding penicillin-binding proteins (PBPs). It is active against common urinary pathogens such as *Escherichia coli*, *Klebsiella pneumoniae* and *Proteus mirabilis*.

Respiratory infections and UTIs are both bacterial infections that can be treated by the same mechanism. Once-daily 500 mg cefprozil gave clinical and bacterial cure rates of 94% and 93% in women with acute UTI, similar to cefaclor. A 2015 in vitro study also found activity against ciprofloxacin-resistant Enterobacteriaceae from community-acquired UTIs.

Two caveats apply:
- The original indication list is missing, and uncomplicated UTI is a labelled use in some jurisdictions. This may therefore not be true repurposing, so confirm the Canadian label status first.
- The clinical evidence covers only acute uncomplicated UTI, mostly in women, and dates from the early 1990s. Resistance patterns have shifted since then.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1952874](https://pubmed.ncbi.nlm.nih.gov/1952874/) | 1991 | RCT | Antimicrob Agents Chemother | 108 college women with acute UTI. Cefprozil 500 mg once daily vs cefaclor 250 mg three times daily for 10 days. Clinical cure 94% vs 94%, bacterial cure 93% vs 94%; both safe and effective |
| [1761453](https://pubmed.ncbi.nlm.nih.gov/1761453/) | 1991 | RCT | J Antimicrob Chemother | Open, randomized comparison of cefprozil 500 mg once daily vs cefaclor 250 mg three times daily in 102 adults with acute uncomplicated UTI |
| [1611652](https://pubmed.ncbi.nlm.nih.gov/1611652/) | 1992 | RCT | Clin Ther | Multicenter randomized study of once-daily cefprozil vs cefaclor for 10 days in patients aged 2 years or older with uncomplicated UTI |
| [7681376](https://pubmed.ncbi.nlm.nih.gov/7681376/) | 1993 | Review | Drugs | Review of antibacterial activity, pharmacokinetics and therapeutic potential. Moderate activity against many Enterobacteriaceae |
| [8464648](https://pubmed.ncbi.nlm.nih.gov/8464648/) | 1993 | Review | Pediatr Ann | Cefprozil has once- or twice-daily dosing and a low rate of gastrointestinal and skin side effects |
| [8042575](https://pubmed.ncbi.nlm.nih.gov/8042575/) | 1994 | Review | Am Fam Physician | Oral cephalosporins are effective, though expensive, alternatives for skin, respiratory and urinary tract infections |
| [1289583](https://pubmed.ncbi.nlm.nih.gov/1289583/) | 1992 | Clinical study (pediatric, uncontrolled) | Jpn J Antibiot | 21 children with acute bacterial infections, including 3 with UTI. Good to excellent response in 19 of 21 |
| [1494237](https://pubmed.ncbi.nlm.nih.gov/1494237/) | 1992 | Clinical study (pediatric, uncontrolled) | Jpn J Antibiot | Pediatric laboratory and clinical study covering serum and urinary concentrations of cefprozil |
| [8529432](https://pubmed.ncbi.nlm.nih.gov/8529432/) | 1995 | In vitro study | Chemotherapy | 637 clinical isolates from Taiwan. Over 80% of *E. coli* and *K. pneumoniae* isolates were inhibited at 8 mg/L |

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02293528 | SPC-CEFPROZIL |
| 02329204 | SPC-CEFPROZIL |
| 02347261 | AURO-CEFPROZIL |
| 02347288 | AURO-CEFPROZIL |
| 02293579 | SPC-CEFPROZIL |

Showing 5 of 7 authorizations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three randomized trials in acute uncomplicated UTI showed cure rates comparable to cefaclor, and the mechanism is direct and plausible. However, the trials are more than 30 years old and no trials are registered. Resistance patterns have also changed, so use should be restricted to uncomplicated UTI with susceptibility support.

The other nine TxGNN predictions are weaker:
- Pneumonia and laryngitis have only indirect evidence (Research Question).
- Epiglottitis, gonococcal urethritis, xanthogranulomatous pyelonephritis and uterine inflammatory disease are Hold.
- Ureaplasma urethritis, urogenital tuberculosis and abdominal tuberculosis contradict the mechanism and are likely false positives (Hold).

**To proceed, the following is needed:**
- Confirm whether UTI is already on the Canadian label, using the Health Canada product monograph. This also supplies the missing warnings and contraindications.
- Review local antibiogram data for common urinary pathogens.
- Obtain mechanism of action data from DrugBank.
- Look for recent trials or real-world data, since the current evidence is from the early 1990s.
- Define the target population, for example uncomplicated cystitis in non-pregnant women, and a safety monitoring plan.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

