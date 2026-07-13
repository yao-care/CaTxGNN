---
layout: default
title: Gadodiamide
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Gadodiamide
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

# Gadodiamide: From MRI Contrast Enhancement to Rheumatoid Arthritis

## One-Sentence Summary

Gadodiamide (Omniscan) is a paramagnetic gadolinium-based contrast agent used intravenously to enhance MRI signals by shortening T1 relaxation time in surrounding tissues — it is a diagnostic imaging agent, not a therapeutic drug.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **10 publications** retrieved — however, all literature describes Gadodiamide as an imaging tool used to *visualize* RA joint inflammation, not to *treat* it.
This prediction is assessed as a **false positive** driven by diagnostic co-occurrence in the knowledge graph rather than any therapeutic mechanism.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | MRI contrast enhancement (paramagnetic imaging agent) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Canada Market Status | Not marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Gadodiamide is a non-ionic, linear gadolinium chelate. Its sole mechanism of action is shortening the T1 relaxation time of nearby water protons in tissues, which produces brighter signal intensity on T1-weighted MRI sequences. It has no known interaction with immune pathways, cytokines, or cellular signaling cascades relevant to inflammatory disease. It does not inhibit TNF-α, IL-6, JAK-STAT pathways, or B/T cell activation — the primary drivers of rheumatoid arthritis pathology.

The high TxGNN score (99.16%) almost certainly reflects **diagnostic co-occurrence** rather than a therapeutic relationship. A large body of MRI research uses gadolinium-based contrast agents, including Gadodiamide, to image synovial inflammation, pannus formation, and bone erosions in RA patients. When TxGNN's knowledge graph links Gadodiamide nodes to RA nodes through shared literature, it cannot distinguish between "this agent was administered *to diagnose* RA" and "this agent was administered *to treat* RA."

In summary, **this prediction is not mechanistically reasonable**. Gadodiamide is an extracellular fluid marker with no anti-inflammatory, immunomodulatory, or disease-modifying properties. The retrieved literature uniformly concerns imaging methodology, not drug therapy. Pursuing this candidate for RA treatment would have no pharmacological basis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

All 10 retrieved publications describe Gadodiamide as an **MRI contrast agent used in diagnostic imaging studies** of RA patients. None evaluate Gadodiamide as a treatment for RA.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17289759](https://pubmed.ncbi.nlm.nih.gov/17289759/) | 2008 | Cross-sectional imaging | Ann Rheum Dis | Evaluated hand MRI (with gadolinium enhancement) vs bone scintigraphy for differential diagnosis of unclassified arthritis |
| [17935920](https://pubmed.ncbi.nlm.nih.gov/17935920/) | 2009 | Observational imaging | Eur J Radiol | Assessed intra-articular distribution of ultrasound-guided injections in RA wrist joints using contrast MRI |
| [18286282](https://pubmed.ncbi.nlm.nih.gov/18286282/) | 2008 | Cross-sectional imaging | Skeletal Radiol | Detailed contrast-enhanced MRI analysis of soft tissue, tendons, joints, and bones in psoriatic arthritis hands and wrists |
| [17340197](https://pubmed.ncbi.nlm.nih.gov/17340197/) | 2007 | Imaging/PK methodology | Ann Biomed Eng | Developed kinetic modeling of contrast-enhanced MRI to quantify RA wrist inflammation and monitor drug therapy response |
| [11454641](https://pubmed.ncbi.nlm.nih.gov/11454641/) | 2001 | Cross-sectional imaging | Ann Rheum Dis | Compared low-field extremity MRI vs X-ray for detecting inflammation and erosions in newly diagnosed untreated RA |
| [11669155](https://pubmed.ncbi.nlm.nih.gov/11669155/) | 2001 | Cross-sectional imaging | J Rheumatol | Characterized MRI features in wrist and finger joints across four groups: early RA, established RA, other arthritis, arthralgia |
| [11976868](https://pubmed.ncbi.nlm.nih.gov/11976868/) | 2002 | Longitudinal imaging | Eur Radiol | Assessed whether MRI synovial volumes and bone marrow edema at baseline predict bone erosion progression at 1 year |
| [11419149](https://pubmed.ncbi.nlm.nih.gov/11419149/) | 2001 | Comparative imaging | Eur Radiol | Compared 0.2T extremity MRI vs 1.5T high-field MRI diagnostic capability in arthritic small joints (103 patients) |
| [11274835](https://pubmed.ncbi.nlm.nih.gov/11274835/) | 2001 | Normal subjects imaging | Eur J Radiol | Evaluated normal gadolinium enhancement patterns of atlantoaxial joints in healthy subjects |
| [11868082](https://pubmed.ncbi.nlm.nih.gov/11868082/) | 2002 | Imaging methodology | Eur Radiol | Compared manual vs stereologic methods for estimating synovial volume on post-contrast 3D T1-weighted MR images in RA |

---

## Canada Market Information

Gadodiamide is **not currently marketed in Canada**. No Drug Identification Numbers (DINs) are on record.

> **Note:** Gadodiamide (brand name Omniscan) has been available in other jurisdictions (USA, EU) as a Health Canada Class III medical device/drug for MRI contrast enhancement. Its withdrawal or non-approval in Canada may relate to safety concerns regarding gadolinium deposition and Nephrogenic Systemic Fibrosis (NSF) risk in patients with severe renal impairment.

---

## Safety Considerations

> Detailed Canadian package insert warnings and contraindications are not available in this Evidence Pack. Based on the known pharmacological class, the following safety concerns are well-established in the medical literature and regulatory documentation from other jurisdictions:

- **Nephrogenic Systemic Fibrosis (NSF)**: Gadolinium-based contrast agents, particularly linear non-ionic chelates like Gadodiamide, are associated with NSF in patients with acute kidney injury or severe chronic kidney disease (eGFR < 30 mL/min/1.73m²). This risk led to Black Box Warnings in the USA and restricted use in multiple markets.
- **Gadolinium Tissue Deposition**: Research (including PMID 21305156 in this Evidence Pack) demonstrates that gadolinium accumulates in bone tissue in patients exposed to chelated gadolinium. The long-term clinical significance of this deposition is under ongoing investigation by regulators worldwide.
- **Hypersensitivity Reactions**: Anaphylactoid reactions have been reported with gadolinium-based contrast agents.

Please refer to the full prescribing information and current regulatory guidance for complete safety data before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Gadodiamide is an MRI contrast agent with no therapeutic mechanism relevant to any of the 10 predicted indications. All TxGNN predictions for this drug represent probable false positives arising from diagnostic co-occurrence in the knowledge graph — the drug is widely used to image musculoskeletal conditions (RA, OA, rare skeletal dysplasias) but has no pharmacological activity that could treat these diseases. Additionally, known safety concerns (NSF risk, gadolinium bone deposition) would present a significant harm-to-benefit challenge if therapeutic repurposing were attempted via systemic administration.

**To proceed, the following would be needed:**
- A credible hypothesis for a novel therapeutic mechanism entirely distinct from MRI contrast enhancement — none currently exists in the literature
- Preclinical data demonstrating anti-inflammatory, immunomodulatory, or disease-modifying activity of gadolinium chelates at sub-imaging doses
- Resolution of the gadolinium deposition safety signal before any chronic or repeated-dose therapeutic use could be considered
- A TxGNN pipeline review to implement filtering that separates diagnostic co-occurrence from therapeutic relationships, preventing similar false positives for other imaging agents in the database
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

