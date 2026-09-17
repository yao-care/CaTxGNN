---
layout: default
title: Levofloxacin
parent: Moderate Evidence (L3-L4)
nav_order: 462
evidence_level: L4
indication_count: 10
---

# Levofloxacin
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

Using the evidence pack, note: `predicted_indications[0]` (per the template's explicit extraction rule) is **punctate epithelial keratoconjunctivitis** — a lower-confidence entry (L4, Hold) whose lone supporting paper actually describes a *microsporidial* (non-bacterial) outbreak, not a levofloxacin-appropriate bacterial pathogen. I followed the spec literally for the required sections, then flagged the stronger candidates buried further down the list in the closing note, since omitting them would be misleading.

# Levofloxacin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibiotic originally used to treat bacterial infections. The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but currently only **1 publication** and **0 clinical trials** support this specific direction, and that publication describes a non-bacterial (microsporidial) outbreak rather than a levofloxacin-matched pathogen.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone-class antibiotic; no Taiwan/Canada license record available — drug is not currently marketed) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Levofloxacin is a fluoroquinolone antibiotic that inhibits bacterial DNA gyrase and topoisomerase IV; its efficacy against bacterial infections is well established, and mechanistically it could plausibly extend to bacterial forms of keratoconjunctivitis.

However, the only literature evidence identified for this candidate is an outbreak report of **microsporidial** keratoconjunctivitis linked to swimming-pool contamination in Taiwan. Microsporidia are eukaryotic parasites, not bacteria, and fluoroquinolones have no standard antimicrobial activity against them. This is a clear mechanism–pathogen mismatch: the literature co-occurrence appears to reflect that levofloxacin was mentioned in the context of eye infections generally, not that it treats this specific condition. The prediction should be treated as model-driven association rather than a mechanistically supported hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak Report | American Journal of Ophthalmology | Describes an outbreak of microsporidial (not bacterial) keratoconjunctivitis from contaminated swimming pools in Taiwan; levofloxacin is not the causative-pathogen-matched therapy for this condition |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level (L4) rests on a single non-bacterial outbreak report with no clinical trials, and the identified pathogen (microsporidia) does not match levofloxacin's antibacterial mechanism — this is insufficient to support advancing the candidate.

**To proceed, the following is needed:**
- Mechanism of action confirmation (currently a data gap)
- Literature specific to bacterial keratoconjunctivitis/ocular infection efficacy, not incidental co-occurrence
- TFDA/Health Canada label safety data (currently a data gap; drug is not marketed)

---

**Note on other candidates in this evidence pack:** Two of the other nine predicted indications for levofloxacin carry substantially stronger evidence than the top-ranked one above and may warrant their own evaluation:
- **Septicemic plague** (rank 9, score 99.80%) — Evidence Level **L2**, decision stage **S2**, recommendation **Proceed with Guardrails**. Levofloxacin holds actual FDA approval (2012, Animal Rule) for plague treatment/post-exposure prophylaxis, backed by 16 publications including African green monkey survival studies.
- **Monoclonal gammopathy / multiple myeloma infection prophylaxis** (rank 7, score 99.81%) — supported by 20 publications including the TEAMM Phase 3 RCT (*Lancet Oncology* 2019) on levofloxacin prophylaxis in newly diagnosed myeloma; scoring/recommendation fields are marked "pending" in this evidence pack and should be completed before a decision is made.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

