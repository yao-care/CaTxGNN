---
layout: default
title: Primidone
parent: Model Prediction Only (L5)
nav_order: 764
evidence_level: L5
indication_count: 10
---

# Primidone
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

# Primidone: From Antiseizure Use to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Primidone is an antiseizure drug whose active metabolites include phenobarbital and PEMA.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction.
This is a model-only signal (Evidence Level L5) with no identifiable mechanistic link, so it is best treated as a likely graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (primidone is an antiseizure agent) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, primidone and its metabolites (phenobarbital and PEMA) act on GABA-A receptors and sodium channels. Their efficacy is in seizure control, and there is no known antineoplastic activity.

The analysis found **no identifiable mechanistic link** between primidone and trigeminal nerve neoplasm. The very high graph score most likely reflects network proximity to neurological terms such as trigeminal neuralgia, not a real therapeutic relationship. This prediction should not be read as biological support for treating a tumour.

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
| 399310 | PRIMIDONE |
| 396761 | PRIMIDONE |

Dosage form, manufacturer and approved indication text are not recorded in these licence entries.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no plausible mechanism. Primidone has no known antineoplastic activity, so the 99.99% score reflects model behaviour rather than evidence.

**Other candidates in the same prediction set:**
- **Trigeminal neuralgia** (L4, Research Question) has a more plausible class-level rationale, since sodium channel-blocking antiseizure drugs are standard therapy. A 2026 mouse study (PMID 41806836) implicates TRPM3 in orofacial neuropathic pain, and primidone has been reported as a TRPM3 antagonist. The evidence is indirect, with no human trials of primidone.
- **Audiogenic seizures** (L4, Research Question) is biologically plausible, but the support is limited to old preclinical and case-level papers.
- Other reflex-epilepsy subtypes (micturition-induced, eating, startle, thinking and reading seizures) are plausible in mechanism, but the retrieved papers are generic antiseizure reviews or unrelated reports.
- **Orgasm-induced seizures** has no trials or literature.
- **Beta-ketothiolase deficiency** (L5) has no mechanistic link and is probably an artifact.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which currently block safety screening
- Mechanism of action data from DrugBank
- Verification of the primidone–TRPM3 link before any clinical design for trigeminal neuralgia
- A manual relevance review of the retrieved literature, which is still unreviewed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

