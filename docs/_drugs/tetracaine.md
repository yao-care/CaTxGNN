---
layout: default
title: Tetracaine
parent: Model Prediction Only (L5)
nav_order: 895
evidence_level: L5
indication_count: 9
---

# Tetracaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Tetracaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Tetracaine is a sodium channel-blocking local anesthetic marketed in Canada in several topical and ophthalmic products.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, a chronic atrophic skin disease driven by Borrelia infection.
Currently **0 clinical trials** and **0 publications** support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Local anesthesia (approved-indication text not available in the license records) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Tetracaine is a local anesthetic that works by blocking sodium channels in nerve membranes, which stops pain signals. It is used mainly on the skin, in the eye and for spinal anesthesia.

Acrodermatitis chronica atrophicans is a late-stage skin manifestation of Borrelia infection (Lyme disease), marked by progressive skin thinning. The disease is infectious and inflammatory, and nerve conduction block does not address either process. We found no mechanistic link between the two.

The high TxGNN score probably reflects patterns in the knowledge graph rather than biological rationale. It should be read as a hypothesis-generating signal only. Route compatibility and similarity to the original indication have not yet been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

Seven DINs are on record; the five main authorizations are listed below. Dosage form and approved-indication text are not available for these entries.

| DIN | Product Name |
|---------|------|
| 02148544 | MINIMS TETRACAINE HYDROCHLORIDE |
| 02230575 | AMETOP GEL 4% |
| 02148528 | MINIMS TETRACAINE HYDROCHLORIDE |
| 02398028 | PLIAGLIS |
| 01930699 | ZAP TOPICAL ANESTHETIC GEL |

---

## Safety Considerations

- **Neurotoxicity with intrathecal use**: Literature retrieved for another predicted disease (cauda equina syndrome) reports cauda equina syndrome and conus medullaris injury after spinal tetracaine. The reports include case reports, a 20-year follow-up, and animal and in vitro neurotoxicity studies. This is a harm signal for intrathecal use at high doses or with maldistribution, not a therapeutic one.

Please refer to the package insert for warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism linking a local anesthetic to a Borrelia-driven skin disease. Evidence is model prediction only (L5).

Other predicted indications do not change this:
- **Acne keloid**: the only evidence is procedural-anesthesia trials of lidocaine/tetracaine cream, which are indirect and not disease-treating.
- **Cauda equina syndrome**: the literature describes harm, not benefit.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (required for safety screening)
- Mechanism-of-action data from DrugBank
- Any biological rationale linking sodium channel blockade to the disease, or evidence from preclinical or clinical studies
- Route-of-administration compatibility assessment for the proposed indication
- A check of whether the disease mapping is valid
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

