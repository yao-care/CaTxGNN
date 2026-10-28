---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 291
evidence_level: L5
indication_count: 8
monitor_inn: "DIPYRIDAMOLE"
predicted_indications: ["thrombotic disease", "sick sinus syndrome 2, autosomal dominant", "transient ischemic attack (disease)", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "lateral sinus thrombosis", "cavernous sinus thrombosis"]
last_modified_at: 2026-10-27
description: "Dipyridamole: predicted new indication thrombotic disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Dipyridamole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Dipyridamole: Platelet aggregation inhibitor (adenosine reuptake and phosphodiesterase inhibitor) → thrombotic disease
{: .text-alpha }

## One-Sentence Summary

Dipyridamole is an antiplatelet and vasodilator medicine that is currently licensed in Canada.
The TxGNN model predicts it may be effective for **thrombotic disease**, with a score of **0.9994**.
No clinical trials are registered for this exact indication, and the **20 publications** retrieved are mostly reviews of antiplatelet therapy in general, so the support is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | thrombotic disease |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 2 of 2) |
| Number of DINs | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not included in the data compiled for this report. From the published literature, dipyridamole is known to block adenosine reuptake and to inhibit phosphodiesterase. Both effects raise cAMP and cGMP in platelets, which suppresses platelet aggregation and is consistent with antithrombotic activity.

"Thrombotic disease" is a broad category rather than a single defined condition. The reviews on antiplatelet drugs, thrombotic thrombocytopenic purpura, and thromboembolism that were retrieved describe the drug class and the biology. None of them tests dipyridamole in a clearly defined thrombotic condition. For this reason the evidence level is capped at L5 and the link is plausible but unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered for thrombotic disease.

## Literature Evidence

None of the publications below is a trial of dipyridamole in a defined thrombotic condition; they are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18174451](https://pubmed.ncbi.nlm.nih.gov/18174451/) | 2008 | Review | Arterioscler Thromb Vasc Biol | Dipyridamole raises cAMP and cGMP, reversibly inhibits platelet aggregation and platelet-mediated thrombotic disease |
| [12765506](https://pubmed.ncbi.nlm.nih.gov/12765506/) | 2003 | Review | Med J Aust | Antiplatelet drugs protect against myocardial infarction, stroke and other serious vascular events in high-risk patients |
| [2182246](https://pubmed.ncbi.nlm.nih.gov/2182246/) | 1990 | Review | Clin Cardiol | Aspirin with dipyridamole in coronary thrombosis; aspirin only partially effective in experimental models |
| [382146](https://pubmed.ncbi.nlm.nih.gov/382146/) | 1979 | Review | Postgrad Med | Aspirin, dipyridamole and sulfinpyrazone show antithrombotic effects in humans |
| [559478](https://pubmed.ncbi.nlm.nih.gov/559478/) | 1977 | Case report | Arch Intern Med | Two patients with thrombotic thrombocytopenic purpura; one relapsed when the dipyridamole dose was tapered and remitted when it was raised |
| [2440111](https://pubmed.ncbi.nlm.nih.gov/2440111/) | 1987 | Review | Semin Hematol | Antiplatelet agents reported to improve thrombocytopenia and clinical status in many TTP patients |
| [25697566](https://pubmed.ncbi.nlm.nih.gov/25697566/) | 2015 | Review | Curr Top Med Chem | Dipyridamole has antioxidant activity in addition to antithrombotic and vasodilator effects |
| [19160220](https://pubmed.ncbi.nlm.nih.gov/19160220/) | 2009 | Systematic review | Cochrane Database Syst Rev | Interventions for haemolytic uraemic syndrome and TTP |
| [20484211](https://pubmed.ncbi.nlm.nih.gov/20484211/) | 2010 | Review | Am J Health Syst Pharm | Antiplatelet and anticoagulant drugs in vasoocclusive and thrombotic complications of sickle cell disease |
| [11945125](https://pubmed.ncbi.nlm.nih.gov/11945125/) | 2002 | Review | Curr Med Chem | Platelet aggregation in thromboembolic disease and recent advances in antiplatelet agents |

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02244475 | DIPYRIDAMOLE INJECTION, USP | Not recorded | Not recorded |
| 00637734 | PERSANTINE | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries. Moderate-level interactions include dexfenfluramine, sibutramine and fenfluramine. Others, such as acetylsalicylic acid, cimetidine, morphine, metformin and omeprazole, are listed with an unclassified severity. Combinations with other antithrombotic drugs call for attention to bleeding risk.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is biologically consistent with antithrombotic activity, but no registered trial and no publication studies dipyridamole in a clearly defined thrombotic condition. The evidence is therefore limited to model prediction plus indirect reviews.

**To proceed, the following is needed:**
- A specific, well-defined thrombotic condition to evaluate, instead of the broad category
- Clinical or controlled studies of dipyridamole in that condition
- Mechanism-of-action data in the compiled record
- Package insert warnings and contraindications from Health Canada
- A bleeding-risk plan for combinations with other antithrombotic drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

