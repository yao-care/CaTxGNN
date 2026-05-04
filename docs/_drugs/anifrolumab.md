---
layout: default
title: Anifrolumab
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Anifrolumab
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

# Anifrolumab: From Systemic Lupus Erythematosus to Diabetic Cataract

## One-Sentence Summary

Anifrolumab (Saphnelo) is a monoclonal antibody targeting the type I interferon receptor (IFNAR1), approved in multiple countries for the treatment of moderate-to-severe systemic lupus erythematosus (SLE). The TxGNN model predicts it may be effective for **diabetic cataract**, with a high model confidence score of **98.50%**. However, **no clinical trials and no supporting publications** have been identified for this indication, and the biological rationale linking IFNAR1 blockade to lens pathology remains speculative.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic lupus erythematosus (SLE) — not approved in Taiwan |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.50% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Anifrolumab works by blocking IFNAR1, the shared receptor subunit for all type I interferons (IFN-α, IFN-β, IFN-ω). By occupying IFNAR1, it prevents type I IFN signalling cascade activation, broadly suppressing interferon-stimulated gene expression. This mechanism has demonstrated clear benefit in SLE, where type I IFN overactivation drives systemic inflammation and tissue damage.

The proposed link to diabetic cataract is indirect. Type I interferons are known to participate in the pro-inflammatory microenvironment of diabetic microvascular complications, including lens oxidative stress pathways. Theoretically, dampening IFN signalling could reduce inflammatory contributors to lens glycation and oxidative injury. However, this pathway has not been experimentally validated in animal models of diabetic cataract, nor has any clinical signal been observed in SLE patients treated with anifrolumab.

It is most likely that the high TxGNN score arises from indirect graph connectivity: the knowledge graph contains well-documented nodes linking SLE to diabetes comorbidity, and diabetes to cataract, creating a plausible-looking but mechanistically weak path. The prediction should be interpreted as a hypothesis-generating signal, not as evidence of efficacy.

> **Note:** Detailed mechanism of action data was not available in the Evidence Pack. The mechanistic discussion above is derived from known pharmacology of anifrolumab as documented in published literature and the embedded rationale notes within this Evidence Pack.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Anifrolumab in diabetic cataract.

---

## Literature Evidence

Currently no related literature available for Anifrolumab in diabetic cataract.

> **Note for context:** A relevant safety review (PMID [41373894](https://pubmed.ncbi.nlm.nih.gov/41373894/)) was retrieved in a related query on cortical cataract. This 2025 review in *International Journal of Molecular Sciences* discusses ophthalmological safety considerations of SLE therapies including anifrolumab. It does **not** support efficacy in any cataract subtype — rather, it highlights that SLE patients face elevated ocular risk from both disease activity and corticosteroid use, suggesting a need for ophthalmological monitoring rather than a therapeutic opportunity.

---

## Taiwan Market Information

Anifrolumab is currently **not approved or marketed in Taiwan**. No Drug Identification Numbers (DINs) or product licenses are on record.

> For reference: Anifrolumab is approved as **Saphnelo** (AstraZeneca) in the United States (FDA, 2021), European Union (EMA, 2022), Japan (PMDA, 2021), and other jurisdictions for adult patients with moderate-to-severe SLE. A Taiwan NDA submission status was not confirmed in this Evidence Pack.

---

## Safety Considerations

Safety data specific to the Taiwan regulatory context was not available in this Evidence Pack.

Based on publicly available prescribing information for Saphnelo, clinicians should be aware of the following general safety considerations:

- **Serious Infections**: Anifrolumab suppresses interferon-mediated antiviral immunity. Risk of serious and opportunistic infections, including herpes zoster reactivation, is elevated. Vaccination (especially live vaccines) should be completed before initiation.
- **Malignancy**: As with other immunomodulatory agents, long-term immunosuppression carries a theoretical malignancy risk; monitoring is advised.
- **Hypersensitivity and Infusion Reactions**: Infusion-related reactions have been reported; pre-medication protocols should be followed.
- **Drug Interactions**: No interaction data was available in this Evidence Pack. Concomitant use with other immunosuppressants (e.g., high-dose corticosteroids, azathioprine, mycophenolate) warrants careful monitoring.

> Please refer to the full prescribing information (package insert) for comprehensive warnings, contraindications, and drug interaction data before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high confidence score (98.50%) to anifrolumab for diabetic cataract, but this is an **L5 evidence level** — meaning the signal is based entirely on computational model prediction with no supporting clinical trials, observational studies, or experimental data. The biological rationale is indirect and speculative, resting on multi-hop graph connections (SLE → inflammation → diabetes → cataract) rather than a direct mechanistic link between IFNAR1 blockade and lens pathology.

**To revisit this candidate, the following would be needed:**

- **Preclinical mechanistic studies**: Demonstrate that type I IFN signalling plays a functional role in lens epithelial cell apoptosis or oxidative stress in diabetic conditions (in vitro or animal models).
- **Epidemiological signal**: Analyse real-world data from SLE patients receiving anifrolumab to determine whether incidence of cataract (particularly diabetic cataract) differs from comparator populations.
- **Biomarker hypothesis**: Identify whether elevated IFN-α signature correlates with cataract progression in diabetic patients with concurrent autoimmune conditions.
- **MOA gap fill**: Obtain complete DrugBank pharmacology data for anifrolumab to enable formal mechanistic similarity scoring.
- **Taiwan regulatory pathway**: If evidence matures, assess Health Authority (TFDA) regulatory requirements for a new indication submission given the drug is currently unapproved in Taiwan.

Until preclinical or epidemiological evidence is established, investment in clinical development for this indication is not recommended.

---

*This report is generated for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

