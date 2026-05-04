---
layout: default
title: Cemiplimab
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: From Cutaneous Squamous Cell Carcinoma to Gallbladder Adenosquamous Carcinoma

## One-Sentence Summary

Cemiplimab (LIBTAYO®) is a fully human anti-PD-1 checkpoint inhibitor antibody, approved in multiple jurisdictions as a treatment for cutaneous squamous cell carcinoma (CSCC), non-small cell lung cancer (NSCLC), basal cell carcinoma (BCC), and cervical cancer — though it is not currently registered in Taiwan.
The TxGNN model identifies **Gallbladder Adenosquamous Carcinoma** as the top-ranked new indication (score 99.99%), with **no clinical trials or published literature** currently supporting this specific drug–disease combination.
This is a multi-indication analysis covering 10 predicted indications; the most evidence-supported prediction is rank 4 (external ear basal cell carcinoma, L3), where cemiplimab already holds FDA approval for the broader BCC indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cutaneous squamous cell carcinoma (CSCC); also approved for NSCLC, BCC, and cervical cancer (FDA/EMA — not registered in Taiwan) |
| Predicted New Indication | Gallbladder adenosquamous carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, cemiplimab is a fully human IgG4 monoclonal antibody belonging to the anti-PD-1 checkpoint inhibitor class. It blocks the interaction between the PD-1 receptor on T cells and its tumour-expressed ligands PD-L1 and PD-L2, thereby restoring cytotoxic T-lymphocyte–mediated anti-tumour immunity. This is the same mechanism shared by pembrolizumab and nivolumab, and its clinical utility is established across multiple squamous and non-squamous malignancies.

Gallbladder adenosquamous carcinoma is a rare mixed-histology biliary tract tumour containing both glandular (adenocarcinoma) and squamous cell components. The squamous portion is theoretically more likely to express PD-L1 — the predictive biomarker most associated with checkpoint inhibitor response — which provides the biological basis for this prediction. PD-1 blockade could, in principle, restore T-cell surveillance against tumour cells in this setting. However, biliary tract cancers as a class show modest overall response rates to checkpoint inhibitors (approximately 15–20% in unselected populations), and the adenosquamous mixed histology adds further biological heterogeneity that complicates immune targeting.

The TxGNN knowledge graph model extrapolates from cemiplimab's established activity across squamous cell malignancies (CSCC as the primary approval, plus NSCLC-squamous and BCC) to predict relevance in gallbladder adenosquamous carcinoma — a logical pattern-based inference. While mechanistically plausible given the shared PD-1/PD-L1 axis, this remains entirely a model-generated hypothesis: no direct clinical trial data, observational evidence, or preclinical studies validate this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cemiplimab in gallbladder adenosquamous carcinoma.

---

## Literature Evidence

Currently no related literature available for cemiplimab in gallbladder adenosquamous carcinoma.

---

## Taiwan Market Information

Cemiplimab is not registered in Taiwan. The Taiwan FDA (TFDA) has issued no Drug Identification Numbers (DINs) for this product. Clinicians or researchers seeking access would need to apply through compassionate use, expanded access, or a special import approval mechanism.

> No DIN records to display.

---

## Multi-Indication Prediction Summary

This Evidence Pack covers **10 predicted indications** (candidate ID: TW-DB14707-multi). The table below summarises the evidence landscape across all predictions:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Gallbladder adenosquamous carcinoma | 99.99% | L5 | Hold |
| 2 | Glottis squamous cell carcinoma | 99.99% | L4 | Research Question |
| 3 | Rectal cloacogenic carcinoma | 99.99% | L5 | Hold |
| **4** | **External ear basal cell carcinoma** | **99.99%** | **L3** | **Proceed with Guardrails** |
| 5 | Adenosquamous prostate carcinoma | 99.99% | L5 | Hold |
| 6 | Urethral verrucous carcinoma | 99.99% | L5 | Hold |
| 7 | Lung occult squamous cell carcinoma | 99.99% | L4 | Research Question |
| 8 | Pancreatic adenosquamous carcinoma | 99.99% | L5 | Hold |
| 9 | Non-keratinizing sinonasal squamous cell carcinoma | 99.99% | L4 | Research Question |
| 10 | Supraglottis squamous cell carcinoma | 99.99% | L4 | Research Question |

