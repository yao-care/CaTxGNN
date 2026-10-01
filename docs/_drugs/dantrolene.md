---
layout: default
title: Dantrolene
parent: Moderate Evidence (L3-L4)
nav_order: 245
evidence_level: L3
indication_count: 9
---

# Dantrolene
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **9** 
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

# Dantrolene: From Skeletal Muscle Relaxant to Malignant Hyperthermia Susceptibility

## One-Sentence Summary

Dantrolene is a skeletal muscle relaxant. The available Health Canada records do not list an approved indication.
The TxGNN model predicts it may be effective for **malignant hyperthermia, susceptibility to**, with **0 registered clinical trials** and **19 publications**, including two consensus guidelines.
This is an established standard-of-care use rather than a true repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available Health Canada records |
| Predicted New Indication | Malignant hyperthermia, susceptibility to |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. The literature describes dantrolene as inhibiting RYR1-mediated Ca²⁺ release from the sarcoplasmic reticulum of skeletal muscle. Malignant hyperthermia (MH) is a pharmacogenetic skeletal muscle disorder, mainly caused by RYR1 mutations, in which volatile anaesthetics or succinylcholine trigger uncontrolled Ca²⁺ release. Dantrolene directly counteracts this process. A 2017 PNAS study reports that dantrolene requires Mg²⁺ to arrest MH.

The prediction is well supported. Two guidelines (Association of Anaesthetists 2020; European Malignant Hyperthermia Group 2021) and several reviews cover MH management, and a 1998 review calls dantrolene sodium the ultimate treatment. The empty original-indication field is most likely a data gap in the record, not a sign of a new use.

Other high-scoring predictions are also RYR1-related: King-Denborough syndrome, central core myopathy, multiminicore and centronuclear myopathies. Their evidence is indirect (case reports, genetic and preclinical studies) and supports only peri-anaesthetic MH risk management, not treatment of the myopathy itself. Predictions for periodic paralysis have no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered. The guidelines note that the rarity of MH and ethical limits mean there is no interventional trial evidence to guide management.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Guideline | Anaesthesia | Association of Anaesthetists MH 2020 guideline; genetically susceptible individuals are at risk on exposure to potent inhalational anaesthetics or suxamethonium |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Guideline | Br J Anaesth | European MH Group consensus on perioperative management of suspected or susceptible patients; notes no interventional trial evidence |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Review | Crit Care Med | Narrative expert review of epidemiology and management of critically ill MH patients |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Review | Orphanet J Rare Dis | MH is a hypermetabolic response of skeletal muscle to volatile anaesthetics and succinylcholine; incidence 1:10,000 to 1:250,000 anaesthetics |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Review | Anesthesiol Clin | MH affects calcium release channels; delayed diagnosis leads to multi-organ failure and death; mortality has improved |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanistic study | PNAS | Dantrolene alleviates MH symptoms via RyR and requires Mg²⁺ to arrest MH |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Review | Postgrad Med J | MH is an autosomal dominant trait; dantrolene sodium is the ultimate treatment; precautions for susceptible patients |
| [14661655](https://pubmed.ncbi.nlm.nih.gov/14661655/) | 2003 | Review | Best Pract Res Clin Anaesthesiol | Pathophysiology involves uncontrolled Ca²⁺ release from the sarcoplasmic reticulum |
| [23198031](https://pubmed.ncbi.nlm.nih.gov/23198031/) | 2012 | Review | Korean J Anesthesiol | MH susceptibility is autosomal dominant with variable expression and incomplete penetrance |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Review | Orphanet J Rare Dis | Early overview of MH as a pharmacogenetic disorder of skeletal muscle |

---

## Canada Market Information

| DIN | Product Name | Dosage Form (from product name) |
|---------|------|------|
| 1997572 | DANTRIUM INTRAVENOUS | Intravenous injection |
| 2529998 | DANTROLENE SODIUM FOR INJECTION, USP | Injection |
| 1997602 | DANTRIUM CAPSULES | Capsule |

The available records do not include approved indication text for any of the three products.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dantrolene has strong mechanistic and guideline support for MH, and it is already marketed in Canada in three products. The L3 grade reflects the lack of registered trials in the input, not weak clinical support. It is not a new-use finding.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking for safety screening)
- Confirmation of the approved indication text for each DIN
- Confirmation of label and guideline dosing
- Monitoring plan for hepatotoxicity and muscle weakness, especially in patients with an existing myopathy
- Detailed mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

