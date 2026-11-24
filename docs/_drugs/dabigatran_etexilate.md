---
layout: default
title: Dabigatran Etexilate
parent: Model Prediction Only (L5)
nav_order: 240
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
description: "Dabigatran Etexilate: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not specified in the data compiled for this report"
monitor_inn: "DABIGATRAN ETEXILATE"
predicted_indications: ["sclerosing cholangitis", "obsolete familial combined hyperlipidemia", "hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "primary release disorder of platelets"]
---

# Dabigatran Etexilate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dabigatran Etexilate: From Anticoagulation to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Dabigatran etexilate is an oral direct thrombin inhibitor marketed in Canada as an anticoagulant. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but this rests on a computational score alone: **0 clinical trials** and **1 publication** are linked, and that publication concerns a different drug (cilofexor) and does not test dabigatran.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the data compiled for this report (the Canadian licence records contain no indication text) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (marketed DINs: 5 of 5) |
| Number of DINs | 5 (marketed: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dabigatran etexilate: "Dabigatran and its acyl glucuronides are competitive, direct thrombin inhibitors. Because thrombin (serine protease) enables the conversion of fibrinogen into fibrin during the coagulation cascade, its inhibition prevents the development of a thrombus." ([DailyMed: Dabigatran (dabigatran etexilate) prescribing information, AvPAK](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39ac558a-b375-f3c1-e063-6394a90aa901), label version 2026-11-02; accessed 2026-11-19.) From general pharmacology, dabigatran is a direct thrombin inhibitor. Thrombin and PAR signaling could plausibly contribute to liver inflammation and fibrosis, which is a possible bridge to sclerosing cholangitis. This is a hypothesis only and is not supported by the supplied evidence.

The only linked publication (PMID 36906733) is a drug-interaction pharmacokinetic study of cilofexor, an FXR agonist in development for sclerosing cholangitis. It says nothing about dabigatran's efficacy. The high score of 0.9982 should therefore be read as a model-derived association and not as confirmation.

Other predicted indications are weaker still. Familial hyperlipidaemia (an obsolete disease term), hypoalphalipoproteinemia and homozygous familial hypercholesterolemia have no plausible link to thrombin inhibition in the data. Primary release disorder of platelets is a bleeding-type disorder, where an anticoagulant would be expected to worsen the problem and not treat it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for sclerosing cholangitis.

For other predicted indications, one trial was returned (NCT07629999, hypoalphalipoproteinemia). It is a Phase 1 first-in-human study of a different investigational agent (BMS-986533) and is most likely a spurious match.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | Other (DDI / pharmacokinetic evaluation) | Clinical Pharmacokinetics | Evaluates cytochrome P450 and transporter-mediated drug interaction potential of cilofexor, an FXR agonist in development for NASH and primary sclerosing cholangitis. It does not study dabigatran. |

---

## Canada Market Information

<!-- licenses:begin -->

| DIN | Product Name | Active Ingredients (DPD) | Status |
|------|------|------|------|
| 02312441 | PRADAXA | DABIGATRAN ETEXILATE (DABIGATRAN ETEXILATE MESILATE) | Marketed |
| 02358808 | PRADAXA | DABIGATRAN ETEXILATE (DABIGATRAN ETEXILATE MESILATE) | Marketed |
| 02468891 | APO-DABIGATRAN | DABIGATRAN ETEXILATE (DABIGATRAN ETEXILATE MESILATE) | Marketed |
| 02468905 | APO-DABIGATRAN | DABIGATRAN ETEXILATE (DABIGATRAN ETEXILATE MESILATE) | Marketed |
| 02468913 | APO-DABIGATRAN | DABIGATRAN ETEXILATE (DABIGATRAN ETEXILATE MESILATE) | Marketed |

Source: Health Canada Drug Product Database (DPD); product names, active ingredients and status as recorded in the DPD, sorted by status and then by DIN.

<!-- licenses:end -->

All five licences are valid single-ingredient products.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): blood coagulation disease, anaemia, macrocytic anaemia and intracerebral haemorrhage. Bleeding risk is the central concern for any anticoagulant, so this applies directly to patients with liver disease, who often have impaired coagulation.

Please refer to the package insert for full warnings, contraindications and drug interactions. No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials for dabigatran in sclerosing cholangitis, and the single linked publication concerns a different drug. The evidence is model prediction with a speculative mechanism, and the bleeding-related safety profile adds caution.

**To proceed, the following is needed:**
- Health Canada package insert warnings, contraindications and approved indications (currently missing)
- Mechanism of action data (for example from DrugBank) and a documented link between thrombin signalling and cholestatic liver disease
- Preclinical evidence (for example thrombin/PAR inhibition in cholangiopathy models) or observational data on dabigatran use in patients with sclerosing cholangitis
- A bleeding-risk assessment in patients with hepatic impairment or portal hypertension before any clinical study is considered

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Dabigatran (dabigatran etexilate) prescribing information, AvPAK](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39ac558a-b375-f3c1-e063-6394a90aa901) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

