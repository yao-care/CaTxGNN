---
layout: default
title: Ozanimod
parent: Moderate Evidence (L3-L4)
nav_order: 697
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-13
description: "Ozanimod: predicted new indication Progressive relapsing multiple sclerosis (evidence level L4). Approved use: Multiple sclerosis (relapsing forms)"
monitor_inn: "OZANIMOD"
predicted_indications: ["progressive relapsing multiple sclerosis"]
---

# Ozanimod
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

# Ozanimod: From Multiple Sclerosis to Progressive Relapsing Multiple Sclerosis

## One-Sentence Summary

Ozanimod is an oral drug already used to treat relapsing forms of multiple sclerosis (MS).
The TxGNN model predicts it may be effective for **progressive relapsing multiple sclerosis**,
but there are currently **no registered clinical trials** for this indication. The supporting material is **18 publications**, mostly reviews and mechanism-related papers rather than direct efficacy studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (relapsing forms) |
| Predicted New Indication | Progressive relapsing multiple sclerosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ozanimod (brand name ZEPOSIA) is a sphingosine 1-phosphate (S1P) receptor modulator selective for S1P1 and S1P5. Currently, detailed mechanism-of-action data is not available in the data compiled for this report. Based on general knowledge of the drug class, S1P1 agonism traps lymphocytes in the lymph nodes, which reduces the number of autoreactive immune cells entering the central nervous system (CNS).

Ozanimod is already approved for relapsing forms of MS. Progressive relapsing MS is closely related to this indication in the disease classification. Ozanimod also crosses the blood-brain barrier, so S1P1/S1P5 activity on CNS cells (astrocytes, oligodendrocytes, microglia) could plausibly affect progression-related neurodegeneration. Preclinical work with a related S1PR-1/5 modulator (RP-101074) points in this direction.

The high prediction score mainly reflects how close progressive relapsing MS is to the already-approved relapsing MS indication. It is **not independent evidence** of benefit in progressive disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Compares immunomodulators and immunosuppressants in progressive MS; notes relative benefits and safety remain unclear because direct comparison trials are lacking |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Update on immunomodulators and immunosuppressants in relapsing-remitting MS |
| [32385738](https://pubmed.ncbi.nlm.nih.gov/32385738/) | 2020 | Review (drug approval summary) | Drugs | FDA approval of ozanimod for relapsing forms of MS, including clinically isolated syndrome, relapsing-remitting disease and active secondary progressive disease |
| [33287177](https://pubmed.ncbi.nlm.nih.gov/33287177/) | 2020 | Review | Neurology International | Comprehensive review of ozanimod in relapsing MS: disease, efficacy and side effects |
| [31598138](https://pubmed.ncbi.nlm.nih.gov/31598138/) | 2019 | Review | Ther Adv Neurol Disord | Latest therapeutic developments and future directions in progressive MS |
| [33797705](https://pubmed.ncbi.nlm.nih.gov/33797705/) | 2021 | Review | CNS Drugs | Overview of S1P receptor modulators in MS |
| [36946625](https://pubmed.ncbi.nlm.nih.gov/36946625/) | 2023 | Review | Expert Opin Pharmacother | Update on S1P receptor modulators (fingolimod, siponimod, ozanimod, ponesimod) in relapsing MS |
| [38162670](https://pubmed.ncbi.nlm.nih.gov/38162670/) | 2023 | Review | Front Immunol | Notes that disease-modifying therapies have limited efficacy in progressive MS, and discusses CNS-bioavailable therapies |
| [37638037](https://pubmed.ncbi.nlm.nih.gov/37638037/) | 2023 | Preclinical study | Front Immunol | S1PR-1/5 modulator RP-101074 showed beneficial effects in a model of CNS degeneration |
| [41919069](https://pubmed.ncbi.nlm.nih.gov/41919069/) | 2026 | Real-world registry study | Ther Adv Neurol Disord | Compares anti-CD20 therapies and S1P receptor modulators in late-onset MS (MSBase registry) |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02506009 | ZEPOSIA | Not specified | Not specified |
| 02505991 | ZEPOSIA | Not specified | Not specified |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from drug-disease relationship data, not package insert text, and need to be checked against the label):
  - Sleep-related breathing disorders: obstructive sleep apnea syndrome, sleep apnea syndrome, congenital central hypoventilation syndrome
  - Cerebrovascular disease: stroke disorder, cerebrovascular disorder, cerebral infarction, transient ischemic attack, vertebrobasilar insufficiency
  - Cardiac disease: myocardial infarction, coronary thrombosis, intermediate coronary syndrome, congestive heart failure, heart failure
  - Conduction disorders: sick sinus syndrome (including familial), atrioventricular block, sinoatrial block
  - Hemoglobinopathy
- **Drug Interactions**: 100 interactions were found in the DDI database; 20 are listed in the data compiled for this report, of which the **Major** ones include:
  - Isometheptene, famotidine, bupropion, morphine, lorcaserin, clarithromycin, diethylpropion, phentermine
  - Corticosteroids: hydrocortisone, triamcinolone, betamethasone, budesonide
  - Antiemetics: dolasetron, palonosetron
- **Moderate** interactions include ranitidine, cimetidine, epinephrine, loperamide, picosulfuric acid and polyethylene glycol (3350 with electrolytes).

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model scoring and a plausible class mechanism. No clinical trials have been registered for progressive relapsing MS, and the literature consists mainly of reviews and preclinical work. The high score largely reflects its closeness to the approved relapsing MS indication. Package insert safety data (warnings and contraindications) have also not been reviewed.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data (for example from DrugBank)
- Approved indication text and dosage forms for the two Canadian DINs
- Direct clinical evidence of ozanimod in progressive forms of MS, such as registered or completed trials
- A cardiac, respiratory and cerebrovascular risk assessment for the target population, given the knowledge-graph contraindication signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

