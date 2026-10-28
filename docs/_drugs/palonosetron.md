---
layout: default
title: Palonosetron
parent: Moderate Evidence (L3-L4)
nav_order: 702
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-28
description: "Palonosetron: predicted new indication Migraine disorder (evidence level L4). Approved use: Not listed in the Canadian license data compiled for this report"
monitor_inn: "PALONOSETRON"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Palonosetron
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

## Palonosetron: From Chemotherapy-Related Nausea and Vomiting to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Palonosetron is a 5-HT3 receptor antagonist (an antiemetic) with marketed products in Canada. The TxGNN model predicts it may be effective for **migraine disorder**, but the evidence is very weak: **0 clinical trials** and **1 publication**, and that publication is a case report of palonosetron *causing* migraine-type headache, which points in the opposite direction from a therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data compiled for this report |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9974 |
| Evidence Level | L4 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, palonosetron is a 5-HT3 receptor antagonist. Serotonin signalling is implicated in migraine, so a theoretical link exists, and the high TxGNN score reflects proximity to migraine in the knowledge network.

This reasoning has important limits. The score reflects network proximity, not clinical proof. The only clinical literature reports palonosetron-induced migraine-type headache. Headache is a recognised adverse effect of the 5-HT3 antagonist class. Taken together, the available evidence suggests a possible adverse effect rather than a treatment benefit.

The other predicted indications are weaker still:
- **Migraine with brainstem aura** (score 0.9967, L5): derived from similarity to other migraine subtypes, with no specific evidence.
- **Atrophoderma vermiculata** (score 0.9913, L5) and **ulerythema ophryogenesis** (score 0.9907, L5): rare skin disorders with no identified mechanistic link to 5-HT3 blockade. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case report | Canadian Journal of Anaesthesia | Reports migraine-type headache induced by palonosetron, a safety signal rather than evidence of benefit |

A 2026 review (PMID 42748473, *European Heart Journal – Cardiovascular Pharmacotherapy*) was linked to a related migraine-susceptibility prediction. It covers QT prolongation with antiemetics and provides no efficacy data for migraine.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02381710 | ALOXI | Not specified | Not specified |
| 02468735 | AKYNZEO | Not specified | Not specified |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Examples of those rated **Major**:
  - Opioids and related analgesics: fentanyl, alfentanil, tramadol
  - Dextromethorphan
  - Triptans: almotriptan, sumatriptan
  - Amiodarone, amisulpride, amitriptyline, anagrelide

  Examples rated **Moderate** include abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin, propofol and loperamide.
- **Clinical note**: Several interacting drugs (e.g., amiodarone, amisulpride, amitriptyline, anagrelide) are associated with QT prolongation. Triptans are also common migraine treatments, so interactions would be directly relevant in a migraine population. The 2026 review points to antiemetic-related QT risk as a concern.
- **Adverse effect signal**: Headache, including migraine-type headache, has been reported with palonosetron.

Warnings and contraindications from the package insert were not available in the data compiled for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any clinical trial. The only clinical report suggests palonosetron can cause migraine-type headache, which argues against a therapeutic role. The other predicted indications have no supporting evidence at all.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications from Health Canada
- Mechanism of action data (for example from DrugBank)
- Preclinical or clinical evidence that 5-HT3 antagonism relieves or prevents migraine, and a review of the safety signal for headache
- A QT and drug-interaction risk assessment, especially with triptans and other QT-prolonging drugs
- Route and dosage form compatibility review for a migraine use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

