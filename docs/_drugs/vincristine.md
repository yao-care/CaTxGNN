---
layout: default
title: Vincristine
parent: Moderate Evidence (L3-L4)
nav_order: 977
evidence_level: L3
indication_count: 3
last_modified_at: 2026-10-13
description: "Vincristine: predicted new indication Ganglioneuroblastoma (evidence level L3). Approved use: Acute lymphoblastic leukemia, Hodgkin lymphoma, non-Hodgkin lymphoma…"
monitor_inn: "Vincristine"
predicted_indications: ["ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm"]
---

# Vincristine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **3** 
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

# Vincristine: From Acute Lymphoblastic Leukemia and Lymphoma to Ganglioneuroblastoma

## One-Sentence Summary

Vincristine is a vinca alkaloid chemotherapy drug, originally used for acute lymphoblastic leukemia, Hodgkin and non-Hodgkin lymphoma, mantle cell lymphoma and Langerhans cell histiocytosis.
The TxGNN model predicts it may be effective for **ganglioneuroblastoma**, a neuroblastic tumour.
Currently there are **no registered clinical trials** and **6 publications** (mostly case reports and small series, plus one prospective trial of a treatment strategy) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute lymphoblastic leukemia, Hodgkin lymphoma, non-Hodgkin lymphoma, mantle cell lymphoma, Langerhans cell histiocytosis (from the knowledge graph; no approved-indication text is available for the Canadian licences) |
| Predicted New Indication | Ganglioneuroblastoma |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Vincristine binds tubulin and inhibits microtubule polymerization, causing mitotic arrest in rapidly dividing cells. The mechanism-of-action field in the data compiled for this report is empty, so this description reflects the drug's well-known pharmacology rather than a sourced entry.

Ganglioneuroblastoma belongs to the neuroblastoma family of neuroblastic tumours. Vincristine is a standard component of multi-agent chemotherapy for these tumours, typically combined with cyclophosphamide, doxorubicin and platinum agents. The high TxGNN score (0.993) is consistent with this biological and clinical rationale.

An important caveat: the available evidence consists of case reports, small series and one prospective trial of a risk-stratified treatment strategy. The contribution of vincristine alone cannot be isolated from the combination regimens.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31342649](https://pubmed.ncbi.nlm.nih.gov/31342649/) | 2019 | Prospective clinical trial | Pediatric Blood & Cancer | JN-L-10 trial: using image-defined risk factors to guide timing of surgery in low-risk neuroblastic tumours, aiming to reduce treatment complications (chemotherapy context) |
| [8255850](https://pubmed.ncbi.nlm.nih.gov/8255850/) | 1993 | Case report | Postgraduate Medical Journal | Unresectable spinal ganglioneuroblastoma achieved histologically proven complete remission with chemotherapy alone (doxorubicin, vincristine, cyclophosphamide, etoposide, ifosfamide, cisplatin) |
| [15701990](https://pubmed.ncbi.nlm.nih.gov/15701990/) | 2005 | Case report | J Pediatr Hematol Oncol | Ganglioneuroblastoma presenting with obstructive jaundice, treated with cisplatin, pirarubicin/doxorubicin, cyclophosphamide and vincristine |
| [7421294](https://pubmed.ncbi.nlm.nih.gov/7421294/) | 1980 | Case series | J Thorac Cardiovasc Surg | 31 patients with intrathoracic ganglioneuroblastoma treated by resection, radiation or chemotherapy; 27 survived, followed up to 25 years |
| [3071124](https://pubmed.ncbi.nlm.nih.gov/3071124/) | 1988 | Case report | Hinyokika Kiyo | Multimodality treatment of adult adrenal ganglioneuroblastoma with large regional lymph node metastasis |
| [8888754](https://pubmed.ncbi.nlm.nih.gov/8888754/) | 1996 | Case report | J Pediatr Hematol Oncol | Stage 4 multifocal ganglioneuroblastoma with gastric involvement in an infant |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02183013 | Vincristine Sulfate Injection USP | Not specified | Not specified |
| 02143305 | Vincristine Sulfate Injection | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, antimitotic) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph lists leukopenia as a contraindicated condition. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count, liver function (including bilirubin), and neurological assessment for peripheral neuropathy |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: liver failure, hyperbilirubinemia (including Gilbert syndrome), cholestasis (including benign recurrent and familial intrahepatic forms), leukopenia, acute urate nephropathy, peripheral neuropathy and other peripheral nervous system disease, neuromuscular disease (including Charcot-Marie-Tooth disease), motor nerve neuritis and neuritis, infectious disease including fungal infection and dermatophytosis.
- **Drug Interactions**: The query returned 100 interactions in total; the main ones in the data are:
  - **Major**: clarithromycin
  - **Moderate**: aprepitant, dexamethasone, metronidazole, eliglustat, naltrexone, glycerol phenylbutyrate, miconazole, rolapitant, rosuvastatin, simvastatin, tinidazole, troglitazone
  - **Minor**: levofloxacin
  - **Unknown severity**: calcitriol, pantoprazole, clotrimazole, morphine, metformin, omeprazole

Package-insert warnings and contraindications for the Canadian products have not yet been obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Vincristine is a long-established component of multi-agent chemotherapy for neuroblastic tumours, and the prediction fits that clinical practice. However, the evidence is limited to case reports, small series and one strategy trial, with no registered trials, so the drug's individual contribution cannot be established.

**To proceed, the following is needed:**
- Canadian package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Approved-indication text and dosage forms for the two Canadian DINs
- Review of published neuroblastoma-family regimens and risk-stratified protocols to clarify vincristine's role
- A safety monitoring plan covering neurotoxicity, hepatic impairment and myelosuppression, and management of interactions (especially with strong CYP3A inhibitors such as clarithromycin)

---

### Other Predictions Reviewed (Not Selected)

- **Retroperitoneal neoplasm** (score 99.23%, L3): The literature covers vincristine-containing regimens in different histologies (paraganglioma, rhabdomyosarcoma, infantile fibrosarcoma, kaposiform hemangioendothelioma), mostly case reports. The evidence is indirect, so this is a research question that needs a histology-specific focus before any recommendation.
- **Vertebral anomalies and variable endocrine and T-cell dysfunction** (score 99.24%, L5): No evidence and no plausible mechanistic link. Vincristine's neurotoxicity and immunosuppressive effects could be harmful in patients with existing T-cell dysfunction. Recommendation: Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

