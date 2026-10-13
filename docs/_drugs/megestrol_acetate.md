---
layout: default
title: Megestrol Acetate
parent: High Evidence (L1-L2)
nav_order: 580
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

# Megestrol Acetate: From Endometrial Carcinoma to Uterine Corpus Endometrial Carcinoma

## One-Sentence Summary

Megestrol acetate is a progestin originally used for endometrial carcinoma (endometrial cancer).
The TxGNN model predicts it may be effective for **uterine corpus endometrial carcinoma**, with **1 clinical trial** (a Phase 2 trial in which megestrol is part of a combination arm) and no indication-specific publications supporting this direction.
This prediction is essentially a restatement of the existing indication rather than a true repurposing finding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometrial carcinoma / endometrial cancer (no approved indication text is available for the Canadian licenses) |
| Predicted New Indication | Uterine corpus endometrial carcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, megestrol acetate is a progestin (a synthetic progesterone-like hormone). Its efficacy in endometrial carcinoma is established, and it is mechanistically expected to act through progesterone receptors, producing antiproliferative and differentiating effects in hormone-sensitive endometrial tissue.

Uterine corpus endometrial carcinoma is essentially the same disease as the original indication, so the prediction is consistent with known biology. It should be understood as confirming the existing use rather than discovering a new one.

Other predicted indications, such as ovarian cancer and uterine carcinosarcoma, rest on weaker or speculative hormone-receptor rationales. They are not the primary focus of this report, though the ovarian cancer prediction has a Phase 3 trial and several Phase 2 studies (see the note in the conclusion).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Randomized trial of temsirolimus alone or combined with hormonal therapy (megestrol acetate plus tamoxifen) in advanced, persistent or recurrent endometrial cancer. Megestrol is part of a combination arm, so this is supportive evidence only. |

## Literature Evidence

Currently no related literature is available for this specific predicted indication.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02195925 | MEGESTROL | Not specified | Not specified |
| 02195917 | MEGESTROL | Not specified | Not specified |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (progestin); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (not a typical myelosuppressive agent) |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood pressure, blood glucose, liver and renal function; adrenal function with prolonged high-dose use |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Megestrol is linked to caution in hypertension, kidney disease, liver disease, gallbladder disease, hyperglycaemia and diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency and Addison disease, male hypogonadism, premature menopause, and androgen insensitivity syndrome.
- **Drug Interactions**: 100 interactions were found, and all 20 listed are of Moderate severity. Most involve glucose-lowering drugs, which may be affected by megestrol-related changes in glucose control: acarbose, metformin, pioglitazone, glimepiride, repaglinide, chlorpropamide, sitagliptin, saxagliptin, linagliptin, alogliptin, the GLP-1 agonists (albiglutide, dulaglutide, semaglutide), the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin) and insulins (aspart, degludec). Others include aprepitant and clarithromycin.
- A published study reports secondary adrenal suppression with megestrol therapy (PMID 10491532), which is consistent with the adrenal-related cautions above.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication is effectively the drug's existing use. A completed Phase 2 randomized trial includes megestrol in a combination arm, and the drug is marketed in Canada. Evidence for megestrol as a single agent in this exact indication is limited in the data compiled here, and the safety profile requires attention, particularly in patients with diabetes.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indication text (currently missing and blocking for safety screening)
- Mechanism of action data (for example from DrugBank)
- Verification of the arm structure and results of NCT00729586
- Confirmation of the outcome of the Phase 3 trial NCT00005975, which studied megestrol for hot flashes in women treated for breast cancer, so it should not be read as evidence for ovarian cancer efficacy
- A glucose and adrenal monitoring plan for patients with diabetes or on prolonged high-dose therapy
- Other predicted indications (for example hereditary breast ovarian cancer syndrome, ovarian clear cell adenocarcinoma, dysgerminoma) lack evidence and are on Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

