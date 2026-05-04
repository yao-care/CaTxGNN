---
layout: default
title: Avelumab
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Urothelial Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab (Bavencio®) is a fully human anti-PD-L1 monoclonal antibody, globally approved (FDA/EMA) for Merkel cell carcinoma and locally advanced or metastatic urothelial carcinoma maintenance therapy, though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Human Herpesvirus 8-Related Tumor** — a category that encompasses HHV-8-driven malignancies such as Kaposi's sarcoma —
with **0 clinical trials** and **0 publications** currently supporting this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Urothelial carcinoma / Merkel cell carcinoma (globally approved; not marketed in Canada) |
| Predicted New Indication | Human Herpesvirus 8-Related Tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Avelumab is a fully human IgG1λ monoclonal antibody that binds PD-L1, blocking its interaction with both PD-1 and B7.1 receptors. This prevents tumour cells from suppressing cytotoxic T-cell activity, thereby restoring immune surveillance. Detailed mechanism of action data was not available in this dataset; however, based on well-established immunological principles and the drug's globally approved indications, the mechanistic rationale is clear and well-characterized.

HHV-8 (Kaposi's sarcoma-associated herpesvirus, KSHV) actively upregulates PD-L1 expression on infected and malignant cells as a viral immune evasion strategy — precisely the checkpoint that Avelumab targets. In theory, blocking PD-L1 in HHV-8-driven malignancies could restore T-cell-mediated anti-tumour and anti-viral activity. This mechanistic overlap explains why the TxGNN knowledge graph assigns a high prediction score: the model recognizes the PD-L1 node as a shared biological hub connecting Avelumab to HHV-8-associated oncogenesis.

However, the plausibility of the mechanism does not substitute for clinical evidence. HHV-8-related tumours (particularly Kaposi's sarcoma) are frequently associated with HIV-induced immunosuppression, where the safety and efficacy profile of immune checkpoint inhibitors remains poorly characterized. The 99.97% TxGNN score reflects knowledge graph connectivity, not empirical clinical performance; there are currently no registered trials or peer-reviewed publications evaluating Avelumab specifically in this disease context. This prediction is rated **L5** and warrants a **Hold** decision pending basic translational and safety data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Avelumab in human herpesvirus 8-related tumor.

---

## Literature Evidence

Currently no related literature available for Avelumab in human herpesvirus 8-related tumor.

---

## Canada Market Information

Avelumab is not currently marketed in Canada. No DINs have been issued.

| DIN | Product Name | Dosage Form | Approved Indication |
|-----|-------------|-------------|---------------------|
| — | — | — | No Canadian approvals on record |

> **Note:** Avelumab (Bavencio®) holds FDA approval (USA) for: (1) Merkel cell carcinoma and (2) locally advanced or metastatic urothelial carcinoma (first-line maintenance following platinum-based chemotherapy). Canadian regulatory status should be verified directly with Health Canada.

---

## Cytotoxicity

Avelumab is classified as an antineoplastic immunotherapy agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunotherapy — Immune Checkpoint Inhibitor (fully human anti-PD-L1 IgG1 monoclonal antibody) |
| Myelosuppression Risk | Low (immune-mediated haematological toxicities, e.g., haemolytic anaemia, thrombocytopenia, are rare but reported) |
| Emetogenicity Classification | Minimal |
| Monitoring Items | LFTs (AST/ALT/bilirubin), thyroid function (TSH/free T4), CBC with differential, serum cortisol/ACTH (adrenal insufficiency), renal function, blood glucose; routine irAE surveillance at each infusion cycle |
| Handling Protection | Standard aseptic handling per monoclonal antibody preparation guidelines; conventional cytotoxic drug handling protocols (closed-system transfer devices, PPE for cytotoxics) are generally not required for immunotherapy biologics |

---

## Safety Considerations

Detailed warnings and contraindications specific to this dataset were not available. Please refer to the Bavencio® prescribing information for full safety data.

> **Reviewer note for HHV-8-related tumour context:** A particular safety concern exists for this proposed indication. HHV-8 malignancies frequently occur in HIV-positive immunosuppressed patients. Using an immune checkpoint inhibitor in this population carries heightened risk of immune reconstitution inflammatory syndrome (IRIS) and unpredictable irAE profiles. This safety signal should be a primary focus before any preclinical or clinical investigation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure TxGNN model prediction (L5) with no supporting clinical trials or peer-reviewed literature for Avelumab in HHV-8-related tumours. Despite a biologically plausible mechanistic link via PD-L1 upregulation, the complete absence of empirical data — combined with meaningful safety concerns in the immunosuppressed patient population most affected by HHV-8 malignancies — precludes advancing to the next evaluation stage.

**To proceed, the following is needed:**

- **MOA & safety data retrieval:** Download and parse full Bavencio® prescribing information to complete the drug-level safety profile (currently blocking: DG001, DG002)
- **Translational literature search:** Broaden the search to checkpoint inhibitor use in Kaposi's sarcoma and KSHV-associated lymphomas (PD-L1 expression studies, case reports, small cohort data)
- **Safety subpopulation analysis:** Assess irAE and IRIS risk specifically in HIV-positive and otherwise immunocompromised patients receiving anti-PD-L1 therapy
- **Health Canada status verification:** Confirm whether Avelumab has been submitted to or reviewed by Health Canada; update market status accordingly
- **Separate evaluation for urothelial subtypes:** Ranks 9 (prostatic urethra urothelial carcinoma, L4) and 10 (kidney pelvis sarcomatoid transitional cell carcinoma, L3) in this evidence pack share direct mechanistic lineage with Avelumab's globally approved urothelial carcinoma indication and carry substantially stronger evidence — these two candidates should be prioritized for independent, expedited evaluation

---

*This report is generated for research reference purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

