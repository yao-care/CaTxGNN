---
layout: default
title: Tetryzoline
parent: Model Prediction Only (L5)
nav_order: 897
evidence_level: L5
indication_count: 2
---

# Tetryzoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Tetryzoline: From Eye Drop Products to Nasal Cavity Disease

## One-Sentence Summary

Tetryzoline (tetrahydrozoline) is marketed in Canada mainly in over-the-counter eye drop products such as Visine.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but only **4 publications** (all from 1954-1956) and **no registered clinical trials** support this direction.
This is probably an established topical nasal decongestant use rather than a new repurposing finding, so the label should be confirmed first.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 (observational studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on the pharmacological class, tetryzoline is an imidazoline alpha-adrenergic agonist. It constricts the blood vessels of mucosal tissue, which reduces swelling and congestion.

This mechanism fits nasal cavity disease well, because nasal congestion is largely driven by swollen, engorged mucosal vessels. The 1950s literature describes tetryzoline (sold as "Tyzine") as a nasal decongestant.

The original indication is not recorded in the data, and none of the Canadian licences list an approved indication. The product names (eye drops) suggest an ocular use, but this is not confirmed. The nasal use is likely an already-known topical decongestant indication, so the model may be rediscovering existing use rather than proposing a new one.

The second-ranked prediction, acute laryngopharyngitis (score 99.98%), has no trials or literature. Its link, topical vasoconstriction reducing upper-airway mucosal edema, is plausible but unverified. Tetryzoline is formulated for nasal and ocular use, so pharyngeal or laryngeal application raises open questions about delivery, dosing and safety.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Abstracts were not available, so the summaries below are based on titles only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [13244019](https://pubmed.ncbi.nlm.nih.gov/13244019/) | 1954 | Clinical trial (design unclear, likely uncontrolled) | Medical Times | Reports a trial of tyzine as a more effective and better-tolerated nasal decongestant |
| [13294143](https://pubmed.ncbi.nlm.nih.gov/13294143/) | 1956 | Clinical observation | Eye, Ear, Nose & Throat Monthly | Observations on tyzine as a new nasal decongestant |
| [13309701](https://pubmed.ncbi.nlm.nih.gov/13309701/) | 1956 | Clinical evaluation (675 patients, likely uncontrolled case series) | New York State Journal of Medicine | Clinical evaluation of tyzine in 675 patients, described as a superior new nasal decongestant |
| [13382599](https://pubmed.ncbi.nlm.nih.gov/13382599/) | 1956 | Clinical evaluation (non-English) | Archivos Médicos Panameños | Clinical evaluation of tetrahydrozoline hydrochloride as a new nasal decongestant |

## Canada Market Information

Five of the 10 licences are listed. Dosage form and approved indication text were not provided for any of them.

| DIN | Product Name |
|---------|------|
| 1942425 | VISINE ORIGINAL |
| 2273446 | ORIGINAL EYE DROPS |
| 2338602 | VISINE MULTI-SYMPTOM |
| 2290596 | ALLERGY EYE DROPS |
| 2448955 | 8-SYMPTOM RELIEF |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the supporting evidence is limited to four uncontrolled clinical reports from the 1950s, with no registered trials. The nasal use is probably already established, so it is unclear whether this is true repurposing. Safety data from the Canadian package insert is also missing.

**To proceed, the following is needed:**
- Download and review the Health Canada package insert or monograph to confirm approved indications and obtain warnings and contraindications
- Confirm whether nasal decongestion is already a labelled or established use, to decide if this is a repurposing candidate
- Obtain mechanism of action data from DrugBank
- For acute laryngopharyngitis, assess pharyngeal or laryngeal delivery, dosing and safety before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

