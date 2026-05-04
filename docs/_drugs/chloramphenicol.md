---
layout: default
title: Chloramphenicol
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 9
---

# Chloramphenicol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Chloramphenicol: From Broad-Spectrum Bacterial Infections to Conjunctivitis

## One-Sentence Summary

Chloramphenicol is a classical broad-spectrum bacteriostatic antibiotic introduced into clinical practice in 1948, historically used to treat serious bacterial infections including typhoid fever, bacterial meningitis, and plague.
The TxGNN model predicts it may be effective for **conjunctivitis**, with **0 registered clinical trials** and **19 publications** currently supporting this direction.
Notably, this prediction aligns with chloramphenicol's already well-established ophthalmic use in many countries outside Canada, effectively validating the model's output against decades of real-world clinical practice.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (typhoid fever, bacterial meningitis, plague) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L3 (Cochrane systematic reviews + multiple comparative RCTs in literature) |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, chloramphenicol is a broad-spectrum bacteriostatic antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit and blocking the peptidyl transferase reaction. This mechanism is effective against a wide range of gram-positive and gram-negative organisms, including *Staphylococcus aureus*, *Streptococcus pneumoniae*, and *Haemophilus influenzae* — the most common causative pathogens of bacterial conjunctivitis.

The mechanistic link between chloramphenicol's original systemic indications and conjunctivitis is direct: both involve bacterial infection, and the same antibiotic activity that clears systemic pathogens applies equally to superficial ocular infections when the drug is delivered topically. Chloramphenicol penetrates ocular tissues effectively, achieving concentrations sufficient for bacteriostatic activity in the conjunctival sac.

It is worth noting that this prediction does not represent a novel repurposing in the traditional sense. Chloramphenicol eye drops and ointments have been used as a first-line treatment for bacterial conjunctivitis for decades and remain widely available over-the-counter in the United Kingdom and other markets. The TxGNN model's exceptionally high confidence score (99.66%) reflects this established clinical reality and demonstrates the model's ability to correctly identify real-world indications — providing strong internal validation of the system's predictive performance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for chloramphenicol and conjunctivitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16378567](https://pubmed.ncbi.nlm.nih.gov/16378567/) | 2005 | Systematic Review | Br J Gen Pract | Cochrane systematic review and meta-analysis of topical antibiotics for acute bacterial conjunctivitis; supports topical antibiotic therapy (including chloramphenicol) as effective for bacterial conjunctivitis in primary care settings |
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Cochrane Review | Cochrane Database Syst Rev | Systematic review of interventions for preventing ophthalmia neonatorum; evaluates ophthalmic chloramphenicol as a prophylactic agent against neonatal conjunctivitis including gonococcal infection |
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | Comparative Study | Curr Ther Res Clin Exp | Head-to-head comparison of moxifloxacin and chloramphenicol for bacterial eye infections; confirms chloramphenicol's established role in ophthalmic practice as a bacteriostatic organochlorine |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | RCT | Acta Ophthalmologica | Randomised single-blind trial: chloramphenicol 0.5% eye drops achieved 81% (104/129) clinical success rate in acute purulent conjunctivitis, comparable to fusidic acid 1% (84%) |
| [8333258](https://pubmed.ncbi.nlm.nih.gov/8333258/) | 1993 | RCT | Acta Ophthalmologica | Norwegian multicentre RCT across 38 general practitioners; no significant difference in bacteriological or clinical response between fusidic acid and chloramphenicol for acute conjunctivitis |
| [17947266](https://pubmed.ncbi.nlm.nih.gov/17947266/) | 2007 | RCT | Br J Ophthalmol | Randomised equivalency trial comparing 2.5% povidone-iodine eye drops versus ophthalmic chloramphenicol for preventing neonatal conjunctivitis in a trachoma-endemic region in Mexico |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | RCT | J Antimicrob Chemother | Multicentre double-blind RCT (n=230) comparing trimethoprim-polymyxin B versus chloramphenicol ophthalmic solution in presumptive bacterial conjunctivitis; both preparations effective with few adverse effects |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | Safety Review | Drug Safety | Critical safety review examining the controversial association between topical ocular chloramphenicol and aplastic anaemia; UK permits widespread use while US restricts it — central to any regulatory risk-benefit analysis |
| [19680306](https://pubmed.ncbi.nlm.nih.gov/19680306/) | 2009 | Review | NZ Med J | Evidence review and management recommendations for acute infective conjunctivitis for New Zealand practitioners; discusses clinical predictors, role of topical antibiotics, and antibiotic choice including chloramphenicol |
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | RCT | Acta Ophthalmologica | Open randomised RCT in Tanzania comparing fusidic acid (93% success), chloramphenicol (48% success), and framycetin (74% success) in bacterial conjunctivitis; lower chloramphenicol success rate attributed to higher in vitro resistance rates |

---

## Safety Considerations

- **Aplastic Anaemia Risk (Topical Use)**: Literature (PMID 8800624) documents a long-standing controversy regarding the association between topical ocular chloramphenicol and aplastic anaemia. Although estimated incidence is very low (~1 in 200,000 courses based on UK post-marketing data), this has led the US to effectively withdraw ophthalmic chloramphenicol from the market, while the UK continues to permit OTC use. This safety signal represents the most critical risk-benefit consideration for any regulatory pathway in Canada.

- **Systemic Toxicity (Non-Ophthalmic Routes)**: Systemic chloramphenicol carries a well-known risk of dose-independent idiosyncratic aplastic anaemia and dose-dependent reversible bone marrow suppression. Grey baby syndrome (cardiovascular collapse in neonates) is associated with systemic use due to immature glucuronyl transferase activity. These systemic risks are less relevant for topical ophthalmic formulations but should be documented in any product monograph.

For complete warnings, contraindications, and drug interaction data, please obtain and review the full product monograph from a jurisdiction where chloramphenicol ophthalmic products are currently registered (e.g., UK, Australia).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Chloramphenicol eye drops for bacterial conjunctivitis represent a well-established, evidence-supported treatment validated by multiple comparative RCTs and two Cochrane-level systematic reviews — this is not a speculative repurposing but a confirmation of existing global clinical practice. However, the drug is currently not marketed in Canada (0 DINs), and the rare but serious risk of aplastic anaemia with topical ophthalmic use warrants a structured regulatory and safety evaluation before any commercialisation pathway is pursued.

**To proceed, the following is needed:**

- **Regulatory pathway clarification**: Determine whether a New Drug Submission (NDS) or Abbreviated New Drug Submission (ANDS) is required for ophthalmic chloramphenicol in Canada; review Health Canada's position on the aplastic anaemia risk signal
- **Full safety data package**: Obtain complete product monograph including warnings, contraindications, and drug interactions from a currently approved jurisdiction (e.g., UK MHRA or Australian TGA dossier)
- **Updated aplastic anaemia risk assessment**: Commission or review recent post-marketing pharmacovigilance data to provide a contemporary incidence estimate for the Canadian risk-benefit analysis
- **Resistance profiling**: Assess current chloramphenicol resistance rates among common conjunctival pathogens (*S. aureus*, *H. influenzae*, *S. pneumoniae*) in Canadian clinical isolates, as the 1987 Tanzania RCT (PMID 3300139) flagged a 48% clinical success rate linked to high local resistance
- **Mechanism of action documentation**: Formally document MOA (50S ribosomal subunit / peptidyl transferase inhibition) for submission and formulary evaluation purposes
- **Market differentiation analysis**: Evaluate clinical unmet need relative to currently approved ophthalmic antibiotics in Canada (fluoroquinolones, aminoglycosides, azithromycin) to establish a viable commercial and clinical rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

