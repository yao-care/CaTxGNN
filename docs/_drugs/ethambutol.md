---
layout: default
title: Ethambutol
parent: Moderate Evidence (L3-L4)
nav_order: 361
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-13
description: "Ethambutol: predicted new indication Epiglottitis (evidence level L4). Approved use: Pulmonary tuberculosis"
monitor_inn: "Ethambutol"
predicted_indications: ["epiglottitis", "laryngitis", "meningococcal infection", "peritonitis", "infectious otitis media"]
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Ethambutol: From Pulmonary Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is an anti-mycobacterial drug originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **epiglottitis**,
but there are currently **no registered clinical trials** and only **1 publication** (a retrospective case series on laryngeal tuberculosis), so the evidence rests essentially on model prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis (from the TxGNN knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, ethambutol is a bacteriostatic anti-mycobacterial agent that is understood to inhibit arabinosyl transferase and so block synthesis of the cell-wall arabinogalactan. It is a standard component of multi-drug tuberculosis regimens.

The only linked publication describes laryngeal tuberculosis, in which the epiglottis was one of the affected sites. Ethambutol was part of the treatment there. This suggests the high prediction score reflects an anatomical association with tuberculosis, not a true epiglottitis indication.

Typical epiglottitis is caused by organisms such as *Haemophilus influenzae* type b and streptococci. Ethambutol has no activity against these. The prediction is therefore mechanistically weak, except for the rare tuberculous subset, which is essentially the original tuberculosis indication at a different site.

Other predicted indications were also reviewed:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Laryngitis | 99.71% | L4 | Relevant only to tuberculous or nontuberculous mycobacterial laryngitis. Evidence is case reports and small series, and several retrieved papers are off-topic. |
| 3 | Meningococcal infection | 99.63% | L5 | No evidence. *Neisseria meningitidis* lacks the mycobacterial target and has effective standard therapy. |
| 4 | Peritonitis | 99.20% | L3 | Supported for tuberculous peritonitis within standard combination therapy (including a systematic review, PMID 16197489). This extends the existing TB indication to an extrapulmonary site. |
| 5 | Infectious otitis media | 99.06% | L5 | No evidence. The common pathogens lack the target. |

Of the five, tuberculous peritonitis has the most support, though it is an extension of the existing indication, not new repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Case series (retrospective) | Eur Respir J | 41 cases of laryngeal tuberculosis (1975–1985). The epiglottis was among the affected sites, and patients were treated with isoniazid, rifampicin, ethambutol and other agents. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00247979 | ETIBI | Not available | Not available |
| 00247960 | ETIBI | Not available | Not available |

## Safety Considerations

- **Disease associations from the knowledge graph** (these come from graph contraindication edges, not package insert text): kidney disease, pyoureter, gout, diabetic retinopathy, diabetic cataract, and optic neuritis.
- **Drug Interactions**: 100 interactions were identified in total. The main moderate-level interactions are with metronidazole, picosulfuric acid, naltrexone, rosuvastatin, simvastatin, tinidazole, and aluminum hydroxide. Others, with the level listed as unknown, include proton pump inhibitors (omeprazole, pantoprazole, lansoprazole), corticosteroids (prednisone, prednisolone, hydrocortisone), morphine, vancomycin, and ranitidine.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of epiglottitis has no registered trials and only one retrospective case series, which concerns laryngeal tuberculosis, not typical bacterial epiglottitis. Ethambutol is not expected to be active against the usual causative organisms, so the high model score is probably not clinically meaningful.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, as this is a blocking gap for safety screening
- Confirmed mechanism of action data from DrugBank
- Approved indication text and dosage form for the Canadian DINs
- If pursuing this direction, redefine the question toward tuberculous infection of the larynx or peritoneum, where ethambutol already has a role within combination therapy
- Attention to ocular toxicity (optic neuritis) and renal function in any further evaluation, in light of the graph-derived contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

