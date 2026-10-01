---
layout: default
title: Mefenamic Acid
parent: Model Prediction Only (L5)
nav_order: 573
evidence_level: L5
indication_count: 8
---

# Mefenamic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Mefenamic Acid: From General NSAID Analgesia to Rheumatoid Arthritis

## One-Sentence Summary

Mefenamic acid is a non-steroidal anti-inflammatory drug (NSAID) used mainly for pain relief. The TxGNN model predicts it may be useful for **rheumatoid arthritis (RA)**. The evidence is **0 registered clinical trials** and **20 publications**, including several older double-blind trials. Its effect there is symptomatic pain and stiffness relief, not disease modification.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence record; generally used as an NSAID analgesic |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 (published double-blind trials, none registered or phase-labelled) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for mefenamic acid is not available in the input. Based on general NSAID pharmacology, it inhibits COX-1 and COX-2 and so reduces prostaglandin synthesis. Prostaglandins contribute to the pain, swelling and stiffness of inflamed joints.

RA is an inflammatory joint disease, so an anti-inflammatory analgesic can plausibly ease its symptoms. This is the same class effect seen with other NSAIDs, not a new mechanism. The prediction is reasonable, but it is closer to an established NSAID use than a true repurposing. Newer NSAIDs have largely replaced mefenamic acid for RA, and it does not slow joint damage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT (crossover) | Curr Med Res Opin | 24 patients; mefenamic acid 1500 mg/day, flurbiprofen and sulindac were all significantly better than placebo for pain, joint tenderness and morning stiffness |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT | J Int Med Res | 40 patients; mefenamic acid and ibuprofen had similar analgesic and anti-inflammatory effects and similar side effects |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | RCT (crossover) | Med J Aust | Mefenamic acid 1500 mg/day compared favourably with ibuprofen 1200 mg/day in patients on salicylates; side effects were mild and mostly gastrointestinal |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Clinical study | Ann Rheum Dis | Early clinical study of mefenamic acid in RA (no abstract available) |
| [5920657](https://pubmed.ncbi.nlm.nih.gov/5920657/) | 1966 | Clinical comparison | Br Med J | Compared mefenamic and flufenamic acids with aspirin and phenylbutazone in RA (no abstract available) |
| [6039589](https://pubmed.ncbi.nlm.nih.gov/6039589/) | 1967 | Clinical comparison | Ann Rheum Dis | Out-patient RA study comparing mefenamic and flufenamic acids with phenylbutazone and aspirin, including evaluation of assessment methods |
| [10439](https://pubmed.ncbi.nlm.nih.gov/10439/) | 1976 | Clinical comparison | J Rheumatol | Single-blind method comparing 10 antirheumatic drugs in 684 RA patients; the available excerpt gives no mefenamic acid-specific result |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scott Med J | Review of the place of mefenamic acid in RA treatment (no abstract available) |
| [29548675](https://pubmed.ncbi.nlm.nih.gov/29548675/) | 2018 | Case-crossover study | Am J Cardiol | 5,921 RA patients with stroke or heart attack; examined the cardiovascular risk of selective and non-selective NSAIDs |
| [5676955](https://pubmed.ncbi.nlm.nih.gov/5676955/) | 1968 | Safety case series | Br Med J | Three patients developed autoimmune haemolytic anaemia on mefenamic acid; all recovered after withdrawal |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2229452 | MEFENAMIC | Not specified | Not specified |

## Safety Considerations

No package insert warnings, contraindications or drug interaction records were available in the input. Please refer to the package insert for safety information.

The retrieved literature raises these signals:
- **Gastrointestinal effects:** side effects in RA trials were mostly gastrointestinal, and severe enteropathy with villous atrophy has been reported with prolonged use.
- **Haematological effects:** autoimmune haemolytic anaemia has been reported.
- **Cardiovascular risk:** the literature discusses stroke and heart attack risk with non-selective NSAIDs in RA patients.
- **Renal and headache effects:** analgesic-associated kidney disease and medication-overuse headache are reported with chronic analgesic use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RA evidence consists of small, decades-old double-blind trials showing symptom relief comparable to other NSAIDs. There are no registered trials, no disease-modifying effect, and better-established alternatives exist. Safety documentation for the Canadian product is also missing.

Other predictions look stronger. **Migraine disorder** (especially menstrual migraine) has placebo-controlled double-blind trials, and its recommendation is Proceed with Guardrails. Suggested guardrails are short perimenstrual courses with monitoring for medication-overuse headache, GI and renal toxicity, and enteropathy. Most other predictions (for example the rare developmental syndromes and trigeminal autonomic cephalalgia) have no supporting evidence and are likely knowledge-graph artefacts.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Confirmation of the approved indication and dosage form for the Canadian licence
- Evidence that mefenamic acid offers an advantage over current NSAIDs in RA

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

