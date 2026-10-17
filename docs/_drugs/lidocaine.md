---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 548
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Lidocaine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Dermatitis, neuralgia, postherpetic neuralgia, hemorrhoid and others"
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
---

# Lidocaine
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

# Lidocaine: From Dermatitis and Neuralgia to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Lidocaine is a local anaesthetic originally used for conditions such as dermatitis, neuralgia, hemorrhoids and postherpetic neuralgia.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis, neuralgia, postherpetic neuralgia, hemorrhoid and others (the Canadian licence records contain no approved indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Lidocaine is generally known as a sodium channel blocker that suppresses nerve signalling. Its efficacy as a local anaesthetic and for neuralgic pain is well established, and mechanistically it might relieve pain and discomfort on the surface of the eye.

The link to punctate epithelial keratoconjunctivitis is therefore limited to symptom relief. There is no evidence that lidocaine changes the course of the disease. Topical anaesthetics can also be toxic to the corneal epithelium, which is a particular concern in a disease that already damages the epithelium. The high model score should be read as a computational signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered for this predicted indication.

## Literature Evidence

Currently no related literature available for this predicted indication.

## Other Predicted Indications Reviewed

The model also ranked nine other indications. None has strong support.

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Papillary conjunctivitis | 99.98% | L5 | No trials or literature; at most symptomatic anaesthesia |
| Rosacea conjunctivitis | 99.92% | L5 | No support; chronic topical anaesthetic use is inappropriate |
| Exposure keratitis | 99.87% | L5 | Only a case series on keratitis in methamphetamine abusers; unfavourable safety signal |
| Atopic conjunctivitis | 99.86% | L4 | Preclinical nerve and goblet cell work (PMID 37819721) and a small nasal anaesthesia study (PMID 8039024); no efficacy data for lidocaine |
| Conjunctival disorder | 99.84% | L4 | Two small trials (NCT05978687 and NCT01350024) and literature on pterygium surgery anaesthesia; this reflects use as an anaesthetic, not treatment of the disorder |
| Nephrotic syndrome | 99.83% | L4 | Pharmacokinetic studies and a methaemoglobinaemia case report; safety information only |
| Non-human animal disease | 99.82% | L5 | Non-specific category; one macaque seizure report |
| Tinea corporis | 99.82% | L5 | Only a pruritus review; no antifungal activity |
| Steroid-resistant nephrotic syndrome | 99.79% | L5 | Computational only; no plausible mechanism |

The strongest signal is for conjunctival disorder. Its trials are listed below to show what that evidence actually covers.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Completed | 41 | Lidocaine Ophtesic gel vs subconjunctival injection for pain during pterygium excision |
| [NCT01350024](https://clinicaltrials.gov/study/NCT01350024) | N/A | Completed | 34 | Two local anaesthesia methods compared for postoperative pain after drooping eyelid surgery |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | RCT | Eye | Lidocaine gel vs tetracaine drops as sole topical anaesthetic for primary pterygium surgery |
| [29135709](https://pubmed.ncbi.nlm.nih.gov/29135709/) | 2018 | Pilot study | Cornea | Subconjunctival injection vs 2% and 5% lidocaine gel in pterygium surgery |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Clinical study | Acta Ophthalmol Scand | Efficacy of lidocaine 2% gel in pterygium surgery |
| [16954710](https://pubmed.ncbi.nlm.nih.gov/16954710/) | 2006 | Clinical study | Ophthalmologica | Viscous lidocaine for pain relief after pterygium surgery |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective study with meta-analysis | J Neurol Neurosurg Psychiatry | Medical treatment of SUNCT and SUNA headache syndromes |
| [19250287](https://pubmed.ncbi.nlm.nih.gov/19250287/) | 2009 | Review | Cephalalgia | Neuropsychiatric side effects of lidocaine in headache treatment |

## Canada Market Information

Lidocaine has 20 valid single-ingredient licences in Canada and none cancelled. The data compiled for this report do not include dosage form or approved indication text for these products. Five main authorisations are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02485311 | LIDOCAINE | Not specified | Not specified |
| 02372983 | XYLOCAINE 0.5% | Not specified | Not specified |
| 02422018 | LIDOCAINE HYDROCHLORIDE INJECTION USP | Not specified | Not specified |
| 02003767 | XYLOCAINE SPRAY | Not specified | Not specified |
| 02419505 | LIDODAN 4% TOPICAL SOLUTION | Not specified | Not specified |

The product names indicate that injectable, spray and topical solution forms are marketed. Whether any ophthalmic formulation is licensed has not been confirmed.

## Safety Considerations

- **Contraindications and conditions of concern** (from knowledge-graph drug-disease links, not label text): hypertension, liver failure, liver disease, cirrhosis, epilepsy, kidney disease, adrenocortical insufficiency, Addison disease, hypothyroidism, open-angle glaucoma, herpes simplex virus keratitis, varicella zoster infection, measles, atopic eczema, osteoporosis, psychotic and other mental disorders, fungal infections, potassium deficiency and gastritis. Glaucoma and herpes simplex keratitis are especially relevant to ocular use.
- **Drug Interactions**: 100 interactions were identified. Major: bupropion. Moderate: aprepitant, cimetidine, liposomal morphine, obeticholic acid, polyethylene glycol (3350 with electrolytes), picosulfuric acid and sodium sulfate. Minor: dexamethasone, kanamycin, neomycin, omeprazole, streptomycin and troglitazone.
- **Literature safety signals**: neuropsychiatric and cardiac side effects with intravenous use (PMID 19250287); methaemoglobinaemia with combined topical agents in a child with nephrotic syndrome (PMID 41995267); possible corneal toxicity with topical anaesthetic misuse.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for punctate epithelial keratoconjunctivitis has a very high model score but no trials or literature. Lidocaine could at most relieve symptoms, and the risk of corneal epithelial toxicity works against its use in an epithelial disease. Across all ten predictions, the available evidence shows lidocaine as an anaesthetic or analgesic, not as a disease-modifying treatment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block safety screening
- Mechanism of action data, for example from DrugBank
- Confirmation of whether an ophthalmic lidocaine formulation is licensed in Canada
- Preclinical or early clinical data on corneal epithelial safety and symptom benefit in punctate epithelial keratoconjunctivitis
- A review of whether atopic conjunctivitis, which has mechanistic preclinical support, is a better research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

