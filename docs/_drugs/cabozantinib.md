---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
---

# Cabozantinib
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

# Cabozantinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Cabozantinib is a multi-targeted oral tyrosine kinase inhibitor established internationally for advanced renal cell carcinoma and thyroid cancer, though it currently has no Health Canada–approved products and is not marketed in Canada.
The TxGNN model predicts it may be effective for **Liposarcoma** (the top-ranked prediction out of 10 candidates, score 99.83%), with **1 clinical trial** and **1 publication** currently supporting this direction.
Both studies address the broader soft tissue sarcoma population rather than liposarcoma specifically, placing this prediction at an early-stage hypothesis level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal Cell Carcinoma / Thyroid Cancer (internationally approved; **not registered in Canada**) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not captured in this evidence pack. Based on published pivotal trial descriptions, Cabozantinib is a small-molecule inhibitor that simultaneously targets VEGFR1/2/3 (anti-angiogenesis), MET (hepatocyte growth factor receptor), AXL, RET, FLT3, and KIT. This multi-kinase profile allows it to suppress tumour angiogenesis while blocking the compensatory escape mechanisms (MET and AXL upregulation) that commonly arise after single-target VEGFR inhibition — which is why it outperformed everolimus in the Phase 3 METEOR trial for advanced RCC.

Liposarcoma, particularly the dedifferentiated subtype (DDLPS), is associated with VEGF overexpression and tumour angiogenesis dependency. MET signalling activation has been reported in DDLPS, and the AXL pathway may play a role in CDK4/MDM2-amplified subtypes. Cabozantinib's simultaneous inhibition of VEGFR2, MET, and AXL offers a mechanistically plausible multi-target rationale that the TxGNN knowledge graph likely captured through topology linking soft tissue sarcoma nodes to Cabozantinib's target profile.

That said, no liposarcoma-specific biomarker or efficacy data exists for Cabozantinib. The one available clinical trial enrolls all soft tissue sarcoma subtypes without a dedicated liposarcoma cohort, and the mechanistic hypothesis — while biologically coherent — remains unvalidated in this specific tumour type. This prediction should be treated as a research question requiring prospective investigation before any development decision is made.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | Active, Not Recruiting | 66 | Randomised comparison of Ipilimumab + Nivolumab alone versus combined with Cabozantinib in advanced soft tissue sarcoma (metastatic/locally advanced). Liposarcoma is eligible as a STS subtype, but no liposarcoma-specific subgroup analysis has been reported to date. Estimated completion May 2026. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 Clinical Trial | American Journal of Clinical Oncology | Evaluated safety of neoadjuvant Cabozantinib combined with concurrent radiation therapy in patients with extremity soft tissue sarcoma. Addressed longstanding concern about fistula/perforation risk when combining Cabozantinib with RT. Preliminary tolerability established; liposarcoma not analysed as a distinct subtype. |

---

## Canada Market Information

Cabozantinib currently has **no Health Canada–approved products** and is not marketed in Canada (0 DINs on record).

> **For reference:** Cabozantinib (Cabometyx® tablets; Cometriq® capsules) is approved by the U.S. FDA for: advanced RCC (second-line monotherapy, 2016; first-line in combination with nivolumab, 2021), hepatocellular carcinoma (second-line, 2019), and thyroid cancer (medullary, 2012; differentiated, 2021). Canadian regulatory filing status should be confirmed directly with Health Canada's Drug Product Database prior to any access or development pathway planning.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — oral multi-kinase inhibitor (VEGFR1/2/3, MET, AXL, RET, KIT, FLT3); not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate — thrombocytopenia (~35%) and neutropenia (~31%) reported in the METEOR Phase 3 trial; Grade 3–4 haematological events require dose modification per prescribing information |
| Emetogenicity Classification | Low (nausea reported in ~45% of patients but predominantly Grade 1–2; vomiting less frequent) |
| Monitoring Items | CBC with differential, liver function tests (AST, ALT, bilirubin), thyroid-stimulating hormone (TSH), serum creatinine, blood pressure (hypertension is a class effect), urine protein-to-creatinine ratio, serum electrolytes (magnesium, phosphate), wound healing status |
| Handling Protection | NIOSH Table 2 hazardous drug — standard oral hazardous drug precautions apply (gloves when handling uncoated tablets; do not crush or split); full closed-system cytotoxic handling protocols are not required |

---

## Safety Considerations

No specific warning, contraindication, or drug interaction data was available in this evidence pack.

> Please refer to the full prescribing information for Cabometyx® or Cometriq® for complete safety details, including: **haemorrhage** (serious and fatal events reported), **perforations and fistulas** (gastrointestinal and non-GI), **thrombotic events** (arterial and venous), **hypertension**, **osteonecrosis of the jaw**, **palmar-plantar erythrodysaesthesia**, **QTc prolongation**, **wound healing complications** (hold at least 28 days before elective surgery), and **embryo-foetal toxicity**.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model generates a compelling high-confidence prediction score (99.83%) and the VEGFR/MET/AXL inhibition hypothesis is biologically plausible for dedifferentiated liposarcoma, but the only available clinical evidence comes from a non-liposarcoma-specific Phase 2 trial (indirect, Grade B) and a Phase 1 safety study — neither provides efficacy data in this specific tumour type, leaving the prediction at L3 evidence level without the target validation needed to justify a development decision.

**To proceed, the following is needed:**
- Liposarcoma-specific subgroup data from NCT05836571 (expected May 2026 completion) — this is the most actionable near-term data source
- Molecular profiling of liposarcoma specimens for VEGFR, MET, and AXL expression/amplification to confirm target presence
- Preclinical efficacy studies in liposarcoma cell lines and patient-derived xenograft models, particularly DDLPS models harbouring CDK4/MDM2 amplification
- Mechanism of action documentation from DrugBank to complete the formal mechanistic linkage analysis (DG002 remediation)
- TFDA/Health Canada package insert safety data retrieval to address the blocking data gap (DG001) before any safety evaluation can proceed
- Regulatory pathway review: if pursuing Canada access, a Health Canada New Drug Submission (NDS) or Priority Review pathway assessment is needed given the current 0-DIN status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

