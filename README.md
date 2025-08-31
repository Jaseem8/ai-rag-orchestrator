# AI RAG Orchestrator & Autonomous Agent Pipeline 🤖🧠

A modular, production-ready framework for building Retrieval-Augmented Generation (RAG) applications, hybrid BM25 + dense vector search, and tool-calling ReAct agents.

[![CI](https://github.com/status/ci.svg)](https://github.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI/LLM](https://img.shields.io/badge/Domain-AI%20%2F%20RAG-brightgreen.svg)](https://github.com)

## 🚀 Architecture Highlights
1. **Dense Vector Search**: Pure-Python Cosine and Dot-Product similarity search with embedding cache.
2. **Hybrid BM25 Retrieval**: Combines sparse keyword scoring with dense embeddings for high-precision retrieval.
3. **ReAct Autonomous Agent**: Reasoning and acting cycle (`Thought -> Action -> Observation -> Final Answer`).
4. **Token Budget & Context Window Management**: Sliding window buffer preventing context overflow.

## 📋 System Architecture
```mermaid
flowchart LR
    UserQuery["User Query"] --> Hybrid["Hybrid BM25 + Vector Search"]
    Hybrid --> ReRanker["Cross-Encoder Re-Ranker"]
    ReRanker --> Context["Context Window Manager"]
    Context --> Agent["ReAct Agent Execution Loop"]
    Agent --> Response["Structured LLM Response"]
```
