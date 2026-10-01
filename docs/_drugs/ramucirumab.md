---
layout: default
title: Ramucirumab
parent: Model Prediction Only (L5)
nav_order: 786
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: From Gastric/GEJ Adenocarcinoma to Uterine Ligament Adenocarcinoma

## One-Sentence Summary

Ramucirumab (marketed in Canada as CYRAMZA) is an anti-angiogenic cancer drug. The evidence pack's rationale text links it to gastric/gastroesophageal junction adenocarcinoma, but the Canadian licence data list no approved indication.
The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**, along with nine other gynecologic adenocarcinoma subtypes.
This is a model prediction only: **0 clinical trials** and **0 publications** support it so far.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian licence data (the evidence pack's rationale text mentions gastric/GEJ adenocarcinoma) |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

The other top-10 predictions are all gynecologic adenocarcinoma subtypes, scored 99.94–99.95%, and all sit at L5 with a Hold recommendation:
- endocervical carcinoma
- adenoid cystic carcinoma of the cervix uteri
- uterine ligament serous adenocarcinoma
- signet ring cell variant cervical mucinous adenocarcinoma
- cervical adenosquamous carcinoma, glassy cell variant
- uterine ligament endometrioid adenocarcinoma
- uterine ligament clear cell adenocarcinoma
- uterine ligament mucinous adenocarcinoma
- intestinal variant cervical mucinous adenocarcinoma

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the supplied data. Based on known drug-class information, ramucirumab is a VEGFR2 antagonist, and anti-angiogenic therapy is biologically plausible in gynecologic adenocarcinomas. This reasoning comes from the drug's known class, not from the supplied data.

Blocking the VEGF pathway already has precedent in cervical cancer (bevacizumab). Ramucirumab is also used in gastric/GEJ adenocarcinoma, so there is a loose conceptual parallel to adenocarcinomas of the female genital tract. Some predicted histologies resemble gastrointestinal adenocarcinoma, such as the signet ring and intestinal variants. Anti-angiogenic therapy has also been explored in endometrial-type cancers.

The very high score probably reflects ontology proximity to related cervical and uterine carcinoma nodes rather than direct clinical evidence. Several of the predicted histologies are very rare, which makes the rationale indirect. The mechanistic link is a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2443805 | CYRAMZA | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR2 antagonist monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (about 99.95%). There are no registered trials and no literature for any of the top 10 predicted indications. The mechanistic link is inferred from drug class, and no safety data are available.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (this blocks safety screening)
- Mechanism of action data from DrugBank
- The approved indication text and dosage form for DIN 2443805
- A search of clinical trial registries and the literature for ramucirumab in cervical and uterine adenocarcinomas
- A comparison of the predicted indications with the original indication, and a route-of-administration compatibility check
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

