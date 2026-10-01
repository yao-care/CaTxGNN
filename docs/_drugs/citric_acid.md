---
layout: default
title: Citric Acid
parent: Model Prediction Only (L5)
nav_order: 198
evidence_level: L5
indication_count: 8
---

# Citric Acid
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

# Citric Acid: From Anticoagulant and Bowel-Preparation Products to Stomach Disease

## One-Sentence Summary

Citric acid appears in Canadian anticoagulant solutions (ACD-A) and bowel-preparation products, but no approved indication text is on file.
The TxGNN model predicts it may be useful for **stomach disease**. In practice, **29 clinical trials** and **20 publications** were retrieved, and **none tests citric acid as a treatment for a stomach disease**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Use (Canada) | No approved indication text on file. Product names suggest anticoagulant citrate dextrose solution, bowel-preparation products and a heparin/dextrose injection |
| Predicted New Indication | Stomach disease |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 (preclinical/mechanistic and diagnostic-use studies only) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for citric acid. Its role in the products above (anticoagulation, bowel cleansing) is not a therapeutic effect on the stomach, so the original use gives no direct mechanistic bridge to gastric disease.

The evidence retrieved is weak and mostly indirect:

- **Diagnostic adjunct, not treatment.** A citric acid test meal delays gastric emptying and lowers gastric pH, which may improve the accuracy of the 13C-urea breath test for *H. pylori*. This helps detect infection; it does not treat gastric disease.
- **Metabolism papers.** Gastric cancer studies (energy metabolism, cuproptosis, metabolic subtypes) mention citrate and TCA-cycle biology. They do not show that giving citric acid has therapeutic value.
- **Salt/complex studies.** A 1997 rat study tested a bismuth–citrate complex combined with a roxatidine metabolite against stress ulcers. Any effect cannot be attributed to citric acid itself.

The high TxGNN score is best read as a model-derived hypothesis, not a supported therapeutic signal.

---

## Clinical Trial Evidence

