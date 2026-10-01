---
layout: default
title: Ampicillin
parent: Model Prediction Only (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin: From General Antibacterial Use to Laryngitis

## One-Sentence Summary

Ampicillin is a beta-lactam (aminopenicillin) antibiotic used against susceptible bacterial infections. The TxGNN model predicts it may be effective for **laryngitis** with a very high score (99.97%), but only **1 clinical trial** (an observational survey of a different drug) and **no ampicillin-specific studies** support this. Most laryngitis is viral, so the prediction is not clinically supported for the general condition and is at most plausible for bacterial laryngeal infections such as epiglottitis or laryngeal abscess.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied licence data (ampicillin is a general-purpose antibacterial for susceptible bacterial infections) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (no completed RCTs; the only trial is an observational survey of amoxicillin/clavulanate) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, ampicillin inhibits bacterial penicillin-binding proteins and so blocks cell-wall synthesis. Its efficacy in susceptible bacterial infections is established. Mechanistically, it could apply only to laryngitis or related laryngeal conditions with a bacterial cause.

The link is weak for laryngitis as a whole. Most laryngitis is viral, and antibiotics would not be expected to help. The literature retrieved for this prediction is about bacterial laryngeal-area conditions (epiglottitis, laryngeal abscess, actinomycosis), not routine laryngitis. The high graph score is therefore not supported clinically for the broad condition.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | Completed | 363 | Post-marketing survey of amoxicillin/clavulanate (CLAVAMOX) dry syrup in Japanese children with infections other than otitis media, including laryngitis. Ampicillin was not tested, so this is weak, indirect evidence. |

## Literature Evidence

No RCTs were retrieved for this indication. The entries below are the most relevant available, and none tests ampicillin for laryngitis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Review | CoDAS | AGREE II quality assessment of clinical guidelines for laryngitis and pharyngitis. Concerns guideline quality, not drug efficacy. |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Review | Anaesth Intensive Care | 161 children with acute epiglottitis, with 45 complications and 5 deaths. Focus is airway management. |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case report | Ann Otol Rhinol Laryngol | Spontaneous laryngeal abscess in a patient with uncontrolled diabetes, plus a review of reported cases. Laryngeal abscesses are rare in the antibiotic era. |
| [12402494](https://pubmed.ncbi.nlm.nih.gov/12402494/) | 2002 | Case report | Acta Otorrinolaringol Esp | Two paraglottic laryngeal abscesses with a literature review. Rapid diagnosis and treatment are needed. |
| [24930374](https://pubmed.ncbi.nlm.nih.gov/24930374/) | 2014 | Case report | J Voice | Laryngeal actinomycosis in a neutropenic patient, resolved after a prolonged penicillin course. |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | Case report | Auris Nasus Larynx | Laryngeal actinomycosis after bone marrow transplantation in a 14-year-old girl. |
| [6465636](https://pubmed.ncbi.nlm.nih.gov/6465636/) | 1984 | Case series | Ann Emerg Med | Three adults with epiglottitis; all had a benign course, but airway obstruction can occur. |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | Case series | West J Med | Nine adults with acute epiglottitis; 4 needed intubation and 6 were initially misdiagnosed. |
| [3347186](https://pubmed.ncbi.nlm.nih.gov/3347186/) | 1988 | Case report | Med J Aust | Three adult epiglottitis cases, with emphasis on variable presentation and diagnostic difficulty. |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Observational study | Otolaryngol Head Neck Surg | Perioperative antibiotic choice in laryngectomy and its association with complications. |

## Canada Market Information

Dosage form and approved indication text were not provided in the supplied data. The five main authorisations shown (of 17 in total):

| DIN | Product Name |
|---------|------|
| 2530481 | AMPICILLIN SODIUM FOR INJECTION BP |
| 1933345 | AMPICILLIN SODIUM FOR INJECTION, USP |
| 2462338 | AMPICILLIN SODIUM FOR INJECTION BP |
| 20877 | TEVA-AMPICILLIN |
| 2462346 | AMPICILLIN SODIUM FOR INJECTION BP |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the Evidence Pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no ampicillin-specific trials or studies for laryngitis. The only trial is an observational survey of a different drug, and the literature consists of reviews and case reports on rare bacterial laryngeal conditions. Since most laryngitis is viral, a broad laryngitis indication is not supported. Other predictions in this pack have more historical evidence but are not currently actionable (for example, gonococcal urethritis, where penicillinase-mediated resistance has removed ampicillin from current guidelines).

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A narrower, clinically defined target (for example, culture-proven bacterial epiglottitis or laryngeal abscess) rather than laryngitis in general
- Any ampicillin-specific comparative or observational data for that subgroup, given rising resistance and beta-lactamase production
- Approved indication text and dosage forms for the 17 DINs, to check route compatibility

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

