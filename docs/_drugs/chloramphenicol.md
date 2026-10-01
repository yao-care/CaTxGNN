---
layout: default
title: Chloramphenicol
parent: Model Prediction Only (L5)
nav_order: 179
evidence_level: L5
indication_count: 9
---

# Chloramphenicol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Chloramphenicol: From an Unlisted Original Indication to Conjunctivitis

## One-Sentence Summary

Chloramphenicol is a long-established broad-spectrum antibiotic, but the supplied data does not list its original approved indication.
The TxGNN model predicts it may be effective for **conjunctivitis**, and **17 publications** (including several randomized comparisons) currently support this direction, although **no clinical trials** are registered in the supplied data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied licence data |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L2 (capped because the phase of the published comparisons is not labelled) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Chloramphenicol binds the 50S ribosomal subunit and inhibits bacterial peptidyl transferase. This gives it broad bacteriostatic activity against common conjunctival pathogens, so the link to bacterial conjunctivitis is direct and plausible.

The empty original-indication field is most likely a data gap. Topical chloramphenicol is a long-established ocular antibiotic, especially in the UK, so this is probably an existing use rather than true repurposing. Confirm this against the product label.

The only Canadian licence in the supplied data is an **injection** (Chloromycetin Succinate). The predicted use is ocular, which is usually topical. Route compatibility has not been assessed, and this is a key gap.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | RCT | Acta Ophthalmol | Open comparison in acute conjunctivitis in Tanzania. Chloramphenicol drops had a 48% clinical success rate versus 93% for fusidic acid and 74% for framycetin. |
| [8333258](https://pubmed.ncbi.nlm.nih.gov/8333258/) | 1993 | RCT | Acta Ophthalmol | Fusidic acid viscous drops versus chloramphenicol 0.5% in Norwegian primary care. No significant difference in response or bacteriological findings. |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | RCT | Acta Ophthalmol | Single-blind comparison with fusidic acid in purulent conjunctivitis. Clinical success was 81% with chloramphenicol versus 84% with fusidic acid. Trivial side effects were more frequent with chloramphenicol (14% vs 5%). |
| [17947266](https://pubmed.ncbi.nlm.nih.gov/17947266/) | 2007 | RCT (equivalency) | Br J Ophthalmol | 2.5% povidone-iodine versus ophthalmic chloramphenicol for preventing neonatal conjunctivitis in a trachoma-endemic area of Mexico. |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | RCT (double-blind) | J Antimicrob Chemother | 230 patients with presumptive bacterial conjunctivitis. All preparations, including chloramphenicol, were effective with very few adverse effects. |
| [2360342](https://pubmed.ncbi.nlm.nih.gov/2360342/) | 1990 | Comparative trial | DICP | Norfloxacin ophthalmic versus chloramphenicol in bacterial conjunctivitis and blepharoconjunctivitis (no abstract available). |
| [16378567](https://pubmed.ncbi.nlm.nih.gov/16378567/) | 2005 | Systematic review | Br J Gen Pract | Cochrane update on topical antibiotics for acute bacterial conjunctivitis, including primary-care settings. |
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | Comparative study | Curr Ther Res | Moxifloxacin versus chloramphenicol for bacterial eye infections. Notes chloramphenicol is used mainly topically because of its known toxicity. |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | Review (safety) | Drug Saf | Reviews the controversial link between topical ocular chloramphenicol and aplastic anaemia. |
| [23571246](https://pubmed.ncbi.nlm.nih.gov/23571246/) | 2014 | Surveillance cohort | Indian J Ophthalmol | Antimicrobial resistance of conjunctival bacteria, including chloramphenicol, in rural Ethiopia. |

## Canada Market Information

| Licence No. | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 312363 | CHLOROMYCETIN SUCCINATE INJECTION | Injection (from product name) | Not listed in the supplied data |

## Safety Considerations

- **Aplastic anaemia:** A rare but reported concern with topical ocular chloramphenicol remains debated (PMID 8800624). Chloramphenicol is generally known for haematological toxicity.
- **Resistance:** Resistance in conjunctival flora is a concern (PMID 23571246).
- **Scope:** Non-bacterial (for example viral) conjunctivitis is not covered by an antibacterial.

Please refer to the package insert for warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism fits bacterial conjunctivitis, and multiple randomized comparisons show chloramphenicol performing comparably to other topical antibiotics. However, the trials are older, no registered trials were found, and the only Canadian licence in the data is an injection.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmation of the original approved indication and whether an ophthalmic product is authorized in Canada
- Route compatibility assessment (injection versus topical ocular use)
- Formal phase and quality grading of the published comparisons
- A risk-benefit statement covering haematological toxicity and resistance, with use limited to bacterial conjunctivitis

The other seven predicted indications (for example diffuse scleroderma, postinfectious vasculitis and Chagas cardiomyopathy) have little or no supporting evidence and are recommended as Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

