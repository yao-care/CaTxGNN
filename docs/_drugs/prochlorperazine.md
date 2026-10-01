---
layout: default
title: Prochlorperazine
parent: Model Prediction Only (L5)
nav_order: 767
evidence_level: L5
indication_count: 10
---

# Prochlorperazine
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

# Prochlorperazine: From Antiemetic/Antipsychotic Use to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Prochlorperazine is a phenothiazine dopamine D2 antagonist, used as an antiemetic and antipsychotic.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but this is a graph-based prediction only, with **0 clinical trials** and **15 publications** that are generic eye-disease reviews and case reports containing no prochlorperazine-specific content.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, prochlorperazine is a D2 receptor antagonist from the phenothiazine class, used for nausea and psychiatric conditions.

No credible mechanistic link to inherited retinal degeneration has been identified, and no known pathway connects D2 antagonism to this disease. The very high TxGNN score reflects knowledge-graph proximity, not pharmacological evidence.

The retrieved publications look like keyword matches on the disease (congenital orbital and extraocular muscle disorders, lens anomalies, optic disc anomalies) rather than evidence about the drug. This prediction should be treated as a model artifact unless independent support emerges.

Other predictions in the pack are equally weak, including hydranencephaly, congenital glycosylation disorders, X-linked and syndromic myopia, Charcot-Marie-Tooth type 1G, polymicrogyria and atypical glycine encephalopathy. All have no trials or literature.

The one exception is **manic bipolar affective disorder** (rank 10, score 99.98%, evidence level L4). It is biologically plausible, because D2 antagonism is the mechanism shared with antipsychotics used for acute mania. However, the support is indirect: mostly 1950s-1970s case reports and class-level reviews, with no trials. The prochlorperazine-specific items are adverse-event reports (a confusional episode in a mildly manic-depressive patient, PMID 13617778, and phenothiazine-related seizures and EEG changes, PMID 6069087). A formal research question would need a modern comparison against established mania treatments.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications studies prochlorperazine. They are background reviews and case reports on congenital eye and orbital conditions. No RCTs were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections, most commonly secondary to sinusitis |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic approach to evaluating diplopia |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis: forms, associated findings and examination |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex: vitreoretinal degeneration with extraocular manifestations |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric ocular pathologies |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Review | Archives of Ophthalmology | Clinical features and management of orbital arteriovenous malformations |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two patients with unilateral cryptophthalmia |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | Journal of Neuro-Ophthalmology | Isolated congenital trochlear-oculomotor synkinesis in a 6-year-old boy |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optometry and Vision Science | Congenital fibrosis of the extraocular muscles with synergistic divergence |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 886432 | PROCHLORAZINE |
| 789720 | ODAN-PROCHLORPERAZINE |
| 886440 | PROCHLORAZINE |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials, the literature is unrelated to the drug, and no mechanism links D2 antagonism to inherited retinal dystrophy.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any drug-specific preclinical or clinical evidence for retinal dystrophy; without it, the manic bipolar disorder prediction (rank 10) is the better candidate for a research question, starting with a comparison against established mania treatments and attention to seizure threshold, confusion, dyskinesia and hyperglycemia

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

