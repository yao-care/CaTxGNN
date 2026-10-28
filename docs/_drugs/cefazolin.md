---
layout: default
title: Cefazolin
parent: Model Prediction Only (L5)
nav_order: 164
evidence_level: L5
indication_count: 8
monitor_inn: "CEFAZOLIN"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
last_modified_at: 2026-10-27
description: "Cefazolin: predicted new indication infectious otitis media (evidence level L5). Approved use: Not recorded in the local data"
---

# Cefazolin
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

## Cefazolin: first-generation cephalosporin (bacterial cell wall synthesis inhibitor) → infectious otitis media
{: .text-alpha }

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic that inhibits bacterial cell wall synthesis.
The TxGNN model predicts it may be useful for **infectious otitis media**, but **no clinical trials** and only **2 publications** (a case report and an unrelated review) were retrieved, and neither directly studies cefazolin as a treatment for this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | infectious otitis media |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 16 of 16) |
| Number of DINs | 16 (valid: 16) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Cefazolin is known to be a first-generation cephalosporin that binds penicillin-binding proteins and blocks bacterial cell wall synthesis. It is active against streptococci and methicillin-susceptible *Staphylococcus aureus*, which can cause otitis media.

The mechanistic link is only partial. Cefazolin has limited activity against the most common otitis pathogens, *Haemophilus influenzae* and *Moraxella catarrhalis*. This weakens the rationale compared with agents designed to cover those organisms.

The retrieved literature does not close this gap. One paper is a 2025 pediatric case report of Gradenigo syndrome (a complication of otitis media) treated with a ceftazidime–cefazolin empiric combination. The other is a 1986 review of Stevens-Johnson syndrome management that mentions otitis media only incidentally. Neither studies cefazolin for infectious otitis media itself, so the evidence level is L5 (model prediction only).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report | Annals of Otology, Rhinology, and Laryngology | Pediatric Gradenigo syndrome (petrous apicitis after acute otitis media) managed with empiric ceftazidime–cefazolin; a complicated condition, not uncomplicated otitis media, and a combination regimen |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Review of Stevens-Johnson syndrome management; otitis media appears only as part of one patient's history, so it is not relevant to efficacy |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02308959 | CEFAZOLIN FOR INJECTION USP | Not recorded | Not recorded |
| 02308967 | CEFAZOLIN FOR INJECTION USP | Not recorded | Not recorded |
| 02108119 | CEFAZOLIN FOR INJECTION | Not recorded | Not recorded |
| 02524791 | CEFAZOLIN SODIUM FOR INJECTION BP | Not recorded | Not recorded |
| 02437112 | CEFAZOLIN FOR INJECTION | Not recorded | Not recorded |

The approved indication text is not recorded in the local data. Sixteen single-ingredient licences are valid; this table lists five of them.

## Safety Considerations

- **Drug Interactions**: The interaction check completed with 100 records. The first entries were rated Moderate for the aminoglycosides kanamycin, neomycin and streptomycin, and for picosulfuric acid. Other listed interactions (for example calcitriol, epinephrine, amphotericin B, mannitol, acetylsalicylic acid, amoxicillin, metformin and omeprazole) have an unknown severity level.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no registered trials and no published study directly evaluating cefazolin for infectious otitis media. Cefazolin's spectrum also misses key otitis pathogens, so the clinical case is weak at this stage.

**To proceed, the following is needed:**
- Direct clinical or microbiological evidence of cefazolin efficacy in infectious otitis media, including coverage of *H. influenzae* and *M. catarrhalis*
- Comparison against guideline-recommended agents for otitis media
- Package insert warnings and contraindications from Health Canada
- Mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

