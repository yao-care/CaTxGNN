---
layout: default
title: Tenofovir Disoproxil
parent: Model Prediction Only (L5)
nav_order: 893
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Tenofovir Disoproxil: predicted new indication Feline acquired immunodeficiency syndrome . The best-supported predic… (evidence level L5). Approved use: Chronic hepatitis B virus infection"
monitor_inn: "Tenofovir disoproxil"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Tenofovir Disoproxil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Tenofovir Disoproxil: From Chronic Hepatitis B and HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tenofovir disoproxil is an antiviral originally used to treat chronic hepatitis B virus infection, HIV infection and AIDS.
The TxGNN model's top-ranked prediction is feline acquired immunodeficiency syndrome. However, it has only one supporting publication and is a veterinary indication, so this report focuses on the best-supported prediction, **simian immunodeficiency virus (SIV) infection**. That prediction has **no registered clinical trials** and **19 publications**, nearly all of them animal-model studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis B virus infection; HIV infection; AIDS (the Canadian licence records contain no approved indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (rank 1; veterinary). The best-supported prediction is simian immunodeficiency virus infection (rank 2). |
| TxGNN Prediction Score | 99.95% (both feline AIDS and SIV infection) |
| Evidence Level | L4 (preclinical/animal studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Tenofovir is a nucleotide reverse transcriptase inhibitor: it terminates viral DNA chain elongation, and this is the basis of its use in HIV and hepatitis B.

Feline immunodeficiency virus (FIV) and simian immunodeficiency virus (SIV) are both lentiviruses closely related to HIV. Their reverse transcriptases are similar enough that a shared mechanism is plausible. SIV and SHIV (simian-human immunodeficiency virus) infection in macaques are standard animal models of HIV. The macaque studies show partial to substantial protection by tenofovir disoproxil, alone or with emtricitabine.

These results mainly support the existing human HIV indications as translational evidence. SIV infection and feline AIDS are not new human indications, so they are not true repurposing opportunities. The very high TxGNN scores largely reflect similarity to HIV.

The other two predictions, a rare neurodevelopmental disorder (99.95%) and an obsolete familial combined hyperlipidemia term (99.60%), have no identifiable mechanistic link, no trials and no literature. They are most likely network-level artifacts rather than real biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Selected publications for SIV infection (all animal or review studies, no human trials of the predicted indication):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal study | J Infect Dis | Oral FTC/TDF prevented vaginal SHIV infection in macaques despite co-infection with Chlamydia and Trichomonas |
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Animal study | J Infect Dis | TDF chemoprophylaxis gave partial protection against repeated SHIV challenges in macaques |
| [24043812](https://pubmed.ncbi.nlm.nih.gov/24043812/) | 2013 | Animal study | PNAS | A TDF-eluting intravaginal ring completely protected macaques from multiple vaginal SHIV challenges |
| [27275923](https://pubmed.ncbi.nlm.nih.gov/27275923/) | 2016 | Animal study | PLoS One | Pod-intravaginal rings delivering TDF and FTC protected macaques from multiple SHIV exposures |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Animal study | J Infect Dis | Oral FTC/TDF prophylaxis against a tenofovir-resistant (K65R) SHIV in macaques |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Animal study | J Acquir Immune Defic Syndr | Oral TDF and topical GS-7340 were evaluated for protecting infant macaques from repeated oral SIV challenges |
| [12404171](https://pubmed.ncbi.nlm.nih.gov/12404171/) | 2002 | Animal study | J Infect Dis | Low-dose topical TDF for infant macaques exposed repeatedly to oral SIV |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Animal study | AIDS Res Hum Retroviruses | A VLP HIV vaccine combined with partially protective oral PrEP prevented SHIV infection in macaques |
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Animal study | J Infect Dis | HAART in SIV-infected macaques reduced CNS viral replication and inflammation, but viral DNA persisted |
| [14557287](https://pubmed.ncbi.nlm.nih.gov/14557287/) | 2003 | Review | Clin Microbiol Rev | Reviews acyclic nucleoside phosphonates (cidofovir, adefovir, tenofovir) against DNA virus and retrovirus infections |

For feline AIDS, the only publication is [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) (2023, *Viruses*), a study of combination antiretroviral therapy (dolutegravir, tenofovir, emtricitabine) in FIV-infected cats. The abstract available for this report is truncated, so its results could not be confirmed.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02247128 | VIREAD | Not specified | Not specified |
| 02403889 | TEVA-TENOFOVIR | Not specified | Not specified |
| 02453940 | PMS-TENOFOVIR | Not specified | Not specified |
| 02274906 | TRUVADA (emtricitabine/tenofovir) | Not specified | Not specified |
| 02452634 | MYLAN-TENOFOVIR DISOPROXIL | Not specified | Not specified |

These are 5 of the 20 valid licences, all single-entity records. They include generic tenofovir products and emtricitabine/tenofovir products.

## Safety Considerations

The knowledge graph lists the following drug-disease contraindication associations. They are not taken from label text and should be verified against the package insert:

- **Liver and kidney:** liver failure, liver disease, kidney disease, fatty liver disease, non-alcoholic steatohepatitis, Fanconi renotubular syndrome
- **Metabolic and bone:** lactic acidosis, hypophosphatemia, osteomalacia, rickets, hypertriglyceridemia, obesity disorder, monogenic obesity
- **Cardiac:** long QT syndrome (including familial), torsades de pointes
- **Infectious:** chronic hepatitis C virus infection, hepatitis C virus infection
- **Neuropsychiatric:** epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, delusional disorder, paranoid schizophrenia
- **Other:** gallbladder disease, pyoureter, obsolete pathologic fracture

No drug interaction records were found. Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indications (feline AIDS and SIV infection) are animal diseases. The evidence is limited to preclinical and veterinary studies (L4). It mainly supports the existing human HIV use rather than a new repurposing opportunity. The remaining two predictions have no evidence and no plausible mechanism.

**To proceed, the following is needed:**
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from Health Canada, including approved indication text, dosage forms and manufacturers for the licences
- Confirmation of whether the 2023 FIV study actually evaluated tenofovir, and with what results
- A decision on whether a veterinary or translational-model indication is within the scope of this repurposing programme. If not, the evaluation should be reframed around human indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

