---
layout: default
title: Obeticholic Acid
parent: Model Prediction Only (L5)
nav_order: 568
evidence_level: L5
indication_count: 6
---

# Obeticholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Obeticholic Acid: From Primary Biliary Cholangitis to Rheumatoid Arthritis

## One-Sentence Summary

Obeticholic acid (OCA) is a farnesoid X receptor (FXR) agonist approved for primary biliary cholangitis (PBC), a chronic cholestatic autoimmune liver disease.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this direction is currently supported by **0 clinical trials** and only **3 loosely related publications**, none of which directly studies OCA in RA.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary Biliary Cholangitis (PBC) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

OCA is an FXR agonist. Its approved mechanism centers on restoring bile acid homeostasis and exerting hepatic anti-inflammatory/anti-fibrotic effects — this is the basis for its PBC indication. There is no established pathway connecting FXR activation to the synovial autoimmune inflammation (TNF/IL-6-driven) that characterizes rheumatoid arthritis.

PBC and rheumatoid arthritis do share a broad "autoimmune disease" categorization, and a small body of literature explores indirect systemic immune effects of FXR activation. However, none of the three retrieved publications actually studies OCA in an RA context — they concern PBC diagnosis/management, autoimmune hepatitis animal models, and liver injury from an unrelated herbal compound used for RA. This pattern is consistent with the prediction arising from semantic proximity in the knowledge graph (both diseases tagged "autoimmune") rather than a genuine pharmacological signal.

Given the absence of both clinical and preclinical evidence directly linking OCA to RA, this candidate should be treated as a low-confidence, exploratory signal rather than a validated repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32299307](https://pubmed.ncbi.nlm.nih.gov/32299307/) | 2020 | Review | United European Gastroenterology Journal | General review of PBC diagnosis and treatment; does not address OCA use in RA |
| [35903109](https://pubmed.ncbi.nlm.nih.gov/35903109/) | 2022 | Review | Frontiers in Immunology | Reviews animal models for autoimmune hepatitis/PBC; treatment of cholestatic autoimmune liver disease relies on bile acid analogues, no RA linkage |
| [33704005](https://pubmed.ncbi.nlm.nih.gov/33704005/) | 2021 | Preclinical/Animal | Xenobiotica | Shows FXR activation prevents liver injury from *Tripterygium wilfordii* preparations (a separate herbal RA treatment) in mice; does not study OCA efficacy in RA itself |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist for OCA in rheumatoid arthritis, and the available literature does not establish a direct mechanistic or clinical link — the prediction more likely reflects a knowledge-graph embedding artifact from shared "autoimmune disease" categorization than a real pharmacological signal. Combined with the drug's non-marketed status in Canada, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed detailed mechanism-of-action data for OCA (currently a data gap in the source record)
- Preclinical studies directly testing FXR modulation in RA-relevant models (synovial inflammation, TNF/IL-6 pathways)
- TFDA/Health Canada label warnings and contraindications (currently a data gap; flagged as Blocking for safety review)
- Re-evaluation if future evidence directly linking FXR agonism to RA pathophysiology emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

