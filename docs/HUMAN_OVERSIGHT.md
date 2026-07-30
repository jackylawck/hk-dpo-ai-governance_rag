# Human Oversight & Escalation Protocol (人工監督與申訴機制)

**Document Control:** V1.0
**Framework Alignment:** ISO/IEC 42001:2023 (Annex A.8.3), EU AI Act (Article 14)
**Scope:** HK DPO AI Governance Local RAG Advisor

## 1. Human-in-the-Loop (HITL) Philosophy (人機協同理念)

This RAG engine is an **Augmented Search Tool (增強檢索工具)**. It does not replace the professional judgment of human resources, legal, or compliance officers. Final accountability for regulatory interpretation always resides with the human professional.

## 2. Operational Oversight Mechanisms (營運監督機制)

* **Source Verification (來源核實):** Users are strictly required to verify the generated answers against the provided legal text chunks. The system forces transparency by displaying the exact extracted paragraphs.
* **Cryptographic Tracing (密碼學追溯):** Every retrieved chunk is tagged with a unique SHA-256 hash. Auditors and compliance officers can cross-reference this hash to guarantee the text has not been synthetically altered.
* **Manual Cross-Check:** Any critical compliance decision derived from the RAG output must be manually cross-checked with the official HK DPO Guideline PDF pages before organizational policy updates.

## 3. Escalation & Feedback Process (申訴與回饋流程)

If the system retrieves irrelevant clauses or fails to extract a known legal requirement:
1. **Manual Search Fallback:** The user must immediately revert to a manual keyword search within the official PDF document.
2. **Report Retrieval Failure:** Log the specific query prompt and report it to the AI Governance Lead.
3. **Parameter Audit:** The engineering team will review the `FAISS` vector similarity threshold (k-value) and the chunking overlap parameters to optimize retrieval precision.
