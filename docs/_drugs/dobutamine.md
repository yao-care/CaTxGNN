---
layout: default
title: Dobutamine
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Acute Heart Failure to Alopecia

## One-Sentence Summary

Dobutamine is a synthetic catecholamine and β1-adrenergic agonist used in clinical settings for the short-term management of acute decompensated heart failure and cardiogenic shock.
The TxGNN model predicts it may be effective for **Alopecia** (rank #1 of 10 predicted indications),
however **no clinical trials** and **no directly relevant publications** support this direction — the high prediction score of 99.85% most likely reflects a **knowledge graph pathway confounding artifact** rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Canada; known pharmacological use: acute decompensated heart failure / cardiogenic shock (IV inotropic support) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

This prediction is **not considered mechanistically plausible**, and the evidence pack's own repurposing rationale explicitly flags it as a false positive. Dobutamine is a β1-adrenergic agonist that increases myocardial contractility and cardiac output by stimulating β1 receptors in the heart muscle. It has no known mechanism of action relevant to hair follicle biology, the hair growth cycle, or the immunological pathways underlying alopecia areata.

The most likely explanation for the high TxGNN scores across multiple hair-loss conditions (alopecia, hypotrichosis simplex of the scalp, congenital hypotrichosis milia, diffuse alopecia areata — ranks 1–4) is the following **indirect knowledge graph confounding pathway**:

> **Dobutamine → treats → Heart Failure ← caused by ← Minoxidil → treats → Alopecia**

In this pathway, dobutamine is legitimately used to rescue patients who develop cardiac toxicity *from* systemic minoxidil (which causes fluid retention and pericardial effusion), while minoxidil separately treats alopecia via an unrelated vasodilatory mechanism acting on scalp hair follicles. The knowledge graph incorrectly chains these two independent relationships into a spurious dobutamine→alopecia treatment signal.

Critically, this confounding pattern repeats across multiple prediction clusters in the top 10, further reinforcing the false-positive interpretation:

| Rank | Disease | Confounding Mechanism |
|------|---------|----------------------|
| 1–4 | Alopecia / Hypotrichosis variants | Dobutamine ← minoxidil cardiotoxicity ← minoxidil treats alopecia (indirect path) |
| 5, 7 | Open-angle / Hereditary glaucoma | Dobutamine is a β-**agonist**; glaucoma treatment requires β-**blockers** (e.g., timolol) — mechanistic direction is reversed; may worsen intraocular pressure |
| 8 | Headache disorder | Headache is a **known side effect** of dobutamine in stress echocardiography (DSE); model appears to misread a side-effect signal as a treatment signal |
| 9 | Hypertrichosis | Minoxidil *causes* hypertrichosis as a side effect — reverse-causal confound via the same minoxidil pathway |
| 10 | Migraine | No plausible β1-adrenergic / meningeal vascular mechanism; identified literature (PMID 17103145) studies dobutamine as a pharmacological comparator, not a treatment candidate |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dobutamine + Alopecia.

---

## Literature Evidence

Two publications were retrieved for Dobutamine + Alopecia. Neither supports dobutamine as a treatment for alopecia; both instead reinforce the knowledge graph confounding hypothesis described above.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case Report (Veterinary) | Journal of Veterinary Cardiology | A cat with **minoxidil poisoning** developed congestive heart failure; dobutamine was administered to treat the resulting hypotension — confirms dobutamine's role in managing minoxidil cardiac toxicity, **not** in treating alopecia |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | Case Report | Pediatric Emergency Care | Child with acute colchicine poisoning; hair loss appeared as a phase-3 recovery symptom; dobutamine not mentioned in relation to hair loss — retrieved due to incidental keyword overlap |

---

## Canada Market Information

Dobutamine is currently **not marketed in Canada**. No DINs are on file in Health Canada's drug product database, and no approved indications are available from the Canadian regulatory record.

> *Context: Dobutamine is widely used in ICU and emergency settings globally as an intravenous inotropic agent. It is typically supplied as a hospital-use injectable concentrate. Its absence from the Canadian DIN database may reflect its status as a hospital-formulary product supplied under alternative regulatory pathways or procurement channels rather than a traditional marketed product.*

---

## Safety Considerations

Please refer to the package insert for safety information.

> *Note: Based on established pharmacological knowledge (not derived from this evidence pack's data), dobutamine is associated with tachycardia, ventricular arrhythmias, hypertension, angina, and headache. It is generally avoided in patients with hypertrophic obstructive cardiomyopathy, atrial fibrillation without rate control, and in combination with monoamine oxidase inhibitors (MAOIs). Formal warning and contraindication data from TFDA/Health Canada package inserts were not available in this evidence pack and should be retrieved before any further assessment.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for dobutamine are rated L5 (model prediction only, no supporting clinical evidence), and the systematic pattern of predictions — dominated by hair-loss conditions mechanistically unrelated to β1-adrenergic agonism — strongly indicates knowledge graph confounding originating from the dobutamine/minoxidil/alopecia indirect pathway rather than a genuine repurposing opportunity. At least two additional clusters (glaucoma, headache disorder) further confirm that the model is misreading side-effect and reverse-causal signals as treatment relationships.

**To proceed, the following is needed:**

- **KG pathway audit**: Rerun TxGNN with masked dobutamine–heart failure edges to confirm whether the alopecia and hair-loss prediction cluster collapses, which would formally validate the confounding hypothesis
- **MOA data retrieval**: Query DrugBank API for dobutamine's complete mechanism, targets, and pharmacodynamic profile to enable rigorous mechanistic assessment
- **Safety data retrieval**: Download and parse the TFDA/Health Canada package insert PDF to complete the mandatory S1 safety pre-screening (currently Blocking gap DG001)
- **Independent hypothesis generation**: If a genuine repurposing hypothesis beyond heart failure is desired, initiate a de novo literature and pathway analysis rather than relying on the current confounded TxGNN predictions
- **Regulatory status clarification**: Confirm whether dobutamine is available in Canada under a hospital formulary or Notice of Compliance Notifiable Change pathway despite the absence of a standard DIN
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

