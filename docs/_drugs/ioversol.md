---
layout: default
title: Ioversol
parent: Model Prediction Only (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Ioversol: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not stated in the data compiled for this report (a diagnostic contras…"
monitor_inn: "Ioversol"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
---

# Ioversol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Ioversol: From Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Ioversol is an iodinated, non-ionic radiographic contrast agent, marketed in Canada under the OPTIRAY brand.
The TxGNN model predicts it may be effective for **osteoarthritis susceptibility**, but **no clinical trials** and **no publications** currently support this prediction.
The result is a computational prediction only and should be treated with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (a diagnostic contrast agent for imaging) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ioversol is an iodinated, non-ionic contrast agent. It attenuates X-rays to improve the visibility of blood vessels and tissues during imaging. It is a diagnostic aid rather than a therapeutic drug.

No mechanistic link to the predicted indication has been identified. Ioversol has no known pharmacological action on genetic susceptibility to osteoarthritis. The high TxGNN score (99.67%) reflects a pattern found by the computational model and is not backed by trials or literature.

For context, the next-ranked prediction, **osteoarthritis**, has one linked publication (PMID 38102013, the LipioJoint-1 trial of genicular artery embolization). In that procedure, the therapeutic effect comes from the embolic agent (an ethiodized-oil-based emulsion). The iodinated contrast is used only for imaging guidance. This is indirect, procedural evidence and does not show a pharmacological benefit of ioversol. The other top-10 predictions include rheumatoid arthritis, rare skeletal dysplasias, hemoglobinopathy, myosclerosis and alopecia. None has a plausible mechanistic rationale, and none has clinical trial support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the top prediction (osteoarthritis susceptibility), currently no related literature is available.

For reference, the only related publication found for the neighbouring prediction, osteoarthritis, is:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Single-arm clinical trial (procedure) | Diagnostic and Interventional Imaging | LipioJoint-1: safety and efficacy of transient genicular artery embolization with an ethiodized-oil-based emulsion for knee osteoarthritis. The effect comes from the embolic agent, not ioversol. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01900854 | OPTIRAY 320 | Not specified | Not specified |
| 02035626 | OPTIRAY 320 (ULTRAJECT) | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. The main ones, rated Major, include:
  - Metformin
  - Amphotericin B (including the lipid complex, cholesteryl sulfate and liposomal forms)
  - Aminoglycosides (kanamycin, neomycin, streptomycin)
  - Vancomycin
  - Polymyxin B
  - Aminosalicylates (mesalazine, balsalazide, olsalazine, sulfasalazine)

  Mannitol is rated Moderate. Several others, including atropine, famotidine, acetylsalicylic acid, morphine and omeprazole, are rated Unknown. Many of the Major interactions involve nephrotoxic drugs or metformin, so renal function should be assessed.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no registered clinical trials, no supporting literature and no plausible mechanism for ioversol, a diagnostic contrast agent, in osteoarthritis susceptibility. The only related publication concerns a procedure in which ioversol is not the active agent.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- A credible biological rationale linking ioversol to osteoarthritis susceptibility
- Any preclinical or clinical evidence of therapeutic activity, as opposed to imaging use
- A check of route and dosage-form compatibility with the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

