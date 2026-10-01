---
layout: default
title: Loperamide
parent: Model Prediction Only (L5)
nav_order: 552
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Diarrhea to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is a widely marketed antidiarrheal, and the Canadian product names (for example "Diarrhea Relief") reflect this use.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis** with a very high score (99.97%), but there are **0 clinical trials** and **0 publications** for this prediction.
The prediction is best read as a knowledge-graph artifact rather than a pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhea (inferred from drug class and product names; the licence records contain no indication text) |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Loperamide is a peripherally restricted mu-opioid agonist that acts on the gut's myenteric neurons to slow motility and reduce secretion. Its efficacy in diarrhea is well established.

**The prediction is not mechanistically plausible.** Loperamide has no known antimicrobial, anti-inflammatory or ocular activity, and no pathway links a gut-restricted opioid to conjunctival infection or inflammation. The high score most likely comes from graph proximity to other conjunctivitis nodes. Ranks 1 and 3 and ranks 5–9 are all conjunctivitis variants, which supports this reading.

**Other top predictions**

| Rank | Predicted Indication | Evidence Level | Notes |
|---|---|---|---|
| 2 | Amebic dysentery | L4 | Only a case report of fulminant amoebic colitis after loperamide use. This is a harm signal, not support. |
| 4 | Gastroduodenitis | L4 | The only prediction in the GI domain, where symptom relief is plausible. It has one 1986 clinical report, and a 2026 case report shows a safety concern. |
| 3, 5–10 | Conjunctivitis variants and Angelucci syndrome | L5 | No mechanistic link and no clinical evidence. |

If any direction deserves follow-up, gastroduodenitis (symptom control only) is the most reasonable candidate. It is not a disease-modifying use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acute contagious conjunctivitis.

The broader "conjunctivitis" prediction (rank 3) matched two azithromycin trachoma trials (NCT04185402, NCT06289647). Loperamide is not studied in either, so they are spurious matches and give no evidence.

---

## Literature Evidence

Currently no related literature available for acute contagious conjunctivitis.

---

## Canada Market Information

There are 14 authorizations in total. The main ones are listed below. The records contain no dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 02238211 | RIVA-LOPERAMIDE |
| 02544989 | JAMP LOPERAMIDE |
| 02291800 | IMODIUM CALMING LIQUID |
| 02499517 | DIARRHEA RELIEF FAST DISSOLVE |
| 02552337 | DIARRHEA RELIEF LIQUID GELS |

---

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the Evidence Pack. Please refer to the Health Canada package insert for full safety information.

Literature retrieved for the lower-ranked predictions contains two safety signals:

- **Respiratory depression:** A 2026 case report (PMID 41924411) describes loperamide-induced respiratory depression in severe chemotherapy-related GI inflammation. Damaged mucosa may increase systemic absorption and central opioid effects.
- **Fulminant colitis in invasive infection:** A 2007 case report (PMID 17241255) describes fulminant amoebic colitis with toxic megacolon after heavy loperamide use. Antimotility agents are generally cautioned against in dysenteric illness.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no mechanistic rationale, no trials and no literature (L5), and its high score looks like a knowledge-graph artifact. Other predicted indications show safety signals rather than efficacy support.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A mechanistic or preclinical rationale for any ocular use, which currently appears absent
- If pursuing gastroduodenitis, a review of the 1986 clinical report's design and a safety assessment for use in inflamed gut

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

