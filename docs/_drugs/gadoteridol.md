---
layout: default
title: Gadoteridol
parent: Model Prediction Only (L5)
nav_order: 420
evidence_level: L5
indication_count: 10
---

# Gadoteridol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Gadoteridol: From MRI Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Gadoteridol is a gadolinium-based MRI contrast agent (marketed in Canada as PROHANCE) used for diagnostic imaging, not for treatment.
The TxGNN model predicts a link to **osteoarthritis susceptibility**, but this is a graph-based prediction with **0 clinical trials** and **0 publications** for that exact term.
The related term "osteoarthritis" has **12 publications**, all on imaging or research use, and none show a therapeutic effect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Canadian licence record; gadoteridol is a diagnostic MRI contrast agent |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 98.90% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Gadoteridol is a non-ionic gadolinium chelate. It improves image contrast in MRI and has no known pharmacological activity on joint tissue.

The high TxGNN score most likely reflects associations in the knowledge graph. Gadoteridol appears often in studies of joints, cartilage, and synovium, but only as an imaging probe. Examples include synovitis assessment on contrast-enhanced MRI and non-ionic contrast in dual- and triple-contrast CT of cartilage. Nothing suggests it treats or modifies osteoarthritis, so there is no mechanistic link between the original use and the predicted indication.

The lower-ranked predictions are similar. Rheumatoid arthritis and congestive heart failure have literature on gadolinium-enhanced imaging only. Brachyolmia, hemoglobinopathy, and several rare skeletal dysplasias have no supporting evidence at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

There is no literature for "osteoarthritis susceptibility" itself. The table below shows the 10 most relevant publications for the closely related prediction, **osteoarthritis**. All are diagnostic or ex vivo studies, not treatment studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27161058](https://pubmed.ncbi.nlm.nih.gov/27161058/) | 2016 | Cohort | Eur J Radiol | Peripatellar synovitis on static and dynamic contrast-enhanced MRI and its association with pain in knee osteoarthritis |
| [32525582](https://pubmed.ncbi.nlm.nih.gov/32525582/) | 2020 | Ex vivo | J Orthop Res | Dual contrast CT (cationic iodine agent plus gadoteridol) characterises cartilage earlier than a single contrast agent |
| [37593815](https://pubmed.ncbi.nlm.nih.gov/37593815/) | 2024 | Ex vivo | J Orthop Res | Triple contrast CT (including gadoteridol) segments cartilage and reveals biomechanical differences in cadaveric knees |
| [31068614](https://pubmed.ncbi.nlm.nih.gov/31068614/) | 2019 | Ex vivo | Sci Rep | Synchrotron microCT quantifies cationic and non-ionic contrast agents in cartilage |
| [39622931](https://pubmed.ncbi.nlm.nih.gov/39622931/) | 2024 | Ex vivo | Sci Rep | Photon-counting dual-contrast CT (with gadoteridol) as a proof of concept for biomechanical assessment of cartilage |
| [33692379](https://pubmed.ncbi.nlm.nih.gov/33692379/) | 2021 | Ex vivo | Sci Rep | Quantitative dual-contrast photon-counting CT for cartilage health |
| [30816584](https://pubmed.ncbi.nlm.nih.gov/30816584/) | 2019 | Ex vivo | J Orthop Res | Full-body clinical CT with dual contrast images proteoglycan and water content in human cartilage |
| [31576504](https://pubmed.ncbi.nlm.nih.gov/31576504/) | 2020 | Ex vivo | Ann Biomed Eng | Triple contrast CT evaluates cartilage composition and segmentation at the same time |
| [32767676](https://pubmed.ncbi.nlm.nih.gov/32767676/) | 2021 | Ex vivo | J Orthop Res | Effects of cartilage constituents on simultaneous diffusion of cationic and non-ionic contrast agents |
| [21305156](https://pubmed.ncbi.nlm.nih.gov/21305156/) | 2009 | Study | Metallomics | Excess gadolinium found in femoral head bone of patients exposed to gadolinium contrast agents (a safety signal) |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2229056 | PROHANCE |

Dosage form and approved indication text are not recorded in the licence data received.

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried data.

Please refer to the package insert for warnings and contraindications. Health Canada package insert data has not yet been obtained.

Publication [21305156](https://pubmed.ncbi.nlm.nih.gov/21305156/) reports gadolinium retention in human bone after exposure to gadolinium contrast agents. This should be considered in any assessment beyond imaging use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph score alone (L5 for the exact indication). The related osteoarthritis literature is limited to imaging and ex vivo research. Gadoteridol is a diagnostic contrast agent with no known therapeutic action on joint tissue, so there is no supporting evidence for repurposing.

**To proceed, the following is needed:**
- Any therapeutic (not diagnostic) preclinical or clinical evidence in osteoarthritis
- Mechanism of action data from DrugBank
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage form for the Canadian licence
- Route compatibility assessment (an intravenous contrast agent versus the routes a joint therapy would need)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

