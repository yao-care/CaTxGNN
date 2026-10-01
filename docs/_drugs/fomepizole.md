---
layout: default
title: Fomepizole
parent: Model Prediction Only (L5)
nav_order: 406
evidence_level: L5
indication_count: 1
---

# Fomepizole
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

# Fomepizole: From Ethylene Glycol/Methanol Poisoning to Sclerosing Cholangitis

## One-Sentence Summary

Fomepizole is generally known as an antidote for ethylene glycol and methanol poisoning. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but this prediction currently rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ethylene glycol / methanol poisoning (general drug knowledge; the Canadian license data provided contains no indication text) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Fomepizole is generally known as a competitive inhibitor of alcohol dehydrogenase (ADH). It blocks the conversion of methanol and ethylene glycol into their toxic metabolites.

No established pathway links ADH inhibition to sclerosing cholangitis. That disease is driven by immune-mediated cholestatic injury and bile duct fibrosis. Possible links, such as ADH-related metabolism in hepatobiliary tissue or a shared neighbor in the knowledge graph, are speculative and unverified.

The high score (0.993) may reflect the graph's topology rather than a real biological rationale. This prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2242980 | ANTIZOL |
| 2435667 | FOMEPIZOLE FOR INJECTION |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the queried source.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, registry, or literature support, and no plausible mechanistic link to sclerosing cholangitis has been established. A high model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to test for any biological link to cholestatic or bile duct disease
- A systematic literature and trial search for fomepizole in hepatobiliary disease
- Preclinical evidence (for example, cholestasis or bile duct fibrosis models) before any clinical consideration
- An assessment of route compatibility and similarity to the original indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

