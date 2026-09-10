---
layout: default
title: Potassium Chloride
parent: 僅模型預測 (L5)
nav_order: 637
evidence_level: L5
indication_count: 1
---

# Potassium Chloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Potassium Chloride: From Hypokalemia (Potassium Repletion) to Renal Tubular Acidosis

## One-Sentence Summary

Potassium Chloride (DB00761) is a standard electrolyte-replacement agent used to prevent and treat hypokalemia (potassium depletion). The TxGNN model predicts it may be effective for **Renal Tubular Acidosis (RTA)**, with **9 clinical trials** and **19 publications** identified in the evidence pack — but none of the trials directly test potassium chloride in RTA patients, and the mechanistic case has a significant caveat (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Potassium repletion / prevention & treatment of hypokalemia (no formal approved-indication text available in this evidence pack) |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 (mechanistic/preclinical association only; no completed trial directly supports use) |
| Canada Market Status | Not Marketed |
| Number of DINs | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this candidate (flagged as a High-severity data gap). Based on known pharmacology, potassium chloride is a simple electrolyte salt used to correct potassium deficits — its efficacy in hypokalemia is well established, and RTA (particularly distal Type 1 and Type 4) frequently presents with hypokalemia, which is the likely basis for the TxGNN association.

However, the underlying pathophysiology of RTA is hyperchloremic metabolic acidosis — a defect in renal acid excretion that already produces excess serum chloride. Administering potassium **chloride** would replete potassium but simultaneously add further chloride load, which could aggravate rather than correct the acidosis. This is why standard clinical practice for RTA uses potassium **citrate** or potassium **bicarbonate**, whose alkali (citrate/bicarbonate) component corrects the acidosis while also repleting potassium — deliberately avoiding the chloride salt form.

In short, the high TxGNN score likely reflects a superficial symptom-level association (both conditions involve "low potassium") rather than a validated mechanistic fit. This is a case where the prediction should be treated with more caution than the score alone would suggest, rather than a straightforward repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | Terminated | 7 | Alkali (sodium bicarbonate) repletion in sickle cell disease patients with low bicarbonate; assessed bicarbonate/potassium response, not KCl or RTA specifically |
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | Terminated | 3 | RCT of ADV7103 (a citrate/bicarbonate-based product) vs. placebo to prevent metabolic acidosis in pediatric/adult distal RTA; terminated with minimal enrollment |
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | Recruiting | 33 | Diagnostic methodology study comparing urinary aldosterone measurement timing for primary aldosteronism; not a treatment trial |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | Recruiting | 43 | Crossover RCT of exogenous ketone bodies on proteinuria/renal function in CKD/polycystic kidney disease; unrelated to KCl or RTA |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | Recruiting | 130 | RCT of SGLT2 inhibitor add-on therapy for acute cardiorenal syndrome in heart-failure-associated AKI; different drug class and mechanism |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | Withdrawn | 0 | Studied potassium **citrate** (not KCl) on urinary chemistry/acid-base status in children with hypercalciuria/urolithiasis; withdrawn with zero enrollment |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | Terminated | 36 | Spironolactone for prevention of electrolyte abnormalities in Amphotericin B-treated patients; different drug and indication |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | Unknown | 31 | Safety of eplerenone in cyclosporine-A-treated transplant recipients; unrelated to KCl/RTA |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | Unknown | 40 | Sodium bicarbonate alkalinization in pediatric patients on topiramate (topiramate-induced RTA); alkali-based, not KCl |

**Note:** None of the identified trials directly evaluate potassium chloride for renal tubular acidosis. Most trials were graded "C" (low relevance) in the underlying relevance assessment; only NCT00120731 was graded "B," and it studied potassium citrate, not the chloride salt.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review | Archivos españoles de urología | Overview of RTA diagnosis and management, including alkali (not chloride) therapy for distal RTA |
| [21314872](https://pubmed.ncbi.nlm.nih.gov/21314872/) | 2011 | Review | International Journal of Clinical Practice | Clinical approach to RTA subtypes in adults, including electrolyte abnormality patterns |
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Review | Acta Medica Indonesiana | General approach to hypokalemia, including renal vs. extrarenal causes |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Review | Archives of Internal Medicine | Pathophysiology and diagnosis of RTA subtypes |
| [37081692](https://pubmed.ncbi.nlm.nih.gov/37081692/) | 2023 | Review | Endocrine Journal | Reclassification of pseudohypoaldosteronism type II as type IV RTA |
| [14048071](https://pubmed.ncbi.nlm.nih.gov/14048071/) | 1963 | Review | Medical Bulletin (Ann Arbor) | Historical overview of RTA |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort | La Tunisie Médicale | Genotype-phenotype correlation of distal RTA in a Tunisian cohort |
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | Cohort | Journal of Clinical Investigation | In classic (type 1) RTA patients corrected with oral **potassium bicarbonate** (not chloride), renal sodium conservation was evaluated |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case Report | Journal of Nephrology | Distal RTA with hypokalemic periodic paralysis during pregnancy |
| [28509102](https://pubmed.ncbi.nlm.nih.gov/28509102/) | 2015 | Case Report | CEN Case Reports | Pediatric Sjögren syndrome presenting with distal RTA and hypothyroidism |

**Note:** No RCT-level evidence was identified. Notably, the two studies that specify a potassium salt used for RTA correction (PMID 783200, NCT00120731) both use **bicarbonate or citrate**, not chloride — consistent with the mechanistic caution raised above.

---

## Canada Market Information

This product family is currently **not marketed in Canada** under this evidence pack — no Health Canada Drug Identification Numbers (DINs) were found (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured safety warnings, contraindications, or drug-interaction data were available in this evidence pack; the missing product label/warning data is flagged as a Blocking data gap that prevents formal safety review.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, no identified clinical trial or publication directly tests potassium chloride in renal tubular acidosis, and the mechanistic rationale is undermined by RTA's underlying hyperchloremic acidosis — additional chloride load from KCl could worsen, not improve, the condition. Standard practice instead uses potassium citrate/bicarbonate. A Blocking data gap (missing label/warning data) also prevents progression to the S1 safety-evaluation stage.

**To proceed, the following is needed:**
- Official product label/warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism-of-action data (DG002)
- Any clinical evidence specifically comparing potassium chloride vs. citrate/bicarbonate forms in RTA patients, to resolve the chloride-load concern before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

