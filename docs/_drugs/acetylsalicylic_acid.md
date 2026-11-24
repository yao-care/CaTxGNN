---
layout: default
title: Acetylsalicylic Acid
parent: Model Prediction Only (L5)
nav_order: 21
evidence_level: L5
indication_count: 7
monitor_inn: "ACETYLSALICYLIC ACID"
predicted_indications: ["atrophoderma vermiculata", "ulerythema ophryogenesis", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "trigeminal autonomic cephalalgia", "thrombophilia"]
last_modified_at: 2026-11-24
description: "Acetylsalicylic Acid: predicted new indication atrophoderma vermiculata (evidence level L5). In Canada: at least 20 DINs"
---

# Acetylsalicylic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Acetylsalicylic Acid: cyclooxygenase inhibitor (NSAID, antiplatelet) → atrophoderma vermiculata
{: .text-alpha }

## One-Sentence Summary

Acetylsalicylic acid (aspirin) is a long-established cyclooxygenase-inhibiting anti-inflammatory and antiplatelet drug marketed in Canada.
The TxGNN model predicts it may be relevant to **atrophoderma vermiculata**, with a prediction score of 0.9959.
**No clinical trials and no publications** were found to support this prediction, so it rests on the computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | atrophoderma vermiculata |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs on record: at least 20) |
| Number of DINs | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for aspirin and extended - release dipyridamole (a combination product containing acetylsalicylic acid): "Aspirin Aspirin inhibits platelet aggregation by irreversible inhibition of platelet cyclooxygenase and thus inhibits the generation of thromboxane A 2, a powerful inducer of platelet aggregation and vasoconstriction." ([DailyMed: Aspirin And Extended - Release Dipyridamole Capsules, 25 Mg / 200 Mg (aspirin and extended - release dipyridamole) prescribing information, Major Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6e652e1-b2e4-47ba-bed2-c5e902f8b8f1), label version 2026-08-19; accessed 2026-11-19.) Aspirin is generally known to irreversibly inhibit cyclooxygenase enzymes, which reduces prostaglandin and thromboxane production. This gives it anti-inflammatory, analgesic and antiplatelet effects.

Atrophoderma vermiculata is a rare follicular atrophic skin condition. The data compiled for this report shows no clear mechanistic link between aspirin's known pharmacology and this disease. The high score is a computational network-based prediction only. Without trials, literature or a plausible mechanism, it should be treated as a hypothesis, not as a supported repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Canada Market Information

Health Canada records list 20 valid single-ingredient licences for aspirin products, and the records may be partial. The local data does not record dosage forms or approved-indication text for these licences, so the approved indication is not recorded in the local data.

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 00530336 | ASA 325MG | ACETYLSALICYLIC ACID | Marketed |
| 02009013 | ASAPHEN | ACETYLSALICYLIC ACID | Marketed |
| 02150328 | ASPIRIN REGULAR STRENGTH | ACETYLSALICYLIC ACID | Marketed |
| 02202352 | RIVASA 80MG CROQUABLE - TAB | ACETYLSALICYLIC ACID | Marketed |
| 02202360 | RIVASA FC | ACETYLSALICYLIC ACID | Marketed |
| 02238545 | ASAPHEN E.C. 80 MG | ACETYLSALICYLIC ACID | Marketed |
| 02242281 | ENTROPHEN | ACETYLSALICYLIC ACID | Marketed |
| 02243974 | ENTROPHEN CHEWABLE | ACETYLSALICYLIC ACID | Marketed |
| 02244993 | ASA 81 MG | ACETYLSALICYLIC ACID | Marketed |
| 02283700 | PRAXIS ASA EC 81 MG DAILY LOW DOSE | ACETYLSALICYLIC ACID | Marketed |
| 02283905 | JAMP-ASA EC | ACETYLSALICYLIC ACID | Marketed |
| 02311496 | PRO-AAS EC - 80 | ACETYLSALICYLIC ACID | Marketed |
| 02311518 | PRO-AAS - 80 (CROQUABLE) | ACETYLSALICYLIC ACID | Marketed |
| 02363127 | ENTERIC COATED DAILY LOW DOSE ASA 81 MG | ACETYLSALICYLIC ACID | Marketed |
| 02372177 | ASA 81 MG | ACETYLSALICYLIC ACID | Marketed |
| 02420279 | RIVASA 81 MG EC | ACETYLSALICYLIC ACID | Marketed |
| 02427206 | JAMP-ASA 81MG EC | ACETYLSALICYLIC ACID | Marketed |
| 02429950 | M-ASA 80 MG CROQUABLE | ACETYLSALICYLIC ACID | Marketed |
| 02433044 | ASA | ACETYLSALICYLIC ACID | Marketed |
| 02485222 | RIVASA 80 MG EC | ACETYLSALICYLIC ACID | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

The data contain only part of the DINs for this ingredient; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screening. Examples rated **Major** include acalabrutinib, acetazolamide, ketorolac, trastuzumab emtansine, ibuprofen and fondaparinux. Examples rated Moderate include abciximab, nifedipine, hydrocortisone, ethanol, alendronic acid and fluvoxamine. These mostly reflect additive bleeding or gastrointestinal risk.

Please refer to the package insert for warnings and contraindications, as label-based safety text was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9959), but there are no clinical trials or publications for atrophoderma vermiculata and no plausible mechanistic link to aspirin. The evidence level is therefore L5, which does not justify further investment at this stage.

**To proceed, the following is needed:**
- Mechanism of action data and a testable biological rationale linking cyclooxygenase or platelet pathways to this condition
- A systematic literature search for case reports or preclinical studies in this disease
- Package insert warnings and contraindications from Health Canada for a safety review
- Dermatology expert review of whether the prediction is clinically meaningful

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Aspirin And Extended - Release Dipyridamole Capsules, 25 Mg / 200 Mg (aspirin and extended - release dipyridamole) prescribing information, Major Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a6e652e1-b2e4-47ba-bed2-c5e902f8b8f1) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

