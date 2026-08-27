---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole: From Anaerobic & Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is a well-established nitroimidazole antibiotic with proven activity against anaerobic bacteria and protozoa, including amebiasis, trichomoniasis, and bacterial vaginosis.
The TxGNN model assigns **Pneumocystosis** a prediction score of **99.99%**; however, this pairing has a clear mechanistic mismatch — Pneumocystis jirovecii is a fungus, and Metronidazole has no antifungal activity.
None of the 23 retrieved clinical trials and none of the 10 literature items support Metronidazole as a treatment for pneumocystosis; the high score almost certainly reflects co-occurrence bias within the HIV/AIDS knowledge graph.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anaerobic bacterial and protozoal infections (amebiasis, trichomoniasis, bacterial vaginosis, C. difficile) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Canada Market Status | Not Marketed (0 DINs found in query) |
| Number of DINs | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, Metronidazole is a nitroimidazole prodrug whose nitro group is selectively reduced by ferredoxin-type electron transport proteins. These proteins exist only in anaerobic organisms and certain protozoa. The resulting cytotoxic free radicals cause DNA strand breaks, killing the microorganism. This mechanism depends entirely on the target organism operating in a low-redox-potential, oxygen-poor environment.

Pneumocystis jirovecii — the causative pathogen of pneumocystosis — is a fungus. Fungi are aerobic organisms and completely lack ferredoxin-based electron carriers. There is therefore a fundamental and well-established mechanistic incompatibility: Metronidazole exerts zero antifungal activity. The standard first-line treatment for Pneumocystis pneumonia (PCP) is trimethoprim-sulfamethoxazole (TMP-SMX), which targets dihydropteroate synthase — an entirely different mechanism.

The TxGNN near-perfect score (0.9999) almost certainly reflects a knowledge graph artifact. HIV/AIDS patients frequently develop PCP alongside other infections that genuinely require Metronidazole — amoebiasis, Clostridium difficile colitis, or anaerobic co-infections. When these conditions co-cluster in the same patient cohort, the knowledge graph records statistical associations that the model may misinterpret as a direct drug–disease therapeutic relationship. This is a well-recognized limitation of co-occurrence-based graph models, and the retrieved clinical trials (all completely off-topic) and literature (all describing co-occurrence, not treatment) confirm this interpretation.

---

## Clinical Trial Evidence

All 23 clinical trials retrieved for the Metronidazole × Pneumocystosis query are entirely unrelated to this drug-disease combination. Topics include opioid risk management in primary care, diabetes education programs, AI-assisted motivational interviewing training, chiropractic care for spinal pain, and dementia caregiver interventions. None evaluate Metronidazole for pneumocystosis or any related indication.

**Currently, no relevant clinical trials for Metronidazole in pneumocystosis are registered.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Lists TMP-SMX as drug of choice for PCP; Metronidazole is cited for amebiasis, trichomoniasis, and giardiasis — no role in PCP |
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | Broad antiparasitic agent review; Metronidazole covers protozoa, TMP-SMX covers PCP — distinct drug categories |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Antiprotozoal regimens reviewed; Metronidazole not listed among PCP treatments |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | AIDS infectious complications review; PCP treated with TMP-SMX or pentamidine — Metronidazole addresses other co-infections |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | Updated HIV opportunistic infection guidelines; PCP standard of care is TMP-SMX, Metronidazole not mentioned |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case Report | Am Rev Respir Dis | Adult male treated with Metronidazole for prior diarrheal illness then developed PCP — Metronidazole was not the PCP treatment; illustrates co-occurrence |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case Report | Kansenshogaku Zasshi | Two AIDS patients: Metronidazole used successfully for amebic dysentery; patient later developed PCP managed separately — co-occurrence, not causal |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case Report | J Formos Med Assoc | HIV patient with amebic colitis and CMV infection; Metronidazole used for amebiasis component in a multi-pathogen context |

> **Interpretation:** Every item in the literature reflects co-management of multiple opportunistic infections in immunocompromised hosts. Metronidazole appears as a treatment for concurrent amebic or anaerobic infections, never as a treatment for pneumocystosis itself.

---

## Canada Market Information

No Health Canada DINs are registered for Metronidazole in the current dataset.

> **Note:** This may reflect a query or data pipeline limitation rather than true absence from the Canadian market. Metronidazole is a generic antibiotic widely available in many countries (e.g., Flagyl®). Direct verification against the Health Canada Drug Product Database (HCDPD) is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pneumocystosis prediction is a false positive arising from knowledge graph co-occurrence in HIV/AIDS patient data. Metronidazole has no antifungal mechanism and cannot address Pneumocystis jirovecii. Pursuing this indication would have no pharmacological basis and would divert resources from more promising leads within this same Evidence Pack.

**Recommended repurposing pivot — three indications warrant further investigation:**

| Rank | Indication | Evidence Level | Decision | Key Rationale |
|------|-----------|---------------|---------|--------------|
| #9 | **Cap Polyposis** | L3 | **Proceed with Guardrails** | PMID 12141801 directly proposes Metronidazole cures cap polyposis via anti-inflammatory mechanism; H. pylori eradication regimens (containing Metronidazole) induce remission; dysbiosis is the accepted pathology |
| #3 | Ulcerative Proctosigmoiditis | L4 | Research Question | Proven efficacy in pouchitis (PMID 8210985); iNOS/NF-κB anti-inflammatory activity supports IBD role; direct RCT evidence lacking |
| #10 | Ulceration of Vulva | L4 | Research Question | Direct treatment evidence for two causative subtypes: vulvar amebiasis (PMID 6835740, 8840708) and vulvar Crohn's disease (PMID 28948431, 25687208 — Tier 2 studies) |

**To unlock the Cap Polyposis lead (highest priority):**
- Obtain Metronidazole MOA data from DrugBank to formalize the anti-inflammatory vs. antibiotic mechanism hypothesis
- Review Health Canada package insert and safety profile (data gap DG001)
- Confirm Canadian market registration status via HCDPD direct query
- Design a prospective case series stratifying H. pylori-positive vs. H. pylori-negative cap polyposis patients — this is the key subgroup question that PMID 12141801 raised in 2002 and remains unanswered 24 years later
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

