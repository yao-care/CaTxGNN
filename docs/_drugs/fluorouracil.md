---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Fluorouracil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Fluorouracil: From Colorectal Cancer to Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil (5-FU) is a pyrimidine antimetabolite and foundational chemotherapy agent, used in combination regimens for colorectal, gastric, breast, and head and neck cancers worldwide.
The TxGNN model predicts it may be effective for **Botryoid-type Embryonal Rhabdomyosarcoma of the Vagina**, an extremely rare pediatric soft tissue malignancy.
This prediction is currently supported by **no clinical trials and no published literature**, placing it at evidence level L5 — hypothesis-generating only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada (no DINs found in regulatory database) |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only, no actual studies) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Fluorouracil is a fluoropyrimidine antimetabolite that acts through two parallel pathways: (1) it inhibits thymidylate synthase (TS), blocking de novo thymidine biosynthesis and stalling DNA replication; and (2) it incorporates into RNA as a fraudulent nucleotide, disrupting RNA processing and protein synthesis. This dual DNA/RNA interference mechanism explains its broad cytotoxic activity and its role as the backbone of FOLFOX, FOLFIRI, and FOLFIRINOX regimens in gastrointestinal oncology.

Botryoid-type embryonal rhabdomyosarcoma (ERMS) of the vagina is an ultra-rare subtype occurring almost exclusively in young girls, and belongs to the rhabdomyosarcoma (RMS) family of soft tissue sarcomas. The established standard of care for RMS is VAC chemotherapy (vincristine + actinomycin-D + cyclophosphamide) with or without local therapy. While 5-FU's TS inhibition could theoretically suppress rapidly proliferating RMS cells, fluoropyrimidines have never appeared in IRS/COG RMS treatment guidelines, and no preclinical or mechanistic studies have investigated 5-FU in this histological subtype specifically.

The high TxGNN score (99.75%) for this indication most likely reflects indirect graph propagation within the knowledge graph — the model infers a path through "soft tissue tumor → chemotherapy-sensitive → pyrimidine metabolism" shared neighbors — rather than a direct biological link. The extreme rarity of botryoid vaginal ERMS, together with the complete absence of clinical or preclinical data, means this prediction should be treated as a hypothesis-generating signal only, not a clinical recommendation. Notably, all top-ranked predictions cluster into two biologically distinct groups: RMS subtypes (ranks 1–7) and sickle cell variants (ranks 8–10), with the sickle cell predictions showing identical TxGNN scores, strongly suggesting batch false-positives from a shared ancestor node in the knowledge graph.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Fluoropyrimidine class) |
| Myelosuppression Risk | Moderate to High — leukopenia, thrombocytopenia, and anemia are common dose-limiting toxicities; life-threatening myelosuppression may occur in patients with dihydropyrimidine dehydrogenase (DPD) deficiency |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly during treatment), liver function tests, renal function, electrolytes; DPYD genotyping or DPD enzyme phenotyping recommended before initiation to screen for deficiency |
| Handling Protection | Must follow cytotoxic drug handling regulations; closed-system drug transfer devices (CSTDs) required for preparation and administration; personnel protective equipment mandatory |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, this is an L5-level prediction with zero clinical trial or literature support; the model score reflects knowledge graph topology rather than validated biology. Botryoid vaginal ERMS is an ultra-rare tumor with an established VAC-based treatment standard, and fluoropyrimidines have no established role in any RMS guideline.

**To proceed, the following is needed:**

- **In vitro cytotoxicity profiling**: Establish 5-FU IC50 against representative RMS cell lines (RD, Rh30, SMS-CTR) to determine baseline sensitivity
- **Biomarker assessment**: Thymidylate synthase (TS) expression and DPD enzyme activity profiling in pediatric ERMS tumor samples
- **Preclinical in vivo data**: Xenograft model experiments in pediatric RMS mouse models before any clinical hypothesis is considered
- **Safety data gap**: Obtain Health Canada–approved package insert for warnings, contraindications, and pediatric dosing guidance (currently a blocking data gap per DG001)
- **MOA documentation**: Formal retrieval of DrugBank mechanism of action data (data gap DG002) to support mechanistic rationale
- **Regulatory pathway assessment**: Pediatric oncology indications in Canada require special consideration under Health Canada's pediatric framework; early regulatory consultation is recommended before advancing any hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

