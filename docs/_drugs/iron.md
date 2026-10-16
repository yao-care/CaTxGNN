---
layout: default
title: Iron
parent: Model Prediction Only (L5)
nav_order: 497
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-13
description: "Iron: predicted new indication Plummer-Vinson syndrome (evidence level L5). Approved use: Iron deficiency anemia"
---

# Iron
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Iron: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Iron is an essential mineral, originally used to treat iron deficiency anemia and related nutritional anemias.
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome** (the top-scoring prediction with usable evidence), supported by **no registered clinical trials** and **19 publications**, mostly reviews and case reports.
This is a close extension of the existing indication rather than a truly new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia (the Canadian licence records contain no indication text; this is taken from the original indications list: iron deficiency anemia, folic acid deficiency anemia, anemia of prematurity, hypochromic anemia, microcytic anemia, deficiency anemia) |
| Predicted New Indication | Plummer-Vinson syndrome (the rank 1 prediction, vitamin B12- and folate-independent constitutional megaloblastic anemia, is mechanistically weak and has no evidence; see below) |
| TxGNN Prediction Score | 99.89% (Plummer-Vinson syndrome); rank 1 prediction scored 99.89% |
| Evidence Level | L4 (Plummer-Vinson syndrome) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 12 |
| Recommended Decision | Hold for the rank 1 prediction; Proceed with Guardrails is not yet justified for any candidate. Plummer-Vinson syndrome is best treated as a research question. |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, iron is an essential element needed for haemoglobin synthesis. Its efficacy in iron deficiency anemia is well established, and it may be applicable to conditions in which iron deficiency is the underlying driver.

**Plummer-Vinson syndrome** is defined by a triad of iron deficiency anemia, dysphagia and esophageal webs. Iron repletion is the established first-line treatment and often relieves dysphagia, sometimes before the blood abnormalities correct. Iron deficiency is thought to cause epithelial atrophy and dysfunction of the upper esophagus. The prediction therefore largely restates the approved use of iron in iron deficiency anemia.

**Other predictions are much weaker:**
- *Vitamin B12- and folate-independent constitutional megaloblastic anemia* (rank 1): this is a DNA synthesis disorder, not an iron supply problem. The link comes only from graph proximity to anemia terms. No trials or literature were found.
- *Non-syndromic esophageal malformation*: structural congenital defects need surgery. No mechanism or evidence supports iron.
- *Biotin metabolic disease*: the literature retrieved is general and does not test iron as a treatment.
- *Vitamin deficiency disorder*: the trials mostly test iron combined with other vitamins and do not isolate a benefit of iron. The category overlaps with the approved use.
- *Esophageal disease*: iron has a role only through Plummer-Vinson syndrome. The one trial treats anemia in a cancer setting, not the esophageal disease.

---

## Clinical Trial Evidence

For Plummer-Vinson syndrome: currently no related clinical trials registered.

