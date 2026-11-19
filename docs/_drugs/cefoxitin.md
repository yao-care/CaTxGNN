---
layout: default
title: Cefoxitin
parent: Model Prediction Only (L5)
nav_order: 165
evidence_level: L5
indication_count: 8
monitor_inn: "CEFOXITIN"
predicted_indications: ["infectious otitis media", "chronic otitis media", "suppurative otitis media", "middle ear disease", "Ureaplasma urethritis", "toxocariasis", "otosalpingitis", "non-suppurative otitis media"]
last_modified_at: 2026-11-05
description: "Cefoxitin: predicted new indication infectious otitis media (evidence level L5). In Canada: 2 DINs (2 marketed)"
---

# Cefoxitin
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

## Cefoxitin: cephamycin antibiotic → infectious otitis media
{: .text-alpha }

## One-Sentence Summary

Cefoxitin is a cephamycin-class injectable antibiotic that is marketed in Canada. The TxGNN model predicts it may be effective for **infectious otitis media**. Only **1 publication** was retrieved for this disease, and it is a review of MRSA that does not test cefoxitin as a treatment. There are **no clinical trials** for this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | infectious otitis media |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 2 of 2) |
| Number of DINs | 2 (marketed: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for cefoxitin: "Cefoxitin is an antibacterial drug. […] Cefoxitin is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Cefoxitin has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: Cefoxitin And Dextrose (cefoxitin sodium) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6c7e9485-1ede-411c-8c46-911439332864), label version 2019-07-29; accessed 2026-11-19.) Based on what is known, cefoxitin is a cephamycin with stability against many beta-lactamases. It is active against *Staphylococcus aureus*, *Streptococcus* species and anaerobes, which are organisms that can be involved in middle ear infections.

The prediction is plausible in terms of pathogen overlap, but it is not supported by clinical data. The only publication retrieved is a review of methicillin-resistant *S. aureus* (MRSA), and MRSA is intrinsically resistant to cefoxitin. That paper therefore gives no support for treatment efficacy. The high score is a model prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | 2020 | Review | Infection and Drug Resistance | One Health review of MRSA epidemiology, virulence and resistance; lists otitis media among the diseases MRSA can cause. It does not evaluate cefoxitin treatment. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02128187 | CEFOXITIN FOR INJECTION | Not recorded | Not recorded |
| 02128195 | CEFOXITIN FOR INJECTION | Not recorded | Not recorded |

Both authorisations are single-ingredient products and both are currently valid.

## Safety Considerations

- **Drug Interactions**: 35 interactions were identified in total. The main ones rated Moderate are kanamycin, neomycin, streptomycin, picosulfuric acid and dicoumarol. Heparin is rated Minor. Many others (for example vancomycin, metronidazole, omeprazole, morphine) have no assigned severity level.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trial and only one indirect publication, which concerns a pathogen (MRSA) that cefoxitin does not cover. The evidence rests on the model prediction alone (L5).

**To proceed, the following is needed:**
- Clinical or microbiological studies that directly test cefoxitin in otitis media, including local susceptibility data for the relevant pathogens
- Health Canada package insert warnings and contraindications
- Mechanism of action data

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cefoxitin And Dextrose (cefoxitin sodium) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6c7e9485-1ede-411c-8c46-911439332864) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

