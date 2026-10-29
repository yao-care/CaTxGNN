---
layout: default
title: Ritonavir
parent: Model Prediction Only (L5)
nav_order: 816
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Ritonavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease / AIDS"
monitor_inn: "RITONAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Ritonavir: From HIV/AIDS and Hepatitis C to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Ritonavir is a protease inhibitor originally used to treat HIV infection/AIDS and chronic hepatitis C virus infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome** with a very high score, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
The prediction is best viewed as a model-level extension of the existing HIV indication rather than a new human therapeutic opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease / AIDS; chronic hepatitis C virus infection (the Canadian licence records provide no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 6 of 7) |
| Number of DINs | 7 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, ritonavir is an HIV protease inhibitor and a strong CYP3A4 inhibitor. It is used both as an antiviral and as a pharmacokinetic booster in combination products (for example, with lopinavir in Kaletra, and with nirmatrelvir in Paxlovid).

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV-1, and its protease is structurally similar. A protease inhibitor could therefore plausibly act on it. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as HIV/AIDS, which is already an original indication, not biological evidence.

Caution is needed. Protease susceptibility differs between species and viruses, so activity against FIV protease cannot be assumed. Feline AIDS is also a veterinary condition, so it is not a human repurposing target.

Two other predictions were reviewed:
- **Simian immunodeficiency virus infection** (score 0.9992, evidence level L4): ritonavir inhibited SIVmac239 in vitro with an EC50 of about 13 nM, compared with about 25 nM for HIV-1 (PMID 12709355). SIV is mainly a research model for HIV, so it has little independent clinical value.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9992, evidence level L5): no plausible mechanistic link is evident. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for feline AIDS. The table below lists the most relevant literature for the second-ranked prediction (simian immunodeficiency virus infection), which is indirect, non-human evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | SIVmac239 was inhibited by ritonavir (EC50 about 13 nM), indinavir and saquinavir at levels comparable to HIV-1 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antiviral Therapy | Susceptibility of HIV-2, SIV and SHIV to 16 approved anti-HIV-1 drugs, relevant to treatment and post-exposure prophylaxis |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal study | J Virol Methods | Oral HAART including lopinavir/ritonavir in SHIV-infected macaques, assessing the CD8 subset (2 animals) |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal study | PLoS Pathog | Highly intensified ART gave long-term viral suppression and a restricted reservoir in SIV-infected macaques |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study | J Virol | Rapid viral decay in SIV-infected macaques on quadruple antiretroviral therapy |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal study | mBio | Lentiviral infection persists in the brain despite effective ART |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal study | PLoS One | Suppressive cART plus the HDAC inhibitor SAHA in SIV-infected rhesus macaques |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal model | Microbes Infect | A novel SHIV carrying an HIV-1 protease gene, proposed as a tool for testing protease inhibitors in vivo |

Most of these studies involve combination regimens, and ritonavir-specific effects cannot always be confirmed from the data provided.

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02357593 | NORVIR | Not specified | Not specified |
| 02523620 | AURO-RITONAVIR | Not specified | Not specified |
| 02524031 | PAXLOVID | Not specified | Not specified |
| 02312301 | KALETRA | Not specified | Not specified |
| 02285533 | KALETRA | Not specified | Not specified |

Seven valid licences are on record (all single-ingredient entries); the five main ones are shown above.

## Safety Considerations

**Contraindication-related conditions (from the knowledge graph, not label text):**
The knowledge graph links ritonavir to the following groups of conditions. These should be confirmed against the official label.
- **Cardiac and rhythm:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, myocardial ischemia, coronary artery disease, cardiomyopathy (including hypertrophic), endomyocardial fibrosis
- **Liver and pancreas:** pancreatitis, liver disease, cirrhosis, gallbladder disease, chronic hepatitis B virus infection, hyperbilirubinemia (including hereditary and Gilbert syndrome)
- **Metabolic:** diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hypertriglyceridemia, familial combined hyperlipidemia, potassium deficiency, gout/hyperuricemia
- **Other:** hemophilia

**Drug Interactions:**
The interaction query returned 100 records. Examples from the first 20:
- **Major:** loperamide, triamcinolone, budesonide
- **Moderate:** acarbose, hydrocortisone, albiglutide, alogliptin, metformin, alosetron, bupropion, aprepitant, dexamethasone, lorcaserin, betamethasone, metronidazole, canagliflozin, chlorpropamide, clarithromycin

Several corticosteroid and antidiabetic drugs appear in these interactions. Ritonavir is a strong CYP3A4 inhibitor, so combined use needs careful review.

Please refer to the package insert for warnings and complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (feline AIDS) has no clinical trials or literature, and the high TxGNN score most likely reflects similarity to the existing HIV/AIDS indication. It is a veterinary condition, so it offers no new human repurposing opportunity.
- The neighbouring SIV prediction has only preclinical, indirect evidence. The third prediction has no plausible mechanistic link.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank) to support mechanistic analysis
- Health Canada package insert warnings and contraindications, which are currently missing and block safety screening
- Ritonavir-specific FIV protease inhibition or antiviral data, if the veterinary direction is of interest
- Approved indication text and dosage forms for the Canadian licences
- A decision on whether to pursue the human-relevant HIV/hepatitis C indications instead, since they are already established
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

