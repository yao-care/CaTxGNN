---
layout: default
title: Rasburicase
parent: Model Prediction Only (L5)
nav_order: 791
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase: From Uric Acid Lowering to Renal Hypouricemia

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase enzyme that breaks down uric acid. The Evidence Pack does not state a formal original indication.
The TxGNN model predicts it may be effective for **renal hypouricemia**, but **0 clinical trials** and **0 publications** support this, and the mechanism points in the opposite direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Evidence Pack (pharmacologically a uric acid-lowering agent) |
| Predicted New Indication | Renal hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this pack. Rasburicase is a recombinant urate oxidase that converts uric acid to allantoin and lowers plasma uric acid.

**The top prediction is not mechanistically plausible.** Renal hypouricemia is already a state of low uric acid, so lowering it further could be harmful. The high score is most likely a graph-proximity artifact from the uric acid pathway, not a real therapeutic link.

**Other predicted candidates (ranks 2-10):**
- **HGPRT partial deficiency** (Lesch-Nyhan spectrum, score 99.97%) is the most mechanistically coherent. Purine overproduction causes hyperuricemia, so lowering uric acid is plausible.
  - Rasburicase does not act on upstream hypoxanthine or xanthine, which can accumulate.
  - It is a short-course intravenous protein with immunogenicity.
  - It also carries G6PD-related hemolysis and methemoglobinemia risks.
- **Hepatic porphyria, portal vein thrombosis, hepatopulmonary syndrome, familial noncirrhotic portal hypertension, copper-associated cirrhosis, hepatoportal sclerosis and phenylalanine metabolism disorders** have no identified mechanistic rationale. Several share an identical score, which suggests a shared graph neighborhood and not drug-specific biology.
- **Renal tubular acidosis** has only a weak, indirect link through renal urate handling and crystal-related kidney injury.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2248416 | FASTURTEC | Not listed | Not listed |

---

## Safety Considerations

- **Risks noted in the candidate assessment**: G6PD-related hemolysis, methemoglobinemia, and immunogenicity of the intravenous protein.

No Health Canada warnings, contraindications, or drug interaction data were retrieved. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are L5 (model prediction only) with no trials or literature. The top-ranked indication, renal hypouricemia, is mechanistically contradictory, and most others appear to be knowledge-graph artifacts.

**To proceed, the following is needed:**
- Health Canada package insert (warnings and contraindications) to allow safety screening
- Mechanism of action data from DrugBank
- A literature and trial search focused on HGPRT partial deficiency, the only mechanistically coherent candidate
- Confirmation of the approved indication text for FASTURTEC

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

