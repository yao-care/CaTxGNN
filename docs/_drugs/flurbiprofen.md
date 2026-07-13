---
layout: default
title: Flurbiprofen
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: From Inflammatory Rheumatic Disease to Ankylosing Spondylitis

## One-Sentence Summary

Flurbiprofen is a propionic acid-derived non-steroidal anti-inflammatory drug (NSAID), established in multiple markets for the treatment of rheumatoid arthritis, osteoarthritis, and related inflammatory joint conditions, though currently not marketed in Canada.
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis (AS)**, with **0 registered clinical trials** and **20 publications** currently supporting this direction — including 4 randomized controlled trials directly evaluating flurbiprofen in AS patients.
Evidence is sufficient to support a structured repurposing evaluation, provided safety data gaps are addressed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, and inflammatory musculoskeletal conditions (established in other markets) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Flurbiprofen is a propionic acid-class NSAID that inhibits both COX-1 and COX-2 enzymes, suppressing the synthesis of prostaglandins — particularly prostaglandin E2 (PGE2). Detailed MOA data is not available from the current Evidence Pack, but based on pharmacological literature included in the evidence review, preclinical studies indicate flurbiprofen is at least as potent as indomethacin and approximately 200 times more potent than aspirin as an anti-inflammatory agent. It exhibits analgesic, anti-inflammatory, and antipyretic activities.

Ankylosing spondylitis (AS) is a chronic inflammatory arthritis primarily affecting the axial skeleton, with HLA-B27-related enthesitis at sacroiliac joints and spinal attachment sites as its pathological hallmark. PGE2 is a critical downstream mediator of the IL-6 and TNF-α inflammatory cascade in AS, driving morning stiffness, spinal pain, and nocturnal pain. NSAIDs are endorsed as first-line pharmacological therapy in AS by the ASAS (Assessment of SpondyloArthritis international Society) international guidelines, and some evidence suggests prolonged NSAID use may slow radiographic progression.

This prediction is strongly mechanistically supported: flurbiprofen's COX-1/COX-2 dual inhibition directly targets the prostaglandin pathways central to AS pathology. More importantly, this is not a theoretical class-effect extrapolation — multiple randomized controlled trials conducted from 1974 to 1986 specifically enrolled AS patients and directly compared flurbiprofen against then-standard treatments including indomethacin, phenylbutazone, and naproxen, consistently demonstrating comparable efficacy. The TxGNN high-rank prediction (99.97%) likely reflects the topological proximity between flurbiprofen's pharmacological network and AS disease nodes, which in this case aligns well with real clinical trial data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for flurbiprofen in ankylosing spondylitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | RCT (double-blind crossover) | British Medical Journal | Flurbiprofen 150 mg/day vs phenylbutazone 300 mg/day in 35 AS patients over 4 weeks; flurbiprofen demonstrated therapeutic efficacy approaching phenylbutazone and was well tolerated, suggesting it as a valuable alternative |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | RCT (double-blind crossover) | New Zealand Medical Journal | Flurbiprofen 200 mg/day vs naproxen 750 mg/day in 30 AS patients over 4 weeks; both equally effective in alleviating pain and stiffness; side effects more frequent with flurbiprofen |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT (comparative) | American Journal of Medicine | Flurbiprofen 200 mg/day vs indomethacin in 57 AS patients over 26 weeks; flurbiprofen as effective as indomethacin, with adequate symptom control achievable at 100 mg/day in some patients |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT (comparative) | American Journal of Medicine | Flurbiprofen 200 mg/day vs phenylbutazone 300 mg/day in 90 AS patients over 26 weeks; equivalent efficacy; some patients adequately managed on 150 mg/day |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | Comparative clinical trial | Current Medical Research and Opinion | Flurbiprofen 150–200 mg/day vs indomethacin 75–100 mg/day in 26 active AS patients over 6 weeks; both equally effective for pain and joint tenderness; no withdrawals due to lack of efficacy in either group |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | Comparative clinical trial | Southern Medical Journal | Parallel double-blind RCT of flurbiprofen vs indomethacin in 26 active AS patients over 6 weeks; comparable pain and tenderness relief; overall subjective improvement similar between groups |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | Comparative clinical trial | European Journal of Clinical Pharmacology | Flurbiprofen 150–200 mg/day vs phenylbutazone 300–400 mg/day in 27 AS patients over 6 weeks; both equally effective; overall patient preference slightly favored phenylbutazone but not statistically significant |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Systematic review | Drugs | Comprehensive pharmacological review: flurbiprofen 150–300 mg/day is comparable to aspirin, indomethacin, and naproxen for RA, osteoarthritis, and AS; generally fewer side effects than aspirin at equivalent doses |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Safety study (pooled Phase III data) | American Journal of Medicine | Pooled kidney and liver function data from 9 Phase III trials (1,677 patients including AS, OA, RA cohorts; 941 on flurbiprofen); no clinically significant hepatic or renal effects identified |
| [3514311](https://pubmed.ncbi.nlm.nih.gov/3514311/) | 1986 | Open-label long-term study | Journal of International Medical Research | 336 patients with AS, psoriatic arthropathy, and related articular conditions followed over 12 months; significant pain improvement from week 2 onward sustained throughout the study period |

---

## Canada Market Information

Flurbiprofen is currently not marketed in Canada. No Drug Identification Numbers (DINs) are on file with Health Canada.

---

## Safety Considerations

Please refer to the package insert for safety information. No safety data (warnings, contraindications, or drug interactions) was retrieved in this Evidence Pack cycle for the Canadian market context.

> **Note for reviewers:** Two blocking data gaps were identified: (1) Canadian regulatory labelling (warnings and contraindications) has not been retrieved — this must be resolved before any safety assessment can proceed; (2) MOA data from DrugBank was not successfully extracted, limiting mechanistic depth in this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Four randomized controlled trials directly confirm flurbiprofen's efficacy in ankylosing spondylitis, consistently demonstrating equivalence to established first-line NSAIDs (indomethacin, naproxen, phenylbutazone). The COX-1/COX-2 inhibition mechanism is directly and specifically applicable to AS pathophysiology, and NSAID therapy remains the guideline-endorsed first-line treatment per ASAS international recommendations. However, the absence of Health Canada safety labelling data is a blocking gap that prevents formal safety clearance.

**To proceed, the following is needed:**

- Retrieve Health Canada (or equivalent regulatory authority) package insert for warnings, contraindications, and special population considerations
- Complete DrugBank MOA extraction to enable formal mechanistic analysis
- Conduct drug-drug interaction screening specific to common AS co-medications (biologics, DMARDs, corticosteroids)
- Evaluate cardiovascular and gastrointestinal risk profile given known NSAID class effects — particularly relevant given the chronic, long-term nature of AS treatment
- Review whether an existing Health Canada DIN pathway or Notice of Compliance would apply for an AS indication, or whether a new submission is required
- Consider updated evidence search (current trials post-2000) to supplement the historical 1970s–1980s RCT base with contemporary data on NSAID use in AS
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

