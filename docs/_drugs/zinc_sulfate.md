---
layout: default
title: Zinc Sulfate
parent: Moderate Evidence (L3-L4)
nav_order: 993
evidence_level: L3
indication_count: 4
---

# Zinc Sulfate
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **4** 
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

# Zinc Sulfate: From Topical and Over-the-Counter Uses to Pharyngitis

## One-Sentence Summary

Zinc sulfate is a long-established ingredient in Canadian over-the-counter products, such as eye drops and haemorrhoid ointments and suppositories.
The TxGNN model predicts it may be effective for **pharyngitis**, with **1 clinical trial** and **2 publications** currently supporting this direction.
The evidence is directionally supportive but indirect, and the trial concerns postoperative sore throat rather than infectious pharyngitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the licence records compiled for this report |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, zinc sulfate is a zinc salt used as an ingredient in several marketed Canadian products (eye drops, anorectal ointments and suppositories). Its use in these products is local rather than systemic.

Zinc is plausibly active in the throat through local mucosal effects: antiviral activity, anti-inflammatory action and support of epithelial repair. Pharyngitis involves mucosal inflammation and epithelial irritation, which is where these effects could matter.

The TxGNN score is a computational prediction and does not replace clinical evidence. The available studies are small, address related but different conditions (postoperative and radiation-induced throat symptoms), and do not directly test infectious pharyngitis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | NA | Completed | 87 | Randomized, double-blinded, placebo-controlled study of preoperative zinc lozenges to reduce postoperative sore throat after intubation for general anaesthesia. The formulation is a lozenge, not zinc sulfate, and the condition is not infectious pharyngitis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | Randomized double-blind, placebo-controlled trial of zinc sulfate supplementation to reduce radiation-induced oral mucositis and pharyngitis in head and neck cancer patients. The abstract excerpt does not report results. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report/Other | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Discusses long-lasting taste disturbance after tonsillectomy, with a possible role for zinc deficiency. Indirectly relevant. |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02236399 | ANODAN-HC 10MG SUPPOSITORIES | Not specified | Not specified |
| 02290596 | ALLERGY EYE DROPS | Not specified | Not specified |
| 02338602 | VISINE MULTI-SYMPTOM | Not specified | Not specified |
| 02387239 | JAMPZINC-HC | Not specified | Not specified |
| 02128446 | ANODAN-HC OINTMENT | Not specified | Not specified |

A total of 14 single-ingredient licences are valid. The product names suggest eye-allergy and anorectal (haemorrhoid) uses.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships in the TxGNN knowledge graph, not from label text). These include:
  - Cardiovascular: hypertension, hypotension, heart disease.
  - Renal and urinary: kidney disease, nephrolithiasis, nephrocalcinosis.
  - Hepatic and gallbladder: liver disease, gallbladder disease.
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperthyroidism, Graves disease, hyperparathyroidism, hypercalcaemia.
  - Eye: angle-closure glaucoma.
  - Other: anxiety and neurotic disorders, sarcoidosis, diarrhoeal disease.

  These likely reflect the ingredients of combination products (for example hydrocortisone and decongestants) and need verification against the product labels.
- **Drug Interactions**: 100 interactions were found. The ones listed here are mostly minor. Moderate interactions include:
  - Alendronic acid
  - Risedronic acid
  - Ibandronate
  - Tetracycline
  - Baloxavir marboxil

  Minor interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone) and several immunosuppressants and biologics.
- **Intranasal use**: For the "nasal cavity disease" prediction (rank 2), the literature points to intranasal zinc sulfate as an agent used to induce anosmia in animals. This is a potential olfactory toxicity signal. It is relevant to any zinc product that reaches the nasal mucosa.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The only trial is Phase NA, tests a lozenge in postoperative sore throat, and does not directly support zinc sulfate for infectious pharyngitis. Package insert warnings and contraindications are not yet available, so safety screening cannot proceed. The high TxGNN score alone is not enough to advance.

**To proceed, the following is needed:**
- Health Canada package insert data (warnings, contraindications, indications) for the 14 licensed products.
- Mechanism of action data, for example from DrugBank.
- Confirmation of the design, power and results of the 2013 RCT (PMID 23720981). If it is well powered and relevant, the evidence level could be upgraded to L2.
- A decision on the route and formulation (for example lozenge or oral rinse), since no licensed Canadian product is currently identified for throat use.
- A review of the knowledge-graph contraindication signals against product labels.

**Other predicted indications (for reference):**
- **Nasal cavity disease** (score 99.81%): L4, Hold. The evidence is preclinical and suggests olfactory toxicity rather than benefit.
- **Acute laryngopharyngitis** (score 99.81%): L4, Research Question. One 2020 publication (PMID 33623304) covers radiation-induced oropharyngeal mucositis, which is indirect evidence.
- **Congenital prothrombin deficiency** (score 99.16%): L5, Hold. There is no clinical evidence or plausible mechanism, and this is likely a knowledge-graph artifact.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

