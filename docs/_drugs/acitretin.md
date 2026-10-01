---
layout: default
title: Acitretin
parent: Moderate Evidence (L3-L4)
nav_order: 22
evidence_level: L4
indication_count: 4
---

# Acitretin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Acitretin: From Psoriasis to Acne

## One-Sentence Summary

Acitretin is an oral second-generation retinoid. The literature describes its main success in psoriasis, but the Canadian licence records supplied here do not state an indication.
The TxGNN model predicts it may be effective for **acne (disease)**, but there is **no acitretin-specific clinical trial** and **no acitretin-specific acne study** in the evidence set. The only registered trial is about isotretinoin and COVID-19, and the clinical literature that does exist concerns acne inversa (hidradenitis suppurativa), a different disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records; the literature describes psoriasis as its main use |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.94% (model rank 1601) |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acitretin is a second-generation retinoid, and retinoids as a class act through RAR/RXR nuclear receptors. They normalize keratinocyte differentiation, have anti-inflammatory effects, and reduce sebaceous gland activity and follicular keratinization. These are all plausible levers in acne. This mechanism is inferred from the retinoid class, not from acitretin-specific data.

There are two important caveats.

1. **The score reflects the retinoid class, not acitretin.** The high TxGNN score most likely comes from class-level retinoid associations in the knowledge graph. The strongest acne evidence in the literature is for isotretinoin, whose anti-acne effect is attributed to inhibition of sebaceous gland activity. Acitretin has weaker sebosuppressive effects.
2. **The clinical signal is for a related but different disease.** The acitretin-specific publications concern acne inversa/hidradenitis suppurativa, a chronic follicular inflammatory disease. They do not concern acne vulgaris. One long-term report on acitretin in hidradenitis suppurativa exists, but it sits in a body of work described as low-level evidence.

The model's other top predictions have no trials or literature and are not supported. These are pediatric systemic lupus erythematosus, fetal erythroblastosis, and a rare familial telangiectasia/cancer syndrome. Fetal erythroblastosis in particular looks like a knowledge-graph artifact, since acitretin is contraindicated in pregnancy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04663906](https://clinicaltrials.gov/study/NCT04663906) | N/A | Unknown | 300 | Tests whether oral **isotretinoin** (not acitretin) increases the risk of COVID-19 infection and complications. It does not test efficacy in acne and offers no direct support for acitretin. |

---

## Literature Evidence

No randomized controlled trials were found. The table lists the most relevant items, with guidelines, systematic reviews and reviews ahead of case-level reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [25640693](https://pubmed.ncbi.nlm.nih.gov/25640693/) | 2015 | Guideline | J Eur Acad Dermatol Venereol | European guideline for hidradenitis suppurativa/acne inversa, a chronic inflammatory follicular disease. It is not specific to acitretin or acne vulgaris. |
| [28476075](https://pubmed.ncbi.nlm.nih.gov/28476075/) | 2017 | Systematic review | Cochrane Database Syst Rev | Update on drugs for discoid lupus erythematosus; this is the cutaneous-lupus context behind the lupus prediction. |
| [29234829](https://pubmed.ncbi.nlm.nih.gov/29234829/) | 2018 | Review | Der Hautarzt | Drug therapy of acne inversa: antibiotics (clindamycin plus rifampicin) and TNF-α inhibitors are highlighted, and adalimumab is the only approved systemic product. |
| [26617362](https://pubmed.ncbi.nlm.nih.gov/26617362/) | 2016 | Review | Dermatol Clin | Medical treatments for hidradenitis suppurativa have low levels of evidence and need validation in randomized trials. |
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Review | Clin Dermatol | Overview of vitamin A and retinoids in dermatology, listing acitretin among the oral retinoids. |
| [9074840](https://pubmed.ncbi.nlm.nih.gov/9074840/) | 1997 | Review | Drugs | Retinoids are used in psoriasis, hyperkeratotic disorders and severe acne; includes the classification of synthetic retinoids by generation. |
| [1617858](https://pubmed.ncbi.nlm.nih.gov/1617858/) | 1992 | Review | Clin Pharmacokinet | Isotretinoin benefits severe recalcitrant acne. Acitretin and etretinate, the second-generation retinoids, have had their major success in psoriasis. |
| [8573927](https://pubmed.ncbi.nlm.nih.gov/8573927/) | 1995 | Review | Dermatology | Isotretinoin's efficacy in acne is attributed to inhibiting sebaceous gland activity; asks whether newer oral retinoids' anti-acne effect can be predicted from experimental models. |
| [20874789](https://pubmed.ncbi.nlm.nih.gov/20874789/) | 2011 | Clinical report (type not classified) | Br J Dermatol | Long-term results of acitretin in hidradenitis suppurativa. Isotretinoin has only limited effect there, and scattered case reports of acitretin had been promising. |
| [12080949](https://pubmed.ncbi.nlm.nih.gov/12080949/) | 2002 | Case report | Cutis | Single patient with severe nodulocystic acne and hidradenitis suppurativa. The title reports acitretin treatment; the abstract excerpt describes two earlier isotretinoin courses with partial improvement. |

---

## Canada Market Information

Health Canada lists 6 licences; five are shown. The records supplied here do not include dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 2468840 | MINT-ACITRETIN |
| 2070847 | SORIATANE |
| 2468859 | MINT-ACITRETIN |
| 2466082 | TARO-ACITRETIN |
| 2070863 | SORIATANE |

---

## Safety Considerations

- **Pregnancy and teratogenicity**: Acitretin is highly teratogenic, with a very long post-treatment contraception window. It is contraindicated in pregnancy, which limits its use in acne populations, who are often of reproductive age.
- **Pediatric use**: Long-term retinoid exposure raises additional concerns about bone and growth effects.
- **Drug interactions**: The interaction query returned no results, which is not the same as no interactions.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score reflects retinoid class associations rather than acitretin-specific evidence. No trial or study tests acitretin in acne vulgaris, and acitretin has weaker sebosuppressive effects than isotretinoin, which already serves this role. Acitretin's teratogenic risk and very long contraception window weigh further against use in acne. At present this is a research question only.

**To proceed, the following is needed:**
- The Health Canada product monograph, to obtain warnings, contraindications and approved indications (a blocking gap for safety screening)
- Mechanism of action data for acitretin from DrugBank
- Acitretin-specific acne data, ideally a comparison with isotretinoin
- If the hidradenitis suppurativa signal is of interest, a separate evaluation of that indication
- A pregnancy-prevention plan covering the long post-treatment contraception window
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

