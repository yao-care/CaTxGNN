---
layout: default
title: Flurbiprofen
parent: Model Prediction Only (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Flurbiprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
monitor_inn: "FLURBIPROFEN"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "spondyloarthropathy, susceptibility to", "ankylosing spondylitis", "pseudoachondroplasia", "hypermobility of coccyx"]
---

# Flurbiprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Flurbiprofen: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Flurbiprofen is a non-steroidal anti-inflammatory drug (NSAID) originally used for rheumatoid arthritis, osteoarthritis and other joint disorders.
The TxGNN model ranks **acromesomelic dysplasia, Hunter-Thompson type** as its top predicted new indication, but **no clinical trials and no publications** support this prediction.
Of the ten predictions reviewed, only ankylosing spondylitis (rank 8) has meaningful supporting literature, and that use is close to the drug's existing indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (from the knowledge graph; the Canadian licence records contain no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% (model rank 518) |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Flurbiprofen is a non-selective cyclooxygenase (COX-1/COX-2) inhibitor that reduces prostaglandin-mediated inflammation and pain. Its efficacy in inflammatory and degenerative joint disease is long established.

For the top prediction, **no plausible mechanism has been identified**. Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by loss-of-function mutations in *CDMP1/GDF5*, which disrupt GDF5/BMP signalling. COX inhibition has no known effect on this pathway. The high score most likely reflects the disease's closeness to musculoskeletal conditions in the knowledge graph rather than a pharmacological rationale.

The other predictions follow the same pattern:

- **Weak or no mechanistic link:** Brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachyolmia-amelogenesis imperfecta syndrome, brachyolmia and pseudoachondroplasia are developmental genetic disorders that COX inhibition would not correct. Myosclerosis and hypermobility of the coccyx have only speculative symptomatic links.
- **Plausible, but already near-label:** Ankylosing spondylitis is the one biologically sensible prediction, because NSAIDs are first-line symptomatic therapy for it. It sits close to flurbiprofen's existing arthropathy indications, so it is not a novel repurposing finding. Spondyloarthropathy susceptibility (rank 7) is a susceptibility phenotype rather than a treatable condition, and its link is indirect through ankylosing spondylitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top predicted indication. No trials were retrieved for any of the other nine predicted indications either.

---

## Literature Evidence

Currently no related literature available for acromesomelic dysplasia, Hunter-Thompson type.

For reference, the following is the strongest literature found for the best-supported alternative prediction, **ankylosing spondylitis**. These are older studies (1974–1986). The retrieved records do not fully confirm design or sample size beyond what is stated in the abstracts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | Double-blind randomized study | Am J Med | Flurbiprofen 200 mg/day was as effective as phenylbutazone 300 mg/day over 26 weeks in 90 patients |
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | Randomized double-blind study | Am J Med | Flurbiprofen was as effective as indomethacin over 26 weeks in 57 patients |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | Randomized double-blind trial | South Med J | Flurbiprofen and indomethacin were equally effective for pain and tenderness in 26 patients |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | Randomized double-blind trial | Eur J Clin Pharmacol | Flurbiprofen and phenylbutazone were equally effective in 27 patients over 6 weeks |
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | Double-blind cross-over trial | Br Med J | Flurbiprofen was well tolerated, with efficacy approaching that of phenylbutazone in 35 patients |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | Double-blind cross-over study | N Z Med J | Flurbiprofen and naproxen were similarly effective in 30 patients; side effects were more frequent with flurbiprofen |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Review | Drugs | Review of flurbiprofen's pharmacology and use in rheumatic diseases, including ankylosing spondylitis |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Pooled safety analysis | Am J Med | Pooled data from nine phase III trials (1,677 patients) on kidney and liver function |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 01912038 | FLURBIPROFEN |
| 01912046 | FLURBIPROFEN |

Both licences are valid single-ingredient products. The data compiled for this report do not include their dosage forms or approved indication text.

---

## Safety Considerations

The package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label safety information.

- **Contraindication signals from the knowledge graph:** These come from drug-disease relationships, not from label text. They flag caution in the following conditions:
  - Cardiovascular: hypertension and hypertensive disorder, myocardial infarction, coronary thrombosis, heart disease and cardiovascular disease.
  - Gastrointestinal: peptic ulcer disease, including active peptic ulcer disease.
  - Renal and hepatic: kidney disease, liver disease, gallbladder disease and pyoureter.
  - Haematological: blood coagulation disease and hemoglobinopathy.
  - Substance abuse or dependence.
- **Drug interactions:** The interaction screen returned 100 interactions in total, of which 20 were retrieved for review. Most are Moderate. Main examples:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, budesonide and triamcinolone.
  - Other anti-inflammatory drugs: acetylsalicylic acid, mesalazine and balsalazide.
  - Antidiabetic agents: metformin, glimepiride and chlorpropamide.
  - Others: aprepitant, potassium citrate, potassium bicarbonate, sodium sulfate, picosulfuric acid and polyethylene glycol with electrolytes.
  - Minor interactions were noted with famotidine, cimetidine and linaclotide.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has only a model score behind it. There are no trials or publications, and no mechanistic link between COX inhibition and GDF5/BMP-driven skeletal dysplasia. The 99.99% score appears to be a knowledge-graph artifact. All other predictions except ankylosing spondylitis are also L5 and Hold. Ankylosing spondylitis (L3, "Research Question") is supported by older comparative studies showing symptomatic relief only, not disease modification, and it is essentially an on-label-adjacent use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which currently block safety screening.
- Mechanism of action data from DrugBank.
- Dosage form and approved indication details for both Canadian DINs.
- For ankylosing spondylitis, a review of the study designs and a comparison with current guideline-based NSAID evidence, if that indication is pursued.
- For acromesomelic dysplasia and the other rare congenital disorders, mechanistic or preclinical evidence before further investment.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

