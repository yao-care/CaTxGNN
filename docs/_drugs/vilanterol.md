---
layout: default
title: Vilanterol
parent: High Evidence (L1-L2)
nav_order: 967
evidence_level: L1
indication_count: 10
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

# Vilanterol: From COPD and Asthma Maintenance Therapy to Obstructive Lung Disease

## One-Sentence Summary

Vilanterol is a once-daily long-acting beta2-agonist (LABA) marketed in Canada only inside combination inhalers (Breo Ellipta, Anoro Ellipta, Trelegy Ellipta).
The TxGNN model predicts it may be effective for **obstructive lung disease**, with **50 clinical trials** and **20 publications** linked to this prediction.
This is closer to a label-concordant use than a true repurposing: the trials show COPD and asthma are already the drug's established uses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the licence data. Marketed products and trials indicate COPD and asthma maintenance therapy |
| Predicted New Indication | Obstructive lung disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 5 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Vilanterol is known to be a long-acting beta2-adrenoceptor agonist. It relaxes airway smooth muscle and gives sustained bronchodilation, so it fits airflow obstruction in COPD and asthma directly.

The licence records contain no approved-indication text. The linked trials nevertheless show the drug being studied as a component of fluticasone furoate/vilanterol, umeclidinium/vilanterol, and fluticasone furoate/umeclidinium/vilanterol. These are the same combinations sold as Breo, Anoro and Trelegy Ellipta. The model's prediction therefore largely reflects an existing use rather than a new one.

Before this is presented as a repurposing candidate, the missing original-indication data should be fixed.

---

## Clinical Trial Evidence

Fifty trials are linked to this prediction. The table shows the 10 most relevant. All are vilanterol-containing combination regimens, not vilanterol alone.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01134042](https://clinicaltrials.gov/study/NCT01134042) | Phase 3 | Completed | 587 | Fluticasone furoate/vilanterol vs fluticasone furoate alone vs fluticasone propionate alone in persistent asthma, 24 weeks |
| [NCT01706198](https://clinicaltrials.gov/study/NCT01706198) | Phase 3 | Completed | 4,233 | 12-month open-label effectiveness study of fluticasone furoate/vilanterol vs usual maintenance therapy in asthma |
| [NCT01686633](https://clinicaltrials.gov/study/NCT01686633) | Phase 3 | Completed | 1,040 | Double-blind comparison of two fluticasone furoate/vilanterol doses vs fluticasone furoate alone in persistent asthma, 12 weeks |
| [NCT01376245](https://clinicaltrials.gov/study/NCT01376245) | Phase 3 | Completed | 646 | 24-week placebo-controlled efficacy and safety of fluticasone furoate/vilanterol in Asian COPD patients |
| [NCT02119286](https://clinicaltrials.gov/study/NCT02119286) | Phase 3 | Completed | 620 | Adding umeclidinium to fluticasone furoate/vilanterol in COPD. The incremental effect is attributed to umeclidinium |
| [NCT01313676](https://clinicaltrials.gov/study/NCT01313676) | Phase 3 | Completed | 16,568 | Survival outcomes study of fluticasone furoate/vilanterol vs placebo in moderate COPD with cardiovascular disease or elevated risk |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | Completed | 1,811 | Once-daily triple therapy (FF/UMEC/VI) vs twice-daily budesonide/formoterol in COPD, 24 weeks |
| [NCT02924688](https://clinicaltrials.gov/study/NCT02924688) | Phase 3 | Completed | 2,436 | Triple therapy (FF/UMEC/VI) vs dual therapy (FF/VI) in inadequately controlled asthma |
| [NCT01551758](https://clinicaltrials.gov/study/NCT01551758) | Phase 3 | Completed | 2,802 | 12-month open-label effectiveness study of fluticasone furoate/vilanterol vs existing COPD maintenance therapy |
| [NCT03248128](https://clinicaltrials.gov/study/NCT03248128) | Phase 3 | Completed | 906 | Fluticasone furoate/vilanterol vs fluticasone furoate alone in children and adolescents aged 5–17 with uncontrolled asthma |

---

## Literature Evidence

Twenty publications are linked to this prediction. The table shows the 10 most relevant, with randomized trials first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | N Engl J Med | IMPACT: once-daily single-inhaler triple therapy vs dual therapy in COPD |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | Am J Respir Crit Care Med | FULFIL: once-daily triple therapy vs dual ICS/LABA therapy in COPD |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | Lancet Respir Med | CAPTAIN: Phase 3A trial of FF/UMEC/VI vs FF/VI in inadequately controlled asthma |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | Post hoc analysis of RCT | Am J Respir Crit Care Med | IMPACT showed lower all-cause mortality with FF/UMEC/VI vs UMEC/VI in COPD. This re-analysis added vital status data for patients censored in the original analysis |
| [31281061](https://pubmed.ncbi.nlm.nih.gov/31281061/) | 2019 | Post hoc RCT analysis | Lancet Respir Med | Modelled the relationship between blood eosinophil counts, smoking status and treatment response in IMPACT |
| [32299860](https://pubmed.ncbi.nlm.nih.gov/32299860/) | 2020 | Post hoc RCT analysis | Eur Respir J | Subgroup analysis of IMPACT by prior exacerbation history |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic review and meta-analysis | BMC Pulm Med | Umeclidinium/vilanterol compared with other bronchodilators in COPD |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Network meta-analysis | Adv Ther | FF/UMEC/VI compared with other triple and dual therapies in COPD |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohort | BMJ | Real-world comparison of two single-inhaler triple therapies (budesonide-glycopyrrolate-formoterol vs fluticasone-umeclidinium-vilanterol) in COPD |
| [37213116](https://pubmed.ncbi.nlm.nih.gov/37213116/) | 2023 | Cohort | JAMA Intern Med | COPD exacerbations and pneumonia hospitalizations among new users of combination maintenance inhalers |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2444186 | BREO ELLIPTA |
| 2408872 | BREO ELLIPTA |
| 2418401 | ANORO ELLIPTA |
| 2474522 | TRELEGY ELLIPTA |
| 2515776 | TRELEGY ELLIPTA |

Dosage form and approved-indication text are not recorded for these licences.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials, including large randomized studies, support vilanterol-containing combinations in COPD and asthma, and the products are already marketed in Canada. The evidence is strong, but it largely confirms an existing use. The package-insert safety data are also missing.

**To proceed, the following is needed:**
- Original-indication data, so the candidate can be framed correctly as label-concordant or genuinely new
- Health Canada package insert warnings and contraindications
- Detailed mechanism of action data
- Re-framing of the other nine predictions, which are on hold:
  - Compensatory emphysema, hyperlucent lung, interstitial emphysema, tracheal stenosis, congenital lobar emphysema, respiratory malformation, tracheal calcification and laryngotracheitis lack a bronchodilator rationale or any supporting evidence. The few linked trials are disease-mapping artifacts.
  - Bronchial neoplasm may be worth a narrower research question: COPD in lung cancer surgery candidates. Vilanterol has no antitumour mechanism.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

