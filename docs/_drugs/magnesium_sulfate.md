---
layout: default
title: Magnesium Sulfate
parent: Model Prediction Only (L5)
nav_order: 566
evidence_level: L5
indication_count: 10
---

# Magnesium Sulfate
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

# Magnesium Sulfate: From Established Injectable Magnesium Therapy to Preeclampsia/Eclampsia

## One-Sentence Summary

Magnesium sulfate is an injectable magnesium salt marketed in Canada under 8 licences, but the evidence pack contains no product-level approved indication text.
The TxGNN model predicts it may be effective for **preeclampsia/eclampsia**, and this is already its standard-of-care use in obstetrics.
The prediction is supported by **50 linked clinical trials** and **20 publications**, and most of the trials compare dosing regimens rather than test new efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Preeclampsia/eclampsia |
| TxGNN Prediction Score | 99.999% (model rank 50) |
| Evidence Level | L1 (see note below) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 8 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* L1 rests mainly on the Magpie Trial (a large placebo-controlled RCT) and Cochrane reviews, which the pack files under the near-synonym entry "toxemia of pregnancy". Most trials listed under this indication are Phase N/A or Phase 4 regimen, duration or dose comparisons.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the drug record. The mechanism below comes from the evidence pack's repurposing analysis. Magnesium acts as an NMDA receptor antagonist and a calcium channel blocker, and it promotes cerebral vasodilation. Together these effects raise the seizure threshold and reduce cerebral vasospasm, which is thought to play a role in eclampsia.

Parenteral magnesium sulfate is described in the literature as the drug of choice for preventing and treating eclamptic seizures. The empty original-indication field in the input is a data gap, not evidence against the use. This prediction therefore mostly confirms an established practice rather than pointing to a new one.

The linked trials mainly ask how best to give the drug. They cover 12-hour versus 24-hour postpartum duration, infusion rate, dosing in obesity, and delivery devices such as the Springfusor pump. They do not ask whether it works.

---

## Clinical Trial Evidence

