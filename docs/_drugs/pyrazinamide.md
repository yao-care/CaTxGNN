---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 784
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pyrazinamide: predicted new indication Infectious otitis media (evidence level L5). Approved use: Pulmonary tuberculosis…"
monitor_inn: "PYRAZINAMIDE"
predicted_indications: ["infectious otitis media", "middle ear disease", "otosalpingitis", "chronic otitis media", "suppurative otitis media", "non-suppurative otitis media", "middle ear cholesterol granuloma", "allergic otitis media", "Lyme disease", "infectious otitis interna"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pyrazinamide: From Pulmonary Tuberculosis to Infectious Otitis Media
{: .text-alpha }

## One-Sentence Summary

Pyrazinamide is an anti-tuberculosis drug, originally used for pulmonary and meningeal tuberculosis.
The TxGNN model predicts it may be effective for **infectious otitis media** with a very high score, but **no clinical trials and no publications** support this specific prediction.
Related literature exists only for tuberculosis involving the middle ear (case reports), which is an extension of the approved TB use rather than a true new indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis, meningeal tuberculosis (tuberculous meningitis) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pyrazinamide is a first-line anti-tuberculosis agent whose activity is limited to *Mycobacterium tuberculosis* and depends on an acidic environment.

It has no activity against the usual bacterial causes of otitis media (*S. pneumoniae*, *H. influenzae*, *M. catarrhalis*). The high TxGNN score therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only plausible link is rare tuberculous otitis media, which is already covered by standard anti-TB therapy and the approved TB indication.

Other ear-related predictions follow the same pattern. Tuberculosis-related ones (middle ear disease, chronic and suppurative otitis media) are extrapulmonary TB extensions. Non-infectious or allergic ones (non-suppurative otitis media, cholesterol granuloma, allergic otitis media) have no plausible mechanistic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked prediction (infectious otitis media). The table below shows the most relevant publications for related predictions (middle ear disease, chronic and suppurative otitis media). All are case reports or animal studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Case report | Int J Mycobacteriol | Nasal and middle ear TB in a 55-year-old woman, treated with rifampicin, isoniazid and pyrazinamide for 9 months; no recurrence at 1 year |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Case report | Am J Kidney Dis | Tuberculous otitis media in a renal transplant recipient after recurrent empiric antibiotic treatment for chronic otitis media |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case report | Cureus | Tuberculous otitis media presenting as otorrhea; delayed diagnosis in a low-prevalence setting |
| [8011030](https://pubmed.ncbi.nlm.nih.gov/8011030/) | 1994 | Clinical observation | Laryngo-Rhino-Otologie | 12 patients with TB first found in the head and neck, including one with middle ear involvement |
| [21439219](https://pubmed.ncbi.nlm.nih.gov/21439219/) | 2011 | Animal study | J Am Assoc Lab Anim Sci | Torticollis in M. tuberculosis-infected mice, including those on pyrazinamide-containing regimens |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00618810 | PDP-PYRAZINAMIDE | Not specified | Not specified |

## Safety Considerations

- **Contraindications / risk conditions (from the knowledge graph, not label text)**: liver failure, acute liver failure, liver disease, hepatitis, gallbladder disease, porphyria (including inherited porphyria and porphyrin metabolism disease), gout, diabetes mellitus, diabetic ketoacidosis, peripheral neuropathy and other peripheral nervous system disease, substance abuse/dependence, and slow acetylator status.
- **Drug Interactions**: 56 interactions were identified in total. Two are rated Moderate: **picosulfuric acid** and **naltrexone**. Others, with unclassified severity, include pantoprazole, omeprazole, lansoprazole, morphine, prednisone, prednisolone, vancomycin, amphotericin B, metronidazole, glyburide and streptomycin.

Official package insert warnings and contraindications were not available for this report; please refer to the Health Canada package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for infectious otitis media rests only on a model score. Pyrazinamide has no activity against common otitis media pathogens, and no trials or literature support it. The literature found concerns tuberculous otitis media, which is already managed within standard anti-TB therapy and is not a new indication. Lyme disease (rank 9) is the only prediction flagged as a research question, based on a speculative persister-targeting hypothesis with no direct clinical evidence.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic argument for any non-TB indication
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form for the Canadian product
- Direct clinical or microbiological evidence for non-tuberculous otitis media, if this direction is to be pursued
- Preclinical or in vitro studies of pyrazinamide against *Borrelia* persisters, if the Lyme disease hypothesis is to be explored
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

