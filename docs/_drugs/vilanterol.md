---
layout: default
title: Vilanterol
parent: High Evidence (L1-L2)
nav_order: 974
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-13
description: "Vilanterol: predicted new indication Obstructive lung disease (evidence level L1). Approved use: Chronic obstructive pulmonary disease, asthma, bronchitis…"
---

# Vilanterol
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

# Vilanterol: From Chronic Obstructive Pulmonary Disease to Obstructive Lung Disease

## One-Sentence Summary

Vilanterol is a long-acting inhaled beta2-agonist, originally used to treat chronic obstructive pulmonary disease (COPD) and asthma.
The TxGNN model predicts it may be effective for **obstructive lung disease**, but this overlaps heavily with its existing indications, so it is better read as a confirmation of current use than as a new repurposing finding.
The data compiled for this report include **30 clinical trials** and **20 publications** for this prediction, including several completed Phase 3 randomized trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic obstructive pulmonary disease, asthma, bronchitis, pulmonary emphysema (the Canadian licence records contain no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on the known pharmacology of the drug class, vilanterol is a selective long-acting beta2-adrenoceptor agonist. It relaxes airway smooth muscle through cAMP-mediated signalling and produces bronchodilation that lasts about 24 hours, which supports once-daily dosing.

COPD and asthma are both obstructive lung diseases. "Obstructive lung disease" is therefore the broader category that contains the drug's existing indications. The prediction is mechanistically sound, but it largely restates approved use rather than identifying a new therapeutic area.

The other predicted indications (ranks 2–10) are weaker. Compensatory emphysema, hyperlucent lung, interstitial emphysema, tracheal stenosis, congenital lobar emphysema, tracheal calcification and laryngotracheitis have no trials or literature, and bronchodilation is not expected to address their causes. The high scores likely reflect name similarity to emphysema or COPD. For bronchial neoplasm, the only trial (NCT04536675) tests dual bronchodilators for postoperative lung function in lung cancer patients who also have COPD. That is supportive care, not antitumour activity. The literature retrieved for respiratory malformation is vilanterol safety and QT studies and COPD reports, not studies of that condition.

---

## Clinical Trial Evidence

The table lists the 10 most relevant of the 30 trials for obstructive lung disease. Most test vilanterol combined with fluticasone furoate and/or umeclidinium, not vilanterol alone.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03162055](https://clinicaltrials.gov/study/NCT03162055) | Phase 3 | Completed | 1119 | Glycopyrronium/formoterol vs umeclidinium/vilanterol over 24 weeks in moderate to very severe COPD |
| [NCT01134042](https://clinicaltrials.gov/study/NCT01134042) | Phase 3 | Completed | 587 | Fluticasone furoate/vilanterol vs fluticasone furoate alone and fluticasone propionate in persistent asthma over 24 weeks |
| [NCT02094937](https://clinicaltrials.gov/study/NCT02094937) | Phase 3 | Completed | 430 | Fluticasone furoate step-down from fluticasone furoate/vilanterol in well-controlled Japanese asthma patients |
| [NCT01686633](https://clinicaltrials.gov/study/NCT01686633) | Phase 3 | Completed | 1040 | Fluticasone furoate/vilanterol 200/25 and 100/25 vs fluticasone furoate 100 in moderate to severe persistent asthma |
| [NCT02301975](https://clinicaltrials.gov/study/NCT02301975) | Phase 3 | Completed | 1526 | Once-daily fluticasone furoate/vilanterol vs twice-daily fluticasone propionate/salmeterol in asthma already controlled on ICS/LABA |
| [NCT01777334](https://clinicaltrials.gov/study/NCT01777334) | Phase 3 | Completed | 905 | Umeclidinium/vilanterol vs tiotropium on trough FEV1 over 24 weeks in COPD |
| [NCT01342913](https://clinicaltrials.gov/study/NCT01342913) | Phase 3 | Completed | 528 | 24-hour lung function of fluticasone furoate/vilanterol vs salmeterol/fluticasone propionate in COPD |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | Completed | 4233 | 12-month open-label effectiveness study of fluticasone furoate/vilanterol vs usual maintenance therapy in asthma |
| [NCT05062304](https://clinicaltrials.gov/study/NCT05062304) | N/A | Completed | 17281 | Real-world replication of the IMPACT trial of single-inhaler triple vs dual therapy in COPD |
| [NCT04265105](https://clinicaltrials.gov/study/NCT04265105) | Phase 2/3 | Completed | 18 | Small pilot of as-needed fluticasone-vilanterol vs standard care in mild asthma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | IMPACT: once-daily single-inhaler triple therapy vs dual therapy in COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL: once-daily triple therapy vs dual ICS/LABA in COPD |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT | Am J Respir Crit Care Med | Reduction in all-cause mortality with fluticasone furoate/umeclidinium/vilanterol in COPD |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | Lancet Respir Med | CAPTAIN: triple therapy vs fluticasone furoate/vilanterol in inadequately controlled asthma |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network meta-analysis | Adv Ther | Comparative efficacy of fluticasone furoate/umeclidinium/vilanterol against other triple and dual therapies in COPD |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic review and meta-analysis | BMC Pulm Med | Umeclidinium/vilanterol vs other bronchodilators in COPD |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohort study | BMJ | New-user comparison of two single-inhaler triple therapies in routine COPD care |
| [26668137](https://pubmed.ncbi.nlm.nih.gov/26668137/) | 2016 | Review | Ther Adv Respir Dis | Clinical trial evidence for fluticasone furoate/vilanterol in asthma |
| [28956463](https://pubmed.ncbi.nlm.nih.gov/28956463/) | 2017 | Review | Expert Rev Respir Med | Role of fluticasone furoate/vilanterol in stable COPD |
| [23232038](https://pubmed.ncbi.nlm.nih.gov/23232038/) | 2013 | Early-phase study | Pulm Pharmacol Ther | Vilanterol well tolerated in healthy subjects, with prolonged bronchodilation in asthma and COPD |

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02444186 | BREO ELLIPTA | Not listed | Not listed |
| 02408872 | BREO ELLIPTA | Not listed | Not listed |
| 02418401 | ANORO ELLIPTA | Not listed | Not listed |
| 02474522 | TRELEGY ELLIPTA | Not listed | Not listed |
| 02515776 | TRELEGY ELLIPTA | Not listed | Not listed |

---

## Safety Considerations

**Drug Interactions**: The interaction screen returned 100 interacting drugs. The main ones in the data compiled for this report are:
- **Moderate**: antidiabetic agents (acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin), QT-relevant drugs (cisapride, clarithromycin, dolasetron), and sympathomimetics (diethylpropion, ephedrine, epinephrine).
- **Minor**: corticosteroids (beclomethasone, betamethasone, budesonide, dexamethasone).

Package insert warnings and contraindications are not available in the compiled data. Please refer to the package insert for them.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 RCTs and large pivotal trials (IMPACT, FULFIL, CAPTAIN) support vilanterol-containing regimens in COPD and asthma, and the drug is already marketed in Canada. This is mainly a confirmation of existing use, not a new indication, and most evidence comes from fixed-dose combinations, not vilanterol alone. The other predicted indications have no supporting evidence and should stay on Hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Health Canada, which are currently missing and block formal safety screening
- Mechanism of action data from DrugBank
- Approved indication text and dosage forms for the five Canadian licences
- Clarification of which product-specific indications vilanterol already covers, so any true new-indication opportunity can be separated from existing use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

