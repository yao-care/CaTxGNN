---
layout: default
title: Fulvestrant
parent: Moderate Evidence (L3-L4)
nav_order: 420
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
monitor_inn: "FULVESTRANT"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acne (disease)", "brachydactyly-syndactyly syndrome", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Fulvestrant: predicted new indication HIV infectious disease (evidence level L4). Approved use: Not recorded in the local data"
---

# Fulvestrant
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Fulvestrant: HIV infectious disease
{: .text-alpha }

## One-Sentence Summary

Fulvestrant is an estrogen receptor antagonist and degrader marketed in Canada, and it is widely used with other agents in hormone receptor-positive breast cancer trials.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **no clinical trials** and only **2 publications** (one preclinical study and one off-target bioinformatic analysis), so this is a model prediction with very limited support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L4 (preclinical evidence only) |
| Canada Market Status | Marketed (valid licenses: 6 of 6) |
| Number of DINs | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fulvestrant is an estrogen receptor (ER) antagonist and degrader, and its use in hormone receptor-positive breast cancer is well established through the combination trials listed below.

The link to HIV is indirect. Estrogen receptor alpha (ERα) is expressed in CD4+ T cells and is hypothesized to influence HIV transcription and latency. A 2026 preclinical study examined how ER ligands, including fulvestrant, and HIV latency-reversing agents affect ERα in CD4+ T cells. This suggests fulvestrant could plausibly affect latency reversal.

This evidence is in vitro and mechanistic only. The high TxGNN score is a computational prediction, and nothing here shows benefit in people living with HIV.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for HIV infectious disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Preclinical in vitro study | JCI Insight | Examined the effect of estrogen, fulvestrant and HIV latency-reversing agents on ERα nuclear translocation and signaling in CD4+ T cells. |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Cross-omics / bioinformatic analysis | Research Square | Concerns HTLV-1-associated myelopathy, not HIV, so it provides little direct support. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02483610 | FULVESTRANT INJECTION | Not listed | Not listed |
| 02530635 | FULVESTRANT INJECTABLE | Not listed | Not listed |
| 02248624 | FASLODEX | Not listed | Not listed |
| 02460130 | TEVA-FULVESTRANT INJECTION | Not listed | Not listed |
| 02558971 | FULVESTRANT INJECTION | Not listed | Not listed |
| 02536293 | FULVESTRANT INJECTION | Not listed | Not listed |

All six licences are valid single-ingredient products.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/endocrine therapy (ER antagonist and degrader), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert and local institutional policy |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not label text): liver disease, gallbladder disease, thrombocytopenia, and blood coagulation disease.
- **Drug Interactions**: 92 potential interactions were identified, all with an unclassified severity level. Examples include warfarin, acetylsalicylic acid, metformin, simvastatin, dexamethasone, prednisone, proton pump inhibitors (omeprazole, pantoprazole, lansoprazole), and ondansetron. The warfarin and aspirin entries deserve review given the coagulation and platelet signals above.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction rests on a single indirect in vitro study, with no clinical trials. Other candidate indications fare no better. The "multiple endocrine neoplasia" trials are almost all breast cancer studies (the existing use) and are likely a mislabeled match. Rheumatoid arthritis is a research question only, since animal data suggest estrogen blockade may worsen inflammation. The remaining predictions are unsupported.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Confirmed approved indication text for the Canadian licences
- Further preclinical work on ERα modulation of HIV latency in CD4+ T cells, and a defined clinical hypothesis before any trial is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

