---
layout: default
title: Streptomycin
parent: 僅模型預測 (L5)
nav_order: 736
evidence_level: L5
indication_count: 10
---

# Streptomycin
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

# Streptomycin: From Systemic Bacterial Infections to Conjunctivitis

## One-Sentence Summary

> Streptomycin is a classic aminoglycoside antibiotic historically established as a first-line therapy for tuberculosis and other systemic bacterial infections (including plague and Buruli ulcer/*M. ulcerans* disease).
> The TxGNN model predicts it may be effective for **Conjunctivitis**,
> with **0 registered clinical trials** and **20 publications** currently associated with this direction, most dating from the 1940s–1970s.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the available regulatory data (streptomycin is not currently marketed in Canada); historically established for tuberculosis and other systemic bacterial infections such as plague and Buruli ulcer |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.87% (rank 3251) |
| Evidence Level | L3 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action documentation is not available in the evidence pack (data gap). Based on well-established pharmacology, streptomycin is an aminoglycoside that inhibits bacterial protein synthesis by binding the 30S ribosomal subunit, giving it broad-spectrum bactericidal activity — historically most notably against *Mycobacterium tuberculosis*, *Yersinia pestis* (plague), and *Mycobacterium ulcerans* (Buruli ulcer).

The link between the original systemic-infection use and conjunctivitis is pathogen-specific rather than broadly generalizable. The strongest mechanistic rationale in the evidence pack concerns **tuberculous conjunctivitis** and **Francisella tularensis-associated ocular disease (Parinaud oculoglandular syndrome)** — both conditions where streptomycin's established antimycobacterial/antibacterial activity against the causative organism provides a clear pathogen-level connection. For general (non-specific-pathogen) bacterial conjunctivitis, however, the supporting evidence is thinner and largely historical, consisting of mid-20th-century field trials and case reports rather than contemporary comparative data.

Given this, the prediction is biologically plausible for specific etiologies (TB, tularemia) but not yet well supported as a general conjunctivitis therapy. Route of administration is also an open question — the historical literature includes both topical (eye-wash, instillation) and systemic use, but the evidence pack does not confirm which formulation(s) would be required or available (`route_compatibility.status: pending`).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18132879](https://pubmed.ncbi.nlm.nih.gov/18132879/) | 1949 | Experimental Study | American Journal of Ophthalmology | Effectiveness of streptomycin in treatment of experimental conjunctivitis caused by *Hemophilus* sp. |
| [13075256](https://pubmed.ncbi.nlm.nih.gov/13075256/) | 1953 | Field Trial (Prophylaxis) | Revue internationale du trachome | Streptomycin/chloramine instillations for prophylaxis and treatment of seasonal conjunctivitis in rural Morocco |
| [13075257](https://pubmed.ncbi.nlm.nih.gov/13075257/) | 1953 | Field Trial (Comparative) | Revue internationale du trachome | Streptomycin eye-wash vs. aureomycin salve for prevention of seasonal conjunctivitis in southern Morocco |
| [15442493](https://pubmed.ncbi.nlm.nih.gov/15442493/) | 1950 | Case Report | La Semana medica | Primary tuberculous conjunctivitis with fistulized submaxillary adenopathies treated with systemic and local streptomycin |
| [5289718](https://pubmed.ncbi.nlm.nih.gov/5289718/) | 1971 | Laboratory Study | The Journal of Hygiene | Streptomycin/neomycin effective at preventing bacterial contamination when isolating trachoma (TRIC) agent from conjunctival scrapings |
| [21484175](https://pubmed.ncbi.nlm.nih.gov/21484175/) | 2011 | Microbiology Survey | J Ophthalmic Inflamm Infect | Bacterial etiology and antibiotic susceptibility patterns (incl. aminoglycosides) in conjunctivitis patients, Lagos, Nigeria |
| [38941282](https://pubmed.ncbi.nlm.nih.gov/38941282/) | 2024 | Case Report | Am J Case Rep | *Francisella tularensis* causing Parinaud oculoglandular syndrome (granulomatous palpebral conjunctivitis) |
| [38298538](https://pubmed.ncbi.nlm.nih.gov/38298538/) | 2023 | Review | Frontiers in Microbiology | Tularemia treatment overview; conjunctivitis as a common presentation of local infection |
| [6789462](https://pubmed.ncbi.nlm.nih.gov/6789462/) | 1981 | Case Report | S Afr Med J | Brucella keratoconjunctivitis following occupational exposure; systemic treatment included streptomycin with tetracyclines/co-trimoxazole |
| [3317953](https://pubmed.ncbi.nlm.nih.gov/3317953/) | 1987 | Review (background) | Survey of Ophthalmology | Historical review of aminoglycosides in ophthalmology, noting streptomycin as the first aminoglycoside discovered (1943); primary focus is tobramycin |

---

## Canada Market Information

Streptomycin is not currently marketed in Canada. No Drug Identification Numbers (DINs) or product licenses are on file (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for the conjunctivitis indication is limited to Level L3 (mostly 1940s–1970s field trials and case reports) with **zero registered clinical trials**, and mechanistic support is strongest only for specific etiologies (tuberculous, tularemic) rather than general bacterial conjunctivitis. Critically, a **Blocking** data gap (DG001: missing warnings/contraindications) means this candidate cannot yet enter the S1 safety pre-assessment stage, and streptomycin is not currently marketed in Canada (0 DINs).

**To proceed, the following is needed:**
- Official label warnings/contraindications data (DG001, blocking) — required before any S1 safety assessment
- Confirmed mechanism of action documentation from DrugBank (DG002)
- Clarification of intended route of administration (topical/ophthalmic vs. systemic) for the conjunctivitis indication, as this is currently unresolved (`route_compatibility.status: pending`)
- Contemporary comparative or controlled evidence, given that existing supportive literature predates modern ophthalmic antibiotic standards by 50+ years
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

