---
layout: default
title: Amikacin
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Amikacin
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

# Amikacin: From Serious Gram-Negative Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Amikacin is a broad-spectrum aminoglycoside antibiotic, clinically established for treating serious infections caused by susceptible gram-negative bacteria (including *Pseudomonas aeruginosa*, *Klebsiella*, *E. coli*, and non-tuberculous mycobacteria). The TxGNN model predicts it may be effective for **Paratyphoid Fever**, with a prediction score of **99.82%** (rank #4,095); however, the current evidence search returned **0 clinical trials** and **0 publications** specifically pairing amikacin with this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious gram-negative bacterial infections (no approved product on file in Canada) |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 (mechanistic rationale and known off-label use in resistant enteric fever; no controlled trials identified in this search) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Amikacin belongs to the aminoglycoside class of antibiotics. It acts by irreversibly binding to the **30S ribosomal subunit** of susceptible bacteria, causing misreading of the genetic code and inhibiting translocation during protein synthesis. This mechanism is bactericidal and is broadly applicable to gram-negative organisms, including members of the *Salmonella* genus.

Paratyphoid fever is caused by *Salmonella enterica* serovars **Paratyphi A, B, and C** — gram-negative bacilli to which amikacin's mechanism of action directly applies. Standard first-line therapy consists of fluoroquinolones or third-generation cephalosporins; however, the global rise of extensively drug-resistant (XDR) and multidrug-resistant (MDR) *Salmonella* strains has prompted clinicians to explore aminoglycosides as rescue or combination agents in treatment-refractory cases. Retrospective case series and infectious disease guidelines have documented the use of aminoglycosides, including amikacin, in these resistant contexts.

The TxGNN model's high prediction score for this pairing is therefore mechanistically coherent: both the original pathogen scope of amikacin and the causative organism of paratyphoid fever are gram-negative bacteria susceptible to 30S ribosomal inhibition. The prediction does not represent a surprising new biological leap, but rather a logical extension into a closely related indication not formally captured in most regulatory filings.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for amikacin in paratyphoid fever.

> *Note: Searches were conducted on ClinicalTrials.gov and ICTRP on 2026-03-24 with zero results returned.*

---

## Literature Evidence

Currently no related literature available from this search.

> *Note: A PubMed search conducted on 2026-03-24 for "amikacin" AND "paratyphoid fever" returned zero results. Relevant supporting evidence may exist under broader search terms (e.g., "aminoglycosides AND enteric fever AND drug-resistant") and warrants a supplementary manual literature review.*

---

## Canada Market Information

Amikacin currently has **no approved products (DINs) on file** in Canada under this evidence pack.

> *Note: Amikacin products are available in many countries (typically as parenteral formulations) and may be accessible through importation or special access programs. A dedicated Health Canada search is recommended to confirm current availability.*

---

## Safety Considerations

Please refer to the package insert for safety information.

> *Note: Full safety data (key warnings, contraindications, drug interactions) was not available in this evidence pack (classified as Data Gap). For clinical use, particular attention should be paid to amikacin's well-documented class effects: nephrotoxicity (dose- and duration-dependent), ototoxicity (irreversible cochlear and vestibular damage), and neuromuscular blockade. Therapeutic drug monitoring (TDM) with peak/trough levels is standard of care.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic link between amikacin and paratyphoid fever is scientifically coherent (gram-negative bacterium + 30S ribosomal inhibitor), there is no direct clinical trial or published literature specifically supporting this indication, and amikacin is not marketed in Canada. The evidence supports a "research question" designation rather than readiness for program advancement.

**To proceed, the following is needed:**

- **Supplementary literature review**: Broaden search to include terms such as "aminoglycosides AND enteric fever AND drug resistance," "amikacin AND Salmonella Paratyphi," and review WHO/CDC guidance on management of drug-resistant typhoid and paratyphoid fever.
- **Safety package**: Retrieve and parse the full product monograph / package insert (any jurisdiction) to populate nephrotoxicity, ototoxicity, and drug interaction warnings prior to any clinical planning.
- **Mechanism of action documentation**: Obtain formal MOA record from DrugBank (DB00479) to complete the mechanistic rationale section.
- **Regulatory pathway assessment**: Confirm whether amikacin is accessible in Canada via Special Access Programme (SAP) or existing DIN, and identify which formulation/route would be feasible for treating enteric fever (parenteral IV/IM).
- **Contextualization within XDR enteric fever guidelines**: Determine whether WHO pre-qualification or published resistance surveillance data supports amikacin as a named agent in resistant paratyphoid treatment algorithms, which would elevate the evidence level from L3 to L2 or higher.
- **Comparator analysis**: Assess whether newer agents for XDR enteric fever (e.g., azithromycin, carbapenems, fosfomycin) have superseded the clinical rationale for aminoglycoside use in this indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

