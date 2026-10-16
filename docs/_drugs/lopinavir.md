---
layout: default
title: Lopinavir
parent: Moderate Evidence (L3-L4)
nav_order: 558
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Lopinavir: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV infectious disease"
---

# Lopinavir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Lopinavir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lopinavir was originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**,
but the support so far consists only of **3 preclinical publications** in macaques and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, lopinavir is an HIV-1 protease inhibitor, and its efficacy in HIV infection is established. SIV is a closely related lentivirus with a structurally similar protease, so antiviral activity is biologically plausible.

The literature found is preclinical, from macaque studies. These include quadruple antiretroviral therapy with rapid viral decay, a chimeric virus (SHIV) carrying an HIV-1 protease gene for testing protease inhibitors, and oral HAART that included lopinavir/ritonavir. This is essentially an extension of the original antiviral indication to an animal model, not a new human therapeutic indication. The high score (99.90%) mainly reflects similarity to the approved HIV indication rather than independent evidence.

Two other predictions were also reviewed. Feline acquired immunodeficiency syndrome (score 99.90%) is a veterinary indication with no trials and no literature. A rare neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter (score 99.90%) has no evident mechanistic link and is likely a graph-based artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical animal study | Journal of Virology | Four SIV-infected cynomolgus macaques given a 7-day course of quadruple antiretroviral therapy showed rapid viral decay |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical animal study | Microbes and Infection | A novel SHIV carrying the HIV-1 protease gene was built as an in vivo tool for testing protease inhibitors in rhesus macaques |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical animal study | Journal of Virological Methods | Oral AZT, 3TC and lopinavir/ritonavir for 28 days in two SHIV-infected macaques, assessing the effect on the CD8 subset |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02285533 | KALETRA | Not listed | Not listed |
| 02312301 | KALETRA | Not listed | Not listed |
| 02243644 | KALETRA | Not listed | Not listed |

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):** The knowledge graph links lopinavir to caution or contraindication in the following groups:
- **Cardiac:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, cardiomyopathy (including hypertrophic), myocardial ischemia, coronary artery disease
- **Liver and biliary:** liver disease, cirrhosis, gallbladder disease, chronic hepatitis B and C, hyperbilirubinemia, Gilbert syndrome
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hypertriglyceridemia, familial combined hyperlipidemia, potassium deficiency
- **Other:** pancreatitis, hemophilia

**Drug Interactions:** 65 interactions are recorded. Examples:
- **Major:** dolasetron, papaverine
- **Moderate:** acarbose, dapagliflozin, famotidine, levofloxacin, metformin, ondansetron, palonosetron, and several laxatives (bisacodyl, castor oil, lactulose, magnesium citrate, among others)
- **Minor:** cimetidine, clotrimazole

Lopinavir is typically co-formulated with ritonavir, a CYP3A4 inhibitor, which adds to interaction and feasibility concerns. Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is preclinical macaque data, and SIV infection is an animal-model extension of the original HIV indication rather than a new human indication. The high TxGNN score reflects similarity to the existing indication, not independent efficacy evidence.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Approved indication text for the three Canadian DINs
- A defined human or clinically relevant use case, since SIV and feline AIDS are animal indications
- Review of cardiac, hepatic and metabolic risks and the interaction profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

