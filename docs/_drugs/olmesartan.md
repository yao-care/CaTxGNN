---
layout: default
title: Olmesartan
parent: Model Prediction Only (L5)
nav_order: 681
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Olmesartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Olmesartan"
predicted_indications: ["Prinzmetal angina", "hypotrichosis simplex of the scalp", "migraine disorder", "alopecia", "pulmonary hypertension", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "kyphoscoliotic heart disease", "open-angle glaucoma"]
---

# Olmesartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Olmesartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Olmesartan is an angiotensin II receptor blocker marketed in Canada in single-ingredient form. The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication. Among the other predicted indications, migraine disorder and pulmonary hypertension have the most supporting material, and they are summarised below for context.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (the Canadian license records contain no indication text) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, olmesartan is an angiotensin II type 1 (AT1) receptor blocker. Blocking this receptor may improve endothelial function and reduce vascular tone.

For Prinzmetal angina, which is caused by coronary vasospasm, this is only a plausible indirect link. No trials or publications support it, and calcium channel blockers remain the standard of care. The high TxGNN score reflects a pattern in the knowledge graph, not clinical proof.

For context, the other top predictions vary widely in plausibility:
- **Migraine disorder (score 99.64%, L3):** Some literature supports modulation of the renin-angiotensin system for migraine prevention, but the evidence is limited.
- **Pulmonary hypertension (score 99.61%, L4):** Preclinical rat studies suggest olmesartan reduces pulmonary vascular remodelling. No human efficacy data are available.
- **Hair-related conditions (hypotrichosis, alopecia, alopecia areata) and rare congenital conditions:** No mechanistic rationale is evident. These high scores are likely graph-based artifacts.
- **Open-angle glaucoma (L4):** Only an indirect review is available, with no olmesartan-specific data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina.

For reference, the only trial found among the other predicted indications was linked to pulmonary hypertension, and it is only indirectly relevant:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04330300](https://clinicaltrials.gov/study/NCT04330300) | Phase 4 | Suspended | 2414 | CORONACION trial of continuing ACE inhibitors/ARBs in COVID-19 patients. It does not target pulmonary hypertension. |

---

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

For reference, the most relevant publications for the other predicted indications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31515634](https://pubmed.ncbi.nlm.nih.gov/31515634/) | 2019 | Systematic review | Curr Pain Headache Rep | ACE inhibitors and ARBs for preventing episodic migraine in adults, with a focus on research gaps (migraine) |
| [16618270](https://pubmed.ncbi.nlm.nih.gov/16618270/) | 2006 | Clinical study (design to be verified) | Headache | Effect of olmesartan on migraine frequency and severity in patients with hypertension or prehypertension (migraine) |
| [16942482](https://pubmed.ncbi.nlm.nih.gov/16942482/) | 2006 | Commentary | Headache | Commentary on olmesartan, migraine and blood pressure (migraine) |
| [18209564](https://pubmed.ncbi.nlm.nih.gov/18209564/) | 2008 | Preclinical | J Cardiovasc Pharmacol | Olmesartan tested in the rat monocrotaline model of pulmonary hypertension (pulmonary hypertension) |
| [16336959](https://pubmed.ncbi.nlm.nih.gov/16336959/) | 2005 | Preclinical | Eur J Pharmacol | Olmesartan in chronic hypoxic rats, assessing hypoxic pulmonary hypertension (pulmonary hypertension) |
| [17089097](https://pubmed.ncbi.nlm.nih.gov/17089097/) | 2006 | Preclinical (mechanistic) | Naunyn-Schmiedeberg's Arch Pharmacol | Olmesartan and hypoxia-induced ERK1/2 activation and pro-inflammatory signals in mouse lung (pulmonary hypertension) |
| [19902393](https://pubmed.ncbi.nlm.nih.gov/19902393/) | 2009 | Review | Arch Soc Esp Oftalmol | General review of glaucoma medical treatment, with no olmesartan-specific data evident (open-angle glaucoma) |

---

## Canada Market Information

Olmesartan has 20 valid single-ingredient licenses in Canada. The records compiled for this report do not include dosage forms or approved indication text. Five representative authorizations are shown:

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02318679 | OLMETEC | Not available | Not available |
| 02318660 | OLMETEC | Not available | Not available |
| 02442205 | TEVA-OLMESARTAN | Not available | Not available |
| 02443414 | SANDOZ OLMESARTAN | Not available | Not available |
| 02461315 | PMS-OLMESARTAN | Not available | Not available |

---

## Safety Considerations

**Drug Interactions:** The interaction screening found 94 interacting drugs in total. Two interactions are rated **Major**:
- Potassium bicarbonate
- Potassium chloride

This is consistent with the risk of high potassium levels with angiotensin receptor blockers.

Many **Moderate** interactions were also identified, including:
- Hydrocortisone
- Exenatide
- Eluxadoline
- Polyethylene glycol (3350 with electrolytes)
- Numerous insulin products (human, aspart, degludec, detemir, glargine, glulisine, lispro and others)

Please refer to the package insert for warnings and contraindications. That information was not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction rests on the model score alone (L5), with no trials, literature or supporting mechanistic data. Calcium channel blockers remain the standard of care. Several other top predictions also lack support. Migraine is the most promising direction (L3), but it is still a research question given the small, mostly hypertensive study populations.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are required before safety screening can proceed
- Mechanism of action data for olmesartan
- Original indication, dosage form and approved indication text for the Canadian licenses
- For Prinzmetal angina: preclinical or clinical data on vasospasm, and comparison against calcium channel blockers
- Verification of the study design of the 2006 migraine study (PMID 16618270), and consideration of a prospective trial in migraine
- Human efficacy data for pulmonary hypertension, which currently has only animal evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

