---
layout: default
title: Inosine Pranobex
parent: Model Prediction Only (L5)
nav_order: 474
evidence_level: L5
indication_count: 10
---

# Inosine Pranobex
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

# Inosine Pranobex: From Immunomodulatory Antiviral Use to Osteoarthritis

## One-Sentence Summary

Inosine pranobex is an immunomodulatory agent marketed in Canada as IMUNOVIR. The TxGNN model predicts it may be effective for **osteoarthritis**, but there are currently **0 clinical trials** and **0 publications** for this specific indication. The best-supported neighbouring signal is **rheumatoid arthritis** (rank 3), with **14 publications** including one small placebo-controlled RCT from 1990.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available Canadian licence record |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.09% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, inosine pranobex is an immunomodulator. The published literature describes effects on neutrophil chemotaxis, lymphocyte and B-cell function, and Epstein-Barr virus-related B-cell growth.

The link to osteoarthritis is weak. The high TxGNN score (0.981) is a knowledge-graph prediction only. It may partly reflect shared immune or inflammatory pathways with rheumatoid arthritis, but this is unverified. Osteoarthritis is mainly a degenerative joint disease, so an immunomodulatory mechanism is not an obvious fit.

The evidence is stronger for rheumatoid arthritis, an immune-mediated joint disease. Old clinical studies (1981–1991) suggest possible benefit there, which makes it the more plausible research direction.

Several other top-ranked predictions have no identifiable mechanistic rationale and look like graph artifacts. These are osteoarthritis susceptibility, hepatic porphyria, pseudoachondroplasia, and several rare hepatic diseases with identical scores.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for osteoarthritis. No trials were registered for any of the other top-10 predicted indications either.

---

## Literature Evidence

Currently no related literature available for osteoarthritis.

The table below shows literature retrieved for **rheumatoid arthritis** (rank 3, score 97.74%, evidence level L2). It is the closest evidence-bearing indication and is shown for context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1693065](https://pubmed.ncbi.nlm.nih.gov/1693065/) | 1990 | RCT | Ann Rheum Dis | Double-blind, placebo-controlled trial of 24 patients on 3 g/day vs 26 on placebo for up to 24 weeks. Outcomes included morning stiffness, articular index, ESR and CRP. Results are not visible in the truncated abstract. |
| [2455393](https://pubmed.ncbi.nlm.nih.gov/2455393/) | 1988 | Pilot study | Z Rheumatol | Isoprinosine given to 10 seropositive patients in the early pre-erosive stage. |
| [6085298](https://pubmed.ncbi.nlm.nih.gov/6085298/) | 1983 | Clinical study (likely open-label) | Clin Exp Rheumatol | Title reports "moderate efficacy"; no abstract available. |
| [6170755](https://pubmed.ncbi.nlm.nih.gov/6170755/) | 1981 | Open study | J Rheumatol | 15 patients on 3 g/day; 9 of 15 had clinical benefit (less morning stiffness, fewer tender joints, lower ESR). |
| [6196834](https://pubmed.ncbi.nlm.nih.gov/6196834/) | 1983 | Clinical series | Rev Rhum Mal Osteoartic | 20 patients treated at 25 or 50 mg/kg/day; no side effects observed. The only reason for stopping treatment was ineffectiveness. |
| [2423433](https://pubmed.ncbi.nlm.nih.gov/2423433/) | 1986 | Clinical review (German) | Immun Infekt | 27 patients with rheumatic diseases. Clinical improvement within one month in 7 patients with moderately active RA. |
| [2421905](https://pubmed.ncbi.nlm.nih.gov/2421905/) | 1986 | Ex vivo study | Clin Ther | Levamisole and methisoprinol modulated impaired neutrophil chemotaxis in RA. |
| [2459076](https://pubmed.ncbi.nlm.nih.gov/2459076/) | 1988 | In vitro study | Int J Immunopharmacol | Inosiplex increased proliferation of EBNA-positive B-cells from RA and infectious mononucleosis patients. |
| [6179407](https://pubmed.ncbi.nlm.nih.gov/6179407/) | 1982 | Review | Allergol Immunopathol | Overview of in vitro and in vivo immunological activities (T-cell differentiation, lymphocyte proliferation). |
| [1715732](https://pubmed.ncbi.nlm.nih.gov/1715732/) | 1991 | Review | Curr Opin Rheumatol | General review of novel immunotherapies applicable to RA. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2240713 | IMUNOVIR | Not listed | Not listed in the licence record |

---

## Safety Considerations

- **Gout / hyperuricaemia**: Inosine is a purine metabolised to uric acid, and product labelling generally cautions against use in gout and hyperuricaemia. This is general pharmacological knowledge, not taken from the Canadian licence data. The model's gout prediction (rank 6) conflicts with this and is likely a false positive.
- **Porphyria**: Safety in hepatic porphyria has not been assessed.

No drug-interaction records were found. For other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction rests on the knowledge-graph score alone, with no trials, no literature and no clear mechanism. The only clinically supported direction is rheumatoid arthritis. That evidence is old (1981–1991), small, and was never compared with modern DMARDs or biologics.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Approved indication, dosage form and manufacturer details for the Canadian licence
- Full-text review of the 1990 RCT (PMID 1693065) to judge effect size and safety
- If pursuing this further, consider re-prioritising rheumatoid arthritis over osteoarthritis and screening against current standard-of-care therapy

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

