---
layout: default
title: Tacrolimus
parent: Model Prediction Only (L5)
nav_order: 876
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-13
description: "Tacrolimus: predicted new indication Seborrheic dermatitis (evidence level L5). Approved use: Atopic eczema / atopic dermatitis"
monitor_inn: "TACROLIMUS"
predicted_indications: ["seborrheic dermatitis", "parapsoriasis", "dermatitis"]
---

# Tacrolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Tacrolimus: From Atopic Eczema to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor originally used to treat atopic eczema (atopic dermatitis).
The TxGNN model predicts it may be effective for **seborrheic dermatitis**,
with **2 clinical trials** and **20 publications** currently supporting this direction, including a completed Phase 3 trial of tacrolimus ointment as maintenance therapy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic eczema / atopic dermatitis |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 20 |
| Recommended Decision | Proceed with Guardrails |

*Evidence level note:* Only one completed Phase 3 trial (n=120) directly addresses seborrheic dermatitis, and a Phase 4 study supports it. Under the strict rule (at least 2 completed Phase 3 RCTs for L1), this fits L2 more closely than L1. The trial's randomization and control design is not described in the data compiled for this report, so it needs verification.

---

## Why is This Prediction Reasonable?

Tacrolimus inhibits calcineurin. This blocks activation of T cells and the release of pro-inflammatory cytokines. Topical tacrolimus is established in atopic dermatitis, where it reduces inflammatory cytokines and chemokines.

Seborrheic dermatitis is a chronic, relapsing inflammatory skin disease of the face and scalp. The host immune response to *Malassezia* yeast is thought to be a core driver. Atopic dermatitis and seborrheic dermatitis therefore share an immunoinflammatory mechanism, which makes the prediction biologically plausible.

Published reviews describe topical calcineurin inhibitors as a steroid-sparing alternative in seborrheic dermatitis. The long-term adverse effects of corticosteroids limit their use. Detailed mechanism-of-action data from DrugBank were not available in the data compiled for this report, so this reasoning rests on the known pharmacology of calcineurin inhibitors.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Protopic (tacrolimus) ointment as maintenance treatment of severe seborrheic dermatitis on the adult face, aiming to reduce relapses and steroid use. No results were provided in the data. |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive use of 0.1% tacrolimus ointment once or twice weekly to keep adult facial seborrheic dermatitis in remission and reduce exacerbations. No results were provided in the data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical study | Annals of Dermatology | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment, modelled on the low-dose intermittent regimen used in atopic dermatitis |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | Am J Clin Dermatol | Topical treatment of facial seborrheic dermatitis (antifungals, keratolytics, corticosteroids) |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Topical calcineurin inhibitors are a safe alternative to corticosteroids in seborrheic dermatitis |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Clinical trial | Annals of Parasitology | Sertaconazole 2% cream compared with tacrolimus 0.03% cream in 60 patients |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Review | J Cutan Med Surg | Evidence for off-label use of topical calcineurin inhibitors in other dermatologic disorders |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematic review / network meta-analysis | Clin Exp Allergy | Topical anti-inflammatory treatments for eczema (indirect evidence) |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | Tacrolimus ointment in atopic dermatitis and other inflammatory skin diseases |
| [17685874](https://pubmed.ncbi.nlm.nih.gov/17685874/) | 2007 | Review | Expert Opin Investig Drugs | New roles for topical tacrolimus; mild side effects and minimal systemic absorption |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | Topical immunomodulators in psoriasis, seborrheic dermatitis, lichen planus and other diseases |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Current status and therapeutic horizons for facial seborrheic dermatitis |

---

## Canada Market Information

Tacrolimus has 20 valid single-ingredient licenses in Canada. The data compiled for this report do not include dosage forms or approved-indication text for these products. Brand names suggest both topical and systemic products: Protopic is the ointment, while Prograf, Advagraf and Envarsus PA are systemic formulations. Please confirm against the product monographs.

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02244149 | PROTOPIC | Not available | Not available |
| 02244148 | PROTOPIC | Not available | Not available |
| 02243144 | PROGRAF | Not available | Not available |
| 02296462 | ADVAGRAF | Not available | Not available |
| 02485893 | ENVARSUS PA | Not available | Not available |

Other products include SANDOZ TACROLIMUS, SANDOZ TACROLIMUS XR and ACH-TACROLIMUS.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertension, long QT syndrome and torsades de pointes, liver failure, kidney disease, epilepsy, hyperglycemia and diabetes mellitus, diabetic ketoacidosis, infectious diseases (including herpes simplex and herpes zoster), cancer and lymphoma, Epstein-Barr virus-related conditions, progressive multifocal leukoencephalopathy, and posterior leukoencephalopathy syndrome. Many of these relate to systemic exposure, and topical use has minimal systemic absorption.
- **Drug Interactions:** The interaction check returned 100 interactions. Major-level examples include amphotericin B, loperamide, mesalazine, omeprazole and balsalazide. Moderate-level examples include famotidine, rabeprazole, systemic corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), and several antidiabetic agents (metformin, pioglitazone, alogliptin, acarbose, albiglutide).
- **Cancer risk:** A 2023 systematic review and meta-analysis (PMID 36370744) examined cancer risk with topical calcineurin inhibitors in atopic dermatitis. The data compiled for this report include no conclusions from it.

Please refer to the Health Canada package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The model score is very high, the mechanism is plausible, and a completed Phase 3 trial plus a Phase 4 study test tacrolimus ointment directly in seborrheic dermatitis. However, trial results were not available, and there is only one Phase 3 study. The package insert warnings are also missing, which blocks formal safety screening.

**To proceed, the following is needed:**
- Obtain and review the results of NCT02004860 and NCT01591070 (efficacy, relapse rate, safety)
- Download and parse the Health Canada package insert for warnings and contraindications
- Confirm which Canadian products are topical, and whether seborrheic dermatitis is covered by the labelled indication (it would be off-label use)
- Retrieve mechanism-of-action data from DrugBank
- Define a long-term safety monitoring plan for topical calcineurin inhibitor use, including the cancer-risk question

---

### Other Predicted Indications (for reference)

- **Parapsoriasis (score 99.24%):** Evidence is limited to two case reports of pityriasis lichenoides treated with topical tacrolimus, with no registered trials. This is a research question, not a candidate for advancement.
- **Dermatitis (score 99.17%):** Extensive trial and literature evidence exists, but it overlaps heavily with the original atopic dermatitis indication, so it is not a truly novel repurposing signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

