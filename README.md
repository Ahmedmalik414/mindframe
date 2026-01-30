# 🧠 Mindframe

**"Structure first. Intelligence second."**

Mindframe is a powerful Python CLI-based project scaffolding tool designed specifically for Generative AI and Agentic AI developers. It enforces professional software architecture patterns from Day 1, ensuring your AI systems are scalable, maintainable, and swap-ready.

---

## 🚀 Why Mindframe?

Most GenAI projects start as "spaghetti code." Mindframe solves this by providing a standardized, industrial-grade project structure that separates concerns across 5 critical layers.

- **Zero Manual Work**: Initialize a full project structure with one command.
- **Clean Boundaries**: Dedicated layers for Domain logic, LLM interface, Knowledge/RAG, Orchestration, and Evaluation.
- **Agentic Ready**: Seamlessly extend standard GenAI projects into autonomous agent systems.
- **Swap-Ready**: Effortlessly switch between OpenAI, Anthropic, or Local models without rewriting your app logic.

---

## 📦 Installation

To use Mindframe globally on your system, install it directly from GitHub:

```bash
pip install git+https://github.com/Ahmedmalik414/mindframe.git
```

For local development/contributions:
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
When you run `mindframe init`, it generates a clean, scalable skeleton:

```text
my_project/
├── config/             # Model & Logging settings
├── data/               # Cache, Embeddings, & Vector DB
├── src/                
│   ├── core/           # LLM Abstractions (GPT, Claude, etc.)
│   ├── prompts/        # Templates & Chaining
│   ├── rag/            # Retrieval logic & Search
│   ├── processing/     # Chunking & Cleaning
│   └── inference/      # Model execution engine
├── tests/              # Unit & Integration tests
├── scripts/            # Automation (env setup, ingestion)
├── Dockerfile          # Container config
└── requirements.txt    # Standard dependencies
```

*Note: The `agentic` type adds `src/orchestration/` containing `agents/` and `memory/` modules.*

---

## 🤝 Contributing
Mindframe is built for the community. If you have ideas for better AI architectural patterns, feel free to open a PR!

---

**Built by [Ahmed Malik](https://github.com/Ahmedmalik414)**  
*Architecture is the frame that supports the mind.*
