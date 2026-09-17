---
layout: default
title: Piperacillin
parent: Model Prediction Only (L5)
nav_order: 623
evidence_level: L5
indication_count: 9
---

# Piperacillin
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

# Piperacillin: From Bacterial Infections to Rheumatoid Arthritis

## One-Sentence Summary

> Piperacillin is a broad-spectrum penicillin-class antibiotic; detailed original indication and mechanism-of-action data are not available in this Evidence Pack.
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
> but the supporting **18 publications** are almost entirely case reports of bacterial infections occurring *in* RA patients who were treated with piperacillin(-tazobactam) — not evidence of any therapeutic effect on RA itself. No clinical trials support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Evidence Pack (drug.original_indications is empty; Piperacillin is a ureidopenicillin antibacterial by drug class) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only; no clinical trials; literature is incidental co-occurrence, not treatment evidence) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002, High severity). Based on known pharmacological class information, Piperacillin is a beta-lactam antibiotic that inhibits bacterial cell-wall synthesis by binding penicillin-binding proteins (PBPs). This mechanism targets bacterial cell division, not the autoimmune/inflammatory pathways (e.g., TNF-α, IL-6, RANKL) implicated in rheumatoid arthritis pathogenesis.

The repurposing rationale attached to this candidate is explicit on this point: none of the retrieved literature describes piperacillin being used to treat RA disease activity. Instead, every relevant article describes RA patients (often on immunosuppressants such as methotrexate, etanercept, or JAK inhibitors) who developed a **secondary bacterial infection** — empyema, prosthetic joint infection, purulent pericarditis, osteomyelitis — for which piperacillin/tazobactam was administered as standard antibacterial therapy. This is a textbook example of **co-occurrence rather than causal/therapeutic association**, likely arising from shared keyword context in the knowledge graph (RA + antibiotic used for RA-related infection) rather than a genuine biological signal.

Consequently, while the raw TxGNN embedding score is very high (99.94%), the qualitative evidence review does not support a plausible mechanistic link between piperacillin and RA treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (ClinicalTrials.gov: 0 results; ICTRP: 0 results, per query_log).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Annals of Translational Medicine | Evaluates antibiotic-associated drug-induced liver injury (DILI) prevalence; not RA-specific, no treatment relevance |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2025 | Cohort | British Journal of Clinical Pharmacology | Predictive model for eosinophilia risk with ampicillin/sulbactam or piperacillin/tazobactam therapy; a safety-signal study, not an RA efficacy study |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case Report | BMJ Case Reports | RA patient on methotrexate/etanercept developed purulent pericarditis; piperacillin-tazobactam given empirically to treat the infection |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Case Report | Cureus | RA patient in remission developed recurrent pleural effusion; antibiotic treatment for a suspected infectious complication, not RA itself |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case Report | Orthopädie (Heidelberg) | RA patient on upadacitinib developed prosthetic knee joint infection (H. influenzae); treated with piperacillin/tazobactam as part of infection management |
| [30371923](https://pubmed.ncbi.nlm.nih.gov/30371923/) | 2019 | Case Report | Orthopedics | RA patient on long-term steroids developed E. coli emphysematous osteomyelitis; antibiotic-impregnated rods used, IV antibiotics for infection control |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Case Report | Frontiers in Immunology | Immunosuppressed RA patient developed atypical bullous erysipelas from E. coli with septic shock; treated with broad-spectrum antibiotics for infection |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case Report (pending classification) | Proceedings (Baylor Univ. Medical Center) | RA patient on low-dose methotrexate developed pancytopenia toxicity; unrelated to piperacillin mechanism |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case Report (pending classification) | Cureus | RA patient with methotrexate-induced pancytopenia; no piperacillin/RA treatment relationship |
| [1921823](https://pubmed.ncbi.nlm.nih.gov/1921823/) | 1991 | Case Report (pending classification) | The Medical Journal of Australia | RA patient with methotrexate overdose causing pancytopenia; unrelated to piperacillin |

**Note:** None of the above articles report piperacillin as a treatment for rheumatoid arthritis disease activity. Most describe antibiotic use for infections that occur secondary to RA immunosuppressive therapy.

---

## Canada Market Information

No Canadian market authorizations (DINs) are currently on file for this candidate. `taiwan_regulatory.total_licenses = 0`, market status: **Not Marketed**.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: Data Gap DG001 (TFDA/Health Canada product-monograph warnings and contraindications) is flagged as **Blocking severity** — this prevents the candidate from entering the S1 safety pre-assessment stage until resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the underlying evidence does not support a genuine drug-disease relationship — all 18 retrieved publications reflect incidental antibiotic use for infections in RA patients rather than any therapeutic effect on RA, there are zero clinical trials, and no plausible mechanism connects piperacillin's antibacterial action to RA pathophysiology. Evidence Level is L5 (model prediction only).

**To proceed, the following is needed:**
- Verified Piperacillin mechanism of action (MOA) data from DrugBank to formally document the absence of an RA-relevant pathway (resolves DG002)
- Official Health Canada product monograph for warnings/contraindications/DDI (resolves DG001, currently blocking)
- Any RA-specific preclinical or mechanistic studies, if they exist, to re-evaluate whether a genuine (rather than co-occurrence-driven) signal is present
- Given the current evidence quality, no further development action is recommended for this indication unless materially different evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

