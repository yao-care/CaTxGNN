---
layout: default
title: Chromium
parent: Moderate Evidence (L3-L4)
nav_order: 188
evidence_level: L4
indication_count: 10
---

# Chromium
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

# Chromium: From Trace-Element Products (Original Indication Not Recorded) to Osteoarthritis

## One-Sentence Summary

Chromium is marketed in Canada in several "MICRO" trace-element products, but the available regulatory data does not record their approved indications.
The TxGNN model predicts it may be effective for **osteoarthritis**, but the matched **48 clinical trials** are almost all orthopedic implant studies in which chromium appears only as an alloy component or released metal ion, and there is **no supporting literature** for this specific prediction.
The high model score is best read as knowledge-graph co-occurrence, not therapeutic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available Health Canada licence data |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.68% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Chromium is a trace element, and products containing it are marketed in Canada, but no therapeutic mechanism linking it to osteoarthritis is supported by the retrieved evidence.

The trial evidence shows the opposite kind of link. In the matched studies, chromium comes from cobalt-chromium implants (hip resurfacing, total knee and hip replacement). These studies measure metal ion release or device performance in people who already have osteoarthritis. The connection is chromium exposure in osteoarthritis patients, not chromium as a treatment. The prediction is therefore probably an artefact of co-occurrence in the knowledge graph.

---

## Clinical Trial Evidence

Of the 48 matched trials, none tests chromium as a treatment for osteoarthritis. The 10 most relevant are listed below; the rest are similar device or ion-level studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01493141](https://clinicaltrials.gov/study/NCT01493141) | N/A | Completed | 46 | Systemic effects of chronic metal ion exposure from metal-on-metal hip resurfacing (safety/toxicity) |
| [NCT00962351](https://clinicaltrials.gov/study/NCT00962351) | N/A | Completed | 120 | Randomized comparison of blood and urine cobalt, chromium and titanium levels: metal-on-metal vs. metal-on-polyethylene hip |
| [NCT04585022](https://clinicaltrials.gov/study/NCT04585022) | N/A | Terminated | 75 | Randomized trial of whole-blood chromium and cobalt levels in two metal-on-metal hip designs |
| [NCT00862511](https://clinicaltrials.gov/study/NCT00862511) | N/A | Completed | 120 | Serum chromium, cobalt, molybdenum and nickel after coated vs. uncoated knee prostheses |
| [NCT03047564](https://clinicaltrials.gov/study/NCT03047564) | N/A | Completed | 120 | Metal ion concentration and clinical outcome, coated vs. uncoated total knee arthroplasty |
| [NCT00156598](https://clinicaltrials.gov/study/NCT00156598) | N/A | Terminated | 5 | Cobalt, chromium and titanium serum levels in metal-on-metal vs. metal-on-polyethylene hips |
| [NCT01437124](https://clinicaltrials.gov/study/NCT01437124) | N/A | Completed | 83 | Metal ion levels and chromosome abnormalities after ceramic-on-metal hip arthroplasty |
| [NCT00293774](https://clinicaltrials.gov/study/NCT00293774) | N/A | Completed | 1632 | Metal-on-metal hip resurfacing vs. conventional hip replacement; chromium is not the intervention |
| [NCT02154516](https://clinicaltrials.gov/study/NCT02154516) | N/A | Completed | 26 | Pilot of a hard-on-hard total hip system; chromium is an implant material |
| [NCT03382652](https://clinicaltrials.gov/study/NCT03382652) | N/A | Completed | 83 | Post-market surveillance of a metal bearing system in total hip arthroplasty |

---

## Literature Evidence

Currently no related literature available for osteoarthritis itself.

A related entry, "osteoarthritis susceptibility" (score 98.54%), returned only case reports and cohorts on adverse reactions to metal implant debris. These point to possible harm from metal release, not benefit.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00786985 | MICRO CR | — | — |
| 02091135 | MICRO +4 REGULAR STRENGTH | — | — |
| 02552787 | MICRO+6 REGULAR | — | — |
| 02507587 | MICRO+6 CONCENTRATE | — | — |
| 02091100 | MICRO PLUS 6 (PEDIATRIC) | — | — |

Six licences are recorded in total; the five main ones are shown. Dosage form and indication text are blank in the source data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For osteoarthritis, the evidence is model prediction plus device and metal-exposure studies, with no therapeutic hypothesis supported (Evidence Level L4). The high TxGNN score alone does not justify further investment.

**Noteworthy finding in a different indication:**
The same chromium prediction list shows a real signal for **rheumatoid arthritis** (score 98.54%, Evidence Level L2). Trivalent chromium was compared with baricitinib in a completed Phase 2/3 randomized trial ([NCT05545020](https://clinicaltrials.gov/study/NCT05545020), n=60; [PMID 39030450](https://pubmed.ncbi.nlm.nih.gov/39030450/), 2024), and a rat adjuvant-arthritis study supports it ([PMID 35829940](https://pubmed.ncbi.nlm.nih.gov/35829940/), 2022). Caveats: small sample, active comparator rather than placebo, and no independent replication. This is best treated as a separate research question, not as support for osteoarthritis.

**To proceed, the following is needed:**
- Original approved indications for the Canadian MICRO products (Health Canada product monographs)
- Package insert warnings and contraindications (currently blocking safety screening)
- Mechanism of action data (e.g., DrugBank)
- Full-text review of the rheumatoid arthritis trial, if that direction is pursued
- For osteoarthritis, a chromium-specific clinical or preclinical study; none is currently available

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

