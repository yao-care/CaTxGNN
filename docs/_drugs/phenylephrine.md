---
layout: default
title: Phenylephrine
parent: Moderate Evidence (L3-L4)
nav_order: 732
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Phenylephrine: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "PHENYLEPHRINE"
predicted_indications: ["acute laryngopharyngitis", "trigeminal autonomic cephalalgia"]
---

# Phenylephrine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Phenylephrine: From Allergic Rhinitis and the Common Cold to Nasal Cavity Disease

## One-Sentence Summary

Phenylephrine is an alpha-1 adrenergic agonist decongestant, originally used for allergic rhinitis, the common cold, pharyngitis, and related upper-airway and eye conditions.
The TxGNN model predicts it may be effective for **nasal cavity disease**,
but this is supported by **no registered clinical trials** and only **5 publications**, mostly indirect or combination-product studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, conjunctivitis (atopic, papillary, vernal), nasopharyngitis, headache disorder, hemorrhoid, proctitis (the label text for Canadian licences is not available) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, phenylephrine is an alpha-1 adrenergic agonist. It constricts the blood vessels of the nasal mucosa, which reduces congestion, swelling, and mucosal bleeding.

This is the same mechanism behind its existing use in rhinitis and the common cold. The predicted indication, "nasal cavity disease," is therefore largely a broader label for uses that already exist, not a truly new therapeutic area. The literature also describes phenylephrine in combination nasal sprays (such as Polydexa with phenylephrine) and as a vasoconstrictor to improve the surgical field in endoscopic sinus surgery.

The available evidence is indirect or based on combination products, not on phenylephrine alone. Absorption into the bloodstream (cardiovascular effects) and a case report of toxicity with topical vasoconstrictors in nasal surgery call for attention to safety.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Experimental and clinical evaluation | Vestnik otorinolaringologii | Safety and efficacy evaluation of Polydexa spray with phenylephrine in acute rhinosinusitis (combination product) |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Review/Clinical article | Vestnik otorinolaringologii | Nasal mucosa state after local anti-inflammatory and antibacterial therapy with a phenylephrine-containing spray |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik otorinolaringologii | Pathogenetic approach to treating inflammatory diseases of the nose and paranasal sinuses |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | Randomized clinical trial | PloS one | Topical tranexamic acid and bleeding during endoscopic sinus surgery (phenylephrine is not the focus) |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case report | Archives of ophthalmology | Cocaine toxicity during dacryocystorhinostomy, with an additional reaction to intranasal phenylephrine |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02479281 | Phenylephrine Hydrochloride Injection USP 1% | Not available | Not available |
| 02504545 | Phenylephrine Hydrochloride Injection USP | Not available | Not available |
| 02148455 | Minims Phenylephrine Hydrochloride | Not available | Not available |
| 02238400 | Phenylephrine Hydrochloride Injection USP 1% | Not available | Not available |
| 01953583 | Phenylephrine Hydrochloride Injection USP | Not available | Not available |

These are 5 of 20 valid single-ingredient licences. The others include over-the-counter cold and sinus products (for example Extra Strength Tylenol Sinus Daytime, Neocitran, Benylin, Dayquil/Nyquil) and Preparation H-PE Gel.

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** hypertension and hypertensive disorder, liver failure and liver disease, kidney disease, epilepsy, insomnia, COPD, peptic and gastric ulcer, porphyria, hypothyroidism, adrenocortical insufficiency (Addison disease), inflammatory bowel disease, pancreatitis, gallbladder disease, thrombocytopenia, and psychotic or other mental disorders.
- **Drug interactions:** 100 interactions were found, and the 20 listed are all of moderate level. The main groups are antidiabetic drugs (acarbose, glimepiride, glipizide, glyburide, insulin, canagliflozin, dapagliflozin, empagliflozin, exenatide, dulaglutide and others) and anticholinergics (atropine ophthalmic, hyoscyamine, clidinium). Diethylpropion is also listed.
- **Literature signal:** a case report describes toxic reactions with topical vasoconstrictors used in nasal surgery.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the evidence is model-based plus a small, indirect literature set, with no registered trials. The predicted indication also overlaps closely with phenylephrine's existing uses in rhinitis and the common cold, so it adds little new therapeutic information.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- Phenylephrine-specific clinical studies in nasal cavity disease, not combination-product studies
- Approved indication text and dosage forms for the Canadian licences
- A safety assessment of systemic absorption, especially in patients with hypertension or taking antidiabetic drugs

---

### Other Predicted Indications (for reference)

| Predicted Indication | TxGNN Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|
| Acute laryngopharyngitis | 99.97% | L5 | Hold | No trials or literature. It overlaps with existing labelled uses (pharyngitis, nasopharyngitis), so the high score likely reflects similarity to those, not new evidence. |
| Trigeminal autonomic cephalalgia | 99.30% | L4 | Hold | The 12 publications describe phenylephrine only as a diagnostic eye-drop probe in pupillometry (cluster headache, SUNCT, Horner's syndrome). They do not show treatment benefit, and its pressor effects could be a concern in headache patients. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

