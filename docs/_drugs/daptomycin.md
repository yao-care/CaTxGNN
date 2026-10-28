---
layout: default
title: Daptomycin
parent: Model Prediction Only (L5)
nav_order: 249
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Daptomycin: predicted new indication Osteoarthritis (evidence level L4). Approved use: Not listed in the Canadian license data compiled for this report (the…"
monitor_inn: "DAPTOMYCIN"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "gout", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia-amelogenesis imperfecta syndrome"]
---

# Daptomycin
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

## Daptomycin: From Gram-Positive Bacterial Infections to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Daptomycin is a cyclic lipopeptide antibiotic marketed in Canada, used against Gram-positive bacterial infections.
The TxGNN model predicts it may be effective for **osteoarthritis**, but there are **no registered clinical trials**, and the **10 publications** retrieved mostly concern bone and joint *infections*, not degenerative osteoarthritis.
This prediction is best viewed as a model-generated hypothesis with little direct support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data compiled for this report (the drug is a Gram-positive antibacterial; the labelled indications could not be confirmed) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 3 of 3) |
| Number of DINs | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, daptomycin is a cyclic lipopeptide that disrupts the membranes of Gram-positive bacteria. Its antibacterial efficacy is established, but this mechanism does not directly apply to non-infectious osteoarthritis.

The retrieved literature explains why the score is likely high. The articles cover **osteoarticular and prosthetic joint infections** (for example *Staphylococcus* and *Corynebacterium*), where daptomycin has been used. They do not address degenerative osteoarthritis. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence of a true disease-modifying effect.

**Other predictions worth noting:**
- **Rheumatoid arthritis** (score 0.9984): a 2025 preclinical study (PMID 39571268) reported that daptomycin reduced collagen-induced arthritis in mice by suppressing inflammatory cytokines and NF-κB signalling. A related study (PMID 40923559) designed daptomycin-derived lipopeptides with similar effects in mice. This is the most mechanistically plausible direction, but it has no human data. It is best treated as a research question.
- **Gout** (score 0.9979): the only article is a case report of daptomycin-induced rhabdomyolysis followed by acute gouty arthritis. This is a safety signal, not evidence of benefit.
- **Rare genetic skeletal syndromes** (pseudoachondroplasia, brachyolmia and others): no evidence and no plausible mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23519823](https://pubmed.ncbi.nlm.nih.gov/23519823/) | 2013 | Cohort | Int Orthop | Safety and efficacy of high-dose daptomycin plus rifampicin in Gram-positive osteoarticular infections |
| [17999973](https://pubmed.ncbi.nlm.nih.gov/17999973/) | 2008 | Cohort | J Antimicrob Chemother | Daptomycin vs standard therapy for osteoarticular infections with *S. aureus* bacteraemia |
| [22511636](https://pubmed.ncbi.nlm.nih.gov/22511636/) | 2012 | Cohort | J Antimicrob Chemother | Clinical experience in knee and hip periprosthetic joint infections |
| [26235888](https://pubmed.ncbi.nlm.nih.gov/26235888/) | 2015 | Cohort | Int J Antimicrob Agents | High-dose daptomycin (>6 mg/kg) for complicated bone, joint and implant-associated infections |
| [21477701](https://pubmed.ncbi.nlm.nih.gov/21477701/) | 2010 | Cohort | Med Clin (Barc) | Spanish experience from the EU-CORE registry of daptomycin use |
| [39571268](https://pubmed.ncbi.nlm.nih.gov/39571268/) | 2025 | Preclinical (animal) | Int Immunopharmacol | Daptomycin alleviated collagen-induced arthritis via reduced inflammatory cytokines and NF-κB (rheumatoid arthritis prediction) |
| [40923559](https://pubmed.ncbi.nlm.nih.gov/40923559/) | 2025 | Preclinical | J Med Chem | New daptomycin-derived lipopeptides inhibited inflammation and arthritis in mice (rheumatoid arthritis prediction) |
| [36693494](https://pubmed.ncbi.nlm.nih.gov/36693494/) | 2023 | Case report | Am J Med Sci | Daptomycin-induced rhabdomyolysis complicated by acute gouty arthritis (gout prediction; safety signal) |
| [32206362](https://pubmed.ncbi.nlm.nih.gov/32206362/) | 2020 | Case report | Case Rep Orthop | Chronic *Corynebacterium striatum* septic arthritis in a patient with osteoarthritis; infection, not treatment of osteoarthritis |
| [22854340](https://pubmed.ncbi.nlm.nih.gov/22854340/) | 2012 | In vitro | J Antibiot | Susceptibility of staphylococci from prosthetic joint infections |

Note: none of the osteoarthritis-related articles studies daptomycin for degenerative osteoarthritis. The studies are about infection, and the only anti-inflammatory evidence is in mouse models of rheumatoid arthritis.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02490463 | Daptomycin for Injection | Not specified | Not specified |
| 02490838 | Daptomycin for Injection | Not specified | Not specified |
| 02465493 | Cubicin RF | Not specified | Not specified |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the model's knowledge graph, not from label text): myopathy, muscular disease, skeletal muscle disease, familial periodic paralysis, diarrhoeal disease, *Clostridium difficile* colitis, perinatal necrotising enterocolitis, eosinophilic pneumonia, pulmonary eosinophilia, peripheral neuropathy, and peripheral nervous system disease.
- **Muscle toxicity**: the case report PMID 36693494 describes daptomycin-induced rhabdomyolysis, which is relevant to any long-term use in chronic joint disease.
- **Drug interactions** (12 recorded):
  - *Moderate*: picosulfuric acid, rosuvastatin, simvastatin, iobenguane (I-131), ibuprofen, diclofenac, ethinylestradiol, celecoxib, cyclosporine, mycophenolic acid. Combinations with statins and NSAIDs deserve particular attention for muscle and other adverse effects.
  - *Minor*: dicoumarol, warfarin.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction is not supported by direct evidence. The literature concerns joint infections, there are no clinical trials, and no mechanism for degenerative osteoarthritis is known. The only mechanistically plausible lead is rheumatoid arthritis, which rests on mouse studies alone. The muscle toxicity signals also argue against chronic use in joint disease.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text and dosage forms for the three Canadian licences
- Mechanism of action data
- If pursuing the rheumatoid arthritis lead: confirmatory preclinical work, then a safety assessment for chronic systemic use, particularly muscle toxicity and creatine phosphokinase monitoring
- Dedicated evidence that daptomycin acts on non-infectious osteoarthritis, which is currently absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

