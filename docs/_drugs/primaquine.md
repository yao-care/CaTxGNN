---
layout: default
title: Primaquine
parent: Model Prediction Only (L5)
nav_order: 763
evidence_level: L5
indication_count: 8
---

# Primaquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Primaquine: From Antimalarial Use to Myiasis

## One-Sentence Summary

Primaquine is an 8-aminoquinoline antiparasitic, used mainly against malaria. The TxGNN model predicts it may be effective for **myiasis** (fly-larvae infestation) with a very high score, but **no clinical trials and no publications** support this prediction. It is a graph-based signal only, and no mechanistic link is apparent.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

The licence record contains no approved-indication text, so the original indication is taken from primaquine's known pharmacology (antimalarial).

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for primaquine. From known pharmacology, it is an 8-aminoquinoline that acts against protozoa. It kills the dormant liver stages of *P. vivax* and *P. ovale*, and it clears *P. falciparum* gametocytes.

Myiasis is an infestation by fly larvae (insects), not a protozoal infection. No plausible mechanism links primaquine's antiprotozoal activity to killing or removing larvae. The score is probably a knowledge-graph artefact. Three related predictions (furuncular, wound and creeping myiasis, all scored 99.73%) appear to inherit their scores from the parent "myiasis" node.

Standard care for myiasis is mechanical larval removal, with ivermectin where needed. Nothing in the evidence suggests primaquine would add to this.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2017776 | PRIMAQUINE |

Dosage form, manufacturer and approved indication are not recorded for this authorization.

## Safety Considerations

Please refer to the package insert for safety information.

For context only, the evidence for other predicted indications flags the following guardrails. They are not specific to myiasis:
- Test for G6PD deficiency before use, because of the risk of haemolysis.
- Consider CYP2D6 genotype, since primaquine is bioactivated by this enzyme.
- Take caution in pregnancy and lactation.
- Monitor for methemoglobinemia.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph score, with no trials, no literature and no plausible mechanism. Established, cheaper standard care (larval removal, ivermectin) already exists. All four myiasis-related predictions are L5 and stay at the S0 stage.

**To proceed, the following is needed:**
- Mechanism of action data for primaquine, to test whether any link to larval biology exists
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Any preclinical or clinical signal of primaquine activity against fly larvae; without it, the myiasis prediction should not advance

**Note on other predictions:** Higher-evidence candidates exist in the same pack, but they are not repurposing in the strict sense. Malaria (L1, 99.38%) is primaquine's established core use, and the empty original-indication field looks like a data gap. Pneumocystosis (L1, 99.32%) is supported by a completed Phase 3 trial (NCT00000640, n=290) of clindamycin plus primaquine. Both are rated "Proceed with Guardrails". Pneumocystosis use is second-line or off-label, so it should be checked against current local labeling.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

