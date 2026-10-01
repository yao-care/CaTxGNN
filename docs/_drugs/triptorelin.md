---
layout: default
title: Triptorelin
parent: Model Prediction Only (L5)
nav_order: 944
evidence_level: L5
indication_count: 10
---

# Triptorelin
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

# Triptorelin: From an Unlisted Original Indication to Hypertrichosis

## One-Sentence Summary

Triptorelin is a GnRH (gonadotropin-releasing hormone) agonist marketed in Canada under the brands Trelstar and Decapeptyl. The pack does not record its original approved indication.
The TxGNN model ranks **hypertrichosis** first (score 99.997%), but there are **0 clinical trials** and only **1 publication**, a case report that does not show benefit.
The prediction is not supported by evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the supplied data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 (the pack assigns L4, but its only publication reports a ciclosporin side effect, not a triptorelin benefit) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Triptorelin is a GnRH agonist. Continuous exposure desensitises pituitary gonadotrophs and suppresses LH, FSH and gonadal sex steroids.

The link to hypertrichosis is weak. Hypertrichosis is not a recognised androgen-driven condition (unlike hirsutism), so suppressing gonadal androgens gives no clear reason to expect benefit.

The only retrieved publication is a 2026 case report of ciclosporin-induced hypertrichosis in a transgender woman with psoriasis. She was also taking estradiol and a testosterone blocker, which the report lists as triptorelin. The hypertrichosis is attributed to ciclosporin, and the case shows it can occur despite androgen suppression. This is not evidence that triptorelin treats hypertrichosis. The high TxGNN score should be treated as an unverified model output.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41822646](https://pubmed.ncbi.nlm.nih.gov/41822646/) | 2026 | Case report | Cureus | Generalised hypertrichosis caused by ciclosporin in a transgender woman on estradiol and triptorelin. Androgen suppression did not prevent it. No therapeutic benefit of triptorelin is shown. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2240000 | TRELSTAR |
| 2243856 | TRELSTAR |
| 2389282 | DECAPEPTYL |
| 2412322 | TRELSTAR |

Dosage form and approved indication text were not supplied for these authorisations.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no plausible mechanism, no trial, and no supportive literature for hypertrichosis. The model score is the only support.

**To proceed, the following is needed:**
- The Health Canada approved indications and product monograph (warnings, contraindications), which are missing from the pack
- Mechanism of action data from DrugBank
- A mechanistic rationale and prospective evidence for hypertrichosis; without these, no further investment is advised

**Note on other predictions in this pack:**
- **Precocious puberty (rank 8, score 99.89%)** is the only candidate with substantial evidence.
  - Evidence: several completed Phase 3 single-arm trials of 1-, 3- and 6-month triptorelin formulations, plus published efficacy and adult-height data. The pack rates it L1, S3, "Proceed with Guardrails".
  - It is effectively an established or on-label use for central (GnRH-dependent) precocious puberty rather than new repurposing. Local labelling should be confirmed.
  - Guardrails: trials are mostly single-arm and non-comparative, and peripheral forms are not covered.
- **Familial male-limited precocious puberty (rank 7)** has only small case series, mostly of antiandrogen or aromatase-inhibitor regimens. The pack treats it as a research question.
- The remaining candidates (Ambras syndrome, Dandy-Walker syndrome, hair shaft abnormality, allergic urticaria, trichomegaly, aromatase excess syndrome, odontal malformation syndrome) have no trials and no drug-specific literature. The periodontal literature appears to be keyword-matched noise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

