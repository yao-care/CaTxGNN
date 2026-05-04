---
layout: default
title: Chromium
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Chromium
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

# Chromium: From Trace Element to Osteoarthritis

## One-Sentence Summary

Chromium (DB11136) is an essential trace mineral with no formally approved drug indication, historically studied as a nutritional supplement involved in insulin signaling and glucose metabolism.
The TxGNN model assigns its highest prediction score to **Osteoarthritis** (98.68%); however, all retrieved clinical evidence relates to chromium as a component of orthopedic implant alloys — not as a therapeutic drug — making this prediction likely a knowledge graph artifact rather than a genuine therapeutic signal.
There are **no therapeutic clinical trials** and **no literature** directly supporting chromium supplementation for osteoarthritis.

> **Analyst Note**: The most actionable finding in this Evidence Pack is **Rheumatoid Arthritis** (rank 3, 98.54%), which has a completed Phase 2/3 RCT (NCT05545020) and pre-clinical mechanistic data for trivalent chromium (Cr³⁺) as an anti-inflammatory agent. A separate "Proceed with Guardrails" evaluation for RA is recommended.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved drug indication (essential trace element) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.68% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Chromium as a pharmacological agent is currently unavailable. Based on established biochemistry, trivalent chromium (Cr³⁺) — the biologically active, nutritionally essential form — enhances insulin receptor sensitivity by potentiating tyrosine kinase activity, thereby improving cellular glucose uptake. It has also been proposed to suppress NF-κB–mediated inflammatory signaling, reduce circulating pro-inflammatory cytokines (TNF-α, IL-6), and modulate immune cell activity. These properties are broadly relevant to joint diseases where systemic low-grade inflammation plays a pathogenic role.

However, the specific high TxGNN score for osteoarthritis (rank 1) is almost certainly driven by an **indirect knowledge graph association** rather than a direct therapeutic relationship. The most plausible pathway is: *OA → orthopedic joint replacement surgery → cobalt-chromium (CoCr) implant alloys → chromium ion release*. This makes chromium appear connected to OA in the graph, but in that context chromium is a byproduct of implant wear — a monitored exposure concern — not a treatment. All 48 clinical trials retrieved for this query involve CoCr alloy implants used in total hip or knee arthroplasty, and none test chromium as a therapeutic intervention.

The situation is meaningfully different for **Rheumatoid Arthritis** (rank 3), where direct therapeutic evidence does exist: a completed Phase 2/3 RCT (NCT05545020; published as PMID 39030450) compared trivalent chromium against baricitinib in RA patients; a rat adjuvant model showed Cr³⁺ suppresses joint inflammation via FOXP3 upregulation and Cathepsin G inhibition (PMID 35829940); and observational studies from 1975–1986 found that RA patients have significantly lower serum chromium levels than healthy controls (PMIDs 1153978, 3776595), supporting a deficiency hypothesis. For osteoarthritis, no comparable signal exists.

---

## Clinical Trial Evidence

