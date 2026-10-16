---
layout: default
title: Dactinomycin
parent: Model Prediction Only (L5)
nav_order: 242
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Dactinomycin: predicted new indication Relapsing-remitting multiple sclerosis (evidence level L5). Approved use: Ewing sarcoma, rhabdomyosarcoma, Wilms tumour…"
---

# Dactinomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Dactinomycin: From Ewing Sarcoma and Other Solid Tumours to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Dactinomycin is a cytotoxic anticancer antibiotic, originally used for Ewing sarcoma, rhabdomyosarcoma, Wilms tumour, gestational trophoblastic neoplasm and testicular germ cell tumours.
The TxGNN model's top prediction is **relapsing-remitting multiple sclerosis**, but it has **no clinical trials and no publications** behind it. Most of the other top-ranked predictions are subtypes or sites of rhabdomyosarcoma, which is already an established use, and these have **0 clinical trials** and a varying amount of literature (from none to about 20 publications).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ewing sarcoma, rhabdomyosarcoma, Wilms tumour, gestational trophoblastic neoplasm, testicular germ cell tumours (per the knowledge graph; no approved indication text is available for the Canadian licence) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis (rank 1) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (for rank 1) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold (rank 1) |

**Summary of all predictions reviewed**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|------|
| 1 | Relapsing-remitting multiple sclerosis | 99.58% | L5 | Hold |
| 2 | Botryoid-type embryonal rhabdomyosarcoma of the vagina | 99.54% | L4 | Hold |
| 3 | Extrahepatic bile duct rhabdomyosarcoma | 99.49% | L4 | Hold |
| 4 | Embryonal extrahepatic bile duct rhabdomyosarcoma | 99.48% | L4 | Hold |
| 5 | Parameningeal embryonal rhabdomyosarcoma | 99.48% | L1 (needs verification) | Proceed with Guardrails |
| 6 | Prostate embryonal rhabdomyosarcoma | 99.46% | L3 | Research Question |
| 7 | Liver sarcoma | 99.42% | L3 | Research Question |
| 8 | Upper aerodigestive tract neoplasm | 99.16% | L3 | Research Question |
| 9 | Head and neck cancer | 99.16% | L3 | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dactinomycin is a transcription-inhibiting DNA intercalator with cytotoxic and myelosuppressive effects. Its efficacy in rhabdomyosarcoma, Ewing sarcoma and Wilms tumour is established, mainly as part of combination regimens such as vincristine, actinomycin D and cyclophosphamide (VAC).

**The rank 1 prediction (multiple sclerosis) is poorly supported.** Immunomodulation in a relapsing autoimmune demyelinating disease is speculative at best. Dactinomycin's toxicity is substantial, and many approved disease-modifying therapies already exist. The high score is likely a graph-based artifact and not a validated signal.

**Ranks 2–7 are mostly extensions of an existing indication.** They are histologic subtypes or anatomic sites of rhabdomyosarcoma (vagina, bile duct, parameningeal, prostate) or a related sarcoma (liver). They are therefore not true repurposing, and support is indirect, via standard VAC-type regimens.

**Ranks 8–9 (upper aerodigestive tract neoplasm, head and neck cancer)** draw their signal from head and neck rhabdomyosarcoma, not from the squamous cell carcinomas typical of these cancers. There is no evidence for dactinomycin in squamous carcinoma.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

Key publications are shown for the better-supported predictions.

