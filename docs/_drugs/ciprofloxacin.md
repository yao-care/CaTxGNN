---
layout: default
title: Ciprofloxacin
parent: Moderate Evidence (L3-L4)
nav_order: 197
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Ciprofloxacin: predicted new indication Diffuse scleroderma (evidence level L4). Approved use: Bacterial infections (typhoid fever, salmonellosis…"
monitor_inn: "CIPROFLOXACIN"
predicted_indications: ["diffuse scleroderma", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Ciprofloxacin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Ciprofloxacin is a fluoroquinolone antibiotic originally used for bacterial infections such as typhoid fever, salmonellosis, bacterial pneumonia, anthrax and Pseudomonas aeruginosa infection.
The TxGNN model predicts it may be effective for **diffuse scleroderma**,
but this direction is supported by **no registered clinical trials** and only **2 publications**, one of them a small study of uncertain design.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (typhoid fever, salmonellosis, bacterial pneumonia, anthrax, Pseudomonas aeruginosa infection, shigellosis, among others) |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

*Note: The Canadian licence data compiled for this report contain no approved-indication text, so the original indications above come from the knowledge-graph indication list for the drug.*

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ciprofloxacin belongs to the fluoroquinolone class, which is generally known to inhibit bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial infections is well established, but this antibacterial mechanism does not directly explain an effect on scleroderma.

The link to diffuse scleroderma is weak and indirect. It rests on two ideas:

1. **Possible antifibrotic effect on skin.** A 2010 double-blind randomized study (PMID 20507401) examined whether oral ciprofloxacin reduces scleroderma severity. The proposed explanation is an effect on fibroblast activity or collagen metabolism. This has not been confirmed, and the study is classified as a small clinical study whose design still needs verification.
2. **Supportive care.** Small bowel bacterial overgrowth is common in systemic sclerosis (PMID 7728404). Antibiotics may help with symptoms such as diarrhoea and malabsorption, but this would be symptom management, not modification of the underlying disease.

Overall, the prediction is plausible as a hypothesis but is not backed by solid clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Small clinical study (reported as a controlled, double-blind randomized trial; design to be verified) | The Journal of Dermatology | Tested whether oral ciprofloxacin reduces the severity of scleroderma and acts as an antifibrotic in the skin. The abstract available here is truncated, so results could not be confirmed. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Cohort / diagnostic study | British Journal of Rheumatology | 24 systemic sclerosis patients with malabsorption symptoms were investigated for small bowel bacterial overgrowth, and treatment outcomes were assessed. Six had the diffuse form. |

---

## Canada Market Information

Ciprofloxacin has 20 valid single-ingredient licences in Canada. The data compiled for this report do not include dosage forms or approved-indication text. Five of the licences are listed below.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02492008 | NRA-CIPROFLOXACIN | Not available | Not available |
| 02303736 | TARO-CIPROFLOX | Not available | Not available |
| 02387131 | SANDOZ CIPROFLOXACIN | Not available | Not available |
| 02248756 | SANDOZ CIPROFLOXACIN | Not available | Not available |
| 01945270 | CILOXAN | Not available | Not available |

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are not label text and should be confirmed against the package insert):
- Cardiac: long QT syndrome (including familial), torsades de pointes
- Neurological and neuromuscular: epilepsy, peripheral neuropathy and other peripheral nervous system disease, myasthenia gravis (including adult-onset), neuromuscular junction disease
- Tendon and musculoskeletal: tendinitis, periarthritis, Achilles bursitis, heel spur, exostosis
- Renal and metabolic: kidney disease, potassium deficiency disease
- Gastrointestinal and infectious: Clostridium difficile colitis, perinatal necrotizing enterocolitis, superimposed infection

**Drug interactions:** The interaction screen returned 100 records. Examples of **Major** interactions include:
- Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
- Bupropion

Examples of **Moderate** interactions include:
- Antidiabetic drugs: metformin, pioglitazone, alogliptin, acarbose, albiglutide
- Famotidine, loperamide, alosetron, aprepitant
- Acetylsalicylic acid, balsalazide, bisacodyl, budesonide, calcium phosphate

The corticosteroid interactions deserve particular attention in scleroderma, where corticosteroids may be part of treatment. Tendon injury risk, which is already a known fluoroquinolone concern, may be compounded by that combination.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Support for diffuse scleroderma is limited to two publications and no registered trials, so the evidence is at L4. The TxGNN score is high, but the antifibrotic rationale is speculative and the single controlled study needs design verification.
- Several knowledge-graph contraindications (peripheral neuropathy, tendinitis, myasthenia gravis, QT prolongation) and major corticosteroid interactions are relevant to a scleroderma population.

**To proceed, the following is needed:**
- Full-text review of the 2010 study (PMID 20507401) to confirm its design, sample size and outcomes
- Mechanism of action data and preclinical evidence of antifibrotic activity
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening), along with approved-indication text and dosage forms for the Canadian licences
- A safety assessment for scleroderma patients, especially regarding tendon, neuropathy and cardiac risks and concurrent corticosteroid use
- A registered, adequately powered randomized trial if development is pursued

**Other predicted indications:** Only septicemic plague (rank 10) shows substantial support, at evidence level L2. This is largely an on-label-adjacent use rather than true repurposing. It is backed by a 2025 randomized trial in bubonic plague (PMID 40768716), nonhuman primate data and guidelines, but the randomized evidence concerns bubonic rather than septicemic disease. The remaining predictions (e.g., hyperamylasemia, congenital analbuminemia, monoclonal gammopathy) have no meaningful therapeutic rationale and should be treated as model artefacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

