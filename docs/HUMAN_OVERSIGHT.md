# Human Oversight & Escalation Protocol / 人工監督與申訴機制

**Document Control / 文檔管控:** V1.0  
**Framework Alignment / 框架對齊:** ISO/IEC 42001:2023 (Annex A.8.3), EU AI Act (Article 14)  
**Scope / 適用範圍:** HK DPO AI Governance Local RAG Advisor (地端 RAG 智能顧問)

---

## 1. Human-in-the-Loop (HITL) Philosophy / 人機協同理念

This RAG engine is an **Augmented Search Tool (增強檢索工具)**. It does not replace the professional judgment of HR, legal, or compliance officers. Final accountability for regulatory interpretation always resides with the human professional.  
本 RAG 引擎定位為增強檢索工具，絕不替代 HR、法務或合規官之專業判斷。法規解讀之最終問責，永遠由專業人員承擔。

---

## 2. Operational Oversight Mechanisms / 營運監督機制

* **Source Text Verification (原文比對覆核):** Users are strictly required to verify generated answers against displayed legal text chunks (使用者必須將系統解答與介面顯示之原始法規文本區塊進行比對)。
* **SHA-256 Audit Tracing (SHA-256 審計追溯):** Every retrieved chunk is tagged with a unique SHA-256 hash for non-repudiation verification (每個被檢索切片均標註 SHA-256 哈希值，確保可追溯性)。
* **Manual PDF Cross-Check (人工 PDF 交叉查驗):** Critical compliance decisions must be manually cross-checked with official DPO PDF pages before policy execution (執行重大政策前，必須與官方數字辦指引 PDF 進行人工頁碼交叉查驗)。

---

## 3. Escalation & Feedback Process / 申訴與異常回饋流程

If the system retrieves irrelevant clauses or fails to extract a known legal requirement (若檢索出無關條文或遺漏法規要求):
1. **Manual Search Fallback (切換人工檢索):** Revert immediately to manual keyword search within the official PDF (立即切換回官方 PDF 之傳統關鍵字搜尋)。
2. **Report Failure (通報檢索異常):** Log the specific query prompt and report to the AI Governance Lead (截取特定查詢 Prompt，通報至 AI 管治負責人)。
3. **Parameter Tuning (工程參數調校):** The engineering team will review `FAISS` similarity thresholds and chunking overlap parameters (工程團隊將調校 `FAISS` 向量相似度閾值與切片重疊參數)。
