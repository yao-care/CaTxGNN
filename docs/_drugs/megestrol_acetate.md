---
layout: default
title: Megestrol Acetate
parent: High Evidence (L1-L2)
nav_order: 575
evidence_level: L2
indication_count: 10
---

# Megestrol Acetate
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Megestrol Acetate: From an Unspecified Labeled Indication to Uterine Corpus Endometrial Carcinoma

## One-Sentence Summary

Megestrol acetate is a synthetic progestin (hormonal agent) marketed in Canada, but the Canadian license records supplied do not state its approved indication.
The TxGNN model predicts it may be effective for **uterine corpus endometrial carcinoma**.
**3 clinical trials** support this direction, of which 1 is a completed randomized Phase 2 trial. No publications were supplied for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied Canadian license records |
| Predicted New Indication | Uterine corpus endometrial carcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied record. Megestrol is a synthetic progestin. It acts through progesterone receptors to oppose estrogen-driven proliferation and promote differentiation in hormone-receptor-positive endometrial tumors. This is consistent with the very high TxGNN score.

Estrogen drives the growth of many endometrial cancers, so a progestin is a biologically sensible treatment. The oral tablet is widely known for use in advanced endometrial carcinoma, but the supplied data lists no original indications. The local label should therefore be checked to see whether this is truly a "new" indication in Canada or already an approved one.

Several other predictions for this drug (for example, ovarian cancer) also have hormonal rationales, but this report focuses on the top-ranked prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Randomized trial of temsirolimus alone or with hormonal therapy (megestrol acetate and tamoxifen) in advanced, persistent, or recurrent endometrial cancer. No results were supplied. |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | Unknown | 60 | PD-1 inhibitor plus progesterone versus progesterone alone in early-stage endometrial cancer patients seeking fertility preservation. Exploratory; megestrol-specific attribution is unclear. |
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | Terminated | 9 | Continuous versus sequential progestin (megestrol) therapy in endometrial intraepithelial neoplasia / atypical hyperplasia. Terminated with only 9 patients, so it cannot support efficacy conclusions. |

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 2195925 | MEGESTROL | Not listed | Not listed |
| 2195917 | MEGESTROL | Not listed | Not listed |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (progestin); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.
- **Literature-noted concern**: Secondary adrenal suppression has been reported with megestrol therapy in patients with advanced cancer (PMID 10491532, cited in the ovarian cancer evidence for this drug). High-dose use has also been studied for effects on blood coagulation (PMID 11727356).

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is biologically plausible and the TxGNN score is very high. A completed randomized Phase 2 trial includes a megestrol-containing arm in endometrial cancer, but no results or publications were supplied. The other two trials are exploratory or terminated early, so the evidence is moderate at best.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- The approved indication text, dosage form and manufacturer for both DINs, to confirm whether endometrial carcinoma is already labeled
- Published results of NCT00729586, and confirmation of the megestrol arm's contribution
- Detailed mechanism of action data (for example, from DrugBank)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

