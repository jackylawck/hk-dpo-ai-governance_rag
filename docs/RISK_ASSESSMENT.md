# Enterprise AI Risk Assessment Report (企業 AI 風險評估報告)

**Document Control:** V1.0
**Framework Alignment:** ISO/IEC 42001:2023 (Annex A.6.1), EU AI Act (Article 9), NIST AI RMF (MAP & MEASURE)
**Scope:** HK DPO AI Governance Local RAG Advisor

## 1. System Risk Categorization (系統風險分類)

Based on the EU AI Act risk classification framework, the Local RAG Advisor is classified as a **Minimal Risk (極低風險)** system.
* The system is deployed exclusively as a secure, local decision-support tool for compliance reading and retrieval.
* It does not profile individuals, conduct automated employment decisions, or process biometric data.

## 2. Risk Identification & Mitigation Matrix (風險識別與控制矩陣)

| Identified Risk (識別風險) | Impact | Likelihood | Mitigation Control (緩解控制措施) | Residual Risk |
| :--- | :--- | :--- | :--- | :--- |
| **Generative Hallucination (生成幻覺)** | High | Low | System bypasses LLM creative generation layers. Implements strict "retrieve-first" context matching against the uploaded PDF. | Minimal |
| **Semantic Retrieval Failure (檢索遺漏/漂移)** | Medium | Low | Overlapping chunking strategy (300-400 chars with 50-100 char buffer) prevents context loss at boundaries[cite: 1]. | Minimal |
| **Copyright Infringement (版權侵犯)** | Medium | Low | The repository DOES NOT host or distribute official guidelines. Users must manually upload authorized PDFs locally. | Minimal |
| **Data Privacy Leakage (隱私洩漏)** | High | Low | 100% local, in-memory execution. Zero data transmitted to external cloud APIs (e.g., OpenAI) for embedding. | Minimal |

## 3. Approval & Accountability (審批與問責)
The residual risks are deemed acceptable. The local-only execution model effectively neutralizes standard cloud-based LLM privacy risks.
