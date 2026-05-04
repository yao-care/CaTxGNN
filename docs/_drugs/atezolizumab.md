---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Atezolizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Atezolizumab: From Urothelial Carcinoma to Prostatic Urethra Urothelial Carcinoma

## One-Sentence Summary

Atezolizumab (Tecentriq) is an anti-PD-L1 monoclonal antibody (immune checkpoint inhibitor) with established efficacy across multiple cancers, including urothelial carcinoma of the bladder and non-small cell lung cancer.
The TxGNN model predicts it may be effective for **Prostatic Urethra Urothelial Carcinoma**, with **2 clinical trials** currently supporting this direction; no direct PubMed literature was identified for this specific histological subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma (no current DINs on record; see note below) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed (0 DINs on file — potential data gap; verify against Health Canada database) |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Atezolizumab is an anti-PD-L1 monoclonal antibody that works by simultaneously blocking the PD-L1/PD-1 and PD-L1/B7.1 axes. This dual blockade releases the brake on CD8+ T cell cytotoxic activity within the tumor microenvironment, allowing the immune system to recognize and destroy cancer cells. Urothelial cancers — from the bladder to the upper urinary tract — are among the most PD-L1-enriched tumor types, which is precisely why atezolizumab received FDA approval for cisplatin-ineligible patients with locally advanced or metastatic urothelial carcinoma. Detailed mechanism of action data from the regulatory record is not available in the current dataset; the above is drawn from the published literature and approved labeling of atezolizumab.

Prostatic urethra urothelial carcinoma is not a biologically separate entity from bladder urothelial carcinoma — both arise from the same urothelial epithelium and share overlapping molecular profiles, PD-L1 expression patterns, and tumor-infiltrating lymphocyte characteristics. In the context of non-muscle invasive bladder cancer (NMIBC), prostatic urethral involvement is a well-recognized anatomical extension, not a distinct disease. The completed Phase 2 trial NCT02844816 in BCG-unresponsive NMIBC is directly relevant because this patient population frequently includes prostatic urethral involvement as a co-existing site.

Given this shared cell of origin, PD-L1 biology, and clinical co-occurrence with NMIBC, the TxGNN prediction represents a mechanistically justified extension of atezolizumab's established urothelial activity — not a novel biological leap.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | Completed | 172 | Atezolizumab monotherapy in BCG-unresponsive recurrent/refractory NMIBC — evaluates whether immune checkpoint blockade can clear urothelial tumors that have escaped BCG immunotherapy; prostatic urethra is a common site of NMIBC involvement |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | Active, Not Recruiting | 914 | Cabozantinib ± Atezolizumab across multiple solid tumor cohorts, explicitly including urothelial carcinoma (bladder, renal pelvis, ureter, urethra); large-scale safety and preliminary efficacy platform spanning the full urothelial anatomical spectrum |

---

## Literature Evidence

Currently no related literature specifically addressing prostatic urethra urothelial carcinoma and atezolizumab is available.

---

## Canada Market Information

No regulatory authorizations for Atezolizumab are currently on file in the database. This likely reflects a data gap rather than true absence from the Canadian market — Health Canada should be queried directly to confirm DIN status for Tecentriq (atezolizumab).

---

## Cytotoxicity

Atezolizumab is an antineoplastic agent (immune checkpoint inhibitor). It does not belong to conventional cytotoxic chemotherapy classes, but cytotoxicity monitoring and oncology-grade handling still apply.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — anti-PD-L1 monoclonal antibody (not a conventional cytotoxic agent; no direct DNA damage mechanism) |
| Myelosuppression Risk | Low for classic myelosuppression; immune-related hematologic adverse events (e.g., immune-mediated hemolytic anemia, thrombocytopenia) occur rarely |
| Emetogenicity Classification | Minimal (IV monoclonal antibody infusion; emetogenicity is not a primary concern) |
| Monitoring Items | Liver function (ALT, AST, bilirubin), thyroid function (TSH, free T4), CBC with differential, serum creatinine, fasting blood glucose, cortisol/ACTH if adrenal insufficiency suspected; immune-related adverse event (irAE) surveillance at each cycle |
| Handling Protection | Standard cytotoxic handling precautions for IV monoclonal antibodies; administer in oncology infusion setting with infusion reaction monitoring |

---

## Safety Considerations

Please refer to the package insert for safety information. Full TFDA or FDA prescribing information for atezolizumab should be reviewed before clinical use, particularly regarding immune-related adverse events (irAEs), which are the primary risk class for this agent.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial in BCG-unresponsive NMIBC (NCT02844816, n=172) — a clinical context in which prostatic urethral involvement is common — provides directly relevant supporting evidence, and the mechanistic link between PD-L1 blockade and urothelial carcinoma at this anatomical site is well-established. The TxGNN score of 99.98% reflects strong graph-level signal consistent with the shared biology.

**To proceed, the following is needed:**

- **Safety documentation**: Obtain and parse the TFDA or FDA prescribing information PDF to extract warnings, contraindications, and immune-related adverse event management guidelines (currently a blocking data gap)
- **Mechanism of action record**: Confirm MOA in structured format from DrugBank API to complete the mechanistic rationale
- **Canada market verification**: Cross-check Health Canada's Drug Product Database directly — current 0-DIN record likely reflects a data pipeline gap
- **Subgroup data**: Request or query for prostatic urethra–specific subgroup analyses from NCT02844816 or NMIBC extension cohorts
- **PD-L1 biomarker data**: Identify PD-L1 expression rates and SP142 IHC data in prostatic urethra UC specifically to guide patient selection criteria
- **Drug interaction profile**: Conduct a DDI review against common co-medications in this patient population (e.g., corticosteroids used to manage irAEs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

