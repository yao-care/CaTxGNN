---
layout: default
title: Fosaprepitant
parent: Model Prediction Only (L5)
nav_order: 411
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Fosaprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "FOSAPREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia", "intracranial abscess", "retinitis", "Plasmodium falciparum malaria", "echinococcus granulosus infectious disease", "hyperargininemia"]
---

# Fosaprepitant
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

# Fosaprepitant: From Chemotherapy-Associated Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fosaprepitant is an intravenous prodrug of aprepitant, a substance P/NK1 receptor antagonist. It is marketed in Canada, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the Canadian license records contain no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Fosaprepitant is known to be a prodrug of aprepitant, which blocks the NK1 receptor (the receptor for substance P). This is general pharmacological knowledge and is not confirmed by the compiled data.

The link to NSIAD is weak. NK1/substance P signaling has been discussed in relation to central fluid regulation, but nothing in the data supports a mechanism in this disease. NSIAD is driven by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), which act downstream of vasopressin release. An NK1 antagonist would not be expected to correct that defect directly. The high score is therefore best treated as a hypothesis-generating output of the model, not as evidence of efficacy.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Pneumocystosis | 99.87% | L5 | No antifungal mechanism identified; likely a network artifact |
| 3 | Leprosy | 99.82% | L5 | No antimycobacterial mechanism identified |
| 4 | Cryptococcal meningitis | 99.79% | L5 | Only speculative blood-brain barrier or neuroinflammatory links |
| 5 | Multiple endocrine neoplasia | 99.76% | L5 | Hypothetical substance P/NK1 link in tumour biology |
| 6 | Intracranial abscess | 99.75% | L5 | No supported mechanism |
| 7 | Retinitis | 99.68% | L4 | One preclinical study (see below); the only prediction with any supporting publication |
| 8 | Plasmodium falciparum malaria | 99.64% | L5 | No antiparasitic mechanism identified |
| 9 | Echinococcus granulosus infection | 99.50% | L5 | No plausible mechanism |
| 10 | Hyperargininemia | 99.41% | L5 | No connection to NK1 antagonism |

Of the ten predictions, retinitis has the most (though still limited) supporting evidence. A mouse study reported that fosaprepitant blocked UVR-B-induced NK1 receptor expression in ocular tissues (PMID 32058829, 2021, *Ocular Immunology and Inflammation*). This is indirect, preclinical, and about UV-induced ocular injury, not retinitis in patients. Its relevance to retinitis needs verification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for nephrogenic syndrome of inappropriate antidiuresis.

---

## Literature Evidence

Currently no related literature available for nephrogenic syndrome of inappropriate antidiuresis.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02363356 | EMEND IV | Not listed | Not listed |
| 02549379 | FOSAPREPITANT FOR INJECTION | Not listed | Not listed |

Both licenses are valid single-ingredient products. No cancelled licenses are recorded.

---

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph (not label text) links fosaprepitant to a contraindication in **liver failure**.
- **Drug Interactions**: 100 interactions were identified in the DDI database. Two are rated **Major**: **eliglustat** and **naloxegol**. Many others are rated Moderate, including:
  - Corticosteroids: dexamethasone, hydrocortisone, betamethasone, budesonide, triamcinolone
  - Acid suppressants: rabeprazole, lansoprazole, cimetidine
  - Antidiabetic drugs: pioglitazone, glimepiride, saxagliptin, nateglinide
  - Others: clarithromycin, miconazole, alosetron, dronabinol, naldemedine

  Only 20 of the 100 interactions were available for review.

Please refer to the package insert for the full warnings and contraindications, which were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone (L5). There are no trials or publications for NSIAD, and the known mechanism of NSIAD (V2 receptor gain-of-function) does not plausibly connect to NK1 antagonism. Package insert safety data are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Health Canada package insert (warnings, contraindications, approved indications, dosage forms)
- Confirmed mechanism of action data from DrugBank
- A mechanistic rationale or preclinical data linking NK1 antagonism to NSIAD
- Consideration of retinitis as a possible alternative research question, starting with verification of the ocular study design and its relevance
- Review of the two Major interactions (eliglustat, naloxegol) and the hepatic-failure signal for any target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

