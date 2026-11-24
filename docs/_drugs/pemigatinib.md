---
layout: default
title: Pemigatinib
parent: Model Prediction Only (L5)
nav_order: 719
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Pemigatinib: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Pemigatinib"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "HER2 positive breast carcinoma", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "amyotrophic lateral sclerosis", "amyotrohpic lateral sclerosis type 22", "axial spondylometaphyseal dysplasia"]
---

# Pemigatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Pemigatinib: From an FGFR-Driven Cancer Indication to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Pemigatinib is a selective FGFR1-3 kinase inhibitor marketed in Canada as PEMAZYRE. The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It rests on a computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (Canadian license indication text is blank) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 3 of 3) |
| Number of DINs | 3 (marketed: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Pemigatinib is a selective inhibitor of FGFR1-3. This description is based on the drug's known class. According to the Mechanism of Action section of the US FDA-approved prescribing information for pemigatinib: "Pemigatinib is a small molecule kinase inhibitor that targets FGFR1, 2 and 3 with IC 50 values of less than 2 nM. Pemigatinib also inhibited FGFR4 in vitro at a concentration approximately 100 times higher than those that inhibit FGFR1, 2, and 3." ([DailyMed: Pemazyre (pemigatinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9e1f2222-1d89-4e63-989c-ccebe2ab1eb4), label version 2026-06-09; accessed 2026-11-19.)

Multiple endocrine neoplasia (MEN) syndromes are driven mainly by loss of MEN1 (menin) and by RET activation, not by FGFR signaling. The only link is speculative: FGFR involvement in neuroendocrine tumour growth. The high TxGNN score (0.9971) is a computational output. No trials or literature back it up, so the mechanistic rationale should be treated as weak.

Other top-ranked predictions are even less plausible. Several look like TxGNN model (deep learning) artifacts: amenorrhea, two veterinary herpesvirus diseases (infectious bovine rhinotracheitis and malignant catarrhal fever), and cytomegalovirus infection. Several ALS entries are also predicted. FGF/FGFR signaling is generally neurotrophic, so inhibiting it could be harmful in ALS. The most biologically plausible alternative is HER2-positive breast carcinoma, where FGFR signaling has been linked to resistance to HER2-targeted therapy. That link is indirect, and the only retrieved paper is a general kinase inhibitor review (PMID 33513356, 2021, *Pharmacological Research*) with no pemigatinib-specific efficacy or safety data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted indication of multiple endocrine neoplasia.

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02519933 | PEMAZYRE | PEMIGATINIB | Marketed |
| 02519941 | PEMAZYRE | PEMIGATINIB | Marketed |
| 02519968 | PEMAZYRE | PEMIGATINIB | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

All three licenses are valid single-ingredient products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective FGFR1-3 kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Endocrine and phosphate-related effects are expected with FGFR inhibitors, so serum phosphate monitoring is reasonable. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Drug Interactions:** The interaction screening returned 50 interacting drugs in total. Several are rated Major, including:
- Aprepitant
- Dexamethasone
- Clarithromycin
- Cobicistat
- Lumacaftor
- Chloramphenicol
- Erythromycin
- Ketoconazole
- Fluconazole

Moderate-level interactions include cimetidine, clotrimazole, deferasirox, ivacaftor, zafirlukast, griseofulvin, elagolix and osilodrostat, among others. Many of these are CYP3A-modulating agents, so co-medication needs careful review.

For warnings and contraindications, please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or publications, and the mechanistic link between FGFR inhibition and MEN syndromes is weak. The package insert safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (blocking gap)
- Mechanism of action data from DrugBank
- Targeted literature review of FGFR signaling in neuroendocrine and MEN-related tumours
- Preclinical or mechanistic studies to justify any move beyond L5
- Consider prioritising HER2-positive breast carcinoma, which has a more plausible, though still indirect, rationale

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism of action data is not available in the data compiled for this report, so this description is based on the drug's known class" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Pemazyre (pemigatinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9e1f2222-1d89-4e63-989c-ccebe2ab1eb4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

