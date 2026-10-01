---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: From Herpesvirus Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Acyclovir is an antiviral drug used mainly against herpes simplex and varicella-zoster (shingles) infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but there are **0 clinical trials** and only **2 publications** for this prediction, and neither publication supports the use.
This is a model-only prediction, and the Hold recommendation applies to this indication only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpesvirus infections (general drug knowledge; the Canadian licence records contain no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acyclovir is a nucleoside analogue antiviral. Its efficacy in herpes simplex and zoster infections is established, and mechanistically it might be applicable to eye surface inflammation only if a herpesvirus is involved.

The prediction score is very high (0.997), but the retrieved evidence does not back it up. One paper is about drug-induced corneal lipidosis in AIDS patients, and the other is about microsporidial keratoconjunctivitis. Microsporidia are not an acyclovir target. Any real link would have to run through herpetic keratitis, and that is not documented in the retrieved material. The high score should be treated as a model signal, not as evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Clinical observation | Am J Ophthalmol | Two AIDS patients developed drug-induced corneal lipidosis, with surface changes linked to drugs that accumulate in lysosomes. It does not test acyclovir for keratoconjunctivitis. |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case series | Indian J Pathol Microbiol | Describes microsporidial keratoconjunctivitis in an eastern Indian cohort. Microsporidia are not an acyclovir target, so it does not support use. |

---

## Canada Market Information

Health Canada lists 20 licences for acyclovir. Five are shown below. The records contain no dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 2524708 | MINT-ACYCLOVIR |
| 2236926 | ACYCLOVIR SODIUM INJECTION |
| 2285975 | TEVA-ACYCLOVIR |
| 2242463 | MYLAN-ACYCLOVIR |
| 2242784 | MYLAN-ACYCLOVIR |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials and only two unrelated papers, so it rests on the model score alone (L5). No acyclovir-specific link to punctate epithelial keratoconjunctivitis was found.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A documented link to a herpesvirus cause of the eye condition, or clinical studies of acyclovir in this indication
- Licence indication text and dosage forms for the Canadian products

**Note:** Other predictions in the same pack have more evidence. Common wart has five acyclovir trials (intralesional, mostly small Phase 2/3 or Phase 4, with no results reported) and is a stronger candidate for follow-up. Post-infectious neuralgia largely reflects acyclovir's existing zoster use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

