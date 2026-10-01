---
layout: default
title: Methylene Blue
parent: Model Prediction Only (L5)
nav_order: 599
evidence_level: L5
indication_count: 3
---

# Methylene Blue
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Methylene Blue: From Unspecified Original Indication to Bronchitis

## One-Sentence Summary

Methylene blue is a long-established injectable and topical dye-type drug. The records supplied here do not list its original approved indication.
The TxGNN model predicts it may be effective for **bronchitis**, but this rests on the model score alone: there are **0 clinical trials** and **no publications** showing that methylene blue treats bronchitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Methylene blue is known to inhibit nitric oxide synthase and soluble guanylate cyclase. In theory, this could affect airway inflammation or smooth-muscle tone. This idea is speculative, and no cited study supports it.

The literature retrieved for this prediction mostly reflects keyword co-occurrence, meaning "bronchitis" and "methylene blue" appear in the same records. It does not show therapeutic benefit. The one bronchoscopy paper concerns using methylene blue as a **diagnostic stain** for bronchial tumours, not treating bronchitis.

The 99.97% score is therefore a computational signal, not evidence of clinical usefulness. It should not be treated as a reason to move forward without further work.

*Note:* The same evidence pack also lists two methemoglobinemia predictions. These have a much stronger biological rationale. Methylene blue is a well-known antidote for acquired methemoglobinemia, so that may be established use rather than true repurposing. Both are rated L4 (indirect evidence only).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No publication tests methylene blue as a treatment for bronchitis. The relevant items below are diagnostic or methodological. The other retrieved papers mention bronchitis only in passing (for example, herbal-medicine, theophylline sensor, and case-report papers) and are not listed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Diagnostic | Zhonghua Wai Ke Za Zhi | Methylene blue staining during fiberoptic bronchoscopy in 47 patients. 97.14% of central malignant bronchial tumours stained versus 8.33% of bronchitis cases, so the dye helped distinguish tumour from bronchitis. This is diagnostic use, not treatment. |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Diagnostic | Terapevticheskii Arkhiv | Chromoendofibroscopy with methylene blue to distinguish benign from malignant gastrointestinal and bronchial neoplasms. No abstract available. |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Methodological | Am Rev Respir Dis | Methylene blue was one of five markers used to quantify intraalveolar fluid in bronchoalveolar lavage. This is a measurement method, not a therapy. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2487993 | Methylene Blue Injection | Not listed | Not listed |
| 2230770 | Methylene Blue Injection USP | Not listed | Not listed |
| 50466 | Methylene Bleu Liq 1% | Not listed | Not listed |
| 674354 | Collyre Bleu Laiter | Not listed | Not listed |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

One caution appears in the pack's rationale for the methemoglobinemia predictions: G6PD deficiency carries a risk of haemolysis with methylene blue. G6PD status would need to be considered in any new use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction is supported only by the model score (L5). There are no clinical trials, and the literature is diagnostic or incidental. No mechanistic link is supported by the supplied data.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for the four DINs, to establish the original indication and confirm what is on-label
- Mechanism of action data (for example, from DrugBank)
- Preclinical or clinical evidence that methylene blue affects airway inflammation or bronchitis outcomes
- Route-compatibility assessment: bronchitis would probably need an inhaled or oral route, and none of the four DINs is currently confirmed for those routes

---

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