The search returned 29 trials. None studies citric acid as a therapy for stomach disease. The most relevant ones are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03812380](https://clinicaltrials.gov/study/NCT03812380) | Phase 3 | Terminated | 62 | Effervescent calcium magnesium citrate to avert complications (fractures, low magnesium, kidney disease) of proton pump inhibitor therapy. The citrate is a supplement carrier, not a gastric treatment |
| [NCT02830789](https://clinicaltrials.gov/study/NCT02830789) | N/A | Completed | 38 | Calcium citrate vs calcium carbonate for secondary hyperparathyroidism after Roux-en-Y gastric bypass |
| [NCT03342456](https://clinicaltrials.gov/study/NCT03342456) | Phase 4 | Completed | 184 | Ilaprazole/doxycycline bismuth quadruple therapy for *H. pylori* duodenal ulcer. Citric acid is not the studied intervention |
| [NCT05196945](https://clinicaltrials.gov/study/NCT05196945) | Phase 4 | Unknown | 316 | Vonoprazan plus amoxicillin for first-line *H. pylori* eradication |
| [NCT06760065](https://clinicaltrials.gov/study/NCT06760065) | Phase 3 | Not yet recruiting | 316 | Keverprazan–amoxicillin dual therapy vs susceptibility-guided quadruple therapy for *H. pylori* rescue |
| [NCT03320538](https://clinicaltrials.gov/study/NCT03320538) | N/A | Completed | 360 | Herbal product (Hou Gu Mi Xi) in peptic ulcer disease. Citric acid is not the tested agent |
| [NCT04095975](https://clinicaltrials.gov/study/NCT04095975) | Phase 4 | Completed | 31 | Baking soda vs LithoLyte to raise urinary citrate and pH for kidney stone risk. Relevant to the kidney, not the stomach |
| [NCT03425747](https://clinicaltrials.gov/study/NCT03425747) | Phase 4 | Completed | 26 | Calcium citrate vs calcium carbonate in chronic hypoparathyroidism |
| [NCT07122284](https://clinicaltrials.gov/study/NCT07122284) | N/A | Completed | 42 | Observational gut microbiota and metabolic profiling in *H. pylori* plus SIBO. No citric acid intervention |
| [NCT04329494](https://clinicaltrials.gov/study/NCT04329494) | Phase 1 | Recruiting | 49 | PIPAC chemotherapy in peritoneal carcinomatosis, including gastric cancer. Unrelated to citric acid |

---

## Literature Evidence

The search returned 20 publications. None is a randomized trial of citric acid for a gastric condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Diagnostic accuracy | Gut Liver | Asks whether a citric acid meal improves 13C-urea breath test accuracy for *H. pylori* in Asian populations. This is a diagnostic use |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Biomarker study | Metabolomics | High serum L-carnitine and citric acid are detectable in Koreans before gastric cancer onset, suggesting a possible risk marker |
| [9379358](https://pubmed.ncbi.nlm.nih.gov/9379358/) | 1997 | Animal study | J Pharm Pharmacol | A roxatidine metabolite salt with a bismuth–citric acid complex protected rats against stress ulcers. The effect is not attributable to citric acid alone |
| [4000241](https://pubmed.ncbi.nlm.nih.gov/4000241/) | 1985 | Clinical study | N Engl J Med | Calcium citrate was absorbed better than calcium carbonate in patients with achlorhydria. This concerns calcium absorption, not treating stomach disease |
| [6027230](https://pubmed.ncbi.nlm.nih.gov/6027230/) | 1967 | Biochemical analysis | Gastroenterology | Measured lactic, pyruvic, citric and uric acid and urea in human gastric juice |
| [37477784](https://pubmed.ncbi.nlm.nih.gov/37477784/) | 2024 | Review | Clin Transl Oncol | Energy metabolism as a target in gastric cancer treatment |
| [39539553](https://pubmed.ncbi.nlm.nih.gov/39539553/) | 2024 | Review | Front Immunol | Role of cuproptosis in gastric cancer |
| [38959111](https://pubmed.ncbi.nlm.nih.gov/38959111/) | 2024 | Molecular cohort | Cell Rep | Metabolic signature subtypes in gastric cancer, including TCA-cycle upregulation in the better-prognosis subtype |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Review | Med Clin North Am | Diet in ulcer disease. Restrictive diets are not supported, and the review does not address citric acid therapy |
| [26088916](https://pubmed.ncbi.nlm.nih.gov/26088916/) | 2015 | Metabolomics | Appl Biochem Biotechnol | LC/MS metabolomic analysis in gastric cancer |

---

## Canada Market Information

Ten authorizations are on file. The first five are shown below. Dosage form and approved indication text are not recorded in the source data.

| DIN | Product Name |
|---------|------|
| 02469731 | Anticoagulant Citrate Dextrose Solution USP (ACD) Formula A |
| 02317966 | Purg-Odan |
| 00788139 | Anticoagulant Citrate Dextrose Solution USP (ACD) Formula A |
| 02254794 | Pico-Salax |
| 01935941 | Heparin Sodium in 5% Dextrose Injection, 25000 unit/500 mL |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for citric acid.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.74%), but no trial or publication shows that citric acid treats a stomach disease. Its only direct link is as a diagnostic aid for *H. pylori* breath testing. The other six predicted indications (pharyngitis, acute laryngopharyngitis, postgastrectomy syndrome, nasal cavity disease, papillary conjunctivitis, blepharoconjunctivitis) also remain on Hold. Rhinitis is the only one flagged as a research question, based on the anti-biofilm sinonasal irrigation work.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are needed before any safety screening
- Mechanism of action data (DrugBank query) to test whether any therapeutic link to gastric disease exists
- A clearly defined use case. Diagnostic adjunct (13C-urea breath test meal) and therapeutic use are separate questions, and the diagnostic one has the more plausible evidence
- Evidence from studies where citric acid itself is the tested intervention in a gastric condition, since current trials and papers involve only salts, complexes or unrelated agents
- Approved indication text and dosage forms for the Canadian products, to clarify the original use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

