# 🤖 AAIDC Module 3 – Production-Ready Agentic AI System (Gemini 2.5 Flash)

## 📌 Overview
This project is the **final capstone (Project 3)** of the **Agentic AI Developer Certification (AAIDC)** by Ready Tensor.

It demonstrates a **production-ready Agentic AI system** that builds upon the multi-agent architecture developed in Module 2 and enhances it with real-world engineering practices such as:

- User Interface (UI)
- Safety & guardrails
- Logging & operational resilience
- Testing
- Clear documentation

The system analyzes a project README or description and provides structured feedback using a **multi-agent workflow orchestrated with LangGraph** and powered by **Google Gemini 2.5 Flash**.

---

## 🎯 Problem Statement
Many AI projects struggle with poor documentation, missing setup instructions, and unclear project scope.  
This system helps developers improve **project readiness and quality** by automatically reviewing project documentation using **Agentic AI workflows**.

---

## 🧠 System Architecture
```
User (Streamlit UI)
        ↓
Input Validation & Safety Checks
        ↓
LangGraph Multi-Agent Workflow
        ├── Repo Analyzer Agent
        ├── Metadata Recommender Agent (Gemini 2.5 Flash)
        └── Reviewer / Critic Agent
        ↓
Structured Results Displayed in UI
```

---

## 🧩 Agents & Responsibilities

### 1️⃣ Repo Analyzer Agent
- Reads and prepares README or project description
- Stores shared context in the workflow state

### 2️⃣ Metadata Recommender Agent (LLM-Powered)
- Uses **Google Gemini 2.5 Flash**
- Generates an improved project title
- Suggests relevant tags using keyword extraction tools

### 3️⃣ Reviewer / Critic Agent
- Evaluates documentation completeness
- Identifies missing sections such as Installation, Usage, and License

---

## 🛠️ Tools Used
- README Reader Tool
- Keyword Extraction Tool
- README Section Checker
- **Google Gemini 2.5 Flash (via LangChain)**

---

## 🖥️ User Interface
A **Streamlit-based UI** allows users to paste README content, trigger analysis, and view structured agent outputs with friendly error handling.

---

## 🔐 Safety & Guardrails
- Input validation (empty input, size limits)
- Prompt-injection pattern detection
- Secure API key handling via environment variables
- Graceful error handling

---

## 📊 Logging & Operational Resilience
- Application-wide logging
- Workflow execution and error tracking

---

## 🧪 Testing
Includes tool-level and agent-level tests.

Run tests:
```bash
pytest
```

---

## ⚙️ Setup Instructions

### Install dependencies
```bash
pip install -r requirements.txt
```

### Configure environment variables
```env
GEMINI_API_KEY=your_api_key_here
```

### Run the application
```bash
streamlit run app.py
```

---

## 📂 Project Structure
```
AAIDC-Module3-Production-Agentic-System/
├── app.py
├── main.py
├── agents/
├── tools/
├── graph/
├── utils/
├── tests/
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📌 Limitations
- Single LLM-powered agent
- No persistent memory
- No external data ingestion

---

## 🚀 Future Enhancements
- Add memory and feedback loops
- Support GitHub repo URL ingestion
- Deploy as hosted API

---

## 🎓 Certification Context
This project fulfills **AAIDC Module 3 requirements** by demonstrating a production-ready multi-agent system using **Gemini 2.5 Flash**.

---

## 📄 License
Educational use only for Ready Tensor AAIDC.
