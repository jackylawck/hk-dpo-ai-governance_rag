# System Lifecycle & Change Management / 生命週期與變更管理

**Document Control / 文檔管控:** V1.0  
**Framework Alignment / 框架對齊:** ISO/IEC 42001:2023 (Clause 8 & Annex A.10), EU AI Act (Article 72)  
**Scope / 適用範圍:** HK DPO AI Governance Local RAG Advisor (地端 RAG 智能顧問)

---

## 1. Versioning & Baseline Alignment / 版本控制與基準對齊

The current production release is mathematically optimized for semantic retrieval of the **HK DPO Generative AI Technical and Application Guideline V1.1 (Dec 2025)**.  
本系統現行版本針對香港數字辦《生成式人工智能技術及應用指引》V1.1 (2025年12月) 進行語義檢索最佳化。

---

## 2. Change Management Triggers / 變更管理觸發條件

The RAG pipeline enters a mandatory review and update cycle upon:
當發生以下情境時，RAG 管道進入強制審查與更新週期：
* Discovery of critical vulnerabilities in underlying NLP/vector libraries (`sentence-transformers`, `FAISS`, `PyPDF2`).  
  基礎 NLP 及向量套件發現重大資安漏洞。
* Accuracy degradation of the chosen open-source embedding model.  
  選用之開源 Embedding 模型出現檢索精準度衰退。
* Structural formatting changes in future official DPO PDF releases breaking parser logic.  
  數字辦未來發布之 PDF 格式出現結構性變更，導致解析器失效。

---

## 3. Regression Testing Protocol / 迴歸測試規範

Prior to deploying updates to the RAG parsing or embedding pipeline:  
於部署 RAG 解析或向量管道更新前：
* **Benchmark Query Testing (基準查詢測試):** Must be evaluated against a benchmark of 20 complex regulatory test scenarios. (必須於 20 個複雜法規測試情境進行基準評估)。
* **Retrieval Accuracy Threshold (檢索精準度閾值):** Must consistently retrieve top-3 relevant legal chunks without semantic degradation. (必須穩定精準命中 Top-3 最相關法規區塊，且無語義漂移)。

---

## 4. Decommissioning Strategy / 系統退役策略

If the local RAG architecture becomes obsolete or superseded by official government tools:  
若本 RAG 架構過時或被政府官方工具取代：
1. A formal decommissioning notice will be published on GitHub (於 GitHub 發布正式退役公告)。
2. The Streamlit instance will be taken offline permanently (永久下線 Web App 實例)。
3. The repository will be archived to maintain transparent audit lineage (歸檔 GitHub 倉庫，保留透明審計軌跡)。
