---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Gefitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# GEFITINIB: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Gefitinib (Iressa®) is a first-generation, orally active EGFR tyrosine kinase inhibitor originally approved globally for the treatment of EGFR-mutation–positive non-small cell lung cancer (NSCLC), though it is currently not registered in Canada.
The TxGNN model's top prediction is **Gingival Fibromatosis**, ranking it first among 10 candidate indications with a prediction score of **99.89%**.
However, no clinical trials or published literature currently support this direction, placing the evidence at the lowest possible level (**L5 — model prediction only**).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-Small Cell Lung Cancer (NSCLC), EGFR mutation–positive — globally approved in multiple jurisdictions; not currently registered in Canada |
| Predicted New Indication | Fibromatosis, Gingival (Gingival Fibromatosis) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Automated retrieval of gefitinib's mechanism of action from the DrugBank pipeline was not successful for this report cycle. Based on the scientific literature retrieved across all 10 candidate indications, gefitinib is a selective, orally bioavailable small-molecule inhibitor that competitively occupies the ATP-binding pocket of the EGFR (ErbB1) intracellular tyrosine kinase domain. This blocks EGFR autophosphorylation and shuts down downstream pro-survival cascades — primarily RAS/MAPK and PI3K/AKT — thereby inhibiting tumor cell proliferation, promoting apoptosis, and suppressing angiogenesis. Clinically meaningful responses are restricted almost entirely to tumors harboring sensitizing EGFR mutations (Exon 19 deletions or L858R point mutations in Exon 21).

Gingival fibromatosis is characterized by progressive, benign overgrowth of gingival connective tissue driven by fibroblast hyperproliferation and excessive extracellular matrix deposition. EGFR signaling does participate in general fibroblast biology and wound healing, which provides a superficial rationale for TxGNN's inference. However, the established pathophysiology of gingival fibromatosis is either hereditary (autosomal dominant mutations predominantly in *SOS1*) or drug-induced by agents such as phenytoin, cyclosporine, and calcium channel blockers — none of which involve EGFR hyperactivation as a primary driver.

The most likely explanation for TxGNN's high score is non-specific inference from EGFR's broad expression in fibrotic tissue, rather than a disease-specific mechanistic link. An additional safety concern exists: gefitinib's known dermatologic toxicities (acneiform eruption, paronychia) reflect EGFR inhibition in normal epithelial tissue, and suppressing EGFR signaling in oral mucosal tissue could theoretically impair epithelial repair — potentially worsening rather than improving gingival pathology. Standard of care for gingival fibromatosis is surgical gingivectomy, not pharmacologic intervention.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for gefitinib in gingival fibromatosis.

---

## Literature Evidence

Currently no related literature available for gefitinib in gingival fibromatosis.

---

## Canada Market Information

Gefitinib is currently not registered or marketed in Canada. No Drug Identification Numbers (DINs) have been issued by Health Canada.

> **Note for context:** Gefitinib (Iressa®) holds regulatory approvals in multiple other jurisdictions — including Japan (PMDA, 2002), China (NMPA), and the European Union (EMA, 2009/reapproval 2014) — for EGFR mutation–positive NSCLC. The absence of Canadian registration reflects regulatory history rather than the global clinical evidence base.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — First-generation EGFR tyrosine kinase inhibitor (TKI); does not belong to conventional cytotoxic chemotherapy categories |
| Myelosuppression Risk | Low — Bone marrow suppression is not a primary toxicity of EGFR-TKIs; hematologic adverse events are infrequent and typically mild compared to cytotoxic agents |
| Emetogenicity Classification | Low — Oral targeted therapy; routine prophylactic antiemetics are generally not required per standard emetogenicity classification guidelines |
| Monitoring Items | Liver function tests (ALT, AST, total bilirubin) at baseline and periodically; pulmonary symptoms and chest imaging (ILD surveillance); 12-lead ECG / QTc interval monitoring; skin integrity assessment (acneiform rash, paronychia, xerosis); renal function in high-risk populations |
| Handling Protection | Applies — As an oral anticancer agent, gefitinib requires cytotoxic drug handling precautions for dispensing, preparation, and disposal per institutional pharmacy and regulatory safety protocols |

---

## Safety Considerations

Formal warning and contraindication data from the Health Canada prescribing label were not available in this evidence pack. The following is derived from the scientific literature retrieved across candidate indications:

- **Notable Adverse Effects (literature-derived):**
  - *Dermatologic:* Acneiform eruption, paronychia, and xerosis are the most frequent adverse effects, occurring in >50% of patients receiving EGFR inhibitors (PMID 18931563). These reflect on-target inhibition of EGFR in normal skin and nail epithelium.
  - *Pulmonary:* Interstitial lung disease (ILD) is a rare but potentially fatal complication; requires immediate drug discontinuation if suspected (PMID 22076388).
  - *Cardiac:* QT interval prolongation via hERG channel blockade has been documented in pharmacological studies and clinical observations (PMID 34474028, PMID 37258113). Risk is increased with concomitant QT-prolonging agents.
  - *Cardiovascular:* Isolated case reports of recurrent myocardial infarction have been published (PMID 21184253); platelet activation potentiation has been proposed as a mechanism.

- **Pharmacokinetic Interactions (literature-derived):** Gefitinib is extensively metabolized by CYP3A4 and CYP2D6, and is a substrate of efflux transporters ABCB1 (P-gp) and ABCG2. Genetic polymorphisms in these pathways contribute to clinically significant inter-individual variability in exposure, efficacy, and adverse event profiles (PMID 41199076). Strong CYP3A4 inducers or inhibitors are expected to alter drug exposure substantially.

Please refer to the prescribing information (package insert) for complete contraindications, drug interactions, and special population warnings, as these were not retrievable from the automated data pipeline for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite TxGNN assigning a 99.89% prediction score to gingival fibromatosis, the biological plausibility is low — the condition is driven by genetic or drug-induced mechanisms with no established EGFR pathology — and the complete absence of clinical trials or literature evidence (L5) means there is no empirical foundation to advance this hypothesis. Furthermore, potential on-target toxicity to oral epithelium raises a preclinical safety flag that must be addressed before any translational work begins.

**To proceed, the following is needed:**

- Preclinical mechanistic studies to determine whether EGFR is causally involved in gingival fibroblast hyperproliferation in fibromatosis (immunohistochemistry of biopsy samples, in vitro gefitinib inhibition assays on gingival fibroblast cell lines)
- Assessment of whether EGFR inhibition in oral mucosa tissue could impair epithelial barrier integrity and worsen gingival pathology (safety signal clarification)
- Formal retrieval of Health Canada / TFDA prescribing label for complete contraindication and warning data before any clinical feasibility discussion
- Cross-referencing with higher-evidence lung cancer predictions in this same pack (Rank 5: Lung Hilum Carcinoma, L4; Rank 8: Pulmonary Sulcus Neoplasm, L4; Rank 9: Lung Germ Cell Tumor, L4) which represent mechanistically plausible directions tied to gefitinib's known EGFR-NSCLC biology and may offer a more productive repurposing path
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

