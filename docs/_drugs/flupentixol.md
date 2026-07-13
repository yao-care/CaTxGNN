---
layout: default
title: Flupentixol
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 9
---

# Flupentixol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Flupentixol: From Schizophrenia / Depression to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

Flupentixol is a thioxanthene-class antipsychotic and dopamine D1/D2 receptor antagonist established for schizophrenia and depression treatment across Europe and Asia. The TxGNN model predicts it may be relevant for **retinal dystrophy with or without extraocular anomalies**, with **0 clinical trials** and **15 publications** retrieved — none of which specifically address flupentixol in this indication. At this stage, the mechanistic rationale relies entirely on an indirect "dopamine → retina" knowledge graph path, placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / Depression (not registered in Canada) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Flupentixol (also spelled flupenthixol) is a thioxanthene antipsychotic that blocks dopamine D1 and D2 receptors and has ancillary activity at serotonin receptors. It has been used clinically for decades to treat schizophrenia, bipolar depression, and anxiety-related depression in many European and Asian markets. Detailed mechanism of action data was not retrieved from the DrugBank pipeline in this evidence pack (Data Gap DG002), but the receptor pharmacology is well-established in the published literature.

The connection to retinal dystrophy rests on dopamine's known role in retinal physiology. Dopaminergic amacrine cells in the inner retina regulate light adaptation, spatial contrast sensitivity, and circadian photoentrainment of the eye. Reduced retinal dopamine has been implicated in myopia progression, and dopamine signalling intersects with photoreceptor function. The TxGNN knowledge graph likely captured a "dopamine receptor → retina" pathway as an indirect mechanistic bridge between flupentixol's pharmacology and retinal disease nodes.

However, the biological rationale for inherited retinal dystrophies is weak. Conditions within this disease category — such as retinitis pigmentosa, Leber congenital amaurosis, and Best disease — are driven by hereditary mutations in photoreceptor or retinal pigment epithelium genes (e.g., *RPGR*, *PRPF31*, *ABCA4*). Dopamine receptor antagonism does not address the underlying genetic or degenerative mechanism, and no clinical precedent exists for antipsychotic-class drugs modifying the course of inherited retinal degeneration. The high TxGNN score most likely reflects broad knowledge graph connectivity rather than a true therapeutic opportunity, and the literature retrieved confirms this assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 15 publications retrieved for the flupentixol × retinal dystrophy query are general ophthalmology reviews and case series concerning extraocular muscle anomalies, congenital ocular conditions, and orbital lesions. None specifically investigates flupentixol in retinal dystrophy. The results appear to reflect keyword overlap on "extraocular anomalies" rather than direct drug-disease relevance. The ten most representative papers are listed below for transparency.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and imaging features of paediatric orbital ocular pathologies — not related to flupentixol |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of lens shape, associated with anterior segment dysgenesis |
| [37408430](https://pubmed.ncbi.nlm.nih.gov/37408430/) | 2023 | Review | Chinese J Ophthalmol | Extraocular muscle structure and innervation — MRI and Sihler technique research progress |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Original Study | Int J Mol Sci | Retinal/optic nerve abnormalities in congenital fibrosis of extraocular muscles (CFEOM) — KIF21A/TUBB3 mutations |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocular Vision Ocular Motility | Ophthalmoplegia and congenital cranial dysinnervation disorders (CCDDs) |
| [27930425](https://pubmed.ncbi.nlm.nih.gov/27930425/) | 2017 | Original Study | Ophthalmic Plast Reconstr Surg | Anatomical description of the anomalous gracillimus orbitis muscle in human orbits |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Original Study | Am J Ophthalmol | Pathogenesis and treatment of maculopathy associated with cavitary optic disc anomalies |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Series | J Neuro-Ophthalmol | Isolated congenital trochlear-oculomotor synkinesis in a 6-year-old — a rare CCDD variant |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Systematic clinical approach to diplopia — history, examination, differential diagnosis |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Case Series/Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex — vitreoretinal degeneration with extraocular manifestations |

> **Note**: None of the above publications directly addresses flupentixol use in retinal dystrophy. This result set should not be interpreted as literature support for this repurposing prediction.

---

## Canada Market Information

Flupentixol is not currently registered or marketed in Canada. No Drug Identification Numbers (DINs) are on file with Health Canada.

> Flupentixol is approved in numerous European countries (UK, Germany, Denmark, Switzerland) and several Asian markets under brand names including **Fluanxol** and **Depixol**. Any future repurposing application in Canada would first require a New Drug Submission or supplemental NDS, which presupposes regulatory registration of the drug itself.

---

## Safety Considerations

No Canadian product monograph is available. TFDA package insert warning and contraindication data was also not retrieved in this evidence pack (Data Gap DG001). The information below is provided based on flupentixol's established pharmacological class (typical antipsychotic / thioxanthene) and should be verified against an authoritative product monograph before any clinical use.

- **Extrapyramidal symptoms (EPS)**: Parkinsonism, akathisia, and acute dystonia are class effects of dopamine D2 antagonists; risk is dose-dependent.
- **Tardive dyskinesia**: Risk increases with prolonged use; may be irreversible. Baseline assessment and regular monitoring required.
- **QTc prolongation**: Common to the antipsychotic class; ECG monitoring is recommended, particularly in patients with cardiac risk factors or on concomitant QT-prolonging agents.
- **Sedation and anticholinergic effects**: Dose-dependent; caution in elderly patients and those operating machinery.
- **Known class-based contraindications**: CNS depression, comatose states, concomitant MAOI therapy, severe hepatic impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a near-perfect prediction score to flupentixol for retinal dystrophy with extraocular anomalies, but this prediction lacks biological plausibility as an actionable repurposing target. Retinal dystrophies are predominantly hereditary genetic disorders; dopamine D1/D2 receptor antagonism does not address the underlying photoreceptor or RPE gene defects that drive these conditions. No clinical trials and no directly relevant literature were identified. The high score is most likely an artefact of broad knowledge graph connectivity through the general "dopamine → retina" node rather than a genuine therapeutic signal. All nine ranked predictions in this evidence pack are at L5 and carry a Hold recommendation.

**To proceed, the following is needed:**
- Retrieve DrugBank MOA data to formally document flupentixol's pharmacological profile (remediate Data Gap DG002)
- Obtain TFDA or Health Canada package insert data for a complete safety baseline (remediate Data Gap DG001)
- Conduct a targeted preclinical literature search specifically on dopamine antagonism and photoreceptor / retinal pigment epithelium function — this is the minimum scientific evidence needed to justify reclassification to L4
- If Canada registration is ever pursued, initiate a Health Canada New Drug Submission prior to any repurposing application
- Consider whether flupentixol's dopamine biology is better evaluated in myopia-related indications (ranks 6–8), where the dopamine-retina pathway has more published mechanistic backing, before committing resources to the primary dystrophy prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

