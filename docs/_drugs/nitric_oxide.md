---
layout: default
title: Nitric Oxide
parent: Model Prediction Only (L5)
nav_order: 657
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
monitor_inn: "NITRIC OXIDE"
predicted_indications: ["malformation syndrome with odontal and/or periodontal component", "hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "pulmonary arteriovenous malformation (disease)", "pulmonary arterial hypertension associated with congenital heart disease", "pulmonary arterial hypertension associated with HIV infection", "pulmonary arterial hypertension associated with chronic hemolytic anemia"]
description: "Nitric Oxide: predicted new indication Malformation syndrome with odontal and/or periodontal component (evidence level L5). Approved use: Not recorded in the local data"
---

# Nitric Oxide
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

## Nitric Oxide: Malformation syndrome with odontal and/or periodontal component
{: .text-alpha }

## One-Sentence Summary

Nitric oxide is a gas originally used to treat pulmonary hypertension, congenital alveolar capillary dysplasia and persistent fetal circulation syndrome.
The TxGNN model predicts it may be effective for **malformation syndrome with odontal and/or periodontal component**, but **no clinical trials** and only **20 loosely related publications** (laboratory and background studies on periodontal biology) support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malformation syndrome with odontal and/or periodontal component |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitric oxide is known as a vasodilator that acts through the cGMP signalling pathway, and its efficacy in pulmonary hypertension of the newborn is established. Mechanistically, however, nothing in the data compiled for this report shows that this action is relevant to a malformation syndrome affecting the teeth and periodontal tissues.

The 20 retrieved papers concern the biology of periodontitis. They cover gingival fibroblasts, inflammation induced by bacterial lipopolysaccharide, herbal extracts, and the way oral bacteria produce nitrite. The only link to nitric oxide is a generic one through inflammatory and NO-signalling pathways. None of the papers tests nitric oxide as a treatment for a developmental malformation syndrome.

The high prediction score therefore reflects a pattern found by the model, not demonstrated clinical or mechanistic support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these papers evaluates nitric oxide as a therapy for the predicted indication. They are periodontal-biology background studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36312752](https://pubmed.ncbi.nlm.nih.gov/36312752/) | 2022 | In vitro | PeerJ | Cystatin C showed antimicrobial and anti-inflammatory activity in gingival fibroblasts exposed to *Porphyromonas gingivalis* |
| [40430099](https://pubmed.ncbi.nlm.nih.gov/40430099/) | 2025 | Preclinical | Int J Mol Sci | ATF3 regulates senescence and osteoclast formation in human periodontal ligament cells |
| [35574962](https://pubmed.ncbi.nlm.nih.gov/35574962/) | 2022 | Cohort | J Am Heart Assoc | Oral microbiome capacity to generate nitrite (a source of NO) was examined in relation to cardiometabolic risk |
| [24670812](https://pubmed.ncbi.nlm.nih.gov/24670812/) | 2014 | Not classified | PLoS One | Metagenomic analysis of nitrate-reducing oral bacteria and their role in NO homeostasis |
| [20646228](https://pubmed.ncbi.nlm.nih.gov/20646228/) | 2011 | Not classified | Oral Dis | *P. gingivalis* vesicles induced iNOS expression and NO production in mouse macrophage cells |
| [35455384](https://pubmed.ncbi.nlm.nih.gov/35455384/) | 2022 | Not classified | Pharmaceuticals (Basel) | A plant extract reduced LPS-induced inflammatory markers, including iNOS, in periodontal ligament cells |
| [31055250](https://pubmed.ncbi.nlm.nih.gov/31055250/) | 2019 | Not classified | Arch Oral Biol | Th1 and Th2 stimuli drive distinct phenotypes in gingival fibroblasts |
| [16881806](https://pubmed.ncbi.nlm.nih.gov/16881806/) | 2006 | Not classified | J Periodontol | Grape seed proanthocyanidins protected against oxidative stress induced by periodontopathogen LPS |
| [41952916](https://pubmed.ncbi.nlm.nih.gov/41952916/) | 2026 | Not classified | J Dent Anesth Pain Med | Narrative review of *P. gingivalis* and pain modulation |
| [42795495](https://pubmed.ncbi.nlm.nih.gov/42795495/) | 2026 | Not classified | Microorganisms | Narrative review of the oral and nasal gateway microbiomes and systemic health |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 02270846 | INOMAX |
| 02451328 | KINOX |

Both are valid single-ingredient authorisations. Dosage form and approved indication text are not recorded in the data compiled for this report.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: methemoglobinemia, sulfhemoglobinemia and heart failure.
- **Drug Interactions**: 61 interactions were identified, and most have no assigned severity level. The notable ones are:
  - **Major**: nitrous acid.
  - **Moderate**: topical or ophthalmic local anaesthetics (tetracaine, lidocaine, benzocaine).
  - **Severity unknown**: morphine, omeprazole, epinephrine, heparin, epoprostenol, hydrocortisone, dexamethasone and vancomycin, among others.

Please refer to the package insert for the full warnings and contraindications, as label-based safety data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score. There are no registered trials, and the retrieved literature is background work on periodontal biology that does not test nitric oxide for this condition. The evidence level is L5, and no mechanistic link has been shown.

**To proceed, the following is needed:**
- Mechanism of action data for nitric oxide, to allow a proper mechanistic assessment
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Preclinical or case-level evidence showing that NO-pathway modulation affects the dental or periodontal features of this syndrome
- Consideration of better-supported predictions in the same data set. In particular, **pulmonary arterial hypertension** has 28 registered trials and an L2 evidence level, and **pulmonary arterial hypertension associated with congenital heart disease** has an L3 level. Both are closer to nitric oxide's established use and are more suitable candidates for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