Ten of the 50 linked trials are shown. The pack provides trial designs but no results, so the key-findings column describes what each trial tests.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06791668](https://clinicaltrials.gov/study/NCT06791668) | N/A | Recruiting | 400 | Observational (retrospective cohort) comparison of magnesium sulphate regimens in severe preeclampsia |
| [NCT03549767](https://clinicaltrials.gov/study/NCT03549767) | NA | Unknown | 241 | Randomized comparison of Springfusor pump versus standard administration in preeclampsia/eclampsia |
| [NCT03112551](https://clinicaltrials.gov/study/NCT03112551) | NA | Unknown | 100 | 12-hour versus 24-hour magnesium sulphate for eclampsia in a low-resource setting (Sudan) |
| [NCT04576364](https://clinicaltrials.gov/study/NCT04576364) | NA | Completed | 280 | RCT of 12-hour versus 24-hour postpartum magnesium sulphate in severe preeclampsia |
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | Completed | 280 | 6 hours versus 24 hours postpartum magnesium sulfate when less than 8 hours were given before delivery |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | NA | Completed | 2000 | Nimodipine versus magnesium sulfate for preventing eclamptic seizures in severe preeclampsia |
| [NCT02396030](https://clinicaltrials.gov/study/NCT02396030) | Phase 4 | Terminated | 62 | Maintenance dose of 1 g/h versus 2 g/h for eclampsia prevention |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | Unknown | 100 | Continuing versus stopping magnesium sulfate after delivery in severe preeclampsia |
| [NCT01408979](https://clinicaltrials.gov/study/NCT01408979) | Phase 4 | Completed | 120 | Short-course postpartum magnesium sulfate prophylaxis in severe preeclampsia |
| [NCT02091401](https://clinicaltrials.gov/study/NCT02091401) | Phase 4 | Completed | 200 | Repeat-bolus Springfusor regimen versus continuous IV regimen, with serum magnesium concentrations |

---

## Literature Evidence

Ten of the 20 linked publications are shown. Randomized trials are listed first, then reviews and other work.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38865319](https://pubmed.ncbi.nlm.nih.gov/38865319/) | 2024 | RCT | PLoS One | Acceptability of the Springfusor pump versus standard care, to avoid painful repeated intramuscular injections |
| [12576241](https://pubmed.ncbi.nlm.nih.gov/12576241/) | 2003 | RCT | Obstet Gynecol | Tested whether magnesium sulfate prevents disease progression in women with mild preeclampsia |
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstet Gynecol | Efficacy, benefits and risks of magnesium sulfate seizure prophylaxis |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | Am J Obstet Gynecol | Describes magnesium sulfate as the ideal anticonvulsant, with efficacy and safety documented over 60 years |
| [2672428](https://pubmed.ncbi.nlm.nih.gov/2672428/) | 1989 | Review | Stroke | Proposes that magnesium counters calcium-dependent arterial constriction and cerebral vasospasm |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstet Gynecol Surv | Cerebral hemodynamics in preeclampsia and the rationale for an alternative to magnesium sulfate |
| [1566765](https://pubmed.ncbi.nlm.nih.gov/1566765/) | 1992 | Preclinical | Am J Obstet Gynecol | Tests whether magnesium sulfate has central anticonvulsant effects on hippocampal seizures |
| [36413336](https://pubmed.ncbi.nlm.nih.gov/36413336/) | 2023 | Observational | Biol Trace Elem Res | Incidence of critical hypermagnesemia and its risk factors in severe preeclampsia |
| [31527059](https://pubmed.ncbi.nlm.nih.gov/31527059/) | 2019 | Implementation report | Glob Health Sci Pract | Magnesium sulfate alone cannot cut maternal mortality without a functioning health system |
| [25353716](https://pubmed.ncbi.nlm.nih.gov/25353716/) | 2015 | Review | Acta Obstet Gynecol Scand | Interventions to reduce preeclampsia/eclampsia deaths in sub-Saharan Africa |

The pivotal Magpie Trial ([PMID 12057549](https://pubmed.ncbi.nlm.nih.gov/12057549/), *Lancet*, 2002) and a Cochrane review ([PMID 21069663](https://pubmed.ncbi.nlm.nih.gov/21069663/), 2010) appear under the related "toxemia of pregnancy" entry. They support the efficacy case for this indication as well.

---

## Canada Market Information

The pack lists 8 licences and gives details for 5. Dosage form and approved-indication text are blank in the data.

| DIN | Product Name |
|---------|------|
| 2139499 | Magnesium Sulfate Injection, USP |
| 2513161 | Magnesium Sulfate Injection, BP 49.3% |
| 2542153 | Magnesium Sulfate in Water for Injection |
| 392618 | Magnesium Sulfate Injection USP |
| 800007 | TIS-U-SOL Solution |

---

## Safety Considerations

No warnings, contraindications or drug-interaction data were found for this drug (the interaction query returned no results). Please refer to the Health Canada package insert for safety information.

The evidence pack's repurposing analysis and the linked literature suggest these practical safeguards:
- Monitor serum magnesium, reflexes, respiratory rate and urine output.
- Keep calcium gluconate available.
- Adjust the dose in renal impairment.
- Watch for hypermagnesemia. One study (PMID 36413336) examined its incidence and risk factors in severe preeclampsia.
- Consider postpartum duration (12 h versus 24 h) and signals of obstetric hemorrhage risk (PMID 35704050).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Magnesium sulfate is already the standard seizure-prophylaxis agent in preeclampsia/eclampsia, backed by the Magpie RCT and Cochrane reviews. The remaining questions are about dosing, duration and safe administration rather than efficacy. Safety data for the Canadian products are missing, so use should stay under structured monitoring.

**To proceed, the following is needed:**
- The Health Canada package insert warnings and contraindications. This is currently a blocking gap.
- Mechanism-of-action data from DrugBank.
- The approved indication text for each Canadian DIN, to confirm whether obstetric use is already on-label.
- A defined monitoring and dosing protocol covering renal impairment, obesity, and 12-hour versus 24-hour postpartum duration.

*This report is for research reference only and is not medical advice. Repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

