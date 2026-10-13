---
layout: default
title: Nitrofurantoin
parent: Model Prediction Only (L5)
nav_order: 658
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is an antibacterial agent that is marketed in Canada and is used for urinary tract infections. Its original indication text is not listed in the data compiled for this report.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 clinical trials** and only **9 publications** (mostly adverse-effect reports), so the prediction is **not supported by therapeutic evidence**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (general knowledge of the drug; no approved indication text in the compiled Health Canada records) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitrofurantoin is a nitrofuran-class antibacterial used for urinary tract infections. It has no known anti-inflammatory or immunomodulatory activity relevant to rheumatoid arthritis (RA).

The relationship between the original and predicted indications is weak. The available literature is dominated by adverse-effect reports: drug-induced pulmonary fibrosis, a methotrexate–nitrofurantoin interaction causing irreversible pulmonary fibrosis in a patient with RA, and a study linking antibiotic exposure to RA flares. These signals suggest possible harm in RA patients, not benefit. The high TxGNN score is most likely a network-proximity artifact in the knowledge graph rather than a true therapeutic signal.

The other predicted indications show the same pattern. Most are rare genetic disorders with no plausible pharmacological link. For methemoglobinemia, nitrofurantoin is a cause of the condition, not a treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort | Scientific Reports | Self-controlled case series in UK primary-care data (newly diagnosed RA cohort, n = 31,992) examining the association between antibiotic exposure and RA flares |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Drug-induced pulmonary fibrosis; nitrofurantoin is listed as a causative drug, and RA is a predisposing systemic disease |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung disease; nitrofurantoin is named among the implicated antibiotics |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | A 94-year-old woman with RA on long-term methotrexate developed irreversible pulmonary fibrosis after nitrofurantoin was added |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | Poor prognosis in RA patients hospitalized for interstitial lung fibrosis (not about nitrofurantoin as a treatment) |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis versus drug-induced liver injury; nitrofurantoin is listed as a possible cause that must be ruled out |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de Dermatologie et de Vénéréologie | Phenylbutazone-induced sialadenitis; nitrofurantoin is mentioned as another drug reported to cause sialadenitis |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Revue de Pneumologie Clinique | Gold salt-induced pneumonitis with CD4 alveolitis (not directly about nitrofurantoin) |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta Medica Scandinavica | Short-term nitrofurantoin therapy for bacteriuria in middle-aged women, with one-year follow-up (no RA outcome) |

None of these publications shows a therapeutic benefit of nitrofurantoin in RA.

---

## Canada Market Information

| DIN | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 02455676 | PMS-NITROFURANTOIN BID | Not listed | Not listed |
| 00312738 | NITROFURANTOIN | Not listed | Not listed |
| 00319511 | NITROFURANTOIN | Not listed | Not listed |
| 02495503 | JAMP NITROFURANTOIN | Not listed | Not listed |
| 02231016 | TEVA-NITROFURANTOIN | Not listed | Not listed |

All 9 licences are valid single-ingredient products. Only the first 5 are shown here.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): diabetes mellitus and diabetic ketoacidosis, anuria, impaired renal function, peripheral neuropathy and other peripheral nervous system disease, interstitial lung disease, pulmonary fibrosis, G6PD deficiency, drug-induced liver injury, hepatitis, obstructive jaundice and biliary tract disease, *Clostridium difficile* colitis, vitamin B12 and other B-vitamin deficiencies (including beriberi and ariboflavinosis), optic neuritis, cystinuria, galactosemia, glycogen storage disease, and perinatal necrotizing enterocolitis.
- **Drug interactions** (100 interactions recorded; examples shown):
  - Moderate: balsalazide, metronidazole, picosulfuric acid, naltrexone, rosuvastatin, simvastatin
  - Minor: anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, scopolamine, and others) and magnesium-containing antacids
- **Relevance to RA:** the literature reports a methotrexate–nitrofurantoin interaction causing irreversible pulmonary fibrosis. RA patients often take methotrexate, and RA itself can involve the lungs. The risk-benefit balance is therefore unfavourable.

Please also refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone, with no clinical trials and no supportive literature. The published signals point toward potential harm, particularly pulmonary and hepatic toxicity and a methotrexate interaction, and there is no plausible anti-rheumatic mechanism.

**To proceed, the following is needed:**
- A plausible mechanistic hypothesis for anti-inflammatory or immunomodulatory activity in RA, supported by preclinical data
- Mechanism of action data
- Health Canada package insert warnings, contraindications and approved indication text
- A formal safety assessment for patients with RA, especially those taking methotrexate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

