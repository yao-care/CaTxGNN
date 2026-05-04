---
layout: default
title: Acetic Acid
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 9
---

# Acetic Acid
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

# Acetic Acid: From Topical Antimicrobial Agent to Post-Bacterial Disorder

## One-Sentence Summary

Acetic acid is a widely used antimicrobial compound employed clinically in topical applications for bacterial infections (including otitis externa and wound irrigation), though it carries no formal regulatory approval in Canada's drug registry.
The TxGNN model predicts it may be effective for **post-bacterial disorder** — conditions arising after active bacterial infection has cleared —
with **18 clinical trials** retrieved but **0 directly relevant publications** supporting this specific therapeutic direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No formal regulatory approval recorded in Canada |
| Predicted New Indication | Post-bacterial disorder |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Acetic acid is a short-chain fatty acid (SCFA) and organic acid with well-documented antimicrobial properties. At clinically used concentrations (0.25%–5%), it lowers local tissue pH to ≤4, creating an environment hostile to bacterial growth — particularly against *Pseudomonas aeruginosa* and other Gram-negative organisms. This mechanism underpins its established clinical use in bacterial otitis externa and wound irrigation. Additionally, as an endogenous gut microbial metabolite, acetic acid participates in immune signaling and intestinal epithelial barrier regulation.

"Post-bacterial disorder" describes conditions that develop after active bacterial infection has resolved — including post-sepsis syndrome, organ injury from bacteremia, reactive arthritis, or dysbiosis-related sequelae. The TxGNN model likely linked acetic acid's documented antibacterial activity and SCFA immunomodulatory properties to this disease cluster. However, the mechanistic bridge is weak: managing post-infectious sequelae requires immune reconditioning and tissue repair, which are not the direct pH-lowering antibacterial actions that characterise acetic acid's known mechanism.

Review of the 18 retrieved clinical trials reveals that acetic acid appears predominantly as a **diagnostic reagent** — specifically VIA (visual inspection with acetic acid) for cervical lesion detection — rather than as a therapeutic agent for post-bacterial conditions. The L4 evidence classification reflects this disconnect: while a theoretical mechanistic pathway exists via SCFA-mediated gut immunomodulation, no clinical or preclinical study has directly investigated acetic acid as a treatment for post-bacterial sequelae. This prediction most likely reflects structural noise in the TxGNN knowledge graph, where association with bacterial infection contexts was incorrectly extrapolated to post-infectious disease categories.

---

## Clinical Trial Evidence

