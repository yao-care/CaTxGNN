---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 55
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Amoxicillin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Bacterial infections, including urinary tract infection…"
monitor_inn: "AMOXICILLIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Amoxicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic originally used for common bacterial infections such as urinary tract infection, otitis media, pneumonia and pharyngitis.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction. The high score most likely reflects knowledge-graph proximity rather than a therapeutic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections, including urinary tract infection, infectious otitis media, streptococcal infection, bacterial pneumonia and pharyngitis (approved-indication text is not available for the Canadian licences) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Amoxicillin belongs to the beta-lactam class of antibacterials, which act by inhibiting bacterial cell wall synthesis. Its efficacy in bacterial infections is well established.

Polyclonal hyperviscosity syndrome is driven by elevated serum immunoglobulins and is not an infectious process. No plausible mechanistic link to amoxicillin was identified. The high score (0.996) likely reflects knowledge-graph proximity, such as infection-related associations, rather than a therapeutic rationale.

The model's other top predictions show the same pattern. Examples are hyperamylasemia, congenital analbuminemia and premalignant haematological disease, and none has a credible mechanism or supporting evidence. The only candidate with a biologically plausible, though weak, link is **septicemic plague**. It is rated L4 and labelled a research question, and the relevant evidence is limited to in vitro and animal studies (PMID 8203841, PMID 21628541). Beta-lactams are generally considered less effective than the recommended aminoglycosides, fluoroquinolones and tetracyclines, especially against intracellular bacteria.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for polyclonal hyperviscosity syndrome.

---

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

---

## Canada Market Information

Amoxicillin has 20 valid single-ingredient licences in Canada and none cancelled. Dosage form and approved-indication text are not available for these licences. Five of them are listed below.

| DIN | Product Name |
|---------|------|
| 02477726 | AG-AMOXICILLIN |
| 02532042 | PRZ-AMOXICILLIN |
| 00628158 | APO-AMOXI |
| 02388073 | AURO-AMOXICILLIN |
| 00406724 | NOVAMOXIN |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph associations, not label text): long QT syndrome, torsades de pointes, liver failure, liver disease, cholestasis, kidney disease, porphyria, myasthenia gravis, osteoporosis, bone fracture, Clostridium difficile colitis, infectious mononucleosis, ventricular tachycardia, and others.
- **Drug Interactions**: The interaction query returned 100 records. The main ones are:
  - **Major**: methotrexate; live cholera vaccine (*Vibrio cholerae* CVD 103-HgR).
  - **Moderate**: tetracyclines (doxycycline, minocycline, demeclocycline); oestrogens (ethinylestradiol, estradiol); coumarin-type anticoagulants (anisindione, dicoumarol); mycophenolate mofetil; entecavir; balsalazide; live probiotics.
  - **Minor**: allopurinol, macrolides (azithromycin, clarithromycin, erythromycin), amiloride.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone. It has no clinical trials, no literature, and no plausible mechanism, because polyclonal hyperviscosity is not an infectious condition. The evidence level is L5.

**To proceed, the following is needed:**
- A mechanistic rationale that links amoxicillin to immunoglobulin-driven hyperviscosity, supported by mechanism of action data.
- Any preclinical or clinical evidence specific to this indication.
- Health Canada package insert warnings and contraindications, which are needed before safety screening.
- If the team wants to pursue something related to this drug, a better candidate than this top-ranked prediction is **septicemic plague**. Pursuing it would require susceptibility-guided preclinical confirmation first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

