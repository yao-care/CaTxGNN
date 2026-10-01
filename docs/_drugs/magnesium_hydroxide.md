---
layout: default
title: Magnesium Hydroxide
parent: Model Prediction Only (L5)
nav_order: 565
evidence_level: L5
indication_count: 6
---

# Magnesium Hydroxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Magnesium Hydroxide: From Antacid Use to Active Peptic Ulcer Disease

## One-Sentence Summary

Magnesium hydroxide is an antacid ingredient found in Canadian over-the-counter products such as Gelusil and Almagel Plus.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**. This is largely a rediscovery of a classic antacid use rather than a new repurposing.
Support comes from **0 registered clinical trials** and **20 publications**, mostly older studies of aluminum/magnesium hydroxide combinations.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antacid use (inferred from product names; no approved indication text in the data) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 (as rated in the Evidence Pack; based on published controlled studies, with no registered trials) |
| Canada Market Status | ✓ Marketed |
| Number of DINs | 4 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Magnesium hydroxide neutralizes gastric acid, raises intragastric pH, and reduces pepsin activity. Preclinical work also suggests it may protect the stomach lining by increasing endogenous prostaglandins. Formal mechanism-of-action data are not available in the Evidence Pack, so this rationale comes from the published literature.

Peptic ulcers are acid-dependent, so a drug that lowers gastric acidity is a natural fit. This is why the model gives such a high score. It is essentially rediscovering the antacid's established role.

Most human evidence comes from aluminum/magnesium hydroxide combinations, so the effects cannot be attributed to magnesium hydroxide alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scand J Gastroenterol | 12-week double-blind trial in 72 duodenal/prepyloric ulcer patients comparing an antacid/anticholinergic regimen, cimetidine and placebo. Cimetidine healed 67% at 3 weeks (p<0.005 vs placebo). The excerpt cuts off before the antacid arm's result. |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | RCT | J Clin Gastroenterol | Compared sodium bicarbonate with aluminum-magnesium hydroxide for buffering postprandial gastric acid in duodenal ulcer patients. |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | RCT | Scand J Gastroenterol | 80 duodenal ulcer patients on a high- or low-fiber diet, all taking an antacid tablet. Healing was 67.5% vs 60%. |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | Review | Clin Gastroenterol | Reviews antacids and anticholinergics in duodenal ulcer treatment. |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Review | Fortschr Med | Antacids help in peptic ulcer disease by neutralizing acid and inhibiting pepsin. |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review (mechanistic) | Curr Pharm Des | Describes the gastroprotective and ulcer-healing mechanisms of antacids. |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | Preclinical (rat) | Scand J Gastroenterol | An Al/Mg hydroxide antacid dose-dependently prevented gastric lesions, with a role for endogenous prostanoids. |
| [2390927](https://pubmed.ncbi.nlm.nih.gov/2390927/) | 1990 | Preclinical (rat) | Dig Dis Sci | Studies whether prostaglandins and epidermal growth factor contribute to antacid-enhanced ulcer healing. |
| [9305482](https://pubmed.ncbi.nlm.nih.gov/9305482/) | 1997 | Clinical study | Aliment Pharmacol Ther | Reports that H2-receptor antagonists and antacids may aggravate *H. pylori* gastritis in duodenal ulcer patients. |
| [2686073](https://pubmed.ncbi.nlm.nih.gov/2686073/) | 1989 | Clinical study | Ter Arkh | Almagel and food effectively reduced stomach and duodenal acidity and protein digestion in duodenal ulcer patients. |

---

## Canada Market Information

| DIN | Product Name |
|---------|------|
| 623709 | STOMAAX PLUS |
| 2243053 | PEPCID COMPLETE |
| 2409836 | GELUSIL ANTACID AND ANTI-GAS |
| 815527 | ALMAGEL PLUS SUS |

---

## Safety Considerations

Please refer to the package insert for safety information. The Evidence Pack contains no drug-interaction records for magnesium hydroxide.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Acid neutralization is an established and mechanistically sound basis for treating peptic ulcer, and controlled human studies exist. However, the evidence is old, mostly involves Al/Mg combinations, and includes no registered trials. The effect of magnesium hydroxide alone is unproven.

**To proceed, the following is needed:**
- Health Canada monographs, warnings and contraindications (a blocking data gap for safety screening).
- Approved indication text and dosage forms for the four DINs.
- Recent controlled trials, or a review that separates the magnesium hydroxide contribution from the aluminum component.
- Comparison against current standard therapy (acid suppressants, *H. pylori* eradication) to define any role for antacids as adjunct or symptom relief.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

