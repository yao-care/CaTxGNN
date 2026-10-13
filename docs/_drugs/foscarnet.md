---
layout: default
title: Foscarnet
parent: Model Prediction Only (L5)
nav_order: 412
evidence_level: L5
indication_count: 4
---

# Foscarnet
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Foscarnet: From Antiviral Therapy to Autosomal Dominant Familial Hematuria-Retinal Arteriolar Tortuosity-Contractures Syndrome

## One-Sentence Summary

Foscarnet is an antiviral drug (a pyrophosphate analog) that inhibits viral DNA polymerase, and it is best known for treating cytomegalovirus (CMV) infections of the eye.
The TxGNN model predicts it may be effective for **autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome**, but **no clinical trials and no relevant publications** currently support this prediction. It rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data compiled for this report |
| Predicted New Indication | Autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. From general pharmacology, foscarnet is a pyrophosphate analog that blocks viral DNA polymerase, and its established use is against herpesvirus infections such as CMV retinitis.

The predicted condition is an ultra-rare genetic disorder caused by COL4A1 mutations. It features tortuous retinal arteries, blood in the urine and joint contractures. It is a defect in collagen IV, not an infection. Foscarnet has no known action on this pathway, so **no plausible biological link was identified**.

The high score most likely reflects proximity in the knowledge graph through shared retinal features (for example, CMV retinitis), not a true therapeutic rationale. The score should therefore be read with caution.

Other high-scoring predictions for this drug show a similar pattern:

- **Brain small vessel disease 1 with or without ocular anomalies** (score 99.54%): also COL4A1-related, with the same lack of mechanistic link.
- **Rheumatoid arthritis** (score 99.52%): the retrieved papers mainly concern CMV/EBV infections and leflunomide, an RA drug used off-label against CMV. Foscarnet does not treat RA itself.
- **Diabetic nephropathy** (score 99.43%): foscarnet is itself nephrotoxic, so the safety direction is likely opposite to a therapeutic effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top predicted indication.

For reference, the second-ranked prediction (brain small vessel disease) retrieved publications that match on ocular keywords only and do not address that disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7802522](https://pubmed.ncbi.nlm.nih.gov/7802522/) | 1995 | RCT (CMV retinitis, toxicity comparison) | Archives of Internal Medicine | Compared morbidity and toxic effects of ganciclovir vs foscarnet in CMV retinitis; not relevant to the predicted disease |
| [8564639](https://pubmed.ncbi.nlm.nih.gov/8564639/) | 1995 | Preclinical (animal toxicity) | J Ocul Pharmacol Ther | Ocular toxicity of iontophoretic foscarnet in rabbits |
| [8865393](https://pubmed.ncbi.nlm.nih.gov/8865393/) | 1996 | Case report | Retina | CMV retinitis associated with Hodgkin's disease |
| [8660168](https://pubmed.ncbi.nlm.nih.gov/8660168/) | 1996 | Questionnaire development | Arch Ophthalmol | Visual function and quality-of-life questionnaire for CMV retinitis |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02505924 | VOCARVI | Not specified | Not specified |

---

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease contraindication links in the TxGNN knowledge graph, not from label text):

- **Cardiac rhythm:** long QT syndrome (including familial), torsades de pointes
- **Neurological:** epilepsy
- **Kidney and electrolytes:** kidney disease, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, hyperphosphatemia, hypophosphatemia
- **Blood:** neutropenia (including several congenital forms), agranulocytosis, anemia, macrocytic anemia, cyclic hematopoiesis

**Drug Interactions:** 100 interactions were identified. Examples include:

- **Major:** amphotericin B (including lipid complex), dolasetron, bupropion
- **Moderate:** famotidine, omeprazole, rabeprazole, dexlansoprazole, clarithromycin, hydrocortisone, dexamethasone, betamethasone, triamcinolone, beclomethasone, mesalazine, balsalazide, loperamide, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes

The documented toxicities of foscarnet (kidney impairment, electrolyte disturbance, seizures) would be a particular concern in the vulnerable populations of the predicted indications, such as patients with cerebrovascular disease or kidney disease.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5), with no clinical trials and no relevant literature. No biological link exists between a viral DNA polymerase inhibitor and a collagen IV disorder. The drug's known kidney, electrolyte, cardiac-rhythm and seizure risks add further concern. The other top predictions show no stronger support.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently missing, and a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Original approved indication from the Canadian license (currently blank)
- Preclinical or mechanistic evidence showing a plausible effect in COL4A1-related disease
- A reassessment of whether the TxGNN score reflects true therapeutic potential or only retinal-phenotype overlap in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

