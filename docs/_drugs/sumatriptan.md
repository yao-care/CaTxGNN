---
layout: default
title: Sumatriptan
parent: Model Prediction Only (L5)
nav_order: 867
evidence_level: L5
indication_count: 1
---

# Sumatriptan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Sumatriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Sumatriptan is a triptan marketed for the acute treatment of migraine.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but the high score mostly reflects its known link to the migraine disease family rather than a true repurposing signal.
No clinical trials are registered for this specific subtype, and the **16 publications** retrieved are indirect (general migraine or migraine with aura).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute migraine (the licence indication text is not available in the Evidence Pack) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 (indirect evidence only; nothing examines this subtype directly) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sumatriptan is a selective 5-HT1B/1D receptor agonist. Per the retrieved literature, it is thought to act by constricting certain large cranial blood vessels and by inhibiting the release of vasoactive neuropeptides from trigeminal nerve endings in the dura (PMID 8536293). A PET study found that sumatriptan reaches central 5-HT1B receptors during a migraine attack (PMID 31135819). Detailed mechanism-of-action data is not yet available in the structured record, so this description comes from the literature.

Migraine with brainstem aura (formerly basilar-type migraine) belongs to the same disease family as the migraine indication sumatriptan already has. This closeness is the most likely reason the model scored it so highly. It is not evidence that the drug works in this subtype.

There are also reasons for caution:
- Brainstem aura involves brainstem-origin neurological symptoms. Triptan vasoconstriction is a theoretical ischaemic concern here, and sumatriptan labelling has traditionally listed hemiplegic and basilar migraine as contraindications. This conflicts with the model's prediction and must be checked against the current Canadian label.
- A cohort/post hoc analysis (PMID 25841032) reported reduced sumatriptan efficacy in migraine with aura compared with migraine without aura. This weakens the efficacy case for aura subtypes in general.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications studies migraine with brainstem aura directly. Study types marked with an asterisk (*) were inferred from the title or abstract, because the pack's automatic classification was pending.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT* | Cephalalgia | Tested whether early sumatriptan treatment can prevent PACAP38-induced migraine attacks (experimental migraine model) |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytother Res | Double-blind trial in 100 patients with acute migraine without aura, comparing ginger powder with sumatriptan |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT* | Cephalalgia | Double-blind, placebo-controlled trial of oral sumatriptan 200 mg in acute migraine with aura (general aura, not the brainstem subtype) |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Reported reduced sumatriptan efficacy in migraine with aura versus without aura |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / evidence assessment | Headache | American Headache Society assessment of the evidence for acute migraine pharmacotherapies |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Critical review of sumatriptan in migraine and cluster headache, including its mode of action |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Imaging/mechanism study* | JAMA Neurol | Examined the association between sumatriptan treatment during a migraine attack and central 5-HT1B receptor binding |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handb Clin Neurol | Status migrainosus as a complication of migraine with or without aura |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Review* | Expert Rev Neurother | Needle-free subcutaneous sumatriptan approved for acute migraine with or without aura and cluster headache |
| [39391443](https://pubmed.ncbi.nlm.nih.gov/39391443/) | 2024 | Case report | Cureus | Rare case of migraine with aura accompanied by myoclonus in a 46-year-old man |

---

## Canada Market Information

Showing 5 of 20 licences. Dosage form and approved indication text are not available in the pack.

| DIN | Product Name |
|---------|------|
| 2256428 | PMS-SUMATRIPTAN |
| 2545357 | JAMP SUMATRIPTAN |
| 2268906 | MYLAN-SUMATRIPTAN |
| 2286823 | TEVA-SUMATRIPTAN DF |
| 2385589 | SUMATRIPTAN DF |

---

## Safety Considerations

- **Subtype-specific concern**: Sumatriptan labelling has traditionally listed hemiplegic and basilar migraine as contraindications because of the theoretical ischaemic risk from vasoconstriction. This must be verified against the current Health Canada label.
- **Drug interactions**: No interaction records were found in the queried source.

Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score mainly reflects sumatriptan's existing migraine indication, not independent evidence for the brainstem aura subtype. There are no registered trials and no direct literature. The drug class carries a traditional contraindication in this subtype, and the available data suggest weaker efficacy in migraine with aura.

**To proceed, the following is needed:**
- The current Health Canada product monograph, to confirm warnings and contraindications for hemiplegic and basilar (brainstem aura) migraine
- Mechanism-of-action data from DrugBank
- A targeted literature search for sumatriptan or triptan use specifically in brainstem aura / basilar-type migraine
- A neurology and safety review of the ischaemic risk before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

