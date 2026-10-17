---
layout: default
title: Rasburicase
parent: Model Prediction Only (L5)
nav_order: 798
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Rasburicase: predicted new indication Renal hypouricemia (evidence level L5). Approved use: Hyperuricemia"
monitor_inn: "RASBURICASE"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
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

# Rasburicase: From Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase originally used to treat hyperuricemia (high blood uric acid).
The TxGNN model predicts it may be effective for **renal hypouricemia**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The prediction is most likely a model artifact and is not biologically plausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia |
| Predicted New Indication | Renal hypouricemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, rasburicase is a recombinant urate oxidase enzyme that converts uric acid into allantoin, which lowers serum uric acid.

Renal hypouricemia is a condition in which uric acid is already abnormally low, typically because of loss-of-function variants in urate transporters such as URAT1 or GLUT9. Lowering uric acid further is mechanistically counterproductive and could increase the risk of harm. The relationship to the original indication is therefore one of opposition rather than similarity.

The very high TxGNN score most likely reflects the shared uric acid pathway in the knowledge graph rather than a plausible therapeutic link. This prediction should not be considered reasonable on mechanistic grounds.

The other nine predictions in the ranked list also have no supporting trials or literature. One of them, partial HPRT deficiency, is mechanistically related to the original indication because it causes hyperuricemia. However, rasburicase would not correct the underlying defect, and its injectable route and immunogenicity limit chronic use. Standard therapies are allopurinol and febuxostat. The remaining predictions are hepatic, renal tubular, and metabolic conditions with no evident mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02248416 | FASTURTEC | Not specified | Not specified |

---

## Safety Considerations

- **Drug Interactions**: 13 interactions were identified.
  - **Major (2):** Prilocaine and nitrous acid.
  - **Moderate (11):** Topical or ophthalmic local anaesthetics (tetracaine, lidocaine, benzocaine, cocaine, proparacaine, oxybuprocaine, cinchocaine) and idelalisib.
- **Other risks noted in the assessment**: Rasburicase carries potential risks of hemolysis in patients with G6PD deficiency, methemoglobinemia, and anti-drug antibody formation.

Please refer to the package insert for further safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. There are no clinical trials or publications, and the mechanism runs against the proposed use: further lowering uric acid in a condition of already low uric acid. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data, to support any mechanistic analysis
- Health Canada package insert warnings and contraindications, to allow safety screening
- A biological rationale explaining why urate lowering would benefit renal hypouricemia, which currently appears absent
- Any clinical or preclinical evidence supporting the predicted indication
- If a different direction is pursued, a review of the higher-plausibility candidate (partial HPRT deficiency) against existing standard therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

