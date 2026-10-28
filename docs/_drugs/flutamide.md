---
layout: default
title: Flutamide
parent: Model Prediction Only (L5)
nav_order: 404
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "FLUTAMIDE"
predicted_indications: ["fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "benign prostate phyllodes tumor", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
description: "Flutamide: predicted new indication Fibroma of prostate (evidence level L5). Approved use: Not recorded in the local data"
---

# Flutamide
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

## Flutamide: Fibroma of prostate
{: .text-alpha }

## One-Sentence Summary

Flutamide is an androgen receptor antagonist originally used to treat prostate cancer.
The TxGNN model's top-ranked prediction is a prostate cancer/brain cancer susceptibility label, which largely overlaps with the original indication, so this report focuses on the **benign reproductive system neoplasm** prediction, the highest-ranked entry with a distinct body of supporting literature (**14 publications**, **0 clinical trials**).
Evidence for this direction is limited to small, older, mostly non-randomized or preclinical studies, so it should be treated as a research question rather than an established opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Fibroma of prostate |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Canada Market Status | Marketed (valid licenses: 1 of 1) |
| Number of DINs | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, flutamide is a non-steroidal androgen receptor (AR) antagonist. Its efficacy in prostate cancer is established, including combined androgen blockade with LHRH agonists, and mechanistically it may be applicable to other androgen-sensitive tissues.

Androgen signalling drives the growth of benign prostatic tissue as well as prostate cancer. The retrieved literature includes a small study of flutamide in men with benign prostatic hyperplasia (BPH), examining prostate volume, PSA and testosterone response (PMID 1722793). Other studies describe the histological effects of combined endocrine therapy on normal and benign prostate (PMID 1989458, 11829828).

Several high-scoring predictions (Brenner tumor, rare prostatic stromal tumors, HIV and related animal retroviral diseases) have no trials or literature and no clear mechanistic rationale. Fibroma of prostate, prostate leiomyoma and benign prostate phyllodes tumor are at best biologically conceivable. The benign-neoplasm entry is the one with the most relevant supporting data, but it is limited to BPH-type effects and does not establish clinical benefit across the broad category.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the benign reproductive system neoplasm prediction.

For context, a related category, male reproductive organ cancer, is dominated by prostate cancer, the existing approved indication. Examples include:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006214](https://clinicaltrials.gov/study/NCT00006214) | Phase 2 | Completed | 63 | Flutamide as chemoprevention in men with prostatic intraepithelial neoplasia |
| [NCT00003645](https://clinicaltrials.gov/study/NCT00003645) | Phase 3 | Terminated | 64 | Adjuvant leuprolide plus flutamide in high-risk surgically treated prostate cancer |
| [NCT00002855](https://clinicaltrials.gov/study/NCT00002855) | Phase 3 | Completed | 306 | Androgen ablation alone versus chemo/hormonal therapy in metastatic prostate cancer |
| [NCT00003026](https://clinicaltrials.gov/study/NCT00003026) | Phase 3 | Completed | 966 | Long-term adjuvant LHRH analogue in locally advanced prostate cancer after radiotherapy and combined androgen blockade |
| [NCT00936390](https://clinicaltrials.gov/study/NCT00936390) | Phase 3 | Completed | 1538 | Dose-escalated radiotherapy with or without short-term androgen deprivation |
| [NCT02918968](https://clinicaltrials.gov/study/NCT02918968) | Phase 4 | Completed | 206 | Enzalutamide versus flutamide in castration-resistant prostate cancer after failing bicalutamide-based combined androgen blockade |
| [NCT06601205](https://clinicaltrials.gov/study/NCT06601205) | Phase 2/3 | Completed | 125 | Pre-surgical trial of finasteride versus low-dose flutamide versus placebo in prostate cancer |
| [NCT00450463](https://clinicaltrials.gov/study/NCT00450463) | Phase 2 | Completed | 64 | PROSTVAC vaccine plus flutamide versus flutamide alone in non-metastatic androgen-insensitive prostate cancer |

These trials reflect the approved prostate cancer indication, not new repurposing. Many test androgen deprivation in general, so attribution to flutamide specifically is uncertain.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1722793](https://pubmed.ncbi.nlm.nih.gov/1722793/) | 1991 | Clinical study | J Androl | Prostate volume, PSA and testosterone response to flutamide in men with BPH (double-blind randomized trial setting, 750 mg/day for 6 months) |
| [1989458](https://pubmed.ncbi.nlm.nih.gov/1989458/) | 1991 | Clinical/histopathology | Am J Surg Pathol | LHRH agonist plus flutamide caused marked atrophy and basal-cell hyperplasia in benign prostate (23 prostatectomies) |
| [10209490](https://pubmed.ncbi.nlm.nih.gov/10209490/) | 1998 | Histopathology | J Pathol | Cycling of benign prostatic epithelial cells during long-term combined androgen blockade |
| [11829828](https://pubmed.ncbi.nlm.nih.gov/11829828/) | 1999 | Clinical/histopathology | Zhonghua Wai Ke Za Zhi | Effect of combined endocrine therapy on normal prostate, BPH, adenocarcinoma and testis |
| [8146068](https://pubmed.ncbi.nlm.nih.gov/8146068/) | 1994 | Preclinical | Prostate | Early flutamide exposure delayed tumour appearance and growth in a rat prostatic tumour model |
| [12855748](https://pubmed.ncbi.nlm.nih.gov/12855748/) | 2003 | Review | Mol Endocrinol | Sex steroid receptor signalling in gonadal tumorigenesis |
| [17128417](https://pubmed.ncbi.nlm.nih.gov/17128417/) | 2007 | Review | Histol Histopathol | Histological changes induced by hormonal and other therapies in benign prostate and adenocarcinoma |
| [26926093](https://pubmed.ncbi.nlm.nih.gov/26926093/) | 2016 | Review | Pharmacol Res | Androgen biotransformation and the androgen, AR and UGT regulatory network in prostate cancer |
| [7526970](https://pubmed.ncbi.nlm.nih.gov/7526970/) | 1994 | Cohort/histopathology | Cancer | Morphologic changes after preoperative estramustine or flutamide in localized prostate cancer |
| [24615730](https://pubmed.ncbi.nlm.nih.gov/24615730/) | 2014 | Preclinical | Prostate | Carboxypeptidase-D in prostate cancer; effect abolished by combined androgen and prolactin receptor targeting |

The evidence is small, old and largely histological or preclinical. No randomized efficacy outcomes in benign reproductive tumours were identified.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02238560 | FLUTAMIDE | Not specified | Not specified |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (non-steroidal androgen receptor antagonist), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function, given the hepatotoxicity concern noted below; other parameters per the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Key Warnings**: Flutamide carries a boxed hepatotoxicity warning (noted in the evidence assessment). Hepatotoxicity is a significant barrier to use in a benign condition. Newer antiandrogens such as bicalutamide and enzalutamide are largely preferred.
- **Contraindications (from the knowledge graph, not label text)**: liver failure, liver disease, gallbladder disease, methemoglobinemia, sulfhemoglobinemia, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, pyruvate dehydrogenase E3 deficiency, and methemoglobinemia due to methemoglobin reductase deficiency.
- **Drug Interactions**: 100 interactions are recorded. Examples include:
  - **Major**: dolasetron, cisapride
  - **Moderate**: clarithromycin, levofloxacin, ondansetron, palonosetron, naltrexone, famotidine, loperamide, obeticholic acid, and several laxatives and bowel-prep agents (bisacodyl, lactulose, lactitol, polyethylene glycol, sodium sulfate, castor oil, glycerin, picosulfuric acid)
  - **Minor**: metronidazole

Please also refer to the package insert, as Canadian label warnings and contraindications were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted benign reproductive system neoplasm indication has no linked clinical trials, and the supporting literature is small, dated and mostly histological or preclinical. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Flutamide's hepatotoxicity makes use in a benign condition hard to justify when safer alternatives exist.

**To proceed, the following is needed:**
- Health Canada package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Controlled clinical evidence of benefit in a specific benign androgen-sensitive condition (such as BPH), with a defined benefit-risk comparison against current standard therapy
- A hepatotoxicity monitoring and risk-mitigation plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

