---
layout: default
title: Isosorbide Mononitrate
parent: Model Prediction Only (L5)
nav_order: 498
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

# Isosorbide Mononitrate: From Its Marketed Nitrate Use to Hypertrichosis

## One-Sentence Summary

Isosorbide mononitrate (ISMN) is a nitric oxide (NO) donor vasodilator marketed in Canada. The TxGNN model predicts it may be effective for **hypertrichosis** with a very high score, but there are **0 clinical trials** and **0 publications** for this prediction. It is a model-only signal, and the mechanistic review found no plausible link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Evidence Pack (Canadian licence records contain no indication text) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not well supported. ISMN releases nitric oxide, which raises cGMP and relaxes vascular smooth muscle. Detailed mechanism-of-action data from DrugBank are not available in the Evidence Pack, so this description comes from the mechanistic review.

The known link between vasodilators and excess hair growth runs through a different pathway. Minoxidil-associated hypertrichosis is tied to K-ATP channel opening, not the NO/cGMP pathway. The high score therefore appears to come from proximity in the knowledge graph. It may also reflect an adverse-effect-type association rather than a therapeutic one.

The other top-ranked predictions are mostly hair or genetic disorders, such as Ambras syndrome, alopecia, hypotrichosis and alopecia areata. None has clinical or literature support. The only speculative link is improved scalp microcirculation for alopecia, and the systemic hypotension and headache burden of nitrates makes a benefit-risk case unlikely.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2126559 | IMDUR |
| 2311321 | PRO-ISMN - 60 |
| 2272830 | APO-ISMN |
| 2301288 | PMS-ISMN |

Dosage forms, manufacturers and approved indication text are not recorded for these licences.

## Safety Considerations

- **Drug Interactions**: The DDI query returned no records. However, co-administration with PDE5 inhibitors or riociguat is contraindicated because of the risk of severe hypotension.
- **Other concerns** noted in the review: nitrate tolerance, systemic hypotension and headache.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a knowledge-graph score alone (L5). There are no trials or literature, and the mechanistic review found no plausible link. All 9 hair- and genetic-disorder predictions in the top 9 are also Hold.

**Other predictions in the pack:**
- **Pulmonary arterial hypertension** (rank 10, score 99.94%) is the only prediction with some support, at L4 and rated a "Research Question". Support is indirect: preclinical work (a hybrid ISMN/bardoxolone methyl molecule; sGC stimulation in a rat model), pharmacology reviews, and a hemodynamic study in coronary artery disease patients rather than PAH. No PAH-specific trial exists.
- Its practical feasibility is limited because PDE5 inhibitors and riociguat, which are standard PAH therapies, are contraindicated with ISMN.
- The periodontal-syndrome literature (rank 3) is generic periodontitis material that never mentions ISMN.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the Canadian licences
- For any further consideration of PAH, a targeted review of PAH-specific evidence and a clear position on the PDE5 inhibitor and riociguat limitation

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

