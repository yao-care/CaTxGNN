---
layout: default
title: Inosine Pranobex
parent: Model Prediction Only (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Inosine Pranobex: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Inosine pranobex"
predicted_indications: ["osteoarthritis", "osteoarthritis susceptibility", "rheumatoid arthritis", "hepatic porphyria", "pseudoachondroplasia", "gout", "hepatoportal sclerosis", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension"]
---

# Inosine Pranobex
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

# Inosine Pranobex: From an Unspecified Original Indication to Osteoarthritis

## One-Sentence Summary

Inosine pranobex is an immunomodulator with reported antiviral activity. It is marketed in Canada, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **osteoarthritis** with a high score (98.1%), but **no clinical trials and no publications** support this prediction.
The only direct human evidence in the data is for a neighbouring indication, **rheumatoid arthritis**: one randomised, placebo-controlled trial from 1990 and one background review.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.09% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, inosine pranobex is described as an immunomodulator that is reported to enhance T-lymphocyte function and modulate cytokine production, and it has reported antiviral activity. Its original indication could not be confirmed from the Canadian licence data.

Osteoarthritis is a degenerative joint disease with an inflammatory component. In principle, immune modulation could be relevant. However, no mechanistic link between this drug and osteoarthritis can be established from the supplied data. The high score is most likely driven by proximity in the knowledge graph to other arthritis indications, not by indication-specific evidence.

Other predicted indications show the same pattern. Osteoarthritis susceptibility, hepatic porphyria, pseudoachondroplasia, and several rare liver diseases all have no supporting studies. Several rare liver conditions share an identical score of 0.9704, which suggests a non-specific graph artifact.

**Rheumatoid arthritis (score 97.7%)** is the most plausible prediction in the list. Immunomodulation is biologically plausible here, and a randomised trial exists (see below).

**Gout (score 97.1%)** raises a concern. Inosine pranobex contains inosine, a purine, and is known to raise serum uric acid. This suggests potential harm rather than benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for osteoarthritis.

---

## Literature Evidence

No literature is available for osteoarthritis. The table below shows the literature found for the next-most-plausible prediction, rheumatoid arthritis, as context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1693065](https://pubmed.ncbi.nlm.nih.gov/1693065/) | 1990 | RCT | Annals of the Rheumatic Diseases | Randomised, double-blind, placebo-controlled study of inosine pranobex (3 g/day) as a possible second-line drug in rheumatoid arthritis: 24 patients on the drug vs 26 on placebo for up to 24 weeks. Outcomes included morning stiffness, articular index, grip strength, pain, ESR, CRP, IgG, IgM and serum urate. The available abstract is truncated, so the results are not verified. |
| [1715732](https://pubmed.ncbi.nlm.nih.gov/1715732/) | 1991 | Review | Current Opinion in Rheumatology | Review of immunotherapies and other novel therapies potentially applicable to rheumatoid arthritis. Background only. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02240713 | IMUNOVIR | Not available | Not available |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the query.
- **Gout-related concern**: The drug is known to raise serum uric acid, which argues against use in gout and warrants caution in patients with hyperuricaemia.

Please refer to the package insert for warnings and contraindications, because this information was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction rests only on a high model score, with no clinical trials, no publications, and no identifiable mechanistic link. The evidence level is L5. The rheumatoid arthritis prediction has a direct RCT but an unverified outcome, so it is better treated as a research question than as a ready candidate.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert to obtain the approved indication, dosage form, warnings and contraindications. This is a blocking gap for safety screening.
- Obtain mechanism of action data for inosine pranobex (for example, from DrugBank).
- Retrieve the full text of the 1990 rheumatoid arthritis RCT (PMID 1693065) to determine efficacy and safety results.
- Search for any osteoarthritis-specific preclinical or clinical studies before further consideration.
- Assess the effect on serum uric acid before considering any joint or rheumatic indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

