---
layout: default
title: Norelgestromin
parent: Model Prediction Only (L5)
nav_order: 560
evidence_level: L5
indication_count: 1
---

# Norelgestromin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Norelgestromin: From Contraception to Amenorrhea

## One-Sentence Summary

Norelgestromin is the active metabolite of norgestimate, a third-generation progestin best known as a component of combined contraceptive patches.
The TxGNN model predicts it may be effective for **Amenorrhea**, but this prediction currently has **no supporting clinical trials or published literature** and is based on model inference alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — the drug is not marketed in Canada and no approved indication text is on file. (Known pharmacologically as a contraceptive-patch component; not confirmed by this evidence pack.) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for norelgestromin ([Data Gap]). Based on known pharmacology, norelgestromin is a third-generation progestin that acts on the endometrium and the hypothalamic-pituitary-gonadal axis — the same pathway targeted by progestins used clinically to induce withdrawal bleeding or regulate menstrual cycle irregularities. This general class-level mechanism is the basis for TxGNN linking the drug to amenorrhea.

However, this link warrants caution. Progestins delivered via long-acting or patch formulations — the delivery form norelgestromin is best known for — are more commonly associated with *causing* amenorrhea as a contraceptive side effect, rather than treating it. The high TxGNN score may therefore reflect this well-documented bidirectional association in the knowledge graph (drug↔disease edges recorded in either causal direction) rather than a validated therapeutic mechanism. Because both the drug's original indication and its detailed MOA are missing from this evidence pack, this mechanistic reasoning is an analogy to the progestin class as a whole, not a directly verified pathway for norelgestromin itself.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Canada Market Information

Norelgestromin currently has no authorized products in Canada — 0 DINs on file, market status "Not Marketed." No licensing or indication information is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on model inference (L5) with zero supporting clinical trials or literature, and the proposed mechanism is ambiguous — the same pharmacological pathway is documented to cause amenorrhea (as a contraceptive effect) rather than treat it. A blocking data gap on TFDA/product label warnings also prevents any safety pre-screening (S1).

**To proceed, the following is needed:**
- TFDA/Health Canada label data (warnings, contraindications) to clear the blocking safety gap (DG001)
- Confirmed mechanism of action (DG002) to resolve the directionality ambiguity between "causing" vs. "treating" amenorrhea
- Confirmation of the drug's actual original indication(s), since none are on file
- At minimum, preclinical or case-level evidence before this candidate can advance past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

