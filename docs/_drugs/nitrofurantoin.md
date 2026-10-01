---
layout: default
title: Nitrofurantoin
parent: Moderate Evidence (L3-L4)
nav_order: 653
evidence_level: L4
indication_count: 10
---

# Nitrofurantoin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is a urinary antibacterial marketed in Canada, used for urinary tract infections.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 clinical trials** and no literature showing a therapeutic benefit.
The 12 retrieved publications mostly describe drug-induced lung and liver harm, or infection and RA flares, so the signal looks like a knowledge-graph artifact rather than a real opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (the Canadian licence records provide no indication text; this is based on the drug's known antibacterial use) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for nitrofurantoin. It is a urinary antibacterial, and no anti-inflammatory or immunomodulatory mechanism that would be relevant to rheumatoid arthritis (RA) has been established.

The literature links nitrofurantoin to RA mainly through harm, not benefit:
- Reviews list nitrofurantoin among drugs that cause pulmonary fibrosis and interstitial lung disease, and RA itself predisposes patients to these lung conditions.
- A case report describes irreversible pulmonary fibrosis in an elderly RA patient treated with methotrexate and then nitrofurantoin for recurrent urinary infections.
- One large UK cohort study examined whether antibiotic exposure is associated with RA flares. This concerns infection and flare risk, not treatment.

The high TxGNN score most likely reflects co-occurrence of RA and drug-induced lung disease in the knowledge graph. It is not evidence of a therapeutic relationship, so the prediction is not mechanistically supported.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Twelve publications were retrieved for RA; the ten most relevant are listed. None reports a therapeutic benefit of nitrofurantoin in RA.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Med J | Drug-induced pulmonary fibrosis; nitrofurantoin is listed as a causative drug, and RA is noted as a predisposing disease |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | Rev Prat | Drug-induced interstitial lung disease; nitrofurantoin is named among the antibiotics implicated |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Internist | Synopsis of alveolitis and pulmonary fibrosis; no abstract available, no treatment benefit shown |
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort | Sci Rep | Self-controlled case series in 31,992 newly diagnosed RA patients examining antibiotic use and RA flares |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | 57 RA patients hospitalized for interstitial lung fibrosis; poor prognosis, no therapeutic role for nitrofurantoin |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta Med Scand | Bacteriuria screening and short-term nitrofurantoin treatment in middle-aged women; no abstract available, no RA benefit evident |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | Irreversible pulmonary fibrosis after a methotrexate and nitrofurantoin interaction in a 94-year-old RA patient |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis versus drug-induced liver injury; nitrofurantoin is listed as a possible cause to rule out |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Rev Pneumol Clin | Gold salt-induced pneumonitis with CD4 alveolitis; not about nitrofurantoin as treatment |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Ann Dermatol Venereol | Phenylbutazone-induced sialadenitis; nitrofurantoin is only mentioned as another reported cause |

---

## Canada Market Information

Nine DINs are on record; five are shown below. The records provide no dosage form or approved indication text.

| DIN | Product Name |
|---------|------|
| 2455676 | PMS-NITROFURANTOIN BID |
| 312738 | NITROFURANTOIN |
| 319511 | NITROFURANTOIN |
| 2495503 | JAMP NITROFURANTOIN |
| 2231016 | TEVA-NITROFURANTOIN |

---

## Safety Considerations

Safety fields in the Evidence Pack are empty, and no drug interactions were found. Please refer to the package insert for safety information.

The retrieved literature raises several signals relevant to this repurposing idea:
- **Pulmonary toxicity**: nitrofurantoin is associated with pulmonary fibrosis and interstitial lung disease, and RA patients already carry lung risk. A case report describes irreversible fibrosis when it was combined with methotrexate, a common RA drug.
- **Liver injury**: nitrofurantoin is a recognized cause of drug-induced liver injury, including autoimmune-like hepatitis.
- **Methemoglobinemia and hemolysis**: preclinical and neonatal case reports link nitrofurantoin to methemoglobin formation and hemolytic anemia.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials exist, and the literature shows harm in RA populations (lung fibrosis, a methotrexate interaction) and no therapeutic effect. The high TxGNN score likely reflects adverse-effect co-occurrence. The other nine predicted indications are also on Hold. Eight have only L5 model-prediction evidence, and the methemoglobinemia prediction (L4) reflects an adverse effect, so using the drug there would worsen the condition.

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any anti-inflammatory link to RA exists
- Package insert warnings and contraindications (Health Canada) to complete safety screening
- Preclinical or observational evidence of a benefit in RA, not just an infection or harm association
- A review of the interaction risk with methotrexate and other RA therapies before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