> **Note:** All retrieved trials are indirectly related to the predicted indication. Acetic acid appears primarily as a colposcopy/diagnostic reagent (VIA), not as a therapeutic intervention for post-bacterial disorder.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03212729](https://clinicaltrials.gov/study/NCT03212729) | N/A | Completed | 10 | Antimicrobial photodynamic therapy as adjunct to endodontic treatment for primary endodontic infections; acetic acid potentially used as irrigation, but study targets active infection, not post-bacterial sequelae |
| [NCT04036318](https://clinicaltrials.gov/study/NCT04036318) | N/A | Completed | 3,022 | Presumptive periodic treatment of STIs in high-risk populations in Tanzania; acetic acid used exclusively as a VIA diagnostic screening tool, not as a therapeutic agent |
| [NCT04120259](https://clinicaltrials.gov/study/NCT04120259) | N/A | Completed | 126 | Apple cider vinegar (~3–5% acetic acid) combined with metformin vs metformin alone in newly diagnosed Type 2 diabetes; target indication is metabolic disease, not post-bacterial disorder |
| [NCT05777863](https://clinicaltrials.gov/study/NCT05777863) | N/A | Completed | 102 | Multidomain lifestyle intervention on brain function and immunometabolic markers in older adults at risk for cognitive decline; no connection to acetic acid or post-bacterial disorder |
| [NCT06612164](https://clinicaltrials.gov/study/NCT06612164) | N/A | Completed | 65 | Kefir consumption effects on gastrointestinal health, immunity, and sleep quality in healthy adults; kefir contains trace amounts of organic acids including acetic acid, but is not a pharmacological study of acetic acid |
| [NCT06005506](https://clinicaltrials.gov/study/NCT06005506) | N/A | Completed | 64 | Active vs passive synbiotic supplementation to assess effects on intestinal microbiota in chronically frail patients (ALS, ADHD, bronchial asthma); no direct relevance to acetic acid or post-bacterial disorder |
| [NCT07386795](https://clinicaltrials.gov/study/NCT07386795) | N/A | Not Yet Recruiting | 19 | Microbiota transplantation combined with prebiotics for functional constipation; not yet recruiting, therapeutic agent is microbiota transplant — not acetic acid |
| [NCT02872675](https://clinicaltrials.gov/study/NCT02872675) | N/A | Completed | 17 | Prebiotic supplementation effects on gut bacterial metabolites and systemic inflammation in adults with asthma/exercise-induced bronchoconstriction; no acetic acid pharmacology |
| [NCT05710094](https://clinicaltrials.gov/study/NCT05710094) | Phase 1 | Completed | 28 | Safety and tolerability of SoftOx Biofilm Eradicator topically applied in patients with chronic leg wounds; wound care antimicrobial context is adjacent but drug is not acetic acid |
| [NCT04824261](https://clinicaltrials.gov/study/NCT04824261) | N/A | Unknown | 100 | 4% boric acid vs clotrimazole solution for otomycosis; neither acetic acid nor post-bacterial disorder — disease is fungal, not post-bacterial |

---

## Literature Evidence

Currently no related literature available for post-bacterial disorder.

---

## Canada Market Information

Acetic acid (DrugBank: DB03166) is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) have been issued and no Health Canada product licences are on record. This absence of regulatory approval means standard Canadian pharmacovigilance and post-market safety data are unavailable for this compound.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap (Blocking):** TFDA package insert warnings and contraindications have not been retrieved. This is classified as a Blocking gap (DG001), preventing progression to the standard S1 safety pre-assessment stage. Retrieval from the regulatory authority's official website is required before further evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for acetic acid in post-bacterial disorder is most likely a false positive driven by knowledge graph structural noise. All 18 retrieved clinical trials are Grade C (indirect relevance), with acetic acid functioning as a colposcopic diagnostic tool rather than a therapeutic agent; no supporting literature exists for this indication; and the mechanistic link between acetic acid's pH-mediated antibacterial action and the immunopathological processes underlying post-bacterial sequelae is too indirect to justify further clinical investment.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Retrieve and parse the regulatory package insert (DG001) — this is required before any S1 safety pre-assessment can be completed
- **Mechanism of action data (High priority):** Query DrugBank API for MOA detail (DG002) to formally assess whether SCFA-mediated immune modulation provides a defensible mechanistic rationale
- **Preclinical evidence:** Commission or identify in vitro/in vivo studies evaluating acetate specifically in post-infection inflammatory or recovery models
- **Indication specificity:** Clarify whether the target is a definable clinical entity (e.g., post-sepsis immune dysregulation, post-infectious IBS) rather than the broad "post-bacterial disorder" category, which may be too heterogeneous to study as a single indication
- **Route and formulation strategy:** Determine whether a systemic formulation of acetic acid/acetate (e.g., oral sodium acetate, intravenous acetate infusion) is feasible and distinguishable from topical antimicrobial use

---

> **Notable Signal — Tinea Corporis (Rank #9):** Among all nine predicted indications, **tinea corporis** carries the strongest evidence profile in this pack (Evidence Level L3; Decision Stage S1 — "Research Question"). Historical case series from 1946–1947 document dilute acetic acid combined with iodine for treating tinea capitis, a 2023 RCT ([PMID 37012894](https://pubmed.ncbi.nlm.nih.gov/37012894/)) evaluated vinegar-based formulations for tinea corporis against terbinafine 1% cream, and in vitro data support antifungal activity against *Trichophyton rubrum* and *T. mentagrophytes* via pH-mediated disruption of cell membrane integrity. While modern antifungals remain superior first-line options, acetic acid may merit formal evaluation as a low-cost alternative in resource-limited settings — provided safety concerns around skin irritation and burn risk (PMID 37256034) are addressed in study design.

---

*This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