**Rank 5: Parameningeal embryonal rhabdomyosarcoma**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19770373](https://pubmed.ncbi.nlm.nih.gov/19770373/) | 2009 | RCT | J Clin Oncol | Compares VAC with VAC alternating with vincristine, topotecan and cyclophosphamide (Children's Oncology Group D9803) in intermediate-risk rhabdomyosarcoma |

The title and abstract are truncated, so the phase and design could not be confirmed. The L1 grade rests on an inference and should be verified against the full record.

**Rank 6: Prostate embryonal rhabdomyosarcoma**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22104356](https://pubmed.ncbi.nlm.nih.gov/22104356/) | 2012 | Cohort | Int J Radiat Oncol Biol Phys | Local control with reduced-dose radiotherapy in low-risk rhabdomyosarcoma (COG D9602) |
| [34900598](https://pubmed.ncbi.nlm.nih.gov/34900598/) | 2022 | Case report/Review | Urol Case Rep | Adult prostate embryonal rhabdomyosarcoma treated with dactinomycin, vincristine and cyclophosphamide plus surgery and radiotherapy; the patient died of the disease |
| [2488079](https://pubmed.ncbi.nlm.nih.gov/2488079/) | 1989 | Review | Cir Pediatr | Genitourinary rhabdomyosarcoma in 12 children treated with VAC-based chemotherapy |

**Ranks 7–9: Liver sarcoma, upper aerodigestive tract neoplasm, head and neck cancer**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11408506](https://pubmed.ncbi.nlm.nih.gov/11408506/) | 2001 | Clinical trial report | J Clin Oncol | Intergroup Rhabdomyosarcoma Study IV results in nonmetastatic disease (risk-based surgery, radiotherapy and chemotherapy) |
| [39058728](https://pubmed.ncbi.nlm.nih.gov/39058728/) | 2024 | Clinical trial report | Cancer | EpSSG RMS 2005: reduced-dose alkylator chemotherapy plus radiotherapy in incompletely resected standard-risk rhabdomyosarcoma |
| [12586800](https://pubmed.ncbi.nlm.nih.gov/12586800/) | 2003 | Cohort | J Clin Oncol | Outcomes in localized nonorbital, nonparameningeal head and neck rhabdomyosarcoma (IRS III and IV) |
| [33567392](https://pubmed.ncbi.nlm.nih.gov/33567392/) | 2021 | Cohort | Eur J Cancer | EpSSG RMS 2005: reduced chemotherapy in completely resected embryonal rhabdomyosarcoma |
| [37814737](https://pubmed.ncbi.nlm.nih.gov/37814737/) | 2023 | Case series/Review | Cureus | Undifferentiated embryonal sarcoma of the liver in a child treated with chemotherapy that includes dactinomycin |
| [1482503](https://pubmed.ncbi.nlm.nih.gov/1482503/) | 1992 | Cohort | Cancer | German Cooperative Soft Tissue Sarcoma Study in children and adolescents |
| [21671362](https://pubmed.ncbi.nlm.nih.gov/21671362/) | 2011 | Retrospective cohort (toxicity) | Pediatr Blood Cancer | Dactinomycin and vincristine toxicity in childhood cancer (Children's Oncology Group) |
| [15143082](https://pubmed.ncbi.nlm.nih.gov/15143082/) | 2004 | Retrospective cohort (toxicity) | J Clin Oncol | Age is a risk factor for VAC-induced hepatopathy |
| [3955515](https://pubmed.ncbi.nlm.nih.gov/3955515/) | 1986 | Case series (late effects) | Cancer | Late effects after VAC-based treatment of head and neck soft tissue sarcoma in children |

Several other retrieved papers (thyroid cancer bioinformatics, flow cytometry of squamous cell carcinoma cell lines, a scientometric analysis, a transplantation cohort) are off-topic and do not support the predictions. No literature was available for multiple sclerosis or for ranks 2–4.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00213071 | COSMEGEN | Not specified | Not specified |

One valid single-ingredient licence is on record. Dosage form and indication text are not available in the compiled data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA-intercalating antitumour antibiotic) |
| Myelosuppression Risk | High. Knowledge graph contraindications include neutropenia, thrombocytopenia, leukopenia, anemia, agranulocytosis and aplastic anemia |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver function (hepatopathy and hepatic vein thrombosis are reported), renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindications / risk conditions (from the knowledge graph, not label text)**: liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anemia, macrocytic anemia, leukopenia, idiopathic aplastic anemia, aplastic anemia, varicella zoster infection, herpes zoster, hepatic vein thrombosis, Budd-Chiari syndrome.
- **Hepatotoxicity**: Published studies describe VAC-related hepatopathy, with age a risk factor. This matters for liver-involved or biliary disease (ranks 3, 4 and 7).
- **Late effects**: Dental abnormalities and other long-term toxicity are reported in childhood survivors treated with dactinomycin-containing regimens.
- **Drug interactions**: 100 interactions were found. Notable ones:
  - **Major**: deferiprone, samarium (153Sm) lexidronam
  - **Moderate**: palifermin, strontium chloride Sr-89, fostamatinib, mercaptopurine, roflumilast, chloramphenicol
  - **Minor**: levofloxacin
  - Many others, such as ondansetron, granisetron, dexamethasone, leucovorin and amphotericin B, have an unclassified severity level.

Package insert warnings and contraindications for the Canadian product have not yet been obtained.

---

## Conclusion and Next Steps

**Decision: Hold (rank 1, multiple sclerosis); Proceed with Guardrails only for rank 5 (parameningeal embryonal rhabdomyosarcoma), pending verification**

**Rationale:**
- The top-scoring prediction (multiple sclerosis) has no trials or literature, an implausible mechanism and a poor safety fit, so it should not advance.
- The other predictions are largely subtypes of an existing rhabdomyosarcoma use. Rank 5 is the best supported, but its L1 grade rests on an inference from a truncated record. Ranks 6–9 have only observational or indirect evidence, mostly in children.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (this is a blocking gap for safety screening)
- Mechanism of action data
- Full-record verification of PMID 19770373 (phase, design, and whether parameningeal embryonal disease was analysed)
- Adult-specific dosing, efficacy and safety data for prostate and liver disease
- Approved indication text and dosage form for DIN 00213071
- For ranks 7–9, evidence beyond rhabdomyosarcoma (squamous carcinomas have none), and a hepatic safety assessment for liver and biliary disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

