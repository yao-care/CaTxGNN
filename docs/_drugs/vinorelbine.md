---
layout: default
title: Vinorelbine
parent: Model Prediction Only (L5)
nav_order: 971
evidence_level: L5
indication_count: 10
---

# Vinorelbine
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

# Vinorelbine: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

Vinorelbine is a vinca alkaloid chemotherapy whose established use is in non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Ewing sarcoma**, with **4 clinical trials** and **5 publications** currently supporting this direction.
None of this evidence is Ewing-specific or randomized, so it is early-stage support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer (from the literature; the Canadian license records have no indication text) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L2 (per Evidence Pack; the supporting studies are single-arm Phase 2, not randomized) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on drug class, vinorelbine is a vinca alkaloid that binds tubulin, inhibits microtubule polymerization and causes mitotic arrest. Its efficacy in NSCLC is established, and mechanistically it may be applicable to Ewing sarcoma.

Ewing sarcoma is a rapidly dividing tumor, so it is plausibly sensitive to antimitotic agents. A preclinical study found synergistic apoptosis in Ewing sarcoma cells when a PLK1 inhibitor was combined with microtubule-interfering drugs, including vinorelbine. This supports the link, but it is laboratory work only.

The clinical evidence is thinner than the score suggests. The Phase 2 studies are single-arm, enrolled mixed pediatric solid tumors, and reported their clearest activity in rhabdomyosarcoma rather than Ewing sarcoma. Any use should be limited to a specialist-led, relapsed/refractory setting.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | Unknown | 210 | Vinorelbine + cyclophosphamide in refractory or relapsed tumors, including Ewing tumors, rhabdomyosarcoma, osteosarcoma, neuroblastoma and medulloblastoma. Status is unknown, so the data may be incomplete. |
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | Completed | 50 | Vinorelbine alone in children with recurrent or refractory malignancies. Includes sarcomas but is small and not Ewing-specific. |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | Recruiting | 105 | CAMPFIRE pediatric master protocol. Whether vinorelbine is in an Ewing-relevant arm needs confirmation. |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | N/A | Active, not recruiting | 100 | Prospective cohort of risk-stratified treatment in pediatric Ewing sarcoma in China. Informs real-world safety, with no controlled efficacy data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase 2 trial | Eur J Cancer | Vinorelbine plus continuous low-dose oral cyclophosphamide in children and young adults with relapsed or refractory solid tumors. Good tolerance, with efficacy in rhabdomyosarcoma. |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Phase 2 trial | Cancer | Vinorelbine in previously treated advanced childhood sarcomas. Activity was shown in rhabdomyosarcoma. |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Front Pharmacol | Review of chemotherapy drugs for soft tissue sarcomas. Context for sarcoma drug selection, not Ewing-specific. |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Preclinical | Int J Cancer | A PLK1 inhibitor combined with microtubule-interfering drugs, including vinorelbine, synergistically induced apoptosis in Ewing sarcoma cells. |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case report | BMC Urol | Extraosseous Ewing sarcoma of the kidney, focused on diagnosis. No vinorelbine efficacy data. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 2271214 | Vinorelbine Tartrate for Injection |
| 2511347 | Vinorelbine Injection, USP |
| 2431130 | Vinorelbine Injection, USP |

---

## Cytotoxicity

Vinorelbine is an antineoplastic. The entries below come from general drug-class knowledge, not from the Evidence Pack, and should be confirmed against the Health Canada monograph.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (vinca alkaloid, antimicrotubule agent) |
| Myelosuppression Risk | High (myelosuppression is the dose-limiting toxicity, per the literature) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential before each dose, liver function, infusion-site checks |
| Handling Protection | Must follow cytotoxic drug handling regulations; avoid extravasation (vesicant) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible and Phase 2 data show vinorelbine is feasible in pediatric relapsed or refractory sarcomas. However, the data are non-randomized, mixed-histology, and show clearer activity in rhabdomyosarcoma than in Ewing sarcoma. Use should stay within a specialist-led, relapsed/refractory research setting.

**To proceed, the following is needed:**
- Ewing-specific efficacy data, for example subgroup results from NCT00180947 and NCT00003234
- Confirmation of whether CAMPFIRE (NCT05999994) includes a vinorelbine arm in Ewing sarcoma
- Health Canada package insert warnings and contraindications
- Mechanism of action data from DrugBank
- A hematologic monitoring and dose-adjustment plan for pediatric and young-adult patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

