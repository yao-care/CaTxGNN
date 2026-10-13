---
layout: default
title: Imiquimod
parent: Model Prediction Only (L5)
nav_order: 475
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: From Common Wart and Actinic Keratosis to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical immune response modifier, originally used for skin and HPV-related conditions such as common warts, anogenital HPV infection, superficial basal cell carcinoma, and actinic keratosis.
The TxGNN model predicts it may be effective for **pre-malignant neoplasm**,
with **2 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Common wart, anogenital HPV infection, superficial multifocal basal cell carcinoma, actinic keratosis (the original-indication list is drawn from the TxGNN knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 (as assigned in the compiled data; see the note in the conclusion) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Imiquimod is a Toll-like receptor 7 (TLR7) agonist. When applied to the skin, it induces local release of type I interferon and pro-inflammatory cytokines, which in turn activates innate and adaptive anti-tumour and antiviral immunity. Detailed mechanism-of-action data were not otherwise available in the compiled data, so this description comes from the mechanistic rationale in the evidence review.

Many of imiquimod's known uses are already pre-malignant or HPV-driven epithelial lesions. Actinic keratosis, for example, is a pre-malignant skin lesion and one of its original indications. The same immune mechanism plausibly applies to related intraepithelial neoplasias, namely vulval (VIN), cervical (CIN), and anal canal (AIN) intraepithelial neoplasia. Cochrane reviews of VIN and AIN, reviews of topical treatment for non-melanoma skin cancer, and case reports support this use.

Note that "pre-malignant neoplasm" is a broad umbrella term. Evidence differs considerably between lesion types, so the prediction should be read lesion by lesion rather than as a single claim.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label, single-arm study of imiquimod 5% cream three days per week in actinic keratoses on the head, assessing how long the effect lasts. Small and uncontrolled, so supportive but not definitive. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomised trial of topical imiquimod versus standard excision (LLETZ) for high-grade cervical intraepithelial neoplasia. Stopped after only 9 participants, so underpowered and unable to support efficacy conclusions. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia, a pre-malignant HPV-associated condition. |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia, where surgery has high morbidity and relapse. |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer. |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, a pre-malignant lesion that can progress to squamous cell carcinoma. |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical strategies, including imiquimod, for non-melanoma skin cancer and precursor lesions. |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | Successful imiquimod 5% treatment of high-grade VIN in a renal transplant recipient. |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | Clearance of penile bowenoid papulosis with imiquimod 5% cream. |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical | Urol Oncol | Rat pharmacokinetic and pharmacodynamic study of intravesical TLR7 agonists (TMX-101 and TMX-202, not imiquimod itself). |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02482983 | TARO-IMIQUIMOD PUMP | Not specified | Not specified |
| 02365561 | VYLOMA | Not specified | Not specified |
| 02340445 | ZYCLARA | Not specified | Not specified |
| 02239505 | ALDARA P | Not specified | Not specified |

All four products are valid single-ingredient authorisations; none are cancelled.

---

## Cytotoxicity

Imiquimod is used for skin cancer and pre-cancerous lesions, but it is an immune response modifier rather than a conventional cytotoxic chemotherapy agent. Detailed cytotoxicity and handling data were not available in the compiled data, so please refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from drug-disease graph edges, not from label text): photoparoxysmal response, photosensitivity disease, autoimmune disease, graft versus host disease, and sunburn.
- **Drug interactions**: The interaction screen identified 59 potential interacting drugs, none with an assigned severity level. Examples include pantoprazole, omeprazole, lansoprazole, morphine, prednisone, prednisolone, simvastatin, warfarin, clopidogrel, hydroxychloroquine, and ibuprofen.
- **Reported adverse events in the literature**: case reports describe malignant conversion of florid oral papillomatosis during imiquimod treatment, erythema multiforme, and lichen planopilaris after imiquimod use.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the Health Canada package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is well understood and is already validated clinically in actinic keratosis, an original indication. Cochrane reviews and case reports support use in related intraepithelial neoplasias. However, the trial evidence is weak: one small single-arm study (n=20) and one terminated randomised trial (n=9). The L1 label assigned in the compiled data is generous. Neither trial meets the usual standard of at least two completed Phase 3 randomised trials, and the data also show that evidence varies widely across the lesion types within this broad category. The product is already marketed in Canada, which lowers the barrier to further work.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block formal safety screening.
- Narrowing the broad "pre-malignant neoplasm" category to specific lesion types (such as VIN, CIN, or AIN) and gathering lesion-specific efficacy data.
- Adequately powered randomised trials in the chosen lesion types, since the existing trials are small or terminated.
- Review of safety signals, including the autoimmune and photosensitivity-related contraindications flagged by the knowledge graph, and the reported cases of malignant conversion and skin reactions.
- Confirmation of the approved indications, dosage forms, and routes for the four Canadian products.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

