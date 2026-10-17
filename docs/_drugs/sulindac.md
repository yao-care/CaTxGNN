---
layout: default
title: Sulindac
parent: Model Prediction Only (L5)
nav_order: 873
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sulindac: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Bursitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis…"
monitor_inn: "SULINDAC"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "pseudoachondroplasia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "WHIM syndrome", "hypermobility of coccyx"]
---

# Sulindac
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Sulindac: From Musculoskeletal Inflammatory Conditions to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Sulindac is a non-steroidal anti-inflammatory drug (NSAID) originally used for inflammatory joint and soft-tissue conditions such as rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout, bursitis and tendinitis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder,
but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bursitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis, gout, osteoarthritis (from the knowledge graph; no approved indication text is available for the Canadian licences) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sulindac is a cyclooxygenase (COX) inhibitor NSAID, its efficacy in inflammatory musculoskeletal conditions is established, and it is used to relieve pain and inflammation in joints and soft tissues.

For the predicted condition, however, the rationale is weak. Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia caused by loss-of-function variants in the CDMP1/GDF5 gene. This gene is part of the BMP/GDF5 signalling pathway, which sulindac does not target. No established mechanistic link exists between COX inhibition and correction of this defect.

The high TxGNN score most likely reflects proximity in the knowledge graph between sulindac and musculoskeletal disease terms, not a biological rationale. At best, an NSAID could relieve joint pain symptomatically, which falls within existing class use and would not be true repurposing.

Other top-ranked predictions show the same pattern. These include brachyolmia, pseudoachondroplasia, brachydactyly-syndactyly syndrome and WHIM syndrome. All have no clinical or literature evidence and little or no mechanistic plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00745596 | TEVA-SULINDAC | Not specified | Not specified |
| 00745588 | TEVA-SULINDAC | Not specified | Not specified |

## Safety Considerations

- **Contraindications and risk conditions (from the knowledge graph, not label text)**: The knowledge graph links sulindac to the following conditions, which signal caution.
  - Cardiovascular: hypertension, congestive heart failure, myocardial infarction, coronary thrombosis, cardiovascular disease
  - Gastrointestinal: active peptic ulcer disease
  - Renal and hepatic: kidney disease, liver disease, nephrolithiasis, acute urate nephropathy
  - Haematological: blood coagulation disease, anaemia, hemoglobinopathy
  - Autoimmune and connective tissue: systemic lupus erythematosus, connective tissue disease
  - Other: gallbladder disease, bone and cartilage disease, substance abuse/dependence
- **Drug Interactions**: The interaction screen returned 100 records. The 20 retrieved included mainly Moderate and some Minor interactions.
  - Moderate: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, metformin, sulfonylureas (glimepiride, chlorpropamide), mesalazine, balsalazide, potassium salts (potassium citrate, potassium bicarbonate), and bowel-preparation agents (picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate)
  - Minor: H2 blockers (famotidine, ranitidine, cimetidine) and linaclotide

Package insert warnings and contraindications could not be retrieved. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5), with no clinical trials or publications. Sulindac has no plausible mechanistic link to the GDF5-driven genetic defect in this condition. The high score likely reflects knowledge-graph proximity to musculoskeletal terms.

**To proceed, the following is needed:**
- Any preclinical or mechanistic evidence connecting COX inhibition to GDF5/BMP signalling or skeletal growth in this condition
- Mechanism of action data for sulindac
- Health Canada package insert warnings and contraindications, which is a blocking gap for safety screening
- A clear definition of the intended use. If it is only symptomatic joint pain relief, this is already within the NSAID class and is not a new indication.
- Consideration of other predicted indications, such as rheumatoid vasculitis, only if supporting clinical evidence emerges. The current evidence there is also lacking.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

