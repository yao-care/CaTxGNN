---
layout: default
title: Cidofovir
parent: Model Prediction Only (L5)
nav_order: 190
evidence_level: L5
indication_count: 4
---

# Cidofovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Cidofovir: From Antiviral Therapy (CMV Retinitis) to Sclerosing Cholangitis

## One-Sentence Summary

Cidofovir is a nucleotide-analog antiviral, generally used against cytomegalovirus (CMV) infections. The Health Canada license record supplied here does not list an approved indication.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Health Canada license data (cidofovir is generally known as a CMV antiviral) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Cidofovir is a nucleotide analog that inhibits viral DNA polymerase, and it is an antiviral, not an anti-inflammatory or immunomodulatory drug.

No plausible antiviral target is evident in sclerosing cholangitis, a chronic inflammatory and fibrosing disease of the bile ducts. The link between cidofovir's antiviral use and this new indication is therefore unclear, and no supporting mechanism was found.

The score of 99.94% (model rank 1654) is a knowledge-graph output only. It should be read as a hypothesis-generating signal, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2473925 | MAR-CIDOFOVIR | Not specified | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no plausible mechanistic link, so it stays at evidence level L5 (model prediction only). Safety information from the Canadian product monograph has not been reviewed.

Other predictions for this drug (rheumatoid arthritis, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome) are also unsupported. The rheumatoid arthritis literature hits concern CMV in transplant patients, retinal toxicity and warts. Most appear to be keyword co-occurrence, not evidence for cidofovir.

**To proceed, the following is needed:**
- Health Canada product monograph (warnings, contraindications, approved indication) for safety screening
- Mechanism of action data, for example from DrugBank
- A biologically plausible hypothesis linking cidofovir to sclerosing cholangitis, supported by preclinical or mechanistic studies
- Route and dosage form compatibility assessment for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

