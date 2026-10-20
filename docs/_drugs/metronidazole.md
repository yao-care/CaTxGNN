---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 611
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Metronidazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Peritonitis, endocarditis, anaerobic bacterial infections, giardiasis…"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
---

# Metronidazole
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

# Metronidazole: From Anaerobic and Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is an antimicrobial originally used for anaerobic bacterial infections, giardiasis, bacterial vaginosis and rosacea.
The TxGNN model predicts it may be effective for **pneumocystosis**, with a very high score, but **no clinical trials** and only **10 publications** (mostly general reviews and case reports, none showing metronidazole activity against Pneumocystis) are available.
The prediction is therefore best treated as a computational signal rather than an evidence-backed lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peritonitis, endocarditis, anaerobic bacterial infections, giardiasis, rosacea, bacterial vaginosis and related conditions (from the knowledge graph; no approved-indication text is available for the Canadian licences) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 15 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on general pharmacology, metronidazole is a nitroimidazole that is activated by reduction of its nitro group in anaerobic bacteria and protozoa, producing DNA-damaging radicals. Its efficacy in anaerobic infections and protozoal diseases such as giardiasis is well established.

The link to pneumocystosis is weak. Pneumocystis is a fungus and lacks this reductive activation pathway. The retrieved literature consists of general antiparasitic reviews, HIV opportunistic infection overviews and case reports in which metronidazole was given for a coexisting infection such as amoebiasis. None of it shows metronidazole efficacy against Pneumocystis. The high score is probably driven by network proximity to antiprotozoal and anti-infective drugs rather than a true mechanistic fit. The standard treatment cited in the literature is trimethoprim-sulfamethoxazole.

Other predictions in the list have more plausible biology, though still limited evidence:
- **Cap polyposis** (L3): case reports and small series describe remission with metronidazole, possibly through anti-inflammatory action.
- **Ulceration of vulva** (L3): metronidazole has an established role in vulvar Crohn's disease and genital amebiasis, with a 22-patient retrospective study and a systematic review.
- **Ulcerative proctosigmoiditis** (L4): plausible through gut dysbiosis, but evidence is indirect.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clinic Proceedings | General review of antiparasitic agents; no Pneumocystis-specific data for metronidazole |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Lists metronidazole for amoebiasis and trichomoniasis; trimethoprim-sulfamethoxazole for Pneumocystis pneumonia |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clinical Pharmacokinetics | Pharmacokinetic rationale for antiprotozoal therapy |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | Treatment of AIDS infectious complications, including Pneumocystis carinii pneumonia |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | Overview of HIV-related opportunistic infections |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Reviews of Infectious Diseases | Critique of antimicrobial prophylaxis trials |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | American Review of Respiratory Disease | Pneumocystis and cytomegalovirus pneumonia in a patient previously treated with metronidazole for diarrhoea |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | Two AIDS patients; metronidazole used for amoebic dysentery, with Pneumocystis pneumonia as a separate problem |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | Colon perforation with peritonitis in an AIDS patient with cytomegalovirus and amoebic colitis |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Case report | J Med Case Reports | Streptococcus intermedius cerebellar abscess as first presentation of sarcoidosis |

Clinical trials: currently no related clinical trials registered.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02092832 | METROGEL 0.75% | Not specified | Not specified |
| 02297809 | METROGEL 1% | Not specified | Not specified |
| 02518767 | METRONIDAZOLE | Not specified | Not specified |
| 02519755 | M-METRONIDAZOLE | Not specified | Not specified |
| 00545066 | APO-METRONIDAZOLE TABLETS | Tablet | Not specified |

Fifteen valid single-ingredient licences are listed in total; the table shows the first five. Others include injection, gel and combination-brand products such as NIDAGEL and PYLERA.

---

## Safety Considerations

**Contraindication-related conditions (knowledge graph, not label text):** liver failure, liver disease, epilepsy, kidney disease, haematological disease, neutropenia, leukopenia, agranulocytosis, blood coagulation disease, peripheral neuropathy and other peripheral nervous system disease, brain disease, optic nerve disease, visual pathway disease, congestive heart failure, diabetes mellitus, diabetic ketoacidosis, gout, gallbladder disease, dermatitis, substance abuse/dependence, non-infectious meningitis, and pyoureter.

**Drug interactions:** 100 interactions were identified; the first 20 reviewed include:
- **Major:** ethanol
- **Moderate:** paclitaxel, adalimumab, trastuzumab emtansine, ethinylestradiol, estradiol, butalbital, amiodarone, celecoxib, amobarbital, loperamide
- **Minor:** abiraterone, tramadol, famotidine, salbutamol, alfuzosin, amisulpride, amitriptyline, anagrelide, propofol

Please refer to the package insert for official warnings and contraindications, as label text was not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials, the biology does not fit (Pneumocystis is a fungus), and the literature does not show metronidazole benefit. Standard therapy already exists.

**To proceed, the following is needed:**
- Direct preclinical or clinical evidence of metronidazole activity against Pneumocystis (none currently exists in the data)
- Mechanism of action data and the Canadian package insert warnings and contraindications
- Consideration of better-supported candidates from the same prediction list (cap polyposis and vulvar ulceration, both L3) as research questions, ideally with controlled studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

