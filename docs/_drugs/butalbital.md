---
layout: default
title: Butalbital
parent: Model Prediction Only (L5)
nav_order: 139
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-13
description: "Butalbital: predicted new indication Visual epilepsy (evidence level L5). Approved use: Not listed in the Canadian license data compiled for this report (but…"
monitor_inn: "BUTALBITAL"
predicted_indications: ["visual epilepsy", "micturation-induced seizures", "thinking seizures", "audiogenic seizures", "eating seizures", "startle epilepsy", "orgasm-induced seizures", "reading seizures"]
---

# Butalbital
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

# Butalbital: From Tension Headache to Visual Epilepsy

## One-Sentence Summary

Butalbital is a barbiturate marketed in Canada only in fixed-dose combination products, which are generally used for tension headache. The TxGNN model predicts it may be effective for **visual epilepsy**, but **no clinical trials** and only **5 publications** (none evaluating efficacy) are available. Most of these publications are case reports of withdrawal seizures, which are a safety signal rather than supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Canadian license data compiled for this report (butalbital combinations are generally used for tension headache) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 11 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Butalbital is a barbiturate. Barbiturates enhance the effect of GABA at GABA-A receptors, prolonging chloride channel opening and strengthening inhibitory neurotransmission. This is a plausible anticonvulsant mechanism, shared with phenobarbital. Detailed mechanism of action data for butalbital itself is not available in the data compiled for this report, so this reasoning relies on class-level knowledge.

The link between the original and predicted indications is weak. Butalbital is used in combination with acetaminophen or aspirin and caffeine (sometimes with codeine) for headache, and it has no established antiepileptic indication. The very high TxGNN score most likely reflects its similarity to anticonvulsant barbiturates rather than direct evidence. None of the retrieved literature evaluates butalbital as a treatment for visual (photosensitive) epilepsy.

The same model also predicts butalbital for seven other seizure types, all with scores of about 99%. These are micturition-induced seizures, thinking seizures, audiogenic seizures, eating seizures, startle epilepsy, orgasm-induced seizures and reading seizures. None has clinical trial support, and the literature is minimal or absent. The predictions therefore appear to be a class-level signal across rare reflex epilepsies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26565790](https://pubmed.ncbi.nlm.nih.gov/26565790/) | 2015 | Cohort | Ther Drug Monit | Therapeutic drug monitoring of pentobarbital (a different barbiturate), which is used for intractable seizures. Not about butalbital. |
| [8742687](https://pubmed.ncbi.nlm.nih.gov/8742687/) | 1996 | Case series | Headache | Three migraine patients with butalbital dependence developed grand mal seizures and behavioural disorder during withdrawal. |
| [15262744](https://pubmed.ncbi.nlm.nih.gov/15262744/) | 2004 | Case report | Arch Neurol | Barbiturate withdrawal after Internet purchase of Fioricet (a butalbital combination). |
| [10431323](https://pubmed.ncbi.nlm.nih.gov/10431323/) | 1999 | Case report | Schweiz Med Wochenschr | Intractable vomiting, convulsions and megaloblastic anaemia, where the medication history was the key to diagnosis. |
| [10349206](https://pubmed.ncbi.nlm.nih.gov/10349206/) | 1998 | Case report | Ann Ital Med Int | Barbiturate withdrawal syndrome (anxiety, insomnia, tremor, seizures, psychosis) linked to abuse of a headache medication. |

For the other predicted seizure types, the only additional publication was a 2021 case report of severe Fioricet withdrawal in an inpatient psychiatric unit ([34790421](https://pubmed.ncbi.nlm.nih.gov/34790421/)), which again describes harm rather than benefit.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 01971409 | TRIANAL TABLET | Not specified | Not specified |
| 00608238 | TEVA-TECNAL | Not specified | Not specified |
| 02554690 | APO-BUTALBITAL-ACETYLSALICYLIC ACID-CAFFEINE | Not specified | Not specified |
| 00608211 | TEVA-TECNAL | Not specified | Not specified |
| 00226327 | FIORINAL | Not specified | Not specified |

Six further valid products are also licensed. They include other TEVA-TECNAL C, FIORINAL-C and APO-BUTALBITAL-codeine combination strengths.

---

## Safety Considerations

- **Disease contraindications from the knowledge graph (not label text):** The TxGNN knowledge graph lists many conditions as contraindicated or cautioned with butalbital. They include:
  - Hepatic: liver failure, liver disease, hepatic coma and hepatic encephalopathy
  - Renal and metabolic: kidney disease, porphyria and other porphyrin metabolism disorders, hypothyroidism and gout
  - Respiratory and neurological: COPD, epilepsy and insomnia
  - Psychiatric: anxiety and neurotic disorders, and dysthymic disorder
  - Blood: thrombocytopenia, neutropenia and agranulocytosis
  - Cardiovascular: hypertension and hypotensive disorders
  - Gastrointestinal and urological: peptic ulcer disease, inflammatory bowel disease, gallbladder disease and benign prostatic hyperplasia
- **Dependence and withdrawal:** The retrieved case reports show that butalbital can cause tolerance and dependence. Abrupt discontinuation can cause withdrawal seizures, psychosis and, in severe cases, death. This is especially relevant for an anticonvulsant use.
- **Drug interactions:** The interaction screen returned 100 interactions in total. The main ones shown include:
  - **Major:** morphine (including liposomal morphine)
  - **Moderate:** corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, triamcinolone), doxycycline, metronidazole, bupropion, aprepitant, dronabinol, opium, canagliflozin and vitamin D analogues
  - **Minor:** pyridoxine

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN model alone (Evidence Level L5), with no clinical trials and no publications showing that butalbital treats visual epilepsy. The available literature documents seizures on withdrawal and dependence, which argues against repurposing. Better-established anticonvulsant barbiturates and other antiseizure drugs already exist.

**To proceed, the following is needed:**
- Health Canada product monograph warnings and contraindications, which are missing and block safety screening
- Detailed mechanism of action data, for example from DrugBank
- Preclinical or clinical evidence that butalbital suppresses photosensitive or other reflex seizures
- A risk-benefit analysis of dependence and withdrawal seizures against existing antiseizure therapies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