**Key highlight — Rank 4 (External Ear BCC):** Cemiplimab received FDA approval for locally advanced and metastatic basal cell carcinoma in February 2021, based on the EMPOWER-BCC 1 Phase 2 trial. "External ear" is an anatomical location subtype — it does not represent a biologically distinct entity excluded from the approved BCC indication. One published case report documents a durable response following cemiplimab discontinuation in a locally advanced BCC patient, supporting proof-of-concept.

### Literature Evidence for Rank 4 (External Ear BCC)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34157152](https://pubmed.ncbi.nlm.nih.gov/34157152/) | 2021 | Case Report | Clinical and Experimental Dermatology | Documents a lasting tumour response persisting after cemiplimab discontinuation in a patient with locally advanced BCC, demonstrating durable immune memory |

---

## Cytotoxicity

Cemiplimab is an antineoplastic drug indicated exclusively for the treatment of malignancies, and is therefore included in this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Anti-PD-1 checkpoint inhibitor (not a conventional cytotoxic agent; no direct DNA damage or cell-cycle arrest mechanism) |
| Myelosuppression Risk | Low (direct myelotoxicity is not expected; immune-mediated haematological events such as immune thrombocytopenia or haemolytic anaemia are uncommon but possible) |
| Emetogenicity Classification | Minimal (not associated with chemotherapy-type emetogenicity; nausea is uncommon and not a class effect) |
| Monitoring Items | Thyroid function (TSH, free T4 at baseline and periodically); liver enzymes (AST/ALT); full blood count; fasting glucose (immune-mediated type 1 diabetes); renal function (creatinine); cortisol if adrenal insufficiency is suspected; infusion reaction monitoring at each administration |
| Handling Protection | Standard monoclonal antibody (biological) handling procedures apply; full cytotoxic drug handling protocols are not required, but institutional biosafety guidelines for injectable biologics should be followed |

---

## Safety Considerations

Please refer to the package insert for safety information. As cemiplimab is not registered in Taiwan, consult the FDA-approved prescribing information for LIBTAYO® for complete warnings, contraindications, and immune-related adverse event (irAE) management guidelines. Key irAE categories from the FDA label include immune-mediated pneumonitis, colitis, hepatitis, endocrinopathies (hypothyroidism, hyperthyroidism, adrenal insufficiency, type 1 diabetes mellitus), nephritis with renal dysfunction, and dermatitis. Infusion-related reactions have also been reported.

---

## Conclusion and Next Steps

**Decision: Hold** *(primary prediction: gallbladder adenosquamous carcinoma)*

**Rationale:**
Gallbladder adenosquamous carcinoma is an ultra-rare indication with no supporting clinical trials or published literature for cemiplimab, and biliary tract cancers as a class have shown historically limited sensitivity to PD-1 checkpoint blockade. The L5 evidence level reflects pure model-generated prediction without any empirical clinical or preclinical validation.

**To proceed, the following is needed:**

- **Biomarker data:** PD-L1 expression (CPS/TPS scoring), tumour mutational burden (TMB), and MSI/MMR status specifically for gallbladder adenosquamous carcinoma to assess immunotherapy eligibility a priori
- **Basket trial mapping:** Identification of ongoing or planned basket trials for biliary tract or rare adenosquamous tumours in which cemiplimab or a class agent could be introduced as a cohort
- **Mechanism of action (MOA) data:** Retrieve full DrugBank entry for cemiplimab (DG002 — High severity data gap) to strengthen the mechanistic rationale analysis
- **Taiwan TFDA safety data:** Download and parse the TFDA package insert PDF (DG001 — Blocking data gap) to enable formal safety screening and complete the S1 evaluation
- **Taiwan regulatory pathway:** Assess the feasibility of TFDA registration or special import approval given that cemiplimab is currently entirely unregistered in Taiwan
- **For rank 4 (external ear BCC — the most actionable prediction):** Cross-reference the EMPOWER-BCC 1 trial eligibility criteria against the "external ear" anatomical subtype; assess Taiwan BCC incidence and unmet need to determine whether a repurposing dossier for this specific subtype is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

