---
layout: default
title: Dexrazoxane
parent: Model Prediction Only (L5)
nav_order: 272
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Dexrazoxane: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "DEXRAZOXANE"
predicted_indications: ["sclerosing cholangitis", "bronchitis", "paratyphoid fever", "conjunctivitis", "epiglottitis", "peritonitis", "laryngitis", "urinary tract infection (disease)", "pyelonephritis", "cystitis"]
---

# Dexrazoxane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Dexrazoxane: From an Unspecified Original Indication to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Dexrazoxane is marketed in Canada as a single-ingredient product, but the data compiled for this report do not list its approved indication.
The TxGNN model predicts it may be effective for **sclerosing cholangitis** with a very high score, yet **no clinical trials and no publications** currently support this prediction.
It is a model prediction only and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (Canadian license records contain no indication text) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Dexrazoxane is known as an iron-chelating agent and topoisomerase II inhibitor. This is general pharmacological knowledge, not part of the data compiled for this report.

A speculative link to sclerosing cholangitis is that iron chelation and topoisomerase II inhibition could influence oxidative stress and inflammation in cholestatic bile duct injury. No trial, publication, or mechanistic study in the compiled data supports this idea. The high score should not be read as proof of efficacy.

The other top-ranked predictions are also supported by the model score alone. These include bronchitis, paratyphoid fever, conjunctivitis, epiglottitis, laryngitis, and urinary tract infections. Several of them are infectious conditions for which dexrazoxane has no antimicrobial mechanism. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Among the lower-ranked predictions, **cystitis** (rank 10) has the most indirect support. Preclinical work links ferroptosis, an iron-dependent form of cell death, to cyclophosphamide-induced hemorrhagic cystitis and to interstitial cystitis. Two older reviews on chemoprotectants provide context. None of these tests dexrazoxane directly in cystitis, so it remains a research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for sclerosing cholangitis.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02153432 | ZINECARD | Not listed | Not listed |
| 02544083 | DEXRAZOXANE FOR INJECTION | Not listed | Not listed |

Both products are valid single-ingredient licenses. None are cancelled.

---

## Cytotoxicity

Dexrazoxane is used alongside antineoplastic therapy but is not itself classified here as a conventional cytotoxic agent. The data compiled for this report do not include its toxicity classification. Please refer to the package insert warnings and precautions, including any handling requirements.

---

## Safety Considerations

- **Contraindications (model signal, not label text)**: The TxGNN model (deep learning) links dexrazoxane to impaired renal function disease and non-infectious meningitis. This may reflect similarities the model learned between related diseases, not biological evidence. These should be verified against the official label.
- **Drug Interactions**: 19 interactions were identified, of which 11 are rated Major and 8 Moderate.
  - **Major**: mostly live vaccines or live-organism products: BCG (Tice), measles, mumps, rubella, rotavirus, smallpox (vaccinia), typhoid (live), yellow fever, varicella zoster, and talimogene laherparepvec.
  - **Moderate**: doxorubicin (including liposomal), dimethyl fumarate, diroximel fumarate, monomethyl fumarate, adenovirus type 4 antigen, *Bifidobacterium longum infantis*, *Lactobacillus acidophilus*, and live cholera vaccine (CVD 103-HgR).

Health Canada package insert warnings and contraindications were not available. Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sclerosing cholangitis prediction rests on a model score alone (L5), with no trials, no literature, and only a speculative mechanism. The essential label information (indications, warnings, contraindications) is also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- The Health Canada package insert, to confirm the approved indication, warnings, and contraindications
- Mechanism of action data (for example, from DrugBank)
- A targeted literature search on dexrazoxane in cholestatic or sclerosing liver disease, and on iron or ferroptosis pathways in bile duct injury
- Preclinical validation before any clinical study, if the hypothesis is pursued
- Review of the renal impairment and meningitis signals from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence, together with the live vaccine interactions, before any new-use study
- Optionally, follow-up on cystitis (chemotherapy-induced or interstitial) as a lower-ranked but better-supported research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

