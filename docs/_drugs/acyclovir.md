---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Acyclovir: predicted new indication Top-ranked: punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Herpes simplex infection, herpes zoster, chickenpox, herpes labialis…"
monitor_inn: "Acyclovir"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
---

# Acyclovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Acyclovir: From Herpes Simplex Infection to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Acyclovir is an antiviral drug originally used to treat herpes simplex infections, herpes zoster, chickenpox, herpes labialis, herpes simplex encephalitis and genital herpes.
The TxGNN model's top-ranked prediction is punctate epithelial keratoconjunctivitis, but that prediction has no clinical support. The best-supported candidate is **common wart** (TxGNN's second-ranked prediction), with **4 clinical trials** and **20 publications** pointing in this direction, including a Phase 2/3 randomized trial.

> Note: The top-ranked prediction (punctate epithelial keratoconjunctivitis) has no clinical trials and only two unrelated papers, so the report focuses on common wart as the most evidence-supported candidate. Other predictions are summarized at the end.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex infection, herpes zoster, chickenpox, herpes labialis, herpes simplex encephalitis, genital herpes (the Canadian licence records contain no indication text) |
| Predicted New Indication | Top-ranked: punctate epithelial keratoconjunctivitis; best-supported: common wart |
| TxGNN Prediction Score | 0.9967 (punctate epithelial keratoconjunctivitis); 0.9946 (common wart) |
| Evidence Level | L5 for the top-ranked prediction; L2 for common wart |
| Canada Market Status | Marketed (marketed DINs: 20 of 20) |
| Number of DINs | 20 (marketed: 20) |
| Recommended Decision | Hold for the top-ranked prediction; Proceed with Guardrails for common wart (as a research question) |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for acyclovir: "Acyclovir is a synthetic purine nucleoside analogue with in vitro and in vivo inhibitory activity against herpes simplex virus types 1 (HSV-1), 2 (HSV-2), and varicella-zoster virus (VZV). The inhibitory activity of acyclovir is highly selective due to its affinity for the enzyme thymidine kinase (TK) encoded by HSV and VZV." ([DailyMed: acyclovir prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=499c6a98-0614-4ded-8526-909942bae8a4), label version 2026-06-26; accessed 2026-11-19.) Based on general knowledge, acyclovir is a nucleoside analogue that is activated by viral thymidine kinase and inhibits viral DNA polymerase. Its efficacy in herpesvirus infections is well established.

**Top-ranked prediction (punctate epithelial keratoconjunctivitis):** Any benefit would depend on a herpesvirus cause. The only two papers retrieved concern microsporidial keratoconjunctivitis and drug-induced corneal lipidosis in AIDS, neither of which is herpesvirus-driven. The very high model score is not supported by clinical data.

**Common wart:** Warts are caused by HPV, a DNA virus. HPV lacks the thymidine kinase that activates acyclovir, so a direct antiviral effect is mechanistically weak. Proposed explanations for the observed effect of intralesional injection include local immune stimulation, inflammation, and inhibition of host or viral DNA synthesis. These are hypotheses only. Even so, several small trials, mostly from Egypt, have compared intralesional acyclovir with cryotherapy, vitamin D3, Candida antigen, 5-FU and HPV vaccine, and a Phase 2/3 randomized trial against cryotherapy has a published report.

---

## Clinical Trial Evidence

Common wart trials:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Phase 2/3 | Unknown | 92 | Randomized trial of intralesional acyclovir vs cryotherapy in plantar warts; safety and efficacy; a matching 2026 publication exists (PMID 40889709) |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Phase 4 | Unknown | 40 | Intralesional acyclovir vs Candida antigen in plantar warts; no results reported |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Phase 4 | Recruiting | 40 | Intralesional vitamin D3 vs acyclovir in common, plantar, flat and periungual warts; primary outcome is complete clearance by week 8 |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | Not applicable | Unknown | 44 | Intralesional acyclovir vs vitamin D3 in plantar warts; efficacy and safety |

Trials are small, and most have unknown status and no reported results.

---

## Literature Evidence

