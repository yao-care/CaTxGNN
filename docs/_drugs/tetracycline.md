---
layout: default
title: Tetracycline
parent: Moderate Evidence (L3-L4)
nav_order: 903
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-13
description: "Tetracycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L4). Approved use: Not stated in the Canadian licence data. The knowledge graph lists ur…"
monitor_inn: "Tetracycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
---

# Tetracycline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

## Tetracycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Tetracycline is a broad-spectrum antibiotic originally used for infections such as urinary tract infection, bronchitis, pneumonia, acne, gonorrhea and conjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are currently **0 clinical trials** and only **1 publication** (a 1992 case report that is indirect evidence), so the support is very limited.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence data. The knowledge graph lists urinary tract infection, bronchitis, acne, anthrax infection, gonorrhea, pharyngitis, conjunctivitis, pneumonia and others |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, tetracycline is a member of the tetracycline antibiotic class. Its efficacy in bacterial infections, including chlamydial (trachoma/inclusion) conjunctivitis, is established, and mechanistically it may be applicable to punctate epithelial keratoconjunctivitis.

Punctate keratitis can follow chlamydial follicular conjunctivitis, which is already within tetracycline's established uses. Tetracyclines also have antibacterial activity against *Chlamydia*, as well as anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting effects that could plausibly matter on the ocular surface.

The high TxGNN score most likely reflects how close this disease sits to the existing conjunctivitis indications in the knowledge graph. It is not a sign of direct evidence for this use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Two patients with chlamydial follicular conjunctivitis were treated with oral tetracycline or doxycycline, and the follicles resolved. Both later had recurrent bilateral punctate epithelial keratitis. This describes persistent keratitis after treatment, not a test of tetracycline for this condition. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00580929 | TETRACYCLINE | Not specified | Not specified |
| 02246962 | PYLERA | Not specified | Not specified |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** liver failure and liver disease, kidney disease and kidney failure, uremia, epilepsy, diabetes mellitus and diabetic ketoacidosis, neutropenia and agranulocytosis, G6PD deficiency, blood coagulation disease, *Clostridium difficile* colitis, gout, peripheral neuropathy, atrial fibrillation and atrioventricular block, respiratory failure, and others. These need confirmation against the Health Canada package insert.
- **Drug Interactions:** 100 interactions were identified in total; the first 20 are reviewed here.
  - **Major:** isotretinoin, acitretin, aminolevulinic acid
  - **Moderate:** ethinylestradiol, amoxicillin, ampicillin, aminophylline, atracurium, atovaquone, balsalazide, bismuth subcitrate potassium, aluminum hydroxide, sodium citrate, topical aminolevulinic acid, asparaginase (*E. coli* and *Erwinia* forms), attapulgite
  - **Minor:** acetazolamide, hydrochlorothiazide, amiloride

Please refer to the package insert for the full set of warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence is a single 1992 case report, which is indirect, and there are no registered trials. The high TxGNN score probably reflects proximity to existing conjunctivitis indications rather than real support for this use (L4).

**To proceed, the following is needed:**
- Direct clinical evidence of tetracycline (or an ocular formulation) in punctate epithelial keratoconjunctivitis
- Detailed mechanism of action data (MOA)
- Health Canada package insert warnings and contraindications, plus approved indication text for the two licences
- Route and formulation compatibility assessment, since an ocular route is likely needed
- Review of the knowledge-graph contraindication signals and major drug interactions

---

## Other Predicted Indications (Reference)

| Predicted Indication | TxGNN Score | Evidence Level | Evidence Summary | Recommendation |
|------|------|------|------|------|
| Chronic ethmoidal sinusitis | 99.15% | L4 | One 2006 in vitro susceptibility study of streptococci; no trials | Hold |
| Chronic rhinosinusitis | 99.15% | L4 | A Cochrane review, a 2023 meta-analysis of doxycycline, and other class-level papers; no tetracycline-specific trials | Research Question |
| Paranasal sinus neoplasm | 99.10% | L5 | Model prediction only | Hold |

Chronic rhinosinusitis has the most supporting literature, but it is mostly about doxycycline and other class members rather than tetracycline itself.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

