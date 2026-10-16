---
layout: default
title: Nabilone
parent: Model Prediction Only (L5)
nav_order: 637
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Nabilone: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the Canadian licence data compiled for this report (…"
---

# Nabilone
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

# Nabilone: From Chemotherapy-Induced Nausea and Vomiting to Migraine Disorder

## One-Sentence Summary

Nabilone is a synthetic cannabinoid that is marketed in Canada. The data compiled for this report do not include its approved indication text. The TxGNN model predicts it may be effective for **migraine disorder**, but no clinical trials are registered for that indication. Only **1 systematic review** supports it directly, and that review is class-level evidence. The closest direct evidence is a small 2012 trial in the related condition of headache disorder (medication overuse headache).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Canadian licence data compiled for this report (nabilone is known to be approved for chemotherapy-induced vomiting refractory to other antiemetics, per a retrieved publication) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 (for migraine disorder; the related headache disorder entry reaches L3) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, nabilone is a synthetic CB1/CB2 cannabinoid receptor agonist, an analogue of delta-9-tetrahydrocannabinol (THC). It is approved for chemotherapy-induced vomiting that does not respond to other antiemetics.

The endocannabinoid system modulates trigeminovascular nociception, CGRP release and central pain processing. Those are pathways involved in migraine. This gives a plausible, though indirect, reason for the prediction.

The supporting evidence is limited. The one item linked to migraine is a 2026 systematic review of cannabinoid interventions for low back pain and migraine. Its title does not show whether nabilone-specific migraine data were included, so the evidence is class-level only. The closest direct evidence is a small 2012 trial of nabilone in medication overuse headache, listed under the broader headache disorder prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder. No trials are registered for the other predicted headache-related indications either.

---

## Literature Evidence

**Migraine disorder**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42773786](https://pubmed.ncbi.nlm.nih.gov/42773786/) | 2026 | Systematic Review | Cannabis and Cannabinoid Research | Reviews RCTs of isolated cannabinoids, synthetic cannabinoids, vaporized cannabis and standardized extracts for low back pain, migraine and medication-overuse headache. The abstract notes uncertainty about indication-specific value. |

**Related headache evidence (predicted indication rank 3: headache disorder)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23070400](https://pubmed.ncbi.nlm.nih.gov/23070400/) | 2012 | Preliminary double-blind, active-controlled randomized trial | J Headache Pain | 30 patients with long-standing intractable medication overuse headache. The study evaluated nabilone for pain, headache frequency, analgesic intake and quality of life. |
| [28281107](https://pubmed.ncbi.nlm.nih.gov/28281107/) | 2017 | Review | Curr Pain Headache Rep | Primer on cannabis for pain and headaches. It describes the endocannabinoid system as a basis for further research. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02256193 | CESAMET | Not listed | Not listed |
| 00548375 | CESAMET | Not listed | Not listed |
| 02312263 | CESAMET | Not listed | Not listed |
| 02380897 | PMS-NABILONE | Not listed | Not listed |
| 02384892 | TEVA-NABILONE | Not listed | Not listed |

All 9 licences are valid single-ingredient products. The list above shows 5 of them. The others are PMS-NABILONE and TEVA-NABILONE products.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for these.

- **Contraindication signals from the knowledge graph** (drug-disease links in the TxGNN knowledge graph, not label text):
  - Psychiatric: psychotic disorder, schizophrenia, schizoaffective disorder, schizophreniform disorder, mental disorder, anxiety disorder, neurotic disorder, dysthymic disorder
  - Substance use: substance-related disorder, substance abuse/dependence
  - Cardiovascular: hypertension and hypertensive disorder, hypotensive disorder, coronary artery disease, sudden cardiac arrest, heart conduction disease
  - Liver: liver failure
- **Drug interactions:** The interaction search returned 100 records. All 20 reviewed were rated Moderate. They include:
  - CNS depressants and opioids: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, alprazolam, amobarbital, ethanol
  - Sedating antihistamines: chlorpheniramine, cetirizine, phenyltoloxamine
  - Antidepressants: amitriptyline
  - Blood pressure agents: nifedipine, amlodipine, acebutolol, alfuzosin, amiloride, hydrochlorothiazide
  - Other: aldesleukin, dichloralphenazone

The psychiatric and cardiovascular signals matter for migraine patients. Many have comorbid anxiety or depression and may take blood pressure or sedating medicines.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The migraine prediction has a high model score (99.89%) and a plausible mechanism, but no registered trials and only class-level literature. The only direct nabilone evidence is a small preliminary trial in medication overuse headache, a related but different condition.
- The knowledge-graph contraindication signals (psychiatric, cardiovascular) and the missing label safety data add to the case for waiting.
- Other predictions are weaker. Several (atrophoderma vermiculata, nephrogenic syndrome of inappropriate antidiuresis, ulerythema ophryogenesis) have no plausible mechanism and are likely knowledge-graph artifacts.

**To proceed, the following is needed:**
- Confirm whether the 2026 systematic review includes nabilone-specific migraine data, and extract the effect sizes.
- Search for nabilone-specific migraine studies, and consider a small proof-of-concept trial.
- Obtain the Health Canada package insert (warnings, contraindications, approved indication, dosage form) for each licence.
- Obtain detailed mechanism of action data from DrugBank.
- Define a safety plan for patients with psychiatric, cardiovascular or substance-use comorbidity, and for those taking sedating medicines.
- Clarify whether the 2012 medication overuse headache trial can support a headache-focused development path.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

