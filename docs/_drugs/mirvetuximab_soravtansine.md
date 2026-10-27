---
layout: default
title: Mirvetuximab Soravtansine
parent: Model Prediction Only (L5)
nav_order: 622
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Mirvetuximab Soravtansine: predicted new indication Antithrombin deficiency type 2 (evidence level L5). Approved use: Platinum-resistant ovarian cancer"
monitor_inn: "Mirvetuximab Soravtansine"
predicted_indications: ["antithrombin deficiency type 2", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "candidiasis", "plasma cell myeloma", "indolent plasma cell myeloma", "tinea corporis", "thrombophilia", "uterine polyp", "pediatric systemic lupus erythematosus"]
---

# Mirvetuximab Soravtansine
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

## Mirvetuximab Soravtansine: From Platinum-Resistant Ovarian Cancer to Antithrombin Deficiency Type 2
{: .text-alpha }

## One-Sentence Summary

Mirvetuximab soravtansine is an antibody-drug conjugate that targets folate receptor alpha (FRα). It is used to treat platinum-resistant ovarian cancer.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2**, but **no clinical trials and no publications** support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Platinum-resistant ovarian cancer (per the drug's pharmacology data; the Canadian licence record has no indication text) |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 97.95% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, mirvetuximab soravtansine is an FRα-targeting antibody-drug conjugate. Its antibody component binds FRα (FOLR1) with high affinity (Kd 0.08 nM in vitro) and delivers the maytansinoid payload DM4, a microtubule inhibitor, to FRα-expressing tumour cells.

The original and predicted indications are not related. Antithrombin deficiency type 2 is an inherited coagulation inhibitor disorder linked to SERPINC1. It does not involve FRα expression or microtubule disruption. A cytotoxic ADC would also be a poor fit for a chronic non-malignant condition. The high TxGNN score most likely reflects an artifact of the knowledge-graph structure rather than real biology. The same applies to the other top-ranked predictions: heparin cofactor 2 deficiency, factor 5 excess with spontaneous thrombosis, candidiasis, thrombophilia, tinea corporis, uterine polyp and pediatric systemic lupus erythematosus. For each of these, the mechanistic review found no plausible link.

The only prediction with any literature is **plasma cell myeloma** (rank 5, score 97.61%). Its link is weak and speculative: myeloma is not a recognised FRα-expressing cancer, and the usual ADC target there is BCMA.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top predicted indication. For the fifth-ranked prediction (plasma cell myeloma), five reviews were retrieved. They concern ADCs and gynaecologic cancers in general, and none provides myeloma-specific evidence for mirvetuximab:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41151612](https://pubmed.ncbi.nlm.nih.gov/41151612/) | 2025 | Review | Dtsch Med Wochenschr | Overview of recent immuno-oncology approvals, including mirvetuximab soravtansine for platinum-resistant ovarian cancer |
| [42828635](https://pubmed.ncbi.nlm.nih.gov/42828635/) | 2026 | Review | Int J Clin Oncol | Japanese regulatory update on anticancer drugs, including mirvetuximab soravtansine for ovarian cancer |
| [38146364](https://pubmed.ncbi.nlm.nih.gov/38146364/) | 2023 | Review | Front Immunol | CAR-T cell immunotherapy for ovarian cancer |
| [34683998](https://pubmed.ncbi.nlm.nih.gov/34683998/) | 2021 | Review | Pharmaceutics | Antibody-drug conjugates in gynaecological malignancies: current status and future perspectives |
| [36618922](https://pubmed.ncbi.nlm.nih.gov/36618922/) | 2022 | Review | Front Pharmacol | Review of ADCs, alone or combined with immunotherapy, for gynaecologic cancer |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02560771 | ELAHERE | Not listed | Not listed |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Antibody-drug conjugate with a cytotoxic payload (DM4, a maytansinoid microtubule inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; ocular (corneal) examinations are relevant given the known ocular toxicity |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

## Safety Considerations

- **Known toxicity**: Drug-induced ocular (corneal) toxicity has been reported. It can be resolved with short-term topical steroids.
- **Drug Interactions**: The interaction query found only the drug's pharmacological target, folate receptor alpha (FOLR1). No specific interacting drugs were identified.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, antithrombin deficiency type 2, has no clinical trials, no literature and no plausible mechanistic link. A cytotoxic ADC would carry a poor risk-benefit balance in a chronic non-malignant disorder. The high TxGNN score appears to be a computational artifact, and the other nine predictions are equally unsupported.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- Approved indication text for the Canadian licence
- Experimental evidence that FRα, or another relevant mechanism, plays a role in the predicted disease
- Re-evaluation of the drug for FRα-expressing malignancies, which are more biologically plausible than the model's top predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