> ⚠️ All trials retrieved for Chromium + Osteoarthritis involve **chromium as a component of cobalt-chromium orthopedic implants**, not as a therapeutic agent. These trials monitor metal ion safety and device performance. They are listed for transparency but do not constitute evidence for chromium supplementation in OA treatment.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT01493141](https://clinicaltrials.gov/study/NCT01493141) | N/A | Completed | 46 | Monitored systemic Cr and Co ion levels from metal-on-metal hip resurfacing in OA patients; chromium is the exposure source under investigation, not a treatment. |
| [NCT00293774](https://clinicaltrials.gov/study/NCT00293774) | N/A | Completed | 1,632 | Large provincial RCT comparing metal-on-metal hip resurfacing vs. conventional total hip replacement for degenerative hip disease; long-term safety and effectiveness data collected over 17 years. |
| [NCT00962351](https://clinicaltrials.gov/study/NCT00962351) | N/A | Completed | 120 | Multi-center RCT comparing blood and urine Cr/Co/Ti ion levels across metal-on-metal vs. metal-on-polyethylene hip bearing surfaces. |
| [NCT01336595](https://clinicaltrials.gov/study/NCT01336595) | Phase 4 | Completed | 331 | Double-blind RCT comparing oxidized zirconium vs. cobalt-chromium femoral components in total knee arthroplasty; CoCr serves as the standard comparator. |
| [NCT00862511](https://clinicaltrials.gov/study/NCT00862511) | N/A | Completed | 120 | Randomized comparison of serum Cr, Co, Mo, and Ni levels between coated and uncoated total knee prostheses to assess passivation surface effectiveness. |
| [NCT02154516](https://clinicaltrials.gov/study/NCT02154516) | N/A | Completed | 26 | Pilot study of hard-on-hard total hip replacement (R3 ODH-ODH) safety and efficacy vs. metal-on-polyethylene control in non-inflammatory arthritis; 11-year follow-up. |
| [NCT03382652](https://clinicaltrials.gov/study/NCT03382652) | N/A | Completed | 83 | Multi-center prospective post-market surveillance of the Continuum Metal Bearing System in primary total hip arthroplasty; survival and outcomes data. |
| [NCT04585022](https://clinicaltrials.gov/study/NCT04585022) | N/A | Terminated | 75 | RCT comparing whole-blood Cr and Co concentrations in metal-on-metal THA vs. hip resurfacing at 5-year follow-up; terminated. |
| [NCT06578897](https://clinicaltrials.gov/study/NCT06578897) | N/A | Completed | 118 | Retrospective outcomes study of revision TKA using Medacta GMK Revision with 3D metal tibial and femoral cones; post-market clinical follow-up. |
| [NCT00759993](https://clinicaltrials.gov/study/NCT00759993) | Phase 2 | Terminated | 60 | The only trial using chromium as a therapeutic agent: chromium picolinate supplementation to prevent serotonergic medication–induced weight gain in psychiatric inpatients. Not related to OA; terminated early. |

---

## Literature Evidence

Currently no related literature available for therapeutic chromium in osteoarthritis.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical note on valence state**: Chromium's safety profile differs fundamentally by oxidation state. **Trivalent chromium (Cr³⁺)** — the nutritionally active form used in supplements (picolinate, nicotinate, chloride) — has a generally favorable safety profile at dietary doses. **Hexavalent chromium (Cr⁶⁺)** is a Group 1 carcinogen (IARC classification) and acutely toxic. Any therapeutic development program must explicitly specify, characterize, and verify the Cr³⁺ formulation; inadvertent Cr⁶⁺ contamination would be a disqualifying safety concern.

---

## Conclusion and Next Steps

**Decision: Hold** (for Osteoarthritis)

**Rationale:**
The TxGNN rank 1 prediction for osteoarthritis (98.68%) is most likely a knowledge graph artifact driven by the structural association between OA, orthopedic joint replacement, and cobalt-chromium implant alloys — not a genuine therapeutic signal. No clinical trials test chromium supplementation as a treatment for OA, no supporting literature was identified, and no plausible direct mechanistic pathway links chromium to OA pathophysiology beyond the general anti-inflammatory properties shared with other joint diseases. Investment in pursuing chromium for OA is not justified at this stage.

**Recommended pivot: Rheumatoid Arthritis (rank 3) should be evaluated as the priority indication**, with a separate "Proceed with Guardrails" review:

- A completed Phase 2/3 RCT (NCT05545020, n=60) compared trivalent chromium directly against baricitinib in RA patients, with published results (PMID 39030450, *Inflammopharmacology*, 2024)
- Pre-clinical evidence shows Cr³⁺ suppresses adjuvant-induced RA in rats via FOXP3 upregulation and Cathepsin G inhibition (PMID 35829940)
- RA patients have documented lower serum chromium vs. healthy controls, supporting a deficiency-correction mechanism (PMIDs 1153978, 3776595)
- Mechanistic plausibility: insulin sensitization reduces systemic inflammation; NF-κB suppression reduces TNF-α and IL-6

**To advance the RA pathway, the following is needed:**

- Critical appraisal of NCT05545020 full results: enrollment criteria, blinding adequacy, primary endpoints, effect sizes, and adverse event profile
- Independent multi-center replication — the published RCT appears to originate from a single research group; external validation is essential before drawing firm conclusions
- Formulation and dose optimization: which Cr³⁺ salt (picolinate vs. chloride vs. nicotinate)? Optimal dose and duration for anti-inflammatory effect?
- Long-term safety data for supranutritional Cr³⁺ dosing, particularly renal excretion and accumulation
- Health Canada regulatory pathway consultation: classification of chromium as an investigational therapeutic vs. natural health product, and implications for IND filing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

