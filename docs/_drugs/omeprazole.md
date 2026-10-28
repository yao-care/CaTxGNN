---
layout: default
title: Omeprazole
parent: Model Prediction Only (L5)
nav_order: 686
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
monitor_inn: "OMEPRAZOLE"
predicted_indications: ["duodenal obstruction"]
description: "Omeprazole: predicted new indication Duodenal obstruction (evidence level L5). Approved use: Not recorded in the local data"
---

# Omeprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Omeprazole: Duodenal obstruction
{: .text-alpha }

## One-Sentence Summary

Omeprazole is a proton pump inhibitor originally used for gastric and duodenal ulcers, gastroesophageal reflux disease (GERD), esophagitis and Zollinger-Ellison syndrome.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 0.9964 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 14 of 14) |
| Number of DINs | 14 (valid: 14) |
| Recommended Decision | Hold (research question only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, omeprazole is a proton pump inhibitor that suppresses gastric acid secretion. Its efficacy in acid-related disorders such as GERD, esophagitis and peptic ulcer is established.


There are important limits. Omeprazole does not directly block bile reflux, and studies in Barrett's oesophagus show modest or inconsistent effects on duodenogastric reflux. Rat studies also suggest that acid blockade combined with duodenogastric reflux may promote mucosal growth and gastric carcinogenesis. This is a safety signal that must be resolved before any repurposing recommendation.

A second predicted indication, duodenal obstruction (score 0.9964), is not supported. Obstruction is usually mechanical, and omeprazole is not expected to relieve it. Any benefit would be indirect, through healing of ulcer disease, which is already an approved effect. That prediction is rated L4 and Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | Not applicable | Completed | 157 | Diagnostic imaging study (endoscopic tri-modal imaging) to distinguish functional dyspepsia from reflux disease. It does not test omeprazole, so relevance is indirect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Clinical study (human) | Gut | Omeprazole 20 mg twice daily and its effect on duodenogastric and gastro-oesophageal bile reflux in Barrett's oesophagus |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Clinical study (human) | Scand J Gastroenterol | Omeprazole may reduce antral duodenogastric reflux in Barrett's oesophagus |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Prospective study | J Pediatr Gastroenterol Nutr | Omeprazole for oesophageal bile reflux in children |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | Clinical study | Eur J Pediatr | Primary duodenogastric reflux in six children and adolescents, unresponsive to antacid therapy |
| [8076761](https://pubmed.ncbi.nlm.nih.gov/8076761/) | 1994 | Clinical study | Gastroenterology | Relationship of duodenogastroesophageal reflux to pH, and its importance in Barrett's oesophagus |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | Update on clinical use and pharmacokinetics of proton pump inhibitors |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Animal study (rat) | Dig Dis Sci | Acid blockade with omeprazole promotes gastric carcinogenesis induced by duodenogastric reflux |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Animal study (rat) | Acta Cir Bras | Whether omeprazole has a protective effect on the gastric mucosa in rats with duodenogastric reflux |
| [8943968](https://pubmed.ncbi.nlm.nih.gov/8943968/) | 1996 | Animal study (rat) | Dig Dis Sci | Duodenogastric reflux stimulates foregut mucosal growth, and acid blockade potentiates this |
| [20697939](https://pubmed.ncbi.nlm.nih.gov/20697939/) | 2010 | Clinical study | Chin J Integr Med | Acupuncture for gastroesophageal reflux (not specific to omeprazole) |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00846503 | LOSEC | Not listed | Not listed |
| 02242462 | LOSEC MUPS | Not listed | Not listed |
| 02295407 | TEVA-OMEPRAZOLE | Not listed | Not listed |
| 02245058 | APO-OMEPRAZOLE | Not listed | Not listed |
| 02296446 | SANDOZ OMEPRAZOLE | Not listed | Not listed |

Fourteen single-ingredient licences are valid in Canada and none are cancelled. Only five are shown here.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** liver failure, liver disease, gallbladder disease, congestive heart failure, osteoporosis, postmenopausal osteoporosis, bone fracture and chronic atrophic gastritis.
- **Drug interactions:** The interaction screen returned 100 records. Major interactions include **acalabrutinib** and **atazanavir**. Moderate interactions include hydrochlorothiazide, alprazolam, atorvastatin, fenofibrate, apalutamide, armodafinil, amphetamine, anagrelide, and amphotericin B and its formulations. Minor interactions include lidocaine, nifedipine, ambrisentan and acetylsalicylic acid.
- **Carcinogenesis signal:** Rat studies suggest that acid blockade combined with duodenogastric reflux may promote gastric carcinogenesis. Human relevance is unknown.

Please also refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Detailed mechanism of action data
- Controlled human studies of omeprazole in duodenogastric reflux, with bile-reflux outcomes
- Assessment of the long-term gastric carcinogenesis signal in humans
- Review of the high-risk interactions (acalabrutinib, atazanavir) and the knowledge graph contraindication signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

