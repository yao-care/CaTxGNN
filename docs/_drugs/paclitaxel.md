---
layout: default
title: Paclitaxel
parent: Model Prediction Only (L5)
nav_order: 692
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From Established Cancer Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a microtubule-stabilizing chemotherapy drug that is already marketed in Canada in several injectable forms.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **50 clinical trials** and **20 publications** currently supporting this direction.
Paclitaxel is already an established breast cancer therapy, so this prediction mainly reflects a gap in the label data (no original indication was recorded), not a true repurposing discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L1 (pack-assigned; see note in Conclusion) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology, paclitaxel stabilizes microtubules. This blocks normal cell division, causes mitotic arrest, and triggers programmed cell death in rapidly dividing tumour cells.

This mechanism does not depend on hormone-receptor status. That is why taxanes are used across breast cancer subtypes, including as a backbone for triple-negative disease, often combined with immune checkpoint inhibitors such as atezolizumab or pembrolizumab. A 2019 review in the evidence set describes paclitaxel as frequently used first-line treatment in breast cancer.

The Evidence Pack lists no original indications and the Canadian license records carry no indication text. The high score therefore mostly confirms an already-established use. The approved label should be checked before treating this as a new indication.

---

## Clinical Trial Evidence

Of 50 linked trials, the 10 most relevant are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: compares two dose-dense, dose-intensified neoadjuvant regimens, one with weekly paclitaxel, in high-risk early breast cancer |
| [NCT00005581](https://clinicaltrials.gov/study/NCT00005581) | Phase 3 | Unknown | 1000 | Adjuvant epirubicin + paclitaxel vs CEF in node-positive breast cancer |
| [NCT01426880](https://clinicaltrials.gov/study/NCT01426880) | Phase 2/3 | Completed | 595 | GeparSixto: adds carboplatin to anthracycline-taxane neoadjuvant therapy in triple-negative and HER2-positive early breast cancer |
| [NCT00455533](https://clinicaltrials.gov/study/NCT00455533) | Phase 2 | Completed | 384 | Neoadjuvant AC followed by ixabepilone vs AC followed by paclitaxel (the standard arm), with biomarker study |
| [NCT00281528](https://clinicaltrials.gov/study/NCT00281528) | Phase 2 | Terminated | 208 | Weekly vs every-2-week vs every-3-week nab-paclitaxel with bevacizumab in metastatic breast cancer |
| [NCT00915603](https://clinicaltrials.gov/study/NCT00915603) | Phase 2 | Completed | 113 | Weekly paclitaxel/bevacizumab ± everolimus as first-line treatment in HER2-negative metastatic breast cancer |
| [NCT01848197](https://clinicaltrials.gov/study/NCT01848197) | N/A | Unknown | 1000 | Paclitaxel every 2 weeks vs weekly as adjuvant treatment |
| [NCT05033769](https://clinicaltrials.gov/study/NCT05033769) | Phase 4 | Unknown | 82 | Eribulin vs paclitaxel in metastatic breast cancer, with immune response as the primary aim |
| [NCT00005649](https://clinicaltrials.gov/study/NCT00005649) | Phase 2 | Completed | Not reported | Capecitabine + standard paclitaxel as first- or second-line therapy in metastatic breast cancer |
| [NCT07074106](https://clinicaltrials.gov/study/NCT07074106) | Phase 2 | Not yet recruiting | 40 | De-escalated neoadjuvant chemotherapy for early triple-negative breast cancer, guided by TILs and imaging response |

---

## Literature Evidence

The set contains no randomized controlled trials for this indication. It consists of reviews, small clinical studies and preclinical work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Paclitaxel mechanisms and clinical effects in breast cancer; frequent first-line use, with resistance as a major obstacle |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Review of paclitaxel and docetaxel in breast and ovarian cancer; notes the licence extension to metastatic breast carcinoma |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase 2 trial | Cancer | Doxorubicin + paclitaxel in advanced breast carcinoma; examines the importance of prior adjuvant anthracycline therapy |
| [9164198](https://pubmed.ncbi.nlm.nih.gov/9164198/) | 1997 | Phase 2 trial | J Clin Oncol | Biweekly paclitaxel + cisplatin in advanced breast carcinoma (ECOG study) |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Real-world study | BioMed Res Int | Neoadjuvant epirubicin/cyclophosphamide followed by weekly paclitaxel-trastuzumab in HER2-positive breast carcinoma |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Clinical study | Cancer | Role of paclitaxel in multimodality treatment of inflammatory breast carcinoma |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | Dose-finding study | Ann Oncol | Maximum tolerable doses of 3-hour paclitaxel with cyclophosphamide in advanced breast cancer |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Preclinical | J Immunother Cancer | Paclitaxel's effect on tumour-associated macrophages may enhance PD-1 blockade in triple-negative breast cancer |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Preclinical/genetic | Nat Commun | TEKT4 germline variations are linked to breast cancer resistance to paclitaxel |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Computational | Chem Biol Drug Des | Patient-derived analysis of paclitaxel combinations and in vivo biomarkers |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02281066 | ABRAXANE for injectable suspension |
| 02391465 | Paclitaxel Injection USP |
| 02320150 | Paclitaxel Injection USP |
| 02496097 | Paclitaxel powder for injectable suspension (nanoparticle, albumin-bound paclitaxel) |
| 02244372 | Paclitaxel for Injection |

Dosage form and approved-indication text are not available in the license records.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule stabilizer) |
| Myelosuppression Risk | High (neutropenia is the typical dose-limiting effect of the class; this is general class knowledge, not from the pack). Please refer to the package insert for specifics. |
| Emetogenicity Classification | Low (general class knowledge) |
| Monitoring Items | CBC with differential, liver function, signs of peripheral neuropathy and hypersensitivity |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

No structured warnings, contraindications or drug-interaction data were available in the pack. The linked literature does report these adverse events with paclitaxel:

- **Peripheral neuropathy**: several supportive-care trials (acupuncture, cryotherapy, compression) target paclitaxel-induced neuropathy.
- **Pneumonitis**: a case series describes interstitial pneumonitis after the first paclitaxel exposure.
- **Eye effects**: case reports describe bilateral uveitis and corneal epithelial lesions.
- **Skin and nail effects**: a case report describes periarticular thenar erythema with onycholysis.
- **Amenorrhea**: the APT trial (paclitaxel + trastuzumab) examined chemotherapy-related amenorrhea.
- **Pregnancy**: one case report describes weekly paclitaxel given during pregnancy; this is anecdotal only.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Breast cancer is a well-supported use of paclitaxel, with multiple completed Phase 2 and Phase 3 trials in the linked set. However, the pack contains no original indication, mechanism, or safety label data, and the literature shows no RCTs specific to this indication. The L1 label rests on completed Phase 3 trials across the broader set of breast cancer predictions, and only one completed Phase 3 trial (GeparOcto) is listed under this indication. Treat the prediction as a label-completeness question rather than a new discovery until the label is confirmed.

**To proceed, the following is needed:**
- The Health Canada monograph for each DIN: indications, warnings, contraindications and drug interactions
- Confirmation of whether breast carcinoma is already an approved indication for each product
- Mechanism of action data from DrugBank
- Separate review of the solvent-based and albumin-bound products, since the trial evidence mixes the two formulations
- Subtype-specific evidence review (triple-negative, ER-positive, HER2-positive) before any narrower claim
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

