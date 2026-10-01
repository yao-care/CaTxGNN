---
layout: default
title: Ethambutol
parent: Moderate Evidence (L3-L4)
nav_order: 359
evidence_level: L4
indication_count: 5
---

# Ethambutol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **5** 
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

# Ethambutol: From Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is an antimycobacterial drug used in multidrug tuberculosis regimens. The Canadian licence records provided contain no indication text, so this original indication comes from the drug's known use and the retrieved literature. The TxGNN model predicts it may be effective for **epiglottitis**, but there are **0 clinical trials** and only **2 publications**, both on laryngeal tuberculosis rather than epiglottitis itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tuberculosis (inferred; licence indication text not provided) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ethambutol inhibits mycobacterial arabinosyltransferase (EmbB), which disrupts cell wall synthesis. This action is specific to mycobacteria.

The link to epiglottitis is indirect. The retrieved literature covers laryngeal tuberculosis, which can involve the epiglottis, and ethambutol treats the underlying mycobacterial infection. This does not make it a treatment for epiglottitis as a distinct condition, which is mostly caused by other bacteria. The very high TxGNN score (0.999) is not backed by any direct clinical evidence for epiglottitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14720571](https://pubmed.ncbi.nlm.nih.gov/14720571/) | 2004 | Review | The Lancet. Infectious diseases | Review of laryngeal tuberculosis (no abstract available) |
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Retrospective case series | The European respiratory journal | 41 laryngeal TB cases (1975–1985); the epiglottis was the second most common site after the true vocal cords. Patients were treated with multidrug regimens including ethambutol. |

Both papers describe tuberculous involvement of the larynx. Neither shows an effect of ethambutol alone.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 247979 | ETIBI |
| 247960 | ETIBI |

Dosage form and approved indication text are not available for these licences.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output plus indirect literature on laryngeal tuberculosis. There are no clinical trials, and the drug's activity is restricted to mycobacteria. Any benefit would apply only to tuberculous epiglottic involvement, which is already covered by standard antitubercular regimens.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Approved indication text for the two DINs
- Detailed mechanism of action data from DrugBank
- Direct evidence for ethambutol in epiglottitis, or a decision to reframe the question as tuberculous laryngeal or epiglottic disease

**Other predictions in this pack:**
- Peritonitis is the strongest of the other candidates (L3, "Research Question"). It corresponds to tuberculous peritonitis, where ethambutol is already a standard regimen component, so it is not a novel repurposing.
- Laryngitis is supported only by case reports of mycobacterial infection.
- Meningococcal infection and infectious otitis media have no supporting evidence and are biologically implausible.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

