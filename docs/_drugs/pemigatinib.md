---
layout: default
title: Pemigatinib
parent: Model Prediction Only (L5)
nav_order: 719
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pemigatinib: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the data compiled for this report"
monitor_inn: "Pemigatinib"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "HER2 positive breast carcinoma", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh", "amyotrophic lateral sclerosis", "amyotrohpic lateral sclerosis type 22", "amyotrophic lateral sclerosis, susceptibility to", "axial spondylometaphyseal dysplasia"]
---

# Pemigatinib
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

# Pemigatinib: From an FGFR-Driven Cancer Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

Pemigatinib is a selective FGFR1-3 kinase inhibitor marketed in Canada as PEMAZYRE. The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It rests on a computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report (Canadian license indication text is blank) |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Pemigatinib is a selective inhibitor of FGFR1-3. Detailed mechanism of action data is not available in the data compiled for this report, so this description is based on the drug's known class.

Multiple endocrine neoplasia (MEN) syndromes are driven mainly by loss of MEN1 (menin) and by RET activation, not by FGFR signaling. The only link is speculative: FGFR involvement in neuroendocrine tumour growth. The high TxGNN score (0.997) is a computational output. No trials or literature back it up, so the mechanistic rationale should be treated as weak.

Other top-ranked predictions are even less plausible. Several look like knowledge-graph artifacts: amenorrhea, two veterinary herpesvirus diseases (infectious bovine rhinotracheitis and malignant catarrhal fever), and cytomegalovirus infection. Several ALS entries are also predicted. FGF/FGFR signaling is generally neurotrophic, so inhibiting it could be harmful in ALS. The most biologically plausible alternative is HER2-positive breast carcinoma, where FGFR signaling has been linked to resistance to HER2-targeted therapy. That link is indirect, and the only retrieved paper is a general kinase inhibitor review (PMID 33513356, 2021, *Pharmacological Research*) with no pemigatinib-specific efficacy or safety data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted indication of multiple endocrine neoplasia.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02519941 | PEMAZYRE | Not specified | Not specified |
| 02519933 | PEMAZYRE | Not specified | Not specified |
| 02519968 | PEMAZYRE | Not specified | Not specified |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

