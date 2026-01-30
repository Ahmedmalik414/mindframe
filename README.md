# 🧠 Mindframe

[![PyPI version](https://img.shields.io/pypi/v/mindframe-ai.svg)](https://pypi.org/project/mindframe-ai/)
[![Python versions](https://img.shields.io/pypi/pyversions/mindframe-ai.svg)](https://pypi.org/project/mindframe-ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**"Structure first. Intelligence second."**

Mindframe is a powerful Python CLI-based project scaffolding tool designed specifically for Generative AI and Agentic AI developers. It enforces professional software architecture patterns from Day 1, ensuring your AI systems are scalable, maintainable, and swap-ready.

---

## 🚀 Why Mindframe?

Most GenAI projects start as "spaghetti code." Mindframe solves this by providing a standardized, industrial-grade project structure that separates concerns across 5 critical layers.

### ✨ Key Features
- **🏗️ Industrial Scaffolding**: Initialize a full, professional project structure in seconds.
- **🧱 Layered Architecture**: Dedicated boundaries for Domain Logic, LLM Abstractions, Knowledge/RAG, Orchestration, and Evaluation.
- **🤖 Agentic Native**: Seamlessly transition from simple RAG to autonomous agent systems with built-in memory and tool patterns.
- **🔌 Model Agnostic**: Effortlessly switch between OpenAI, Anthropic, or Local models (Ollama/Llama) with production-ready base classes.
- **📈 Scalability First**: Enforces best practices that make your AI systems maintainable and ready for production.

---

## 📦 Installation

Mindframe is available on [PyPI](https://pypi.org/project/mindframe-ai/). You can install it globally via pip:

```bash
pip install mindframe-ai
```

### 🛠️ Local Development
To contribute to Mindframe or use the latest developmental version:

```bash
git clone https://github.com/Ahmedmalik414/mindframe.git
cd mindframe
pip install -e .
```

---

## 🛠 Usage

### 1. Standard GenAI (RAG) Project
Perfect for knowledge-based chatbots and standard LLM applications.
```bash
mindframe init my_project
```

### 2. Agentic AI Project
Adds specialized layers for planning, tool execution, and memory management.
```bash
mindframe init my_agent --type agentic
```

---

## 📂 The "Authoritative" Structure

When you run `mindframe init`, it generates a clean, scalable skeleton designed for high-performance AI applications:

```text
my_project/
├── config/             # Configuration for LLMs, prompts, and system settings
├── data/               # Vector database storage, local cache, and embeddings
├── src/                
│   ├── core/           # LLM Base classes & Provider abstractions
│   ├── prompts/        # Version-controlled prompt templates & chains
│   ├── rag/            # Retrieval-Augmented Generation & Search logic
│   ├── processing/     # Data ingestion, chunking, and normalization
│   └── inference/      # Model execution and throughput management
├── tests/              # Unit, integration, and evaluation tests
├── scripts/            # Deployment and data ingestion scripts
├── Dockerfile          # Production-ready containerization
└── requirements.txt    # Managed project dependencies
```

> **Note:** The `agentic` type adds the `src/orchestration/` layer containing `agents/` and `memory/` modules for autonomous logic.

---

## 🤝 Contributing
Mindframe is built for the community. If you have ideas for better AI architectural patterns, feel free to open a PR!

---

**Built by [Ahmed Malik](https://github.com/Ahmedmalik414)**  
*Architecture is the frame that supports the mind.*
