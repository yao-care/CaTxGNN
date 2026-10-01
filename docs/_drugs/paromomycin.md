---
layout: default
title: Paromomycin
parent: Model Prediction Only (L5)
nav_order: 701
evidence_level: L5
indication_count: 8
---

# Paromomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Paromomycin: From Intestinal Amebiasis to Idiopathic Copper-Associated Cirrhosis

## One-Sentence Summary

Paromomycin is a poorly absorbed oral aminoglycoside that acts on gut bacteria and protozoa, and is used for intestinal amebiasis. The TxGNN model predicts it may be effective for **idiopathic copper-associated cirrhosis**. There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Intestinal amebiasis (general drug knowledge; the Canadian license record contains no indication text) |
| Predicted New Indication | Idiopathic copper-associated cirrhosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Paromomycin is known as an aminoglycoside that is barely absorbed from the gut. It works locally against intestinal bacteria and protozoa.

Idiopathic copper-associated cirrhosis is a liver disease driven by copper accumulation and liver injury. Paromomycin has no known role in copper metabolism or copper-driven liver damage. No mechanistic link has been established.

The high score (0.999) is therefore a model output only. The same score appears for several other liver and portal-system conditions, which suggests the prediction may be an artifact of shared neighbors in the knowledge graph rather than true biology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top prediction.

---

## Other Predicted Indications

The model produced seven further predictions, all with no trials or literature except peritonitis. The mechanistic assessments are summarized below.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Primitive portal vein thrombosis | 99.90% | L5 | No anticoagulant or antithrombotic activity; likely a knowledge-graph artifact |
| 3 | Early-onset familial noncirrhotic portal hypertension | 99.90% | L5 | Rare genetic portal condition with no known link to aminoglycoside activity |
| 4 | Hepatopulmonary syndrome | 99.90% | L5 | Only a speculative link through gut bacterial translocation; no supporting studies |
| 5 | Hepatoportal sclerosis | 99.90% | L5 | No known effect on portal venous obliteration |
| 6 | Hepatic porphyria | 99.86% | L5 | Paromomycin does not target heme biosynthesis |
| 7 | Acute urate nephropathy | 99.79% | L5 | Biologically counterintuitive; aminoglycosides are associated with nephrotoxicity |
| 8 | Peritonitis | 99.03% | L4 | Indirect link only, via the underlying intestinal pathogen |

**Peritonitis** is the only other prediction with retrieved literature. Only 10 of 20 retrieved publications were provided, and no clinical trials were found. The relevant items are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34840954](https://pubmed.ncbi.nlm.nih.gov/34840954/) | 2021 | Case report | IDCases | Metronidazole plus paromomycin used for fulminant amoebic colitis during chemotherapy in a patient with small-cell lung cancer |
| [11096579](https://pubmed.ncbi.nlm.nih.gov/11096579/) | 1999 | Review | Curr Treat Options Gastroenterol | Amebiasis management, centered on metronidazole for amebic liver abscess |
| [4293095](https://pubmed.ncbi.nlm.nih.gov/4293095/) | 1967 | Review | JAMA | Nephrotoxicity of antibiotics, relevant to aminoglycoside safety |

Most of the other retrieved papers concern leishmaniasis (in vitro or formulation studies) and are not relevant to peritonitis. The case report supports activity against the intestinal pathogen, not direct treatment of peritonitis. Because paromomycin is poorly absorbed orally, systemic or intraperitoneal efficacy is not supported.

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2078759 | HUMATIN |

---

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried data.
- **Nephrotoxicity note**: Aminoglycosides are associated with kidney toxicity (PMID 4293095). This is a particular concern for the predicted indication of acute urate nephropathy.

Please refer to the package insert for warnings and contraindications, as these are not available in the current data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any clinical trial, publication, or plausible mechanism. Paromomycin's local gut action has no known connection to copper-associated cirrhosis. Evidence remains at L5 and the candidate has not advanced past the initial screening stage.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking paromomycin to copper-associated liver disease
- Approved indication text and dosage form for the Canadian license, to confirm the original indication and route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

