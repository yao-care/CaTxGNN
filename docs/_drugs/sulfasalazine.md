---
layout: default
title: Sulfasalazine
parent: Moderate Evidence (L3-L4)
nav_order: 739
evidence_level: L4
indication_count: 10
---

# Sulfasalazine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Sulfasalazine: From Rheumatoid Arthritis to Osteoarthritis

## One-Sentence Summary

> Sulfasalazine is a sulfa-based disease-modifying antirheumatic drug (DMARD), originally used to treat rheumatoid arthritis and ulcerative colitis, though it is not currently marketed in Canada.
> The TxGNN model predicts it may also be effective for **Osteoarthritis**,
> with **2 clinical trials** and **8 relevant publications** currently supporting this direction — evidence that is largely preclinical and mechanistic rather than clinical.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis / Ulcerative colitis (based on internationally established use; no Canadian license record available) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sulfasalazine is a sulfa-based anti-inflammatory / disease-modifying antirheumatic drug (DMARD) that is metabolized into sulfapyridine and 5-aminosalicylic acid; its efficacy in rheumatoid arthritis and ulcerative colitis has been proven clinically, and mechanistically it may be applicable to osteoarthritis through anti-inflammatory and chondroprotective pathways.

Rheumatoid arthritis and osteoarthritis are both joint diseases characterized by synovial inflammation, cytokine-driven cartilage degradation, and metalloproteinase activity — even though RA is primarily autoimmune and OA is primarily degenerative, the downstream inflammatory cascade in the joint overlaps substantially. This mechanistic overlap is a plausible basis for the TxGNN model linking a rheumatoid arthritis drug to an osteoarthritis indication.

Several preclinical and mechanistic studies directly support this link: sulfasalazine has been shown to inhibit metalloproteinase (MMP/ADAMTS) release from cytokine-stimulated chondrocytes, block leukotriene/prostaglandin release from synovial tissue, and reduce cartilage degradation in rat models of osteoarthritis (monosodium iodoacetate and ACL-transection/menisectomy models). While these findings are biologically consistent with the TxGNN prediction, they have not yet been confirmed in a dedicated clinical trial of sulfasalazine for osteoarthritis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A (retrospective cohort) | Completed | 479 | Real-world claims-based comparison of tofacitinib + MTX withdrawal vs. continuation in RA patients; not a direct sulfasalazine-OA trial but relevant to joint-disease treatment pattern context |
| [NCT00551707](https://clinicaltrials.gov/study/NCT00551707) | Phase 2 | Completed | 51 | Evaluated CRx-102 (dipyridamole + low-dose prednisolone) vs. its components in active RA; proof-of-concept data referenced hand osteoarthritis benefit, supporting a joint-disease anti-inflammatory rationale but not testing sulfasalazine directly |

*Note: Neither trial directly evaluates sulfasalazine in osteoarthritis; both are included for mechanistic/contextual relevance to inflammatory joint disease treatment.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Preclinical | J Orthop Res | Sulfasalazine attenuated ACL-transection/menisectomy-induced cartilage destruction via inhibition of the cystine/glutamate antiporter (system Xc-) in a rat OA model |
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Preclinical | Int J Biol Macromol | Sulfasalazine-loaded hyaluronic acid reduced inflammation and cartilage degradation in an MIA-induced rat OA model with sustained drug release over 60 days |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | Mechanistic (in vitro) | Rheumatology (Oxford) | Sulfasalazine blocked proteoglycan/collagen release from cytokine-stimulated cartilage and downregulated MMPs/ADAMTS proteinases |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | Mechanistic (in vitro) | Mod Rheumatol | Compared effects of sulfasalazine and tofacitinib on articular chondrocyte protein profiles |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Ex vivo (human tissue) | Wien Klin Wochenschr | Sulfasalazine and metabolites inhibited leukotriene C4 release from synovial tissue of OA, chondrocalcinosis, and RA patients |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Review | Front Immunol | Reviewed ferroptosis mechanisms across inflammatory arthritis types including osteoarthritis and RA |
| [11478054](https://pubmed.ncbi.nlm.nih.gov/11478054/) | 2001 | Review | Hand Clin | Reviewed pharmacologic treatment options across OA and RA |
| [9567207](https://pubmed.ncbi.nlm.nih.gov/9567207/) | 1998 | Review | Curr Opin Rheumatol | Overview of clinical trials in rheumatic diseases including OA and RA therapeutics |

---

## Canada Market Information

Sulfasalazine is currently **not marketed in Canada** (market status: Not Marketed; 0 DINs on record). No product authorization or approved indication text is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data could not be retrieved for this evaluation (Health Canada/TFDA labeling data gap — flagged as a **Blocking** data gap that prevents formal safety screening).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Supporting evidence for the osteoarthritis prediction is limited to preclinical and mechanistic studies (L4); no completed clinical trial has directly evaluated sulfasalazine for osteoarthritis.
- A **Blocking** data gap exists on official safety labeling (warnings/contraindications), which prevents the candidate from entering the S1 safety pre-screening stage. The drug is also not currently marketed in Canada, so no local regulatory or DIN pathway exists yet.

**To proceed, the following is needed:**
- Official TFDA/Health Canada labeling data (warnings, contraindications) to resolve the blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank to strengthen the mechanistic rationale (DG002)
- A dedicated Phase 2 clinical trial (or systematic review of existing RA/OA cohorts) directly testing sulfasalazine in osteoarthritis populations
- Clarification of the market-entry pathway in Canada, since the drug currently holds no active license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

