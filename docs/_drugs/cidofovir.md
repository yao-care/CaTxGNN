---
layout: default
title: Cidofovir
parent: Model Prediction Only (L5)
nav_order: 192
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Cidofovir: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not specified in the Canadian licence data compiled for this report"
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

# Cidofovir: From Antiviral Therapy to Sclerosing Cholangitis

## One-Sentence Summary

Cidofovir is a nucleotide-analog antiviral that inhibits viral DNA polymerase and has a single marketed product in Canada. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, with a very high score. However, **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the Canadian licence data compiled for this report |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for cidofovir is not available in the data compiled for this report. Based on general knowledge, cidofovir is a nucleotide analog that inhibits DNA polymerase in cytomegalovirus (CMV) and other DNA viruses.

A possible indirect link is AIDS-related or CMV-associated cholangiopathy, which can present as secondary sclerosing cholangitis. This is speculative and is not supported by the supplied data. Primary sclerosing cholangitis is largely immune-mediated, so an antiviral mechanism is not an obvious fit. The high TxGNN score reflects patterns in a knowledge graph and should not be read as evidence of efficacy.

Other predictions in the candidate list have even weaker support:

- **Rheumatoid arthritis (score 99.82%):** None of the 5 retrieved publications tests cidofovir in this disease. They cover CMV in transplant recipients, drug-related retinal toxicity and wart treatment. The association appears to come from leflunomide, an RA drug used as an anti-CMV agent, which is the reverse direction of repurposing.
- **Colobomatous microphthalmia-rhizomelic dysplasia syndrome (99.62%)** and **brachydactyly-syndactyly syndrome (99.49%):** These are rare developmental genetic disorders with no plausible link to an antiviral mechanism. The scores likely reflect network artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the lead prediction, sclerosing cholangitis.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02473925 | MAR-CIDOFOVIR | Not specified | Not specified |

---

## Cytotoxicity

Cidofovir is an antiviral, not an antineoplastic agent, so this section does not apply.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from PrimeKG drug-disease edges, not from label text): kidney disease, pyoureter, acidosis disorder, acquired lactic acidosis.
- **Nephrotoxicity:** Cidofovir is known to be nephrotoxic and is generally given with probenecid and hydration. This is a significant concern for any new use.
- **Drug interactions:** The interaction check found 55 interacting drugs. Examples of **Major** interactions include:
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Aminoglycosides: kanamycin, neomycin, streptomycin
  - Polymyxin B and vancomycin
  - Aminosalicylates: mesalazine, balsalazide, olsalazine, sulfasalazine
  - Deferasirox and deferoxamine
  - Iodinated contrast agents: diatrizoate, iodipamide
  - Iobenguane (I-131)

  **Moderate** interactions include exenatide and trospium. Many of these are nephrotoxic agents, which adds to the renal risk.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only support for sclerosing cholangitis is a model prediction (evidence level L5), with no clinical trials or literature. The mechanistic fit is weak, and cidofovir's nephrotoxicity and extensive interaction profile raise the bar for any new use.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism-of-action data from DrugBank
- The approved indication, dosage form and manufacturer for the Canadian licence
- A targeted literature search on cidofovir or antivirals in CMV-associated or secondary cholangiopathy
- Preclinical or mechanistic evidence for a role in sclerosing cholangitis
- Route-of-administration compatibility assessment and a renal safety plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

