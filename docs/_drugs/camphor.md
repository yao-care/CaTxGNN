---
layout: default
title: Camphor
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Camphor
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

# Camphor: From Traditional Topical Use to Migraine Disorder

## One-Sentence Summary

Camphor (DB01744) is a naturally occurring bicyclic monoterpenoid with a long history of traditional use as a topical counter-irritant and mild analgesic, with no formally approved indication currently on record in Canada.
The TxGNN model predicts it may be relevant for **Migraine Disorder**, with **no registered clinical trials** and **5 publications** identified in support of this direction.
However, critically, several of those publications document camphor as a headache *trigger* rather than a treatment — a finding that substantially complicates the repurposing rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record in Canada |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Camphor is a bicyclic monoterpenoid derived from the wood of *Cinnamomum camphora* that is known pharmacologically to modulate TRPV1 and TRPM8 transient receptor potential ion channels. Currently, detailed mechanism of action data is not available in this evidence pack. Based on published pharmacological knowledge, camphor acts as a counter-irritant by activating cutaneous sensory neurons via TRPV1, producing local analgesic and cooling sensations. Because TRPV1 receptors are densely expressed on trigeminal nociceptors — the sensory neurons that mediate migraine pain — camphor's channel-modulating activity could theoretically interfere with peripheral sensitisation processes central to migraine pathophysiology.

The proposed therapeutic connection is indirect and mechanistically bidirectional: TRPV1 activation at acute or high doses is pro-nociceptive, whereas prolonged or low-level TRPV1 stimulation can result in receptor desensitisation, which is the basis for the analgesic use of capsaicin and related compounds. Historically, topical camphor-menthol combinations have been applied to the forehead as folk remedies for tension-type and mild headaches, providing limited indirect precedent. However, no established clinical evidence links camphor to migraine-specific mechanisms such as cortical spreading depression, CGRP release, or dural neurogenic inflammation.

⚠️ **Critical caveat:** Two of the five identified publications are case reports documenting that camphor-containing products — specifically essential-oil toothpastes — appear to have *provoked* cluster headache episodes. This raises the important concern that camphor may maintain an adverse rather than a therapeutic relationship with headache disorders. Any future research programme would need to directly resolve this question before advancement.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35856604](https://pubmed.ncbi.nlm.nih.gov/35856604/) | 2022 | Case Series | Headache | Five cases of cluster headache attributed to pro-convulsant essential oils in toothpaste; camphor identified as a likely contributing trigger — **adverse association** |
| [34373243](https://pubmed.ncbi.nlm.nih.gov/34373243/) | 2021 | Case Report | BMJ Case Reports | Two cases of cluster headache temporally linked to toothpaste containing camphor and eucalyptus essential oils — **adverse association** |
| [36404301](https://pubmed.ncbi.nlm.nih.gov/36404301/) | 2022 | Phase 3 RCT | The Journal of Headache and Pain | DRAGON study: erenumab (anti-CGRP monoclonal antibody) vs. placebo for prevention of chronic migraine in Asian patients; demonstrates efficacy of CGRP-pathway targeting — camphor not involved, included as migraine disease-area context |
| [27058833](https://pubmed.ncbi.nlm.nih.gov/27058833/) | 2016 | Historical Review | Zeitschrift für Kinder- und Jugendpsychiatrie | Historical analysis of neuropsychopharmacological agents used in children during the 1940s–50s; camphor noted among substances used during this period |
| [593588](https://pubmed.ncbi.nlm.nih.gov/593588/) | 1977 | Historical Clinical Report | Minerva Medica | Early report on therapy for essential hemicrania (a historical term for migraine); abstract data unavailable |

---

## Safety Considerations

As no approved drug product containing camphor is currently marketed in Canada, no official product package insert is available. Based on general pharmacological and toxicological knowledge:

- **CNS excitatory risk:** Camphor possesses significant central nervous system excitatory properties at supratherapeutic doses; seizures have been reported in overdose cases, particularly in children following oral ingestion.
- **Systemic toxicity:** Systemic absorption via skin or mucous membranes — especially in infants and young children — can lead to serious toxicity. Many regulatory authorities restrict camphor concentrations in topical products for this reason.
- **Pro-convulsant properties:** The literature identified for this report specifically notes camphor among essential oils with pro-convulsant characteristics, a safety concern particularly relevant for headache patients who may have co-morbid neurological conditions.

Please refer to pharmacopoeia monographs (e.g., USP, BP) and safety databases for comprehensive hazard and handling information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base does not currently support advancing camphor as a migraine treatment candidate. No clinical trials exist, the mechanistic link via TRPV1 modulation is indirect and unvalidated in migraine models, and — most importantly — the identified literature raises a safety signal suggesting camphor may provoke rather than relieve headache disorders.

**To proceed, the following is needed:**
- Preclinical evaluation of camphor in validated migraine models (e.g., trigeminal sensitisation assays, cortical spreading depression models) to establish proof-of-concept
- Dose–response characterisation of TRPV1 modulation versus activation to define a potential therapeutic desensitisation window
- Direct investigation of whether topical scalp/temporal application produces meaningful trigeminal-nerve effects without systemic exposure
- A formal safety review addressing the documented adverse association (camphor as cluster headache trigger) before any pro-therapeutic interpretation can proceed
- Retrieval of complete mechanism of action data from DrugBank (DB01744) to strengthen the biological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

