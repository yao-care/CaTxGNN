---
layout: default
title: Sirolimus
parent: High Evidence (L1-L2)
nav_order: 721
evidence_level: L2
indication_count: 10
---

# Sirolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Sirolimus: From Renal Transplant Rejection Prophylaxis to Liposarcoma

## One-Sentence Summary

Sirolimus is an mTOR inhibitor originally developed as an immunosuppressant for prophylaxis of renal transplant rejection. The TxGNN model predicts it may be effective for **liposarcoma**, with **5 clinical trials** and **13 publications** currently supporting this direction — though most direct trial evidence comes from sirolimus analogues (temsirolimus, ridaforolimus, everolimus) rather than sirolimus itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal transplant rejection prophylaxis (not captured in this Canada regulatory dataset — drug currently unmarketed in Canada; inferred from literature context on immunosuppressive use) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Canada Market Status | ✗ Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not directly available from DrugBank in this evidence pack. Based on the clinical and literature evidence collected, sirolimus is well established as an **mTOR (mechanistic target of rapamycin) inhibitor**, originally used as an immunosuppressant to prevent organ rejection after renal transplantation.

The predicted new indication, liposarcoma, is mechanistically supported by molecular evidence showing that the Akt-mTOR and MAPK signaling pathways are aberrantly activated in dedifferentiated liposarcoma specimens (PMID 26518767). Since mTOR is a central regulator of cell growth, survival, and proliferation, its hyperactivation is a recurring oncogenic driver across multiple soft-tissue sarcoma subtypes — providing a plausible biological rationale for repurposing an mTOR inhibitor into this tumour class.

Direct clinical support for sirolimus itself is limited to one completed Phase 2 trial combining sirolimus with cyclophosphamide in myxoid liposarcoma and chondrosarcoma (NCT02821507, n=70). The remaining trial and literature evidence largely involves sirolimus's close analogues within the "rapalogue" class (temsirolimus, ridaforolimus, everolimus), which share the same mTOR-inhibition mechanism and have been tested more extensively in advanced sarcoma populations. Notably, the same drug class shows even stronger, guideline-level evidence (L1, Phase 3 RCT) for a related mTOR-driven neoplasm — lymphangioleiomyomatosis — reinforcing the biological plausibility of mTOR inhibition in mesenchymal/neoplastic disease more broadly.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus + cyclophosphamide combination in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; based on preclinical evidence that mTOR inhibition prevents tumour growth |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | AP23573 (ridaforolimus, mTOR inhibitor) dosed 5 days/2 weeks in advanced sarcoma |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus (sirolimus prodrug) + liposomal doxorubicin in recurrent soft tissue/bone sarcoma; dose-finding and efficacy |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus (mTOR inhibitor) in advanced dedifferentiated liposarcoma and leiomyosarcoma |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + temsirolimus in pediatric recurrent/refractory sarcoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT | Clin Cancer Res | Phase 2 trial of ribociclib (CDK4 inhibitor) + everolimus (mTOR inhibitor) in dedifferentiated liposarcoma/leiomyosarcoma; synergistic growth inhibition |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Preclinical/Mechanistic | Tumour Biol | Akt-mTOR and MAPK pathway activation confirmed in 99 dedifferentiated liposarcoma specimens; in vitro mTOR inhibitor antitumor effect |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohort | J Am Soc Nephrol | Sirolimus after early cyclosporine withdrawal reduced malignancy risk in renal transplant recipients |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Review of novel therapeutics, including targeted/mTOR-pathway agents, in soft tissue sarcoma |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Review of rationale and trial results for molecular-targeted agents in advanced sarcomas |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Molecular subgroup classification and targeted treatment strategies for rare connective tissue tumours/sarcomas |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical | Cancer Genomics Proteomics | Combination of chloroquine + rapamycin (autophagy inhibition) effective against well-differentiated liposarcoma models |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Cohort | Transplant Proc | Cancer screening study evaluating immunosuppressive drug effects (including sirolimus) on malignancy development post-transplant |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical | In Vivo | Chloroquine + rapamycin arrests tumour growth in a patient-derived orthotopic xenograft model of dedifferentiated liposarcoma |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | MLN0128, a next-generation ATP-competitive mTOR kinase inhibitor, shows potent antitumor activity in bone/soft-tissue sarcoma models |

---

## Canada Market Information

Sirolimus is currently **not marketed** in Canada under this evidence pack's regulatory dataset (0 licenses/DINs on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: a blocking data gap has been identified — TFDA/Health Canada label warnings and contraindications for sirolimus have not yet been retrieved, which prevents a formal safety initial review. See Next Steps below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is a completed Phase 2 trial directly testing sirolimus in myxoid liposarcoma, supported by molecular evidence of Akt-mTOR pathway activation in this tumour type and multiple Phase 1/2 trials of pharmacologically related mTOR inhibitors (temsirolimus, ridaforolimus, everolimus) in advanced sarcoma populations. However, safety labeling data is entirely unavailable, and the drug is not currently marketed in Canada, so the recommendation is to proceed cautiously while critical data gaps are closed.

**To proceed, the following is needed:**
- TFDA/Health Canada product monograph, including warnings, contraindications, and precautions (currently a Blocking gap — required before S1 safety initial review can begin)
- Detailed mechanism-of-action documentation from DrugBank (High-severity gap)
- Confirmation of drug-drug interaction profile (current DDI query returned no results)
- If commercialization in Canada is being considered, a DIN application/regulatory pathway assessment, since the drug currently holds no Canadian market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

