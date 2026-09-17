---
layout: default
title: Yellow Fever Vaccine
parent: Moderate Evidence (L3-L4)
nav_order: 834
evidence_level: L4
indication_count: 10
---

# Yellow Fever Vaccine
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

# Yellow Fever Vaccine: From Yellow Fever Prevention to Plasma Cell Myeloma

## One-Sentence Summary

> Yellow Fever Vaccine is a live attenuated viral vaccine used to prevent yellow fever infection; it has no approved therapeutic indication.
> The TxGNN model predicts it may be effective for **Plasma Cell Myeloma**,
> but this candidate is supported by only **1 case report** and **0 clinical trials**, and the underlying evidence pack itself flags this prediction as mechanistically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of yellow fever infection (prophylactic vaccine) — no structured indication text available; drug is not currently marketed in Canada |
| Predicted New Indication | Plasma Cell Myeloma |
| TxGNN Prediction Score | 97.98% |
| Evidence Level | L4 |
| Canada Market Status | ✗ Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, Yellow Fever Vaccine is a live attenuated viral vaccine (strain 17D) that induces adaptive immunity against the yellow fever Flavivirus. It has no established pharmacological pathway related to plasma cell biology, immunoglobulin production, or antineoplastic activity, and no class of vaccines is currently recognized as a treatment for multiple myeloma.

The single supporting publication (PMID 15089771) describes a bone marrow transplant recipient with myeloma who was **safely vaccinated** against yellow fever post-transplant — this is evidence about **vaccine safety in an immunocompromised host**, not evidence that the vaccine treats myeloma. The evidence direction is therefore inverted relative to what a repurposing candidate requires.

Given the high TxGNN score paired with the complete absence of mechanistic or interventional evidence, this prediction is most plausibly explained as an embedding-based similarity artifact (e.g., co-occurrence of "myeloma" and "vaccine" in immunocompromised-host safety literature) rather than a genuine therapeutic signal. This pattern also recurs across several other top-ranked TxGNN predictions for this drug (e.g., indolent plasma cell myeloma, ranked #2, has zero supporting evidence at all), reinforcing that these high scores should not be interpreted as repurposing leads without independent mechanistic validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Plasma Cell Myeloma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15089771](https://pubmed.ncbi.nlm.nih.gov/15089771/) | 2004 | Case Report | European Journal of Haematology | Describes safe administration of the live attenuated 17D yellow fever vaccine in a myeloma patient 2.5 years post-bone marrow transplant; reports on vaccine tolerability, not anti-myeloma efficacy |

---

## Canada Market Information

Yellow Fever Vaccine is not currently marketed in Canada under this evidence pack — no DIN-listed products or licenses were found.

---

## Safety Considerations

Please refer to the package insert for safety information. A blocking data gap exists: product label warnings and contraindications for this drug have not yet been obtained, which precludes a complete safety assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is numerically high, but there is no mechanistic rationale, no clinical trial evidence, and the single available publication addresses vaccine safety in myeloma patients rather than any therapeutic effect on myeloma itself. Combined with a blocking gap in product label safety data, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- Product label warnings/contraindications (DG001, Blocking) — required before any safety-stage review
- Mechanism of action data from DrugBank (DG002, High) — required to assess mechanistic plausibility
- Independent preclinical or mechanistic evidence directly linking yellow fever vaccination (or its immune pathway) to anti-myeloma activity, since none currently exists
- A review of whether this and the other top-ranked predictions for this drug (all similarly unsupported) reflect a systematic embedding artifact rather than genuine repurposing signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

