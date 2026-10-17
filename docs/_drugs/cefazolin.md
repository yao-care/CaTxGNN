---
layout: default
title: Cefazolin
parent: Moderate Evidence (L3-L4)
nav_order: 164
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-13
description: "Cefazolin: predicted new indication Infectious otitis media (evidence level L4). Approved use: Bacterial pneumonia, endocarditis, bacterial arthritis, cholangitis"
monitor_inn: "CEFAZOLIN"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
---

# Cefazolin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

# Cefazolin: From Bacterial Pneumonia and Other Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic, originally used for bacterial infections such as bacterial pneumonia, endocarditis, bacterial arthritis and cholangitis.
The TxGNN model predicts it may be effective for **infectious otitis media**, but there are currently **no registered clinical trials** and only **2 publications** (a case report and an unrelated review), so the evidence is indirect and weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia, endocarditis, bacterial arthritis, cholangitis (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available in the data compiled for this report. Based on known pharmacology, cefazolin is a first-generation cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. It is active against streptococci and methicillin-susceptible *Staphylococcus aureus*, which can cause otitis media.

Its original indications (pneumonia, endocarditis, bone and joint infections) are driven by the same gram-positive organisms, so a bacterial ear infection is a plausible extension. However, the link is limited. Cefazolin has weak activity against *H. influenzae* and *M. catarrhalis*, the most common otitis pathogens, and none against *Pseudomonas*. The high TxGNN score likely reflects proximity to other bacterial infection indications in the knowledge graph rather than direct clinical support.

Among the other ear-related predictions, **suppurative otitis media** has the strongest signal (a 1982 comparative study, L3). The remaining predictions (otosalpingitis, non-suppurative and allergic otitis media) rest on model scores alone and have a weak antibacterial rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case report/Case series | Ann Otol Rhinol Laryngol | Ceftazidime-cefazolin empiric combination for pediatric Gradenigo syndrome, a rare complication of petrous apicitis after acute otitis media |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Stevens-Johnson syndrome management; otitis media appears only incidentally in the case history, so it is not relevant to cefazolin efficacy |

Related evidence for suppurative otitis media, where the signal is stronger: [PMID 6752467](https://pubmed.ncbi.nlm.nih.gov/6752467/) (1982, Jpn J Antibiot), a controlled comparison of cefmetazole vs cefazolin in 172 evaluable patients, with cefazolin as the comparator.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02308959 | CEFAZOLIN FOR INJECTION USP | Injection | Not listed |
| 02308967 | CEFAZOLIN FOR INJECTION USP | Injection | Not listed |
| 02108119 | CEFAZOLIN FOR INJECTION | Injection | Not listed |
| 02524791 | CEFAZOLIN SODIUM FOR INJECTION BP | Injection | Not listed |
| 02437112 | CEFAZOLIN FOR INJECTION | Injection | Not listed |

Sixteen valid single-ingredient licences are held in total; only the first five are shown. Dosage forms are inferred from the product names (all are injectable).

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, congenital prothrombin deficiency.
- **Drug Interactions**: 100 interactions were found. The moderate-level ones are the aminoglycosides **kanamycin, neomycin and streptomycin**, and **picosulfuric acid**. Other interactions (e.g., amphotericin B, epinephrine, metformin, omeprazole, morphine) have an unknown severity level.

Please refer to the Health Canada package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no registered trials and the only directly cited publications are a case report and a non-relevant review. Cefazolin also has coverage gaps against the main otitis media pathogens, and better-suited agents already exist.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Contemporary comparative or randomized evidence in otitis media, with suppurative otitis media as the more promising sub-indication
- Review of pathogen coverage and local resistance patterns against current standard-of-care agents
- Assessment of route compatibility, as cefazolin is injectable only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

