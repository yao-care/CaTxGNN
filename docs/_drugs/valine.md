---
layout: default
title: Valine
parent: Moderate Evidence (L3-L4)
nav_order: 816
evidence_level: L4
indication_count: 10
---

# Valine
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

# Valine: From Nutritional Supplementation to Sclerosing Cholangitis

## One-Sentence Summary

> Valine is an essential branched-chain amino acid (BCAA) with no disease-specific approved indication on file — it functions primarily as a nutritional/parenteral component rather than a conventional therapeutic drug.
> The TxGNN model predicts it may be relevant to **Sclerosing Cholangitis**,
> but this is currently supported only by **0 clinical trials** and **2 indirect observational/genetic-association publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file (Valine is an essential BCAA, used nutritionally/in parenteral formulations, not marketed with a disease-specific label) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (marked as a High-severity data gap). Based on known pharmacology, Valine is an essential branched-chain amino acid involved in protein synthesis and energy metabolism; it is not a single-indication therapeutic agent, so there is no established original MOA to anchor a mechanistic rationale for this prediction.

The link to sclerosing cholangitis in the supporting literature is indirect: one paper (PMID 39015781) uses Mendelian randomization to explore causal relationships between blood metabolites — including amino acid pathways — and cholestatic liver diseases (PBC/PSC), and the other (PMID 15790420) studies plasma tyrosine and fatigue in PBC/PSC patients, which does not directly implicate Valine. Both are exploratory epidemiological or metabolomic association studies rather than direct evidence that Valine (or BCAA supplementation) affects the disease course of sclerosing cholangitis.

A further caution: across the other predicted indications for Valine in this evidence pack (e.g., angle-closure glaucoma, hyperthyroidism, thyroid hormone resistance), the majority of "supporting" literature turned out to be naming artifacts — papers describing amino acid substitution mutations (e.g., "V509A," "L341V") where "Val" refers to a mutated residue, not the drug Valine. This pattern raises the possibility that even the top-ranked sclerosing cholangitis prediction may partly reflect text-mining noise in the underlying knowledge graph rather than a genuine pharmacological signal, and should be interpreted with corresponding caution.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Mendelian randomization | Frontiers in Medicine | Explores causal relationships between blood metabolites/metabolic pathways and cholestatic liver diseases (PBC/PSC); indirect metabolomic association, not direct Valine intervention evidence |
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examines plasma tyrosine (not valine) and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis patients |

## Canada Market Information

No Canadian marketing authorization (DIN) is currently on file for Valine; market status is recorded as **Not Marketed**, with 0 total licenses.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by two indirect observational/genetic-association studies with no clinical trials, no confirmed mechanism of action, and no marketing authorization for Valine in Canada. Given that other predicted indications for this drug were traced to amino-acid-mutation naming artifacts in the source literature, this signal cannot yet be distinguished from data/model noise.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank or another authoritative source (currently a blocking data gap)
- Manual review confirming the sclerosing cholangitis literature signal is not itself a naming-artifact false positive, similar to those found in this drug's other predictions
- Dedicated preclinical or clinical evidence testing Valine/BCAA supplementation specifically in PBC/PSC patients
- Package insert/regulatory safety data (warnings, contraindications, drug interactions), which are currently unavailable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

