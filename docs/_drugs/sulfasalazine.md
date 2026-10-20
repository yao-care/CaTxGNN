---
layout: default
title: Sulfasalazine
parent: Model Prediction Only (L5)
nav_order: 872
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sulfasalazine: predicted new indication Osteoarthritis (evidence level L5). Approved use: Rheumatoid arthritis, ulcerative colitis, inflammatory bowel disease…"
monitor_inn: "SULFASALAZINE"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "osteoarthritis susceptibility", "congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "WHIM syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "spondyloarthropathy, susceptibility to", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis"]
---

# Sulfasalazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Sulfasalazine: From Rheumatoid Arthritis and Ulcerative Colitis to Osteoarthritis

## One-Sentence Summary

Sulfasalazine is an anti-inflammatory drug originally used for rheumatoid arthritis, ulcerative colitis, inflammatory bowel disease, juvenile arthritis and spondyloarthropathy.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are **no registered clinical trials**, and the supporting evidence is mainly **preclinical studies and general rheumatology reviews** among 20 publications.

Note: the top-ranked TxGNN prediction is brachydactyly-syndactyly syndrome (score 99.94%). It has no supporting trials or literature, and no plausible mechanistic link to sulfasalazine. This report therefore focuses on osteoarthritis, the highest-ranked prediction with meaningful supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ulcerative colitis, inflammatory bowel disease, juvenile idiopathic arthritis, spondyloarthropathy (the Canadian licence records contain no indication text) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold (treat as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the literature, sulfasalazine has anti-inflammatory activity, including inhibition of NF-kB signalling and reduced release of prostaglandins and leukotrienes. Its efficacy in inflammatory joint disease such as rheumatoid arthritis is established, so it may also be applicable to the inflammatory and cartilage-degrading processes in osteoarthritis.

Preclinical studies support this link:
- A sulfasalazine-containing hyaluronic acid formulation reduced inflammation and cartilage degradation in a rat osteoarthritis model (PMID 29548914).
- Sulfasalazine reduced cartilage destruction in an ACL transection and meniscectomy model, possibly through inhibition of the cystine/glutamate antiporter (PMID 26466556).
- It blocked the release of proteoglycan and collagen from cytokine-stimulated cartilage and down-regulated metalloproteinases (PMID 19690126).
- It changed the protein profile of articular chondrocytes (PMID 24329131).

No human osteoarthritis trials were found in the data compiled for this report, so the clinical benefit is unproven.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 20 publications linked to osteoarthritis include several that are only loosely related. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Preclinical (rat model) | Int J Biol Macromol | Sulfasalazine-hyaluronic acid system gave sustained release for up to 60 days and reduced inflammation and cartilage degradation |
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Preclinical (animal model) | J Orthop Res | Reduced cartilage destruction after ACL transection and meniscectomy via inhibition of system xc- |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | Preclinical (in vitro) | Rheumatology (Oxford) | Blocked proteoglycan and collagen release from cytokine-stimulated cartilage; down-regulated metalloproteinases |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | Preclinical (in vitro) | Mod Rheumatol | Sulfasalazine and tofacitinib altered the protein profile of articular chondrocytes |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Preclinical (in vitro) | Wien Klin Wochenschr | Sulfasalazine and its metabolites affected prostaglandin and leukotriene release from human synovial tissue |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Review | Front Immunol | Review of ferroptosis in inflammatory arthritis, including osteoarthritis |
| [24231065](https://pubmed.ncbi.nlm.nih.gov/24231065/) | 2014 | Systematic review | Semin Arthritis Rheum | Interstitial lung disease induced or exacerbated by DMARDs and biologics in rheumatoid arthritis |
| [9567207](https://pubmed.ncbi.nlm.nih.gov/9567207/) | 1998 | Review | Curr Opin Rheumatol | Update on clinical trials in rheumatic diseases, including osteoarthritis |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00598488 | PMS-SULFASALAZINE-E.C. TAB 500MG | Not specified | Not specified |
| 00598461 | PMS-SULFASALAZINE 500MG/TAB USP | Not specified | Not specified |
| 02064480 | SALAZOPYRIN TAB 500MG | Not specified | Not specified |
| 02544652 | JAMP SULFASALAZINE | Not specified | Not specified |
| 02064472 | SALAZOPYRIN EN-TABS 500 MG | Not specified | Not specified |

---

## Safety Considerations

- **Contraindications and conditions of concern** (from knowledge graph drug-disease associations, not label text): inherited porphyria and other porphyrias, kidney disease, liver disease, gallbladder disease, asthma, neutropenia, agranulocytosis, aplastic anaemia, G6PD deficiency, slow acetylator status, urinary tract obstruction, glycogen storage disease, cystinuria and galactosemia.
- **Drug Interactions**: The interaction query returned 100 records. The main ones from the list reviewed are:
  - **Major**: prilocaine (topical), human immunoglobulin G (intravenous), methenamine.
  - **Moderate**: NSAIDs (ketorolac, ibuprofen, celecoxib), azathioprine, nephrotoxic agents (amphotericin B, amikacin), acyclovir, oestrogens (estradiol, ethinylestradiol), alpelisib, apalutamide, asparaginase, bacitracin, topical aminolevulinic acid.
  - **Minor**: folic acid.

Please refer to the package insert for full warnings and precautions. The label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
The osteoarthritis prediction rests on animal and in vitro studies, with no human trials. The plausible anti-inflammatory and cartilage-protective mechanism makes it worth investigating, but it is not yet ready for clinical development. The other top predictions (rare congenital syndromes) have no supporting data and should stay on hold. Spondyloarthropathy (rank 8) is already a labelled use, so it is not true repurposing.

**To proceed, the following is needed:**
- Human clinical data in osteoarthritis, such as a pilot randomised trial or a systematic review
- Package insert warnings and contraindications from Health Canada, which are currently missing
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian products
- Assessment of route and formulation, since the preclinical work used a local sulfasalazine-hyaluronic acid delivery system rather than oral tablets
- A risk-benefit review for the likely osteoarthritis population, given the haematological, hepatic and renal safety concerns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