For context, the closest trials among the other predicted indications:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05702970](https://clinicaltrials.gov/study/NCT05702970) | Phase 4 | Unknown | 258 | Vitamin D plus oral sucrosomial iron vs IV ferric carboxymaltose in heart failure with iron deficiency (vitamin deficiency disorder) |
| [NCT01475617](https://clinicaltrials.gov/study/NCT01475617) | Phase 2/3 | Completed | 61 | Multivitamin-mineral supplement to prevent deficiency after bariatric surgery; iron is one component |
| [NCT01927328](https://clinicaltrials.gov/study/NCT01927328) | Phase 4 | Unknown | 40 | IV iron isomaltoside for anemia in oesophagogastric adenocarcinoma; treats anemia, not the esophageal disease (esophageal disease) |
| [NCT06148545](https://clinicaltrials.gov/study/NCT06148545) | N/A | Completed | 57 | Iron plus vitamin D on iron status in children with iron deficiency anemia |
| [NCT04137354](https://clinicaltrials.gov/study/NCT04137354) | N/A | Completed | 504 | Intermittent iron and vitamin A supplementation in Ethiopian schoolchildren |
| [NCT01047098](https://clinicaltrials.gov/study/NCT01047098) | N/A | Completed | 114 | Prenatal vitamin-mineral supplements during lactation and iron status |

---

## Literature Evidence

Literature for Plummer-Vinson syndrome (most relevant first):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40802140](https://pubmed.ncbi.nlm.nih.gov/40802140/) | 2025 | Retrospective cohort | Dig Dis Sci | Multicenter analysis of clinical features and treatment outcomes of PVS; notes possible progression to esophageal squamous cell carcinoma |
| [39760192](https://pubmed.ncbi.nlm.nih.gov/39760192/) | 2025 | Systematic review | Oral Dis | Head and neck cancer manifestations in PVS |
| [29089792](https://pubmed.ncbi.nlm.nih.gov/29089792/) | 2017 | Review | J Blood Med | Current insights on iron deficiency anemia and PVS |
| [16978405](https://pubmed.ncbi.nlm.nih.gov/16978405/) | 2006 | Review | Orphanet J Rare Dis | Describes the triad of dysphagia, iron deficiency anemia and esophageal webs; extremely rare |
| [38871147](https://pubmed.ncbi.nlm.nih.gov/38871147/) | 2024 | Review | Clin Gastroenterol Hepatol | Classic triad of PVS |
| [7575056](https://pubmed.ncbi.nlm.nih.gov/7575056/) | 1995 | Case report and review | Arch Intern Med | Iron repletion often improves dysphagia; some patients need dilatation; surveillance endoscopy advised |
| [12823219](https://pubmed.ncbi.nlm.nih.gov/12823219/) | 2003 | Case report | Dis Esophagus | Two patients whose symptoms resolved with iron supplementation |
| [34616256](https://pubmed.ncbi.nlm.nih.gov/34616256/) | 2021 | Case report | Case Rep Gastroenterol | Iron supplementation as mainstay; dysphagia often responds before the anemia corrects |
| [26502163](https://pubmed.ncbi.nlm.nih.gov/26502163/) | 2015 | Review | J Pediatr Gastroenterol Nutr | PVS as a rare cause of dysphagia in children |
| [31417270](https://pubmed.ncbi.nlm.nih.gov/31417270/) | 2019 | Review | J Multidiscip Healthc | Multidisciplinary management; long-term surveillance for malignancy risk |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02502917 | PMS-IRON SUCROSE | Not recorded | Not recorded |
| 02243716 | VENOFER | Not recorded | Not recorded |
| 02546078 | FERINJECT | Not recorded | Not recorded |
| 02477777 | MONOFERRIC | Not recorded | Not recorded |
| 02243333 | FERRLECIT | Not recorded | Not recorded |

Seven further single-ingredient licences are also valid (including VELPHORO, ACCRUFER, ADDNUTRIV and several pregnancy multivitamin products), for 12 in total.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (disease associations, not label text): peptic ulcer disease, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease, ulcerative colitis, inflammatory bowel disease, hemolytic anemia, gastroenteritis.

**Drug Interactions:** 79 interactions were identified. Main ones:
- **Major:** dolutegravir, bictegravir
- **Moderate:** rabeprazole, omeprazole, doxycycline, tetracycline, ciprofloxacin, delafloxacin, alendronic acid, risedronic acid, ibandronate, levodopa, cefdinir, chloramphenicol, magnesium oxide, sodium citrate, pancrelipase, deferiprone, baloxavir marboxil
- **Minor:** cimetidine

Many of these reflect chelation or reduced absorption, so dose separation is typically relevant.

**Additional signal:** intravenous iron can cause hypophosphatemia through increased FGF23 (PMID 34534708). Plummer-Vinson syndrome also carries an elevated esophageal cancer risk, so surveillance matters regardless of iron treatment.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** for the rank 1 prediction (megaloblastic anemia) and for the weakly supported candidates. **Plummer-Vinson syndrome** is a Research Question: it is clinically credible but largely a restatement of the approved iron deficiency indication.

**Rationale:**
- Plummer-Vinson syndrome has consistent literature that iron repletion relieves symptoms, but it rests on reviews, case reports and one retrospective study (L4), with no registered trials.
- The other predicted indications lack a credible mechanism or test iron only as part of combination products.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada (a blocking gap for safety screening)
- Mechanism of action data for iron
- Review of PMID 40802140 for iron treatment outcomes, which could support L3
- Licence details (dosage form, approved indication) for Canadian products
- Confirmation of the population in NCT01927328 if esophageal disease is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

