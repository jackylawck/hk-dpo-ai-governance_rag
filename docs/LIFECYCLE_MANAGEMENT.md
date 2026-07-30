# System Lifecycle & Change Management (生命週期與變更管理)

**Document Control:** V1.0
**Framework Alignment:** ISO/IEC 42001:2023 (Clause 8 & Annex A.10), EU AI Act (Article 72)
**Scope:** HK DPO AI Governance Local RAG Advisor

## 1. Versioning & Baseline Alignment (版本控制與基準對齊)

The current system is optimized for semantic retrieval of legal and regulatory texts. Its primary baseline is the **HK DPO Generative AI Technical and Application Guideline V1.1 (Dec 2025)**[cite: 1].

## 2. Change Management Triggers (變更管理觸發條件)

The RAG architecture will require maintenance, testing, and potential code updates upon:
* Discovery of a critical security vulnerability in the underlying NLP and vectorization libraries (`sentence-transformers`, `FAISS`, `PyPDF2`).
* Depreciation or significant accuracy degradation of the chosen open-source embedding model.
* A major structural format change in future official HK DPO PDF releases that breaks the current text extraction parser.

## 3. Regression Testing Protocol (迴歸測試規範)

Prior to deploying any updates to the RAG parsing or embedding logic:
* **Retrieval Accuracy Testing:** The updated system must be tested against a benchmark of 20 complex regulatory queries. 
* **Precision & Recall Metrics:** The system must consistently retrieve the top-3 most relevant legal chunks for each query without degrading semantic alignment.

## 4. Decommissioning Strategy (系統退役策略)

If the local RAG architecture becomes unmaintainable or is superseded by official government retrieval tools:
1. A formal decommissioning notice will be published on the GitHub repository.
2. The Streamlit Community Cloud instance will be taken offline permanently.
3. The repository will be archived to maintain the transparency of the chunking and embedding methodology for historical audit purposes.
