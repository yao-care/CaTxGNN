---
layout: default
title: Abemaciclib
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Abemaciclib
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

# Abemaciclib: From Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib (Verzenio) is an oral CDK4/6 inhibitor originally developed and approved globally for hormone receptor-positive (HR+), HER2-negative breast cancer treatment.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **1 publication** currently supporting this direction.
While direct clinical evidence is absent, the mechanistic rationale is substantiated by CDK4/6's established role in T cell and synovial fibroblast proliferation, with sister drug Palbociclib having prior RA preclinical research.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HR+/HER2- Breast Cancer (CDK4/6 inhibitor class) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed (0 DINs issued) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Abemaciclib inhibits cyclin-dependent kinases 4 and 6 (CDK4/6), arresting the cell cycle at the G1-to-S transition by preventing phosphorylation of the retinoblastoma protein (Rb). In HR+/HER2- breast cancer, this mechanism halts estrogen-driven tumor proliferation. Although detailed mechanism of action data was not available in the current Evidence Pack, the drug's CDK4/6 selectivity is well-established in the published literature and provides the foundation for this repurposing hypothesis.

In rheumatoid arthritis, two cell populations drive disease pathology: hyperactivated T lymphocytes (mediating autoimmune inflammation) and synovial fibroblasts (FLS), which proliferate abnormally, invade cartilage, and secrete destructive enzymes. Both cell types are dependent on CDK4/6 activity for G1-to-S progression. CDK4/6 inhibition has been demonstrated in preclinical settings to suppress FLS proliferation and reduce pro-inflammatory cytokines including IL-6 and TNF-α. Importantly, palbociclib — a structurally related CDK4/6 inhibitor — has published preclinical RA data, establishing class-level biological plausibility that extends naturally to abemaciclib.

Abemaciclib's pharmacokinetic profile strengthens the rationale further: it achieves higher systemic exposure and superior CNS/tissue penetration compared to palbociclib and ribociclib, supporting its ability to reach inflamed synovial tissue. The single retrieved publication (PMID 40504547) provides indirect corroborating evidence — documenting the emergence of clinically significant autoimmune conditions in breast cancer patients receiving CDK4/6 inhibitors, which implies genuine immunomodulatory activity of this drug class that could be mechanistically relevant to RA.

---

## Clinical Trial Evidence

Currently no related clinical trials for Abemaciclib in Rheumatoid Arthritis are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Retrospective Cohort | The Oncologist | CDK4/6 inhibitors combined with endocrine therapy in HR+/HER2- breast cancer were found to influence immune function, potentially enhancing antitumor immunity but also triggering autoimmune reactions; documents prevalence of autoimmune diseases and identifies potential predictive biomarkers in this patient population |

---

## Canada Market Information

Abemaciclib is currently not marketed in Canada. No Drug Identification Numbers (DINs) have been issued and no approved product licenses are on record.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — CDK4/6 inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low to Moderate — neutropenia and leukopenia reported in breast cancer trials; incidence substantially lower than conventional chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (neutrophil count), ALT/AST (hepatotoxicity signal), serum creatinine/eGFR, signs and symptoms of interstitial lung disease |
| Handling Protection | Standard oral oncology agent precautions apply; full cytotoxic drug handling protocols are generally not mandated, but institutional guidelines for oral antineoplastic agents should be followed |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale for Abemaciclib in rheumatoid arthritis is scientifically coherent — CDK4/6 inhibition directly targets the proliferative machinery of both autoimmune T cells and invasive synovial fibroblasts, and class-level preclinical evidence from palbociclib supports CDK4/6 as a legitimate RA target. However, direct clinical evidence for Abemaciclib specifically in RA is entirely absent at this stage, warranting a guardrailed research approach rather than a full development commitment.

**To proceed, the following is needed:**

- **Targeted RA preclinical studies**: Abemaciclib-specific experiments in established RA models (e.g., collagen-induced arthritis, FLS proliferation and invasion assays) to confirm drug-level (not just class-level) efficacy
- **Mechanism of action data**: Formal MOA retrieval from DrugBank API to confirm CDK4/6 selectivity profile and any secondary targets relevant to RA pathophysiology
- **Drug-drug interaction assessment**: RA patients routinely use DMARDs (methotrexate, leflunomide) and biologic agents (TNF inhibitors, JAK inhibitors) — DDI profiling with abemaciclib is essential before any clinical development
- **Safety profiling in immune-compromised patients**: Abemaciclib's known adverse events (Grade 3/4 neutropenia, diarrhea) carry additional risk in patients already immunosuppressed by standard RA therapies
- **Regulatory feasibility review**: Determine whether Health Canada's requirements for a new indication filing in a non-oncology setting can be met with preclinical-only evidence, and whether dose optimization for RA (likely requiring lower doses than oncology) needs separate PK/PD modeling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

