---
layout: default
title: Isosorbide Mononitrate
parent: Model Prediction Only (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Isosorbide Mononitrate: Original indication data gap → Hypertrichosis

## One-sentence summary

Isosorbide mononitrate is a NO donor/vasodilator (inferred from mechanistic descriptions of various candidates in the evidence bundle), but this evidence bundle does not provide its formally approved indications and Canadian market information (the drug is currently **not marketed in Canada**, 0 DINs). The TxGNN model identified **Hypertrichosis** as the candidate indication with the highest prediction score (99.99%), but there is currently **no clinical trial or literature evidence to support it**. The evidence bundle itself also notes that this score merely reflects the statistical similarity of knowledge graph embeddings, not pharmacological reasoning.

---

## Quick overview

| Item | Content |
|------|---------|
| Original indication | Data gap (not provided in this evidence bundle; no marketing record in Canada available to substantiate) |
| Predicted new indication | Hypertrichosis |
| TxGNN prediction score | 99.995% (ranked 194) |
| Evidence level | L5 (model prediction only, no actual research) |
| Canadian market status | Not marketed |
| DIN count | 0 |
| Recommended decision | Hold |

---

## Why is this prediction reasonable?

This evidence bundle does not include the formal mechanism of action description for isosorbide mononitrate (DG002, High severity). However, the pharmacological background can be reconstructed from the mechanistic descriptions of candidate items: isosorbide mononitrate belongs to the nitrate class of NO donors, which causes vascular smooth muscle relaxation through the NO-sGC-cGMP pathway. Clinically, drugs of this class are predominantly used for vascular-related indications such as angina pectoris and portal hypertension (see descriptions of other candidates in the evidence bundle, such as studies on portal pressure in liver cirrhosis: PMID 3384359, 2759546).

As for Hypertrichosis, the evidence bundle's `repurposing_rationale` explicitly states: "No known mechanism: Isosorbide mononitrate is a NO donor/vasodilator with no known association with the pathophysiology of excessive hair growth; this score merely reflects the statistical similarity of TxGNN graph embeddings, not pharmacological reasoning." In other words, this is a candidate ranked high in the knowledge graph but **lacking rational pharmacological connection**, which should be regarded as a noise candidate requiring manual exclusion rather than a priority development direction.

It is noteworthy that among the same batch of candidates, **Pulmonary arterial hypertension** ranked 10th possesses evidence strength far exceeding the present candidate (L4/S1/Research Question), as its NO-sGC-cGMP pathway is directly relevant to PAH pathophysiology and is supported by 6 related publications (including animal models and mechanistic studies). If one were to select a subsequent research direction among the predicted candidates for this drug, PAH would be a more worthwhile target than Hypertrichosis, though one must remain mindful of the serious hypotension contraindication when used in combination with PDE5 inhibitors.

---

## Clinical trial evidence

Currently, there are no registered clinical trials available (search results for Hypertrichosis-related trials: 0 hits, including ClinicalTrials.gov and ICTRP).

---

## Literature evidence

Currently, there is no relevant literature (PubMed search for isosorbide mononitrate + hypertrichosis yielded 0 results).

---

## Canadian market information

Isosorbide mononitrate is currently not marketed in Canada, with no DIN authorization records available.

---

## Safety considerations

Refer to the drug package insert for safety information (warnings, contraindications, and drug-drug interactions in this evidence bundle are all data gaps; DG001 is a Blocking-level issue that will block entry into S1 safety initial assessment).

---

## Conclusions and next steps

**Decision: Hold**

**Rationale:**
Although the TxGNN score is high (99.995%), the evidence bundle itself has explicitly labeled this as knowledge graph statistical similarity noise, lacking any clinical trial, literature, or mechanistic reasonableness support (L5/S0); moreover, the drug is not marketed in Canada and safety data has blocking-level gaps, making it unsuitable for advancement at this stage.

**If advancement is desired, the following must be supplied:**
- TFDA/Health Canada package insert warnings and contraindications data (DG001, Blocking, blocking S1 safety initial assessment)
- Complete mechanism of action (MOA) data for isosorbide mononitrate (DG002)
- To verify the Hypertrichosis direction: any in vitro/animal-level mechanistic reasonableness data must first be obtained; currently completely lacking
- It is recommended to separately evaluate candidate items with higher evidence levels from the same batch (Pulmonary arterial hypertension, L4/S1), where the mechanistic association is clear and preliminary literature evidence already exists

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

