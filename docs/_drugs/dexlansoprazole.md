---
layout: default
title: Dexlansoprazole
parent: High Evidence (L1-L2)
nav_order: 269
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Dexlansoprazole: predicted new indication Active peptic ulcer disease (evidence level L1). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, esophagitis…"
---

# Dexlansoprazole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Dexlansoprazole: From Peptic Ulcer Disease and GERD to Active Peptic Ulcer Disease

## One-Sentence Summary

Dexlansoprazole is a proton pump inhibitor originally used for peptic ulcer disease, gastroesophageal reflux disease (GERD) and esophagitis.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, but this is essentially an on-label use rather than a true repurposing case.
Direct support comes from **2 completed Phase 3 trials** (in erosive esophagitis) and **3 literature records** in the data compiled for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, esophagitis, peptic esophagitis (the Canadian licence records contain no indication text) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, dexlansoprazole is a proton pump inhibitor. It blocks the H+/K+ ATPase in stomach acid-producing cells and suppresses gastric acid secretion.

Active peptic ulcers are acid-mediated, and lowering acid allows the ulcer to heal. This is the same mechanism behind the drug's existing indications in peptic ulcer disease and acid-related disorders. The prediction is therefore mechanistically sound, but it largely overlaps with the original indications and does not represent a new therapeutic area.

Other predicted diseases are weaker. Gastrojejunal (marginal) ulcer is plausible because it is acid-driven, but the evidence is indirect. Gastric ulcer and duodenal ulcer fall within the drug's class-level acid-related indications and share the same Phase 3 trials. Several other predictions (achlorhydria, leather-bottle stomach, duodenal obstruction, duodenogastric reflux) are likely artifacts of network proximity and have no supporting evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | Completed | 2054 | Dexlansoprazole MR 60/90 mg vs lansoprazole 30 mg for 8 weeks in healing erosive esophagitis |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | Completed | 2038 | Companion trial with the same design: dexlansoprazole MR 60/90 mg vs lansoprazole 30 mg |

These trials were run in erosive esophagitis, so their link to ulcer healing is inferred. The registry entries do not state an ulcer endpoint. Additional Phase 3 trials (NCT00321737, NCT00255164, NCT00255151) studied maintenance of healed erosive esophagitis and are linked to the gastric and duodenal ulcer predictions rather than to this one.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Systematic review/meta-analysis | Am J Gastroenterol | Network meta-analysis comparing P-CABs and PPIs for healing grade C/D esophagitis |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | Review | Curr Opin Investig Drugs | Development of dexlansoprazole, a modified-release enantiomer of lansoprazole, for reflux esophagitis |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | Preclinical/mechanistic | J Chin Med Assoc | PPIs including dexlansoprazole suppress vacuolar-type ATPase and induce ER stress, relevant to the long-term PPI and gastric cancer risk question |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02354969 | DEXILANT | Not listed | Not listed |
| 02354950 | DEXILANT | Not listed | Not listed |
| 02529025 | APO-DEXLANSOPRAZOLE | Not listed | Not listed |
| 02528991 | APO-DEXLANSOPRAZOLE | Not listed | Not listed |

All four licences are valid single-ingredient products.

---

## Safety Considerations

- **Disease-level contraindication signals (from the knowledge graph, not label text)**: liver disease, gallbladder disease, osteoporosis, postmenopausal osteoporosis, bone fracture.
- **Drug Interactions**: 100 interactions were identified. Examples include:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: fosamprenavir, foscarnet, fostamatinib, furosemide, gefitinib, hydrochlorothiazide, bosutinib, bumetanide, amphotericin B, amikacin, amphetamine, ampicillin
  - **Minor**: acetylsalicylic acid, axitinib, brivaracetam, cyanocobalamin

  Many acid-dependent absorption interactions (such as with atazanavir and some kinase inhibitors) are class effects of PPIs.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Two large completed Phase 3 trials support dexlansoprazole in acid-related disease, and the mechanism is well established. However, those trials were in erosive esophagitis, and the ulcer indication overlaps with the drug's existing use, so this is not a novel repurposing finding.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Confirmation of the Canadian approved indication text, dosage forms and manufacturers
- Detailed mechanism of action data from DrugBank
- Confirmation of ulcer-specific endpoints in the Phase 3 trials
- A review of the drug interaction list and of the bone and liver-related signals before use in at-risk patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

