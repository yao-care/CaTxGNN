---
layout: default
title: Arginine
parent: Model Prediction Only (L5)
nav_order: 69
evidence_level: L5
indication_count: 1
---

# Arginine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Arginine: From Parenteral Nutrition Amino Acid Component to Gastroparesis

*The Canadian licence records give no approved-indication text. The "original indication" in this title is inferred from the product names (L-arginine injection, Clinimix, Travasol), which are amino acid and parenteral nutrition products.*

## One-Sentence Summary

Arginine is an amino acid marketed in Canada mainly in injectable and parenteral nutrition products.
The TxGNN model predicts it may be useful for **gastroparesis**, but the support is thin: **1 clinical trial** (not relevant) and **10 publications**, all preclinical or case reports, with no human study of arginine in gastroparesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (products are amino acid / parenteral nutrition) |
| Predicted New Indication | Gastroparesis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L4 (preclinical and mechanistic only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. The plausible link comes from known biology. L-arginine is the substrate of neuronal nitric oxide synthase (nNOS), which produces the nitric oxide needed for nitrergic relaxation of the stomach and pyloric sphincter. If arginine or nNOS signalling is impaired, gastric emptying can slow.

Three preclinical studies point the same way:
- **Glucocorticoid-induced gastroparesis in mice** occurs through depletion of L-arginine (PMID 25057793).
- **Tetrahydrobiopterin (BH4) deficiency in newborn mice** induces gastroparesis. BH4 is an essential nNOS cofactor (PMID 23639814).
- **A rat Parkinson's model** shows impaired nitrergic relaxation of the pyloric sphincter (PMID 35380456).

This evidence is indirect. It shows that the arginine/NO pathway matters in gastric motility, not that giving arginine treats gastroparesis in people. The TxGNN score is a model output, not clinical evidence. The drug's original indications and mechanism are missing from the record, so the fit with its known pharmacology could not be checked.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01702051](https://clinicaltrials.gov/study/NCT01702051) | N/A | Unknown | 150 | Observational study of autologous pancreatic islet transplantation for glycaemic control after pancreatectomy. It tests neither arginine nor gastroparesis, so it gives no supporting evidence (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25057793](https://pubmed.ncbi.nlm.nih.gov/25057793/) | 2014 | Preclinical (mouse) | Endocrinology | Dexamethasone caused gastroparesis in mice through depletion of L-arginine. The most direct link to arginine. |
| [23639814](https://pubmed.ncbi.nlm.nih.gov/23639814/) | 2013 | Preclinical (mouse) | Am J Physiol Gastrointest Liver Physiol | BH4 deficiency (a cofactor for NO synthesis) induced gastroparesis in newborn mice. |
| [35380456](https://pubmed.ncbi.nlm.nih.gov/35380456/) | 2022 | Preclinical (rat) | Am J Physiol Gastrointest Liver Physiol | Parkinson's rat model with gastroparesis showed impaired nitrergic relaxation of the pyloric sphincter. |
| [18312542](https://pubmed.ncbi.nlm.nih.gov/18312542/) | 2008 | Preclinical (rat) | Neurogastroenterol Motil | Reduced nNOS is a proposed mechanism of diabetic gastroparesis. Jejunal neuropathy studied in diabetic BB rats. |
| [18322959](https://pubmed.ncbi.nlm.nih.gov/18322959/) | 2008 | Preclinical (mouse) | World J Gastroenterol | Ghrelin and GHRP-6 effects on gastric motility in diabetic mice with gastroparesis. No arginine involvement. |
| [19023028](https://pubmed.ncbi.nlm.nih.gov/19023028/) | 2009 | Preclinical (dog) | Am J Physiol Gastrointest Liver Physiol | Synchronized gastric electrical stimulation improved impaired gastric accommodation via the nitrergic pathway. |
| [31984783](https://pubmed.ncbi.nlm.nih.gov/31984783/) | 2020 | Preclinical (rat) | Am J Physiol Gastrointest Liver Physiol | Sacral nerve stimulation increased gastric accommodation in rats. |
| [21193530](https://pubmed.ncbi.nlm.nih.gov/21193530/) | 2011 | Preclinical (animal) | Am J Physiol Gastrointest Liver Physiol | Hyperglycaemia inhibits gastric motility via nodose ganglia KATP channels. |
| [8194696](https://pubmed.ncbi.nlm.nih.gov/8194696/) | 1994 | Preclinical (rat) | Gastroenterology | Food-protein anaphylaxis delayed gastric emptying in rats. |
| [33867519](https://pubmed.ncbi.nlm.nih.gov/33867519/) | 2021 | Case report | Am J Case Rep | Lifestyle changes normalized serum lactate in an m.3243A>G carrier. Not relevant to arginine in gastroparesis. |

No RCTs, systematic reviews or human studies were found. The first three papers are the most relevant to the arginine/NO hypothesis.

## Canada Market Information

Showing 5 of 20 authorizations. Dosage form and approved-indication text are not recorded for these entries.

| DIN | Product Name |
|---------|------|
| 399736 | L-ARGININE HYDROCHLORIDE INJECTION |
| 2046709 | CLINIMIX |
| 2013932 | CLINIMIX |
| 2013940 | CLINIMIX |
| 872296 | TRAVASOL |

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is preclinical and indirect (L4), the single registered trial is unrelated, and no human study of arginine in gastroparesis exists. The Canadian package-insert safety data has not been obtained, which blocks safety screening. The high TxGNN score alone does not justify moving forward. This remains a research question.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, downloaded and parsed
- Mechanism of action and approved indications from DrugBank and the licence records
- Evidence that arginine supplementation, not just arginine/NO pathway disruption, improves gastric emptying (for example, a pilot study, or a review of human data on L-arginine and gastric motility)
- Route and dose feasibility assessment (available routes are not yet compared with those needed for gastroparesis)

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

