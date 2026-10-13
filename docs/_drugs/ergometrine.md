---
layout: default
title: Ergometrine
parent: Model Prediction Only (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Ergometrine
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

# Ergometrine: From Uterine Smooth Muscle Contraction to Hypertrichosis

## One-Sentence Summary

Ergometrine (ergonovine) is an ergot alkaloid. It is marketed in Canada as an injectable product, and the data compiled for this report do not list an approved indication text. The TxGNN model's top prediction is **hypertrichosis**, but there are **no clinical trials and no publications** supporting it. The only indications with any literature are migraine and pulmonary hypertension, and that literature is indirect and points toward safety concerns rather than benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, ergometrine is an ergot alkaloid that acts on uterine smooth muscle through serotonergic, alpha-adrenergic and dopaminergic receptors.

No plausible mechanistic link to hypertrichosis was identified. Nothing in ergometrine's pharmacology connects it to the regulation of hair follicle growth. The high TxGNN score (rank 1205) appears to be an artifact of the knowledge graph, with no supporting clinical or literature data.

The other top-ranked predictions are similarly unsupported:

- **Ambras-type hypertrichosis, nephrogenic syndrome of inappropriate antidiuresis, congenital malformation syndromes, hair shaft abnormalities and leprosy:** all are genetic, structural or infectious conditions with no pharmacological rationale for an ergot alkaloid and no trials or publications.
- **Migraine disorder:** this is the most biologically plausible link. Ergot alkaloids such as ergotamine, dihydroergotamine and methysergide are established migraine agents acting through serotonin receptors and cranial vasoconstriction, and ergometrine shares the ergoline scaffold. However, ergometrine itself has no direct trials, and existing ergot and triptan options are better characterized.
- **Migraine with brainstem aura:** vasoconstrictors are generally avoided here because of theoretical ischemic risk.
- **Pulmonary hypertension:** ergot-related 5-HT2B activity has been linked to pulmonary hypertension and valvulopathy, so the signal points toward harm rather than benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked prediction (hypertrichosis). The table below shows the most relevant publications retrieved for the migraine-related predictions, which are indirect evidence only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9793694](https://pubmed.ncbi.nlm.nih.gov/9793694/) | 1998 | Review | Cephalalgia | Review of methysergide, an ergometrine derivative, as a serotonin antagonist/agonist for migraine prophylaxis; efficacy is supported by open and controlled studies, but this concerns a related drug, not ergometrine |
| [10971665](https://pubmed.ncbi.nlm.nih.gov/10971665/) | 2000 | Case report | Headache | Postpartum cerebral angiopathy with diffuse arterial narrowing and haemorrhage in a woman with chronic migraine with aura; highlights vasoconstrictive risk |
| [20509463](https://pubmed.ncbi.nlm.nih.gov/20509463/) | 2009 | Review (historical) | J R Coll Physicians Edinb | History of ergot of rye chemistry and pharmacology, 1900-1940; no efficacy data |

Literature retrieved for pulmonary hypertension (PMIDs [22731893](https://pubmed.ncbi.nlm.nih.gov/22731893/), [41844474](https://pubmed.ncbi.nlm.nih.gov/41844474/) and [3214444](https://pubmed.ncbi.nlm.nih.gov/3214444/)) covers pre-eclampsia management, uterotonics in pregnant patients with cardiac disease, and an unrelated animal study of nilvadipine. None of it supports a therapeutic role for ergometrine.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02441241 | ERGONOVINE MALEATE INJECTION USP | Not specified | Not specified |

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertensive disorder, hypertension, epilepsy, kidney disease, pyoureter, liver disease, gallbladder disease, stroke disorder, cerebrovascular disorder, susceptibility to ischemic stroke, cerebral infarction, arteriosclerosis obliterans and HELLP syndrome.
- **Drug interactions:** 83 interactions were recorded. Major interactions include:
  - Isometheptene
  - Epinephrine (including topical)
  - Ephedrine
  - Lorcaserin
  - Clarithromycin
  - Cobicistat

  Moderate interactions include doxycycline, tetracycline, minocycline, aprepitant, dexamethasone, cimetidine, miconazole and clotrimazole.
- **Additional concerns:** ergot derivatives carry vasospasm, stroke and cerebral angiopathy risks and are contraindicated in pregnancy.

Please also refer to the package insert, as label warnings and contraindications were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions rest only on a model score, with no trials, no publications and no plausible mechanism. Migraine is biologically plausible, but it has no direct ergometrine evidence and the vasoconstrictive safety profile argues against pursuing it over better-characterized ergot and triptan options.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- The approved indication text and dosage form for DIN 02441241
- Direct ergometrine efficacy data for any candidate indication, with migraine as the only one worth a research question
- A safety assessment of vasoconstrictive, cerebrovascular and drug interaction risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

