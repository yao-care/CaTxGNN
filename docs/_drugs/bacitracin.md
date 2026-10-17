---
layout: default
title: Bacitracin
parent: Model Prediction Only (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Bacitracin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Keratitis, keratoconjunctivitis, blepharoconjunctivitis"
monitor_inn: "BACITRACIN"
predicted_indications: ["otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
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

# Bacitracin: From Keratitis to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Bacitracin is a topical antibiotic originally used for ocular infections such as keratitis, keratoconjunctivitis and blepharoconjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Keratitis, keratoconjunctivitis, blepharoconjunctivitis (from the knowledge-graph indication data; the Canadian licence records contain no indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, bacitracin is a polypeptide antibiotic that acts mainly against Gram-positive bacteria by interfering with bacterial cell wall synthesis. Its use in ocular infections is already established.

Punctate epithelial keratoconjunctivitis is closely related to the original indications, since all affect the surface of the eye. The prediction is therefore plausibly an extension of the existing ocular anti-bacterial use.

There is an important limitation. Punctate epithelial keratoconjunctivitis is often viral (for example adenoviral) or non-infectious (for example toxic). In those cases a Gram-positive-directed antibiotic would likely give limited benefit. No studies were found to confirm this specific use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication.

For context, the fourth-ranked prediction, otitis externa, has some literature, though it is limited and indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17503066](https://pubmed.ncbi.nlm.nih.gov/17503066/) | 2007 | Double-blind clinical comparison | Eur Arch Otorhinolaryngol | In 151 patients with acute bacterial otitis externa, a polymyxin B + bacitracin ointment was compared with the same ointment plus hydrocortisone acetate |
| [9820118](https://pubmed.ncbi.nlm.nih.gov/9820118/) | 1998 | In vitro study | Zentralbl Veterinarmed B | Bacteria from chronic canine otitis externa showed increased antibiotic resistance across 20 antibiotics |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02245571 | BACIJECT | Not specified | Not specified |
| 00584908 | BACITIN | Not specified | Not specified |
| 02451026 | BACITRACIN OINTMENT | Not specified | Not specified |
| 00621366 | BIODERM OINTMENT | Not specified | Not specified |
| 02236917 | OZONOL ANTIBIOTICS PLUS | Not specified | Not specified |

All five authorisations are currently valid single-ingredient products.

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: Contraindication links were found for several conditions, including:
  - Eye conditions: herpes simplex virus keratitis, viral and fungal eye infections, open-angle glaucoma, ocular hypertension
  - Kidney and liver disease
  - Neuromuscular conditions: myasthenia gravis and neuromuscular junction disease
  - Cardiac conduction problems: atrioventricular block
  - Others: diabetes and diabetic ketoacidosis, adrenocortical insufficiency, epilepsy, respiratory failure

  These associations are database-derived and should be verified against the product labelling.
- **Drug Interactions**: 84 interactions were recorded in total. Major-level interactions include:
  - Aminoglycosides: kanamycin, neomycin, streptomycin
  - Deferasirox
  - Iodinated contrast agents: diatrizoate, iodipamide, iodixanol, iohexol

  Moderate-level interactions include mesalazine, balsalazide, olsalazine, sulfasalazine, exenatide, vancomycin and picosulfuric acid.
- Systemic use of bacitracin carries a nephrotoxicity concern, which is relevant to the non-ocular predictions.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications for this indication, so evidence is at L5 (model prediction only). Many forms of punctate epithelial keratoconjunctivitis are viral or non-infectious, where bacitracin is unlikely to help. Several eye-related contraindication links also need review.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clarification of the dosage forms and approved indications for the Canadian licences
- Evidence on whether bacterial involvement exists in the target condition, through a literature review or a small exploratory study
- Review of the other top predictions: most are non-specific ontology categories or have no plausible link to bacitracin. Otitis externa (L4) is the only one with supporting literature, and it is better framed as a research question.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

