---
layout: default
title: Nafarelin
parent: Model Prediction Only (L5)
nav_order: 640
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nafarelin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Endometriosis"
monitor_inn: "NAFARELIN"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "pelvic organ prolapse", "syndrome with a Dandy-Walker malformation as major feature", "female genital tuberculosis", "physiological sexual disorder", "isolated genetic hair shaft abnormality", "dysplasia of cervix"]
---

# Nafarelin
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

# Nafarelin: From Endometriosis to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Nafarelin is a GnRH (gonadotropin-releasing hormone) agonist originally used for endometriosis and central precocious puberty.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (the Canadian licence record contains no indication text; this comes from the knowledge graph) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known pharmacology, nafarelin is a GnRH receptor agonist. After an initial stimulation, it desensitizes the pituitary receptor and suppresses gonadal sex steroids. This explains its use in endometriosis and central precocious puberty.

Ambras syndrome is a congenital genetic disorder of hair growth with no established hormonal driver. The plausibility of a GnRH-mediated effect is therefore low. The prediction rests on a high model score (0.9987) only.

Other top predictions show a similar pattern. Hypertrichosis (generic) has a speculative link through androgen-dependent hair growth, but this fits hirsutism better than congenital hypertrichosis. "Central precocious puberty 1" is probably a genetic subtype of an existing indication, so it is an on-label extension rather than true repurposing. The one publication retrieved, for "physiological sexual disorder", concerns nafarelin versus danazol for endometriosis pain. It is indirect evidence at best.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the lead prediction. One publication was retrieved for the rank 7 prediction (physiological sexual disorder):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7951404](https://pubmed.ncbi.nlm.nih.gov/7951404/) | 1994 | Clinical study (design not confirmed) | Int J Fertil Menopausal Stud | Compared nafarelin and danazol for dysmenorrhea, dyspareunia and pelvic pain in endometriosis; this is an already approved use and does not directly address a sexual disorder |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02188783 | SYNAREL | Not listed | Not listed |

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): hypertensive disorder, hypertension, hyperglycemia, osteoporosis, postmenopausal osteoporosis, diabetes mellitus, diabetic ketoacidosis, substance abuse/dependence, obesity disorder, monogenic obesity.
- **Drug interactions**: No drug-drug interactions were identified. The only pharmacology record is the expected target, the GnRH1 receptor (GNRHR).

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.87%), but there are no clinical trials or publications, and the mechanism is implausible for a congenital hair-growth disorder. The evidence level is L5.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- A literature and trial search specific to Ambras syndrome and hypertrichosis
- Review of whether "central precocious puberty 1" should be mapped to the existing approved indication, as it may be a more practical direction than the lead prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

