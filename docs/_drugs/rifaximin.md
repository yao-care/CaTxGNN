---
layout: default
title: Rifaximin
parent: Model Prediction Only (L5)
nav_order: 800
evidence_level: L5
indication_count: 6
---

# Rifaximin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Rifaximin: From Gut-Restricted Antibacterial Use to Oral Candidiasis

## One-Sentence Summary

Rifaximin is an oral, poorly absorbed antibacterial that acts mainly in the gut. The TxGNN model predicts it may be effective for **oral candidiasis**, but there are **0 registered clinical trials** and **1 publication**, and that publication reports a possible *adverse* link between rifaximin and resistant Candida infections. The prediction is not supported by current evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence record (rifaximin is a gut-restricted oral antibiotic) |
| Predicted New Indication | Oral candidiasis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L4 (one cohort study, which signals risk rather than benefit) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Rifaximin is an oral, non-absorbable antibiotic that works against bacteria in the gut. It has no known antifungal activity.

Oral candidiasis is a fungal infection of the mouth, so rifaximin's antibacterial mechanism does not fit it. The very high TxGNN score (0.997) most likely reflects closeness to oral-disease nodes in the knowledge graph rather than a real therapeutic link.

The only publication points the opposite way. In allogeneic stem cell transplant recipients, rifaximin exposure was associated with infections by micafungin-resistant Candida species. A plausible explanation is disruption of the gut microbiota. This is a safety signal, not support for repurposing.

The other top predictions (commissural lip fistula, osteoradionecrosis of the mandible, oral leukoedema, burning mouth syndrome) also have no plausible mechanism and no clinical evidence. They look like knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | Cohort | Annals of Hematology | In allogeneic stem cell transplant recipients, rifaximin prophylaxis (given to reduce gut bacterial infections and graft-versus-host disease) was linked to infections by micafungin-resistant Candida species. |

A related candidiasis prediction (rank 6) also cites a multicentre case-control study of candidaemia risk factors in hospitalized patients with liver cirrhosis ([PMID 32360775](https://pubmed.ncbi.nlm.nih.gov/32360775/), 2021). Whether rifaximin was a significant factor is unclear and needs full-text review.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2410702 | ZAXINE | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

The published cohort suggests that rifaximin use may favour resistant Candida infections in immunocompromised transplant patients. This should be treated as a risk to evaluate, not as evidence of benefit.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Rifaximin has no known antifungal activity, and no trials support oral candidiasis. The only literature suggests a harmful association. The high model score is likely a graph artifact.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications
- Mechanism of action data, to confirm there is no antifungal activity
- Full-text review of PMID 34180023 and PMID 32360775 to assess the Candida resistance risk
- Any in vitro or clinical evidence of antifungal or anti-oral-candidiasis effect, before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

