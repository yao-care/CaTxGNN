---
layout: default
title: Sulfasalazine
parent: Model Prediction Only (L5)
nav_order: 865
evidence_level: L5
indication_count: 10
---

# Sulfasalazine
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

# Sulfasalazine: From an Anti-Inflammatory Agent to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Sulfasalazine is an established anti-inflammatory drug marketed in Canada. The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation. This prediction has **0 clinical trials** and **0 publications** behind it, and no plausible mechanistic link has been identified, so it is a graph-based computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the drug record. The Evidence Pack's rationale analysis describes sulfasalazine as acting through NF-kB inhibition, inhibition of system xc- (SLC7A11), and the anti-inflammatory activity of its 5-ASA component.

None of these pathways connects to brachydactyly-syndactyly syndrome, a congenital limb malformation. The high TxGNN score therefore reflects a pattern in the knowledge graph, not a biological or clinical rationale. Without supporting studies, this prediction should not be treated as a credible repurposing lead.

Among the other top-10 predictions, **osteoarthritis** (rank 5, score 99.64%) and **spondyloarthropathy susceptibility** (rank 8, score 99.53%) have some supporting material.

- **Osteoarthritis:** preclinical work suggests sulfasalazine may reduce cytokine-induced cartilage breakdown in vitro and in animal models (for example, a sulfasalazine-containing hyaluronic acid system in a rat model). The evidence is rated L4.
- **Spondyloarthropathy:** the literature is reviews and observational or genetic studies, with no trials. It is also rated L4.

The remaining predictions in the top 10 have no evidence and no identified mechanistic link.

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
| 598488 | PMS-SULFASALAZINE-E.C. TAB 500MG |
| 598461 | PMS-SULFASALAZINE 500MG/TAB USP |
| 2064480 | SALAZOPYRIN TAB 500MG |
| 2544652 | JAMP SULFASALAZINE |
| 2064472 | SALAZOPYRIN EN-TABS 500 MG |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanistic link. It is a computational signal only (evidence level L5).

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking sulfasalazine pharmacology to the pathogenesis of this syndrome
- Any preclinical or clinical evidence specific to this condition
- Health Canada package insert data on warnings and contraindications, which is currently missing and would block safety screening
- Mechanism of action data from DrugBank
- A decision to redirect review effort to osteoarthritis (rank 5), which has preclinical support. Its two registered trials are not clearly relevant to sulfasalazine, so human efficacy data for osteoarthritis are still lacking.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

