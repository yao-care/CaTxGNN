---
layout: default
title: Colchicine
parent: Moderate Evidence (L3-L4)
nav_order: 220
evidence_level: L4
indication_count: 3
---

# Colchicine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Colchicine: From Its Established Uses (Gout and Familial Mediterranean Fever) to Plasmodium falciparum Malaria

## One-Sentence Summary

Colchicine is an anti-inflammatory drug mainly used for gout and familial Mediterranean fever (FMF), according to the literature retrieved. The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, but there are **0 clinical trials** and only **6 publications**, all laboratory or serology studies and none testing colchicine itself. This is a model prediction with very weak support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Canadian licence data; the literature describes gout and FMF as its main uses |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Colchicine is known to bind tubulin and disrupt microtubules. Several older laboratory studies show that compounds targeting the cytoskeleton (tubulin- or actin-binding agents) can inhibit the growth of P. falciparum in culture. This gives a plausible but indirect link between colchicine and malaria.

The link is weak for several reasons:

- No study in the evidence set tests colchicine in malaria patients.
- Parasite tubulin differs from mammalian tubulin and is generally considered poorly sensitive to colchicine.
- Colchicine has a narrow therapeutic index, so an in vitro effect is unlikely to translate into a safe antimalarial dose.

The high TxGNN score (0.996) is a model output, not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro | PLoS One | Curcumin (not colchicine) disrupts P. falciparum microtubules, supporting the idea that the parasite cytoskeleton is a drug target |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro | Mol Cell Biol | pfmdr1 expression in mammalian cells increases susceptibility to chloroquine; concerns chloroquine resistance, not colchicine |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro | Antimicrob Agents Chemother | Tubulozoles inhibit protein synthesis in P. falciparum; colcemid, a colchicine analogue, had a similar effect on protein synthesis |
| [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) | 1989 | In vitro | Cell Biol Int Rep | Tubulin-binding compounds were active against P. falciparum in culture; plasmodial tubulin appears different from mammalian tubulin |
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro | Cell Biol Int Rep | Duplicate record of the paper above |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Observational serology | Clin Exp Immunol | Anti-intermediate-filament antibodies found in patients with acute malaria; not relevant to colchicine efficacy |

---

## Canada Market Information

The record lists no dosage form or approved indication text for these products.

| DIN | Product Name |
|---------|------|
| 2373823 | JAMP-COLCHICINE |
| 2402181 | PMS-COLCHICINE |
| 572349 | COLCHICINE TAB 0.6MG |
| 2456559 | EURO-COLCHICINE |
| 2519380 | MYINFLA |

---

## Safety Considerations

- **Narrow therapeutic index**: Colchicine has no clear distinction between non-toxic, toxic and lethal doses. Unintentional poisoning is common and often has a poor outcome (PMID 20586571).
- **Dosing and interactions**: Renal and hepatic function and CYP3A4/P-gp interactions are key dosing concerns for colchicine in general.

Please refer to the package insert for the full warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The malaria prediction rests only on a high model score and indirect laboratory findings about cytoskeleton-targeting compounds. No study tests colchicine against malaria. The narrow therapeutic index makes it unlikely that an effective antiparasitic dose would be safe.

**To proceed, the following is needed:**
- Direct in vitro data showing colchicine activity against P. falciparum at clinically achievable concentrations
- Detailed mechanism-of-action data
- The Health Canada product monograph (warnings, contraindications, interactions)
- Approved indication text for the Canadian licences

**Note:** The same evidence pack shows a stronger prediction for **familial Mediterranean fever** (L3, Proceed with Guardrails). Colchicine is widely known as first-line FMF therapy, so this is probably an established use rather than true repurposing. Confirm its label status against the regulatory record before classifying it.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

