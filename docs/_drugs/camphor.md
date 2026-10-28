---
layout: default
title: Camphor
parent: Model Prediction Only (L5)
nav_order: 149
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Camphor: predicted new indication Migraine disorder (evidence level L4). Approved use: Not stated in the available licence data"
monitor_inn: "Camphor"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "erectile dysfunction (disease)", "pulmonary hypertension", "kyphoscoliotic heart disease", "ulerythema ophryogenesis", "Raynaud disease", "atrophoderma vermiculata", "Tourette syndrome"]
---

# Camphor
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Camphor: From Topical Counter-Irritant Use to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Camphor is a long-established topical and rectal-use ingredient marketed in Canada, but the data compiled for this report do not state a formal approved indication for it.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no registered clinical trials** and only **3 publications** (case-level reports and a historical review), so the evidence is weak.
A newer preclinical animal study (2026) offers the strongest, though still early, signal for a related migraine prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 5 of 5) |
| Number of DINs | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled drug record. Based on general pharmacological knowledge, camphor modulates sensory ion channels (TRPV1, TRPM8 and TRPA1) and acts as a topical counter-irritant. These channels are plausibly relevant to trigeminal pain signalling in headache disorders.

The evidence connecting camphor to headache is thin and partly contradictory. The retrieved publications are case-level reports of cluster headache linked to toothpastes containing camphor and eucalyptus essential oils. They suggest a possible *trigger* for headache rather than a treatment. A historical review of paediatric neuropsychopharmacology is also not evidence of efficacy.

The most relevant signal is a 2026 preclinical study. It reports that natural (+)-camphor alleviated reserpine-induced migraine with local cerebral vasospasm in an animal model, possibly through the p38β MAPK/ATF2 pathway. It has not been tested in humans, and the full text has not been reviewed.

Other predictions (for example migraine with brainstem aura, Tourette syndrome, Raynaud disease and rare skin conditions) have no supporting evidence. The pulmonary hypertension hits are a false positive: "CAMPHOR" is the name of a quality-of-life questionnaire and has nothing to do with the compound.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case series | Headache | Five cases of cluster headache linked to toothpastes containing pro-convulsant essential oils |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case report | BMJ Case Reports | Two cluster headache cases temporally related to toothpaste containing camphor and eucalyptus oils |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Review | Z Kinder Jugendpsychiatr Psychother | Historical analysis of paediatric neuropsychopharmacotherapy in the 1940s–50s; not specific evidence for migraine |

Related preclinical evidence (listed under the related migraine prediction):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42849823](https://pubmed.ncbi.nlm.nih.gov/42849823/) | 2026 | Preclinical animal study | J Ethnopharmacol | Natural (+)-camphor alleviated reserpine-induced migraine with cerebral vasospasm via the p38β MAPK/ATF2 pathway |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 00299561 | CREO-RECTAL ADULTES/ADULTS | Not listed | Not listed |
| 00299596 | CREO-RECTAL ENFANTS/CHILDREN | Not listed | Not listed |
| 00319716 | DEMO-CINEOL ADULTES/ADULTS | Not listed | Not listed |
| 00319724 | DEMO-CINEOL ENFANTS/CHILDREN | Not listed | Not listed |
| 02157292 | BLISTEX DCT | Not listed | Not listed |

---

## Safety Considerations

- **Neurological risk**: Camphor is a known CNS convulsant at high doses, and case reports link camphor-containing essential oils to headache and seizure concerns. This is a significant concern for any neurological indication.
- **Toxicity data**: An oral acute toxicity study in rats (edible camphor) showed oxidative stress and tissue changes, which raises toxicity considerations.
- **Vascular effects**: Vasoconstriction risk is not excluded for vascular indications such as Raynaud disease.

No drug interaction records were found. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence is limited to case reports (which suggest camphor-containing products may trigger headache) and a single early animal study. There are no human efficacy data, and the known neurotoxicity profile of camphor adds caution.

**To proceed, the following is needed:**
- Full-text review of the 2026 preclinical study and an independent preclinical replication
- Detailed mechanism of action data
- Package insert warnings and contraindications from Health Canada, plus approved indication and dosage form details for each DIN
- Dose and safety review, particularly for neurotoxicity and seizure risk, before formulating any clinical question
- Assessment of route compatibility (existing topical and rectal products versus the route needed for migraine)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

