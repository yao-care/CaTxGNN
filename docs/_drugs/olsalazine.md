---
layout: default
title: Olsalazine
parent: Model Prediction Only (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
---

# Olsalazine
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

# Olsalazine: From Ulcerative Colitis to Myelodysplastic Syndrome

## One-Sentence Summary

Olsalazine is a 5-ASA (mesalazine) azo-bonded prodrug clinically used for ulcerative colitis. The TxGNN model assigns a very high prediction score (**99.91%**) for **Myelodysplastic Syndrome**, but currently **0 clinical trials** and **0 publications** support this direction, and the evidence pack itself flags this as a likely knowledge-graph clustering artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative Colitis (based on known pharmacology; not confirmed via Canada regulatory filing — drug is unlicensed there) |
| Predicted New Indication | Myelodysplastic Syndrome |
| TxGNN Prediction Score | 99.91% (rank 2251) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Olsalazine is a dimeric prodrug of 5-aminosalicylic acid (5-ASA/mesalazine); after bacterial cleavage in the colon it acts locally to suppress prostaglandin and leukotriene synthesis, an anti-inflammatory effect established for ulcerative colitis.

There is no known mechanistic pathway linking this colon-localized anti-inflammatory action to myelodysplastic syndrome, which is driven by clonal hematopoietic stem cell abnormalities and epigenetic/somatic mutations. The repurposing rationale supplied with this candidate explicitly notes that the high TxGNN score coincides with MDS-family disease nodes clustering near each other in the knowledge graph (e.g., unclassified MDS, 5q- syndrome/partial deletion of chromosome 5q, refractory cytopenia of childhood, ringed sideroblast anemia — ranks 2251–3081, all with identical L5/Hold status), and it is flagged as a probable false-positive signal from hub-node clustering rather than a biologically grounded connection.

Similarly, several other top-10 predictions for this drug (alopecia, diffuse alopecia areata, hypotrichosis simplex, congenital hypotrichosis milia) form a second unrelated disease cluster (hair/follicle disorders) with the same score profile and same lack of supporting evidence — reinforcing that these are graph-proximity effects rather than independently validated repurposing hypotheses.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Olsalazine currently holds no Canadian market authorization (0 DINs on file); no product listings are available for this drug in the supplied regulatory data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction sits at evidence level L5 — a model score only, with zero supporting clinical trials or literature across all queried sources (ClinicalTrials.gov, ICTRP, PubMed). The rationale text accompanying this candidate itself identifies the signal as likely arising from disease-node clustering in the knowledge graph rather than a real mechanistic link, and the drug has no Canadian market presence to support a safety baseline.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for Olsalazine (currently a Blocking data gap)
- TFDA/Health Canada label warnings and contraindications (currently a Blocking data gap, required before any S1 safety screening)
- Preclinical or mechanistic studies directly linking 5-ASA compounds to myelodysplastic syndrome pathophysiology, to distinguish true signal from graph-clustering artifact
- If pursued, an independent literature/trial search specifically for 5-ASA class effects on bone marrow/hematopoietic stem cells
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

