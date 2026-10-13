---
layout: default
title: Meloxicam
parent: Model Prediction Only (L5)
nav_order: 581
evidence_level: L5
indication_count: 10
---

# Meloxicam
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

# Meloxicam: From Rheumatoid Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Meloxicam is a COX-2-preferential NSAID, originally used to treat rheumatoid arthritis, osteoarthritis and related joint conditions.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type** (a rare genetic skeletal disorder), but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (the Canadian licence records contain no indication text; the original indications come from the knowledge graph and also include osteoarthritis, juvenile idiopathic arthritis and spondyloarthropathy) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, meloxicam is a COX-2-preferential NSAID that reduces prostaglandin synthesis. Its efficacy in inflammatory and degenerative joint disease is established.

Acromesomelic dysplasia, Hunter-Thompson type is a rare skeletal dysplasia caused by CDMP1/GDF5 mutations. Meloxicam does not address this genetic defect. The high score most likely reflects network proximity to skeletal and joint phenotypes in the knowledge graph, not a therapeutic mechanism. At most, meloxicam could provide symptomatic pain relief for joint complaints, which is not disease modification.

**Other top-ranked predictions** follow a similar pattern:
- **Brachyolmia-amelogenesis imperfecta syndrome, brachyolmia, myosclerosis, WHIM syndrome and colobomatous microphthalmia-rhizomelic dysplasia syndrome**: no plausible mechanism and no evidence.
- **Pseudoachondroplasia**: NSAIDs are used for joint pain, but only symptomatically.
- **Rheumatoid nodulosis, spondyloarthropathy (susceptibility) and RF-positive polyarticular JIA**: close to existing indications, so they are better viewed as extensions of the current use than as true repurposing. The only retrieved paper, a Phase 4 registry on celecoxib and nonselective NSAIDs in JIA, gives class-level safety data but nothing specific to meloxicam.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02353148 | MELOXICAM | Not specified | Not specified |
| 02258315 | TEVA-MELOXICAM | Not specified | Not specified |
| 02390884 | AURO-MELOXICAM | Not specified | Not specified |
| 02353156 | MELOXICAM | Not specified | Not specified |
| 02258323 | TEVA-MELOXICAM | Not specified | Not specified |

All 10 licences are valid single-ingredient products. Only the first 5 are shown.

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** hypertension, kidney disease and impaired renal function, congestive heart failure and other heart or cardiovascular disease, myocardial infarction, stroke and cerebrovascular disorders, active peptic ulcer disease, gastritis, blood coagulation disease, anaemia and haemoglobinopathy, diabetes mellitus and diabetic ketoacidosis, hyperlipidaemia, and substance abuse/dependence.
- **Drug Interactions:** 100 interactions were found. Most of those listed are Moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, metformin, glimepiride, chlorpropamide, mesalazine, balsalazide, aprepitant, vancomycin, kanamycin, and several bowel preparations and potassium salts. Linaclotide is Minor.

Package insert warnings and contraindications were not retrieved, so please refer to the Health Canada package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no trials, no literature, and no plausible mechanism. Meloxicam would at best relieve symptoms and would not modify the disease. The knowledge-graph contraindication list is also extensive.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Evidence that meloxicam affects the GDF5/CDMP1 pathway or clinical outcomes in this disorder, if any exists
- Consider prioritising the closer-to-label predictions (RF-positive polyarticular JIA, spondyloarthropathy, rheumatoid nodulosis) as research questions, since they lie within the established class use of NSAIDs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

