---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Avapritinib
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

# Avapritinib: From GIST / Systemic Mastocytosis to Axial Spondylometaphyseal Dysplasia

## One-Sentence Summary

Avapritinib (Ayvakit) is a potent, highly selective inhibitor of KIT and PDGFRA kinases, approved by the FDA for PDGFRA D842V-mutant gastrointestinal stromal tumors (GIST) and advanced systemic mastocytosis, though it is not currently marketed in Canada.
The TxGNN model predicts it may be effective for **Axial Spondylometaphyseal Dysplasia**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | PDGFRA D842V-mutant GIST; Advanced systemic mastocytosis (FDA-approved; not marketed in Canada) |
| Predicted New Indication | Axial Spondylometaphyseal Dysplasia |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Avapritinib is a first-in-class, highly selective tyrosine kinase inhibitor specifically engineered to target KIT D816V and PDGFRA D842V mutations — activation-loop substitutions that confer resistance to most earlier-generation KIT inhibitors. In GIST and systemic mastocytosis, constitutive activation of these mutant kinases drives uncontrolled proliferation of tumour cells and neoplastic mast cells; avapritinib potently suppresses this signalling cascade. Detailed mechanism of action data (MOA) from DrugBank is currently unavailable and represents a blocking data gap (DG002).

Axial spondylometaphyseal dysplasia is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the *PAPSS2* gene, which encodes 3'-phosphoadenosine 5'-phosphosulfate synthase 2 — an enzyme critical for sulfate activation and sulfation of proteoglycans in cartilage matrix. The primary disease mechanism is therefore a defect in sulfate metabolism and chondrocyte extracellular matrix production, a pathway entirely distinct from KIT/PDGFRA signal transduction.

While PDGFRA signalling does play a broader role in mesenchymal progenitor cell biology, there is no established experimental connection between PDGFRA inhibition and PAPSS2-related chondrodysplasia. The TxGNN prediction most likely arises from indirect graph neighbourhood relationships within the knowledge network — possibly through shared bone metabolism or skeletal dysplasia nodes — rather than from any direct biological mechanism. This prediction should be treated as highly speculative hypothesis generation only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Avapritinib in axial spondylometaphyseal dysplasia.

---

## Literature Evidence

Currently no related literature available for Avapritinib in axial spondylometaphyseal dysplasia.

---

## Canada Market Information

Avapritinib is not currently approved or marketed in Canada. No Drug Identification Numbers (DINs) are on record with Health Canada.

---

## Cytotoxicity

Avapritinib is an antineoplastic targeted therapy approved for GIST and systemic mastocytosis.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective KIT/PDGFRA tyrosine kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate (anaemia and neutropenia reported; substantially lower myelosuppression risk than fluoropyrimidines or platinum agents) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST), neurological status (intracranial haemorrhage symptoms), cognitive function, blood pressure |
| Handling Protection | Follow institutional guidelines for oral targeted oncolytics; standard precautions apply — not classified as a conventional cytotoxic requiring closed-system transfer devices |

---

## Safety Considerations

Please refer to the package insert for safety information.

> No TFDA or Health Canada package insert data is currently available for this assessment (Data Gap DG001). The FDA prescribing information should be consulted as the primary safety reference. Of note, avapritinib carries a class-specific risk of **intracranial haemorrhage and posterior reversible encephalopathy syndrome (PRES)** that distinguishes it from other KIT inhibitors — this is particularly relevant when evaluating use outside its approved oncology indications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence connecting avapritinib to axial spondylometaphyseal dysplasia, and the mechanistic link between KIT/PDGFRA inhibition and the PAPSS2-driven sulfate metabolism defect underlying this condition is highly speculative. All ten predicted indications in this evidence pack are rated L5 with a Hold recommendation.

**To proceed, the following is needed:**

- **Fill Data Gap DG001**: Obtain Health Canada or TFDA package insert to establish a safety baseline before any repurposing evaluation can advance past Stage S0
- **Fill Data Gap DG002**: Retrieve full MOA profile from DrugBank to enable mechanistic link analysis
- **Preclinical hypothesis testing**: In vitro or animal studies to assess whether KIT/PDGFRA signalling has any functional role in PAPSS2-related cartilage pathology
- **Consider prioritising ALS-related predictions (Ranks 3, 5–10)**: The neuroinflammation/KIT-mast cell hypothesis for ALS carries a higher — though still speculative — mechanistic rationale; a focused evidence pack querying ALS-specific trials and masitinib/imatinib ALS literature would better characterise this cluster
- **Regulatory pathway clarification**: Since avapritinib is not marketed in Canada, any repurposing programme would need to account for the absence of an existing regulatory framework domestically

---

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All predictions are generated by the TxGNN computational model and have not been validated in clinical trials.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

