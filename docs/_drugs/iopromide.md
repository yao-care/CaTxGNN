---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide：從顯影造影劑到骨關節炎易感性（Osteoarthritis Susceptibility）

## 一句話摘要

Iopromide 是一種非離子型低滲透壓碘化顯影劑，原始用途為 CT／血管攝影等影像檢查時的顯影增強，並非治療特定疾病的藥物。TxGNN 模型預測其可能與**骨關節炎易感性（Osteoarthritis Susceptibility）**相關，惟目前**0 篇臨床試驗、0 篇文獻**支持此關聯，證據等級最低，且高分疑似為知識圖譜混淆所致的偽陽性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原始適應症 | 顯影造影劑（CT／血管攝影影像增強），非治療性用途；加拿大Not marketed，無核准適應症紀錄 |
| 預測新適應症 | Osteoarthritis susceptibility（骨關節炎易感性） |
| TxGNN 預測分數 | 99.57%（排名第 8382） |
| 證據等級 | L5（僅模型預測，無任何實際研究） |
| 加拿大市場狀態 | Not marketed |
| DIN 數量 | 0 |
| 建議決策 | Hold（暫緩） |

---

## 為何此預測看似合理？

目前尚無詳細的作用機轉（MOA）資料。根據現有資訊，Iopromide 屬於非離子型低滲透壓碘化顯影劑家族，其臨床應用僅限於 CT、血管攝影等影像診斷時的對比增強，並無已知的藥理治療機轉，也未被核准用於治療任何疾病。

從機轉角度看，顯影劑與骨關節炎之間沒有已知的生物學連結——骨關節炎的病理機轉涉及軟骨退化、關節發炎與骨贅生成，而顯影劑僅作用於 X 光衰減特性以利影像判讀，不具抗發炎、軟骨保護或修復相關藥理活性。

證據包內同一藥物針對 rank 2（osteoarthritis）的預測理由已明確指出：TxGNN 給出的高分很可能源自知識圖譜混淆——顯影劑因大量用於「疾病影像診斷」相關文獻中，與各種疾病病名高頻共現，被模型誤判為治療性關聯，而非真正的療效訊號。此一混淆模式同樣適用於本項排名第一的 osteoarthritis susceptibility 預測，且該項目連一篇共現文獻都沒有，機轉合理性更為薄弱。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻資料。

---

## 加拿大市場資訊

Iopromide 目前在加拿大**Not marketed**，無有效藥品許可證（DIN）紀錄，故無法提供核准適應症或劑型資訊。

---

## 安全性考量

請參考藥品仿單以獲取安全性資訊。

（補充：本證據包標記一項阻斷級資料缺口 DG001——TFDA 仿單警語／禁忌尚未取得，此為進入安全性初評的必要前提，詳見下方「後續所需」。）

---

## 結論與後續建議

**決策：Hold（暫緩）**

**理由：**
Iopromide 為顯影造影劑而非治療性藥物，機轉上與骨關節炎易感性無合理連結；該預測缺乏任何臨床試驗或文獻佐證（0/0），且證據等級為最低的 L5，同批預測中類似的高分項目已被證實可能是知識圖譜混淆的偽陽性訊號。另外值得注意的是，同一藥物在 hemoglobinopathy（rank 9）方向反而出現**方向相反的安全性訊號**——文獻報告低滲透壓靜脈顯影劑可能於鐮刀型細胞疾病患者誘發腦血管閉塞事件，提示此類顯影劑用於老藥新用評估時應格外謹慎。

**若要繼續推進，需要補充：**
- TFDA／加拿大官方仿單之警語與禁忌資料（DG001，阻斷級，須先解決才可進入安全性初評）
- 完整作用機轉（MOA）資料（DG002）
- 獨立的機轉假說或臨床前實驗數據，證明顯影劑與骨關節炎病理生理之間存在合理連結
- 針對 TxGNN 高分是否為顯影劑／影像文獻共現造成之知識圖譜混淆，進行專門的訊號驗證分析
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

