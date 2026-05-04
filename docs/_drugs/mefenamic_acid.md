---
layout: default
title: Mefenamic Acid
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 8
---

# Mefenamic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Mefenamic Acid: From Dysmenorrhea and Acute Pain to Rheumatoid Arthritis

## One-Sentence Summary

Mefenamic acid is a fenamate-class NSAID widely used internationally for dysmenorrhea, mild-to-moderate pain, and fever, though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 registered clinical trials** and **20 publications** — including multiple RCTs from the 1960s–1970s — currently supporting this direction.
However, as RA treatment has evolved substantially toward DMARDs and biologics, the clinical utility of mefenamic acid in modern RA management requires reassessment before moving forward.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Analgesic / Anti-inflammatory (NSAID class; no Canadian DINs on file) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, mefenamic acid is a fenamate-class NSAID that inhibits both COX-1 and COX-2 enzymes, thereby reducing prostaglandin and thromboxane synthesis from arachidonic acid. Unlike most NSAIDs, mefenamic acid also directly antagonizes prostaglandin receptors (particularly EP1 and FP receptors), giving it a dual mechanism of action that makes it particularly effective when prostaglandin levels are pathologically elevated.

Rheumatoid arthritis is a chronic systemic inflammatory disease in which synovial prostaglandins — particularly PGE2 — play a central role in mediating joint inflammation, pain, and swelling. Mefenamic acid's ability to reduce synovial fluid prostaglandin levels through both synthesis inhibition and receptor antagonism aligns directly with the core inflammatory cascade in RA, making the mechanistic rationale sound in principle.

Historically, mefenamic acid was explicitly tested in RA during the 1960s–1970s, with multiple randomized controlled trials demonstrating analgesic and anti-inflammatory efficacy comparable to ibuprofen, sulindac, and flurbiprofen at the doses tested. However, the current standard of care for RA has evolved dramatically — NSAIDs today are considered only adjunctive symptom-relief agents alongside DMARDs (e.g., methotrexate, hydroxychloroquine) and biologic/targeted agents (TNF inhibitors, IL-6 inhibitors, JAK inhibitors). The TxGNN prediction is mechanistically plausible, but the drug's role in contemporary RA management is supportive rather than disease-modifying, and no modern ICH-compliant Phase 3 trial exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | Double-blind crossover RCT | Current Medical Research and Opinion | 24 RA patients: mefenamic acid (1500 mg/day), flurbiprofen, and sulindac all significantly superior to placebo on pain score, articular index, and morning stiffness; no significant differences among active drugs |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | Comparative RCT | Journal of International Medical Research | 40 RA patients (double-blind, within-patient design): mefenamic acid and ibuprofen showed equivalent analgesic and anti-inflammatory effects; mild GI side effects similar between groups |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | Comparative RCT | Medical Journal of Australia | Double-blind crossover in RA patients on maintenance salicylates: mefenamic acid 1500 mg/day compared favourably with ibuprofen 1200 mg/day; side effects mild and predominantly gastrointestinal |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Clinical Study | Annals of the Rheumatic Diseases | Early clinical study directly evaluating mefenamic acid in rheumatoid arthritis |
| [23611159](https://pubmed.ncbi.nlm.nih.gov/23611159/) | 2014 | Formulation Study | Pharmaceutical Development and Technology | Development of time-controlled triple-concentric mefenamic acid tablet optimized for RA's morning stiffness pattern: burst release followed by 2–4 h lag then 8 h controlled release |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scottish Medical Journal | Narrative review specifically examining the place of mefenamic acid within the RA treatment landscape |
| [16223958](https://pubmed.ncbi.nlm.nih.gov/16223958/) | 2006 | Animal / In Vitro Study | Molecular Pharmacology | Mefenamic acid showed neuroprotection in Alzheimer's models; notes epidemiological observation that long-term NSAID use in RA patients correlates with reduced Alzheimer's risk, suggesting additional CNS anti-inflammatory actions |
| [20668](https://pubmed.ncbi.nlm.nih.gov/20668/) | 1977 | Review | Seminars in Arthritis and Rheumatism | Class-level review of anti-inflammatory drugs including mefenamic acid; contextualizes its position among NSAID options for arthritis |
| [10439](https://pubmed.ncbi.nlm.nih.gov/10439/) | 1976 | Single-blind Study | Journal of Rheumatology | Assessment of 10 drugs in 684 RA patients using daily pain charts; mefenamic acid evaluated among analgesic/antirheumatic agents |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Review | Clinical Pharmacy | Diclofenac review providing NSAID class-level comparator context; describes shared COX-inhibitory mechanism relevant to RA |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While three head-to-head RCTs from the 1960s–1970s confirm mefenamic acid's symptom-relief efficacy in RA, modern RA management is dominated by DMARDs and biologics — NSAIDs serve only as adjunctive therapy — and no ICH-compliant Phase 3 trial exists. Combined with zero Canadian DINs, missing MOA data, and an absent safety profile in this Evidence Pack, there is insufficient basis to advance beyond a research question at this time.

**To proceed, the following is needed:**
- Clarify the target clinical role: adjunctive symptom relief in DMARD-treated RA vs. standalone anti-inflammatory use in specific subpopulations (e.g., early RA, NSAID-naive patients)
- Obtain complete safety data, including package insert warnings, contraindications, and drug interactions (especially with methotrexate, given NSAID-associated nephrotoxicity risk)
- Retrieve mechanism of action data from DrugBank (DG002 data gap)
- Assess whether the historical RCT evidence base is sufficient for a regulatory submission or whether a new Phase 2/3 trial meeting current ICH E6(R2) GCP standards is required
- Evaluate risk of mefenamic acid–induced enteropathy (villous atrophy) for long-term RA use, as documented in case literature (PMID 29095288)
- Confirm whether a Canadian DIN application is feasible given the current not-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

