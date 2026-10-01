---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 777
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is a first-line antitubercular drug. The TxGNN model predicts it may be effective for **infectious otitis media**, but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. It is a model-only signal and has not been tested in patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Pyrazinamide is a first-line antitubercular agent, and its efficacy in tuberculosis is well established. The Canadian licence record in the Evidence Pack contains no approved indication text, so the original indication here is based on the drug's known class use and still needs to be confirmed against the label.

A mechanistic link exists only for the **tuberculous subtype** of otitis media. In that setting, pyrazinamide's existing antimycobacterial activity would be applied at an ear site, which is not a new mechanism. It has no plausible activity against the common bacterial or viral causes of infectious otitis media. The high model score therefore most likely reflects network proximity in the knowledge graph rather than a pharmacological rationale for general otitis media.

Related predicted indications do have case-level support. Tuberculous otitis media (listed under middle ear disease, chronic otitis media and suppurative otitis media) is documented in case reports and case series. In those reports, pyrazinamide was part of standard multidrug anti-TB therapy. This evidence applies only to the TB etiology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| Licence Number | Product Name |
|---------|------|
| 618810 | PDP-PYRAZINAMIDE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials or literature, and the only plausible mechanism covers tuberculous otitis media rather than infectious otitis media in general. The tuberculous subtype is already treated with standard anti-TB regimens that include pyrazinamide, so it is better framed as a research question under the more specific predicted indications.

**To proceed, the following is needed:**
- Confirmation of the approved indication from the Health Canada product monograph
- Safety information (warnings and contraindications) from the package insert, before any safety screening
- Mechanism of action data for pyrazinamide
- A decision on whether to reframe the candidate as tuberculous otitis media, supported by a systematic review of the existing case reports
- Route compatibility assessment for ear-site disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