Common wart publications (most relevant 10):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | RCT | J Am Acad Dermatol | Intralesional acyclovir vs cryotherapy in plantar warts |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | RCT | Arch Dermatol Res | Intralesional acyclovir vs hepatitis B vaccine in resistant plantar warts (48 patients) |
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | RCT/Comparative | Arch Dermatol Res | Intralesional acyclovir vs 5-fluorouracil in recalcitrant warts |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | Comparative study | Arch Dermatol Res | Intralesional acyclovir vs quadrivalent HPV vaccine in recalcitrant cutaneous warts (60 patients) |
| [41686619](https://pubmed.ncbi.nlm.nih.gov/41686619/) | 2026 | Systematic review/network meta-analysis | Medicine | Comparison of treatment modalities for cutaneous warts, including intralesional acyclovir |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | Comparative study | Cureus | Intralesional acyclovir vs PPD immunotherapy in viral warts |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | Clinical study | J Cutan Med Surg | Intralesional acyclovir as a potential option for cutaneous warts |
| [38793636](https://pubmed.ncbi.nlm.nih.gov/38793636/) | 2024 | Case reports and review | Viruses | Remission of HPV-related diseases (penile condyloma, among others) with acyclovir or valaciclovir |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | Case report | J Drugs Dermatol | Persistent plantar warts resolved after oral acyclovir given for herpes zoster |
| [6467981](https://pubmed.ncbi.nlm.nih.gov/6467981/) | 1984 | Report | Cutis | Acyclovir ointment in verruca vulgaris |

---

## Canada Market Information

The table below lists each DIN with its current status in the DPD. The compiled data lack dosage form and approved indication text for each licence, so those columns are omitted.

<!-- review:begin ca-lic-20261106-acyclovir-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Acyclovir has 20 valid single-ingredient licences in Canada and none have been cancelled." Removed: it described the products as single-ingredient or combination products in a way that did not match the Health Canada DPD data (the Health Canada Drug Product Database as of 2026-11-06). Revised 2026-11-24: the number of DINs and any reference to the earlier licence table, which showed only some of the DINs, were removed from the corrected sentence; the Quick Overview and the table under Canada Market Information show the current number and status of DINs. Source: [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html).

<!-- review:end ca-lic-20261106-acyclovir-1 -->

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00569771 | ZOVIRAX | ACYCLOVIR | Marketed |
| 02039524 | ZOVIRAX | ACYCLOVIR | Marketed |
| 02207621 | APO-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02207648 | APO-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02207656 | APO-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02236926 | ACYCLOVIR SODIUM INJECTION | ACYCLOVIR (ACYCLOVIR SODIUM) | Marketed |
| 02242463 | MYLAN-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02242464 | MYLAN-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02242784 | MYLAN-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02285959 | TEVA-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02285967 | TEVA-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02285975 | TEVA-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02404044 | XERESE | ACYCLOVIR; HYDROCORTISONE | Marketed |
| 02477130 | APO-ACYCLOVIR OINTMENT | ACYCLOVIR | Marketed |
| 02494558 | ACYCLOVIR SODIUM INJECTION | ACYCLOVIR (ACYCLOVIR SODIUM) | Marketed |
| 02522306 | TARO-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02524708 | MINT-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02524716 | MINT-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02524724 | MINT-ACYCLOVIR | ACYCLOVIR | Marketed |
| 02531224 | ACYCLOVIR SODIUM INJECTION | ACYCLOVIR (ACYCLOVIR SODIUM) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

Other authorizations include MINT-ACYCLOVIR, TEVA-ACYCLOVIR, MYLAN-ACYCLOVIR, APO-ACYCLOVIR and TARO-ACYCLOVIR, plus further acyclovir sodium injection products. Product names indicate that oral, injectable and topical products exist, which is relevant because the wart trials use intralesional injection of the intravenous formulation.

---

## Safety Considerations

**Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links acyclovir to a broad list of disease contraindications. These are model-derived associations and need verification against the label. Examples:
- Kidney disease and impaired renal function
- Hemolytic-uremic syndrome and thrombocytopenic purpura
- Hypertension and cardiovascular or cerebrovascular disease (myocardial infarction, stroke, peripheral arterial disease)
- Diabetes mellitus, hyperglycemia and diabetic ketoacidosis
- Adrenocortical insufficiency (Addison disease)

**Drug Interactions:** The interaction screen returned 100 interactions in total. Those with a Moderate level are:
- Balsalazide
- Mesalazine
- Olsalazine
- Sulfasalazine
- Trospium

Other listed interactions (for example amphotericin B, metformin, morphine, omeprazole, epinephrine) have an unknown severity level.

Please refer to the package insert for key warnings and label contraindications.

---

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction (punctate epithelial keratoconjunctivitis); Proceed with Guardrails for common wart as a research question.**

**Rationale:**
- Punctate epithelial keratoconjunctivitis has a very high model score (0.9967) but no trials and only unrelated literature (L5), so it cannot be advanced.
- For common wart, a Phase 2/3 RCT and several comparative studies support intralesional acyclovir (L2). However, the mechanism is weak, the trials are small and mostly regional, and several have unknown status.

**To proceed, the following is needed:**
- The package insert warnings and contraindications from Health Canada (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the published results of NCT06261684 and an assessment of the RCT quality
- Larger, multi-centre, blinded trials with standardized outcomes against current standard care
- A review of the regulatory and formulation question: intralesional injection of the intravenous product would be off-label use
- Verification of the knowledge-graph contraindications (especially renal disease) against the label

**Other predictions (summary):**

| Predicted Indication | Evidence Level | Decision | Comment |
|------|------|------|------|
| Disease of orbital region | L5 | Research question | Relevant herpetic eye disease trials (keratitis, uveitis) but orbital disease is not directly tested; includes unrelated trials |
| Sequela of COVID-19 | L5 | Hold | Literature covers herpesvirus reactivation, not COVID-19 sequelae |
| Epidemic keratoconjunctivitis | L5 | Hold | Adenovirus cause; acyclovir not expected to act |
| Post-infectious neuralgia | L5 | Hold | No trials or literature |
| Hepatitis C induced liver cirrhosis | L5 | Hold | HCV is an RNA virus; no mechanism |
| Eosinophilic pustular folliculitis | L5 | Hold | No viral cause; no data |
| Vulvovaginal candidiasis | L5 | Hold | Fungal cause; likely a co-occurrence artifact |
| Papular urticaria | L5 | Hold | Insect bite hypersensitivity; no data |

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Canada data (the Drug Product Database, DPD). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient"; revised 2026-11-24 to remove the DIN count and the reference to the earlier licence table | Corrected (revised 2026-11-24; earlier version kept in the record) | [Health Canada Drug Product Database (DPD)](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database.html) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: acyclovir prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=499c6a98-0614-4ded-8526-909942bae8a4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

