---
layout: default
title: Cimetidine
parent: Model Prediction Only (L5)
nav_order: 195
evidence_level: L5
indication_count: 4
monitor_inn: "CIMETIDINE"
predicted_indications: ["peptic ulcer perforation", "duodenal obstruction", "acne (disease)", "abnormality of glucagon secretion"]
last_modified_at: 2026-10-27
description: "Cimetidine: predicted new indication peptic ulcer perforation (evidence level L5). Approved use: Not recorded in the local data"
---

# Cimetidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Cimetidine: H2-receptor antagonist (acid suppression) → peptic ulcer perforation
{: .text-alpha }

## One-Sentence Summary

Cimetidine is an acid-suppressing H2-receptor antagonist that has been marketed in Canada.
The TxGNN model predicts it may be effective for **peptic ulcer perforation**, but there are **no registered clinical trials** and only **literature that is mostly indirect or case-level** (20 publications, mainly case reports and general ulcer papers) behind this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | peptic ulcer perforation |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, cimetidine is an H2-receptor antagonist that reduces gastric acid secretion. Acid suppression addresses the underlying ulcer disease, and this is the likely reason the model links the drug to ulcer perforation.

However, perforation is an acute surgical emergency, not a condition that acid suppression alone treats. Several supplied reports describe perforation occurring while patients were on cimetidine (PMIDs 3967139, 6743974) or after it was withdrawn (PMID 922364). A hospital review found only a 10% fall in perforations after cimetidine became available, versus a 45% fall in elective ulcer operations (PMID 7082957). The score therefore most likely reflects the link to ulcer disease in general, not a demonstrated benefit for perforation. The evidence signals possible treatment failure rather than protection.

No cited study tests cimetidine as a treatment for perforated ulcer itself, so the evidence level is L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8364140](https://pubmed.ncbi.nlm.nih.gov/8364140/) | 1993 | Review | Aliment Pharmacol Ther | Continuous H2-antagonist therapy reduces ulcer recurrence; relapse rates vary with study design |
| [7082957](https://pubmed.ncbi.nlm.nih.gov/7082957/) | 1982 | Case report/Letter | Br J Surg | After cimetidine, elective ulcer surgery fell 45% but perforations fell only 10% |
| [6743974](https://pubmed.ncbi.nlm.nih.gov/6743974/) | 1984 | Case report | Br J Surg | Nine duodenal ulcer perforations occurred during cimetidine therapy; all needed vagotomy and drainage |
| [3967139](https://pubmed.ncbi.nlm.nih.gov/3967139/) | 1985 | Case report | Br J Surg | Report of perforation occurring on cimetidine |
| [922364](https://pubmed.ncbi.nlm.nih.gov/922364/) | 1977 | Not classified | Br Med J | Perforation of peptic ulcer after withdrawal of cimetidine |
| [6649737](https://pubmed.ncbi.nlm.nih.gov/6649737/) | 1983 | Not classified | Z Gastroenterol | Operations fell 35% after cimetidine; ulcer-complication operations fell less than elective ones |
| [6861858](https://pubmed.ncbi.nlm.nih.gov/6861858/) | 1983 | Not classified | Eur J Clin Pharmacol | Ulcer-related discharges were about 10% lower once cimetidine became available |
| [1975090](https://pubmed.ncbi.nlm.nih.gov/1975090/) | 1990 | Not classified | Minerva Chir | Overview of ulcer therapy and surgery before and after the cimetidine era |
| [2573146](https://pubmed.ncbi.nlm.nih.gov/2573146/) | 1989 | Not classified | Scand J Gastroenterol Suppl | H2 antagonists protect mucosa against NSAID injury |
| [6150640](https://pubmed.ncbi.nlm.nih.gov/6150640/) | 1984 | Not classified | Am J Med | Hospitalisations for duodenal ulcer fell, but the perforation rate did not change significantly |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00584215 | CIMETIDINE | Not recorded | Not recorded |
| 00487872 | CIMETIDINE | Not recorded | Not recorded |

## Safety Considerations

**Drug Interactions** (100 interactions were found in the interaction database; examples):
- **Moderate**: paclitaxel, fentanyl, acalabrutinib, lidocaine, acebutolol, dihydrocodeine, codeine, tramadol, nifedipine, alfentanil
- **Minor**: dolutegravir, zidovudine, acetaminophen, ketorolac, ibuprofen, ethinylestradiol, albendazole, ethanol, alendronic acid, cholecalciferol

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or publication directly shows that cimetidine treats peptic ulcer perforation. The available case reports suggest perforation can occur despite therapy, and perforation requires surgical management. The high score appears to reflect the general link to ulcer disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada
- Mechanism of action data
- Controlled studies, if any, that examine cimetidine as an adjunct in perforated ulcer or in preventing perforation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

