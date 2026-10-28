---
layout: default
title: Chlorambucil
parent: Model Prediction Only (L5)
nav_order: 180
evidence_level: L5
indication_count: 7
monitor_inn: "CHLORAMBUCIL"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma"]
last_modified_at: 2026-10-27
description: "Chlorambucil: predicted new indication Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Chlorambucil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Chlorambucil: DNA-alkylating agent → Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma
{: .text-alpha }

## One-Sentence Summary

Chlorambucil is an oral DNA-alkylating chemotherapy drug that has long been used in B-cell blood cancers.
The TxGNN model predicts it may be effective for **pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma**, with a score of 0.9972.
Evidence is thin: **no registered clinical trials** and **1 publication** (a 2003 review that is not specific to this subtype) were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma |
| TxGNN Prediction Score | 0.9972 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Chlorambucil is a nitrogen mustard-type alkylating agent: it damages the DNA of rapidly dividing cells and can kill malignant lymphocytes. Alkylators have been used for many years against slowly growing B-cell cancers.

The predicted disease is a subtype of chronic lymphocytic leukemia/small lymphocytic lymphoma (CLL/SLL), a mature B-cell cancer. Biologically, the link is plausible, and the prediction looks more like a refinement of a known disease group than a true shift to a new area.

There are important limits. The only retrieved publication is a 2003 Dutch-language review on risk-adapted management of CLL. It describes two CLL subtypes but gives no subtype-specific data on chlorambucil. It is a general review rather than a study of this disease, so the evidence level is held at L5. Modern practice also favours targeted agents (BTK inhibitors, venetoclax, anti-CD20 antibodies) over chlorambucil, especially in high-risk disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Review | Nederlands tijdschrift voor geneeskunde | CLL is the most common leukemia in the Western world and not truly indolent. Two subtypes exist (pre-germinal centre with unmutated immunoglobulin genes, and a post-germinal type), which supports a risk-adapted treatment approach. |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00004626 | LEUKERAN | Not recorded | Not recorded |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High. Bone marrow suppression (low white cells, platelets and red cells) is a recognised effect of this class |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Complete blood count with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations. Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Conditions flagged as contraindicated or cautioned in drug-disease relationship data (not label text):** thrombocytopenia, neutropenia, agranulocytosis, leukopenia, lymphopenia, anemia, interstitial lung disease, pulmonary fibrosis, drug-induced liver injury, nephrotic syndrome, epilepsy, and acute leukemias (including mixed phenotype acute leukemia).
- **Drug Interactions:** 100 interactions were recorded. Those classed as Major are:
  - Deferiprone
  - Samarium (153Sm) lexidronam

  Moderate interactions include amphotericin B products, palifermin, strontium chloride Sr-89, mercaptopurine, roflumilast and chloramphenicol. Levofloxacin is minor. Others, such as prednisone, warfarin, omeprazole and simvastatin, are unclassified.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but no trial or study directly examines chlorambucil in this subtype. The one publication is a general 2003 review, and current practice has largely moved to targeted therapies.

**To proceed, the following is needed:**
- Subtype-specific clinical data on chlorambucil, ideally comparison against current standard therapies
- Health Canada package insert warnings and contraindications, which are currently missing
- Mechanism-of-action data
- A review of how the hematologic and organ toxicities listed above apply to the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

