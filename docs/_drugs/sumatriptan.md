---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 741
evidence_level: L5
indication_count: 1
---

# Sumatriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Sumatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Sumatriptan is a triptan-class 5-HT1B/1D receptor agonist globally established for the acute treatment of migraine.
> The TxGNN model predicts potential relevance to **Migraine with Brainstem Aura**,
> but this prediction is supported only by mechanistic/indirect literature (**0 clinical trials**, **20 publications**), and the underlying pharmacology raises a **theoretical safety concern rather than a therapeutic opportunity** for this specific subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Canadian regulatory data (drug not marketed in Canada); sumatriptan is internationally established for acute treatment of migraine, with or without typical aura |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.74% (rank 5686) |
| Evidence Level | L4 |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Sumatriptan is a selective 5-HT1B/1D receptor agonist. Its established mechanism in ordinary migraine involves constriction of dilated intracranial/meningeal blood vessels and inhibition of vasoactive neuropeptide release from trigeminovascular afferents, thereby aborting the migraine attack. This mechanism is well validated for migraine with typical (cortical) aura and migraine without aura.

Migraine with brainstem aura (formerly "basilar-type migraine") is a distinct subtype involving symptoms attributable to the vertebrobasilar circulation (e.g., dysarthria, vertigo, diplopia, ataxia, decreased consciousness). Because sumatriptan's mechanism of action is vasoconstrictive, its application to this subtype carries a **theoretical ischemic risk in the posterior circulation** rather than a clear therapeutic rationale. Major clinical guidelines (including AHS/AAN) have historically listed migraine with brainstem aura as a **relative contraindication** for triptans, not a target for indication expansion.

In other words, the TxGNN model appears to have identified a strong semantic/network association between "sumatriptan" and "migraine with brainstem aura" — likely driven by shared disease-class proximity to migraine — but the clinical literature interprets this same mechanistic link as a **caution signal**, not supporting evidence for expanded use. This is an important distinction that should be explicitly flagged for any reviewer relying on the TxGNN score alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytotherapy Research | Double-blind RCT comparing ginger powder vs. sumatriptan in acute treatment of common migraine (without aura) |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | AHS evidence assessment of acute migraine pharmacotherapies, including triptans |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Double-blind, placebo-controlled trial of oral sumatriptan (200mg) specifically in migraine **with aura** |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Found **reduced sumatriptan efficacy** in migraine with aura compared to migraine without aura |
| [25841027](https://pubmed.ncbi.nlm.nih.gov/25841027/) | 2015 | Commentary | Neurology | Discusses whether presence of aura predicts migraine severity and triptan treatment response |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Critical review of clinical experience managing migraine and cluster headache with sumatriptan |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Review | Expert Rev Neurother | Reviews needle-free subcutaneous sumatriptan approval for migraine with or without aura, and cluster headache |
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT | Cephalalgia | Randomised trial: early sumatriptan treatment prevents PACAP38-induced experimental migraine attacks |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Mechanistic Study | JAMA Neurology | Imaging study of central 5-HT1B receptor binding during sumatriptan treatment of migraine attacks |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Study | Neurology | Examines effect of subcutaneous sumatriptan specifically on the migraine aura phase |

Note: None of the retrieved literature directly studies sumatriptan in **migraine with brainstem aura**; the most relevant items (PMID 25841032, 1313746) concern migraine with *typical/cortical* aura, a clinically distinct entity.

---

## Canada Market Information

Sumatriptan currently has **no Health Canada market authorization (DIN) on file** in this evidence pack — the product is recorded as not marketed in Canada, with 0 licenses. No product-level formulation or indication text is available to summarize.

---

## Safety Considerations

- **Mechanistic Safety Signal**: Sumatriptan's vasoconstrictive mode of action, combined with the vertebrobasilar circulation symptoms defining migraine with brainstem aura, has led major headache treatment guidelines to historically treat this subtype as a **relative contraindication** for triptan use — this is a critical caveat that must accompany the TxGNN prediction score.

Please refer to the package insert for further safety information (key warnings, contraindications, and drug interaction data are not currently available in this evidence pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting evidence is indirect (L4, mechanism/association-level only) and the pharmacological rationale actually points toward a **safety concern rather than efficacy** in this specific migraine subtype. Additionally, a blocking data gap (TFDA/regulatory label warnings and contraindications, DG001) prevents this candidate from passing the S1 safety screening stage.

**To proceed, the following is needed:**
- TFDA/Health Canada product label data — warnings, contraindications, and DDI information (blocking gap, DG001)
- Confirmed original mechanism-of-action documentation from DrugBank (DG002)
- Dedicated clinical or pharmacovigilance data on triptan use specifically in migraine with brainstem aura (cerebrovascular safety outcomes)
- Reassessment against current AHS/AAN and International Headache Society guidance on triptan contraindications in this subtype before any further advancement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

