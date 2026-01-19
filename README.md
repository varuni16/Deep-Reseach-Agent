# 🕵️‍♂️ Deep Research AI Agent

### Autonomous Research Assistant powered by LangGraph & Streamlit

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic%20Workflow-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 🔴 [Live Demo: Click Here to Try the App](https://share.streamlit.io/varuni16/deep-reseach-agent)
*(Note: If the app is sleeping, click "Wake App" to start the agents)*

---

## 📖 Overview
The **Deep Research Agent** is an autonomous multi-agent system designed to perform comprehensive web research on any given topic. Unlike simple search wrappers, this agent orchestrates a team of specialized AI workers to **plan, search, read, and write** detailed academic-style reports.

Built with **LangGraph** for state management and **Streamlit** for a professional frontend, it solves the problem of information overload by autonomously synthesizing data from multiple sources into a coherent document.

## 🤖 How It Works (The Architecture)
The system uses a **StateGraph** workflow with four distinct agents:

1.  **🕵️‍♂️ Search Agent:** Breaks down the user's topic into sub-queries (Overview, Details, Latest Updates) and finds high-quality sources using DuckDuckGo.
2.  **📝 Summarizer Agent:** Visits found URLs, scrapes the content using `Trafilatura`, and extracts key information. It includes intelligent fallback logic to skip unreadable PDFs or blocked sites.
3.  **✍️ Synthesis Agent:** Compiles all gathered information into a structured, academic-format report with citations.

## 🚀 Key Features
* **Autonomous Research:** Just enter a topic (e.g., "Future of AI 2025"), and the agents handle the rest.
* **Smart Scraping:** Custom logic to filter out broken links, skip PDFs, and bypass basic anti-bot protections.
* **Self-Correction:** If a source is blocked, the agent automatically retries with alternative candidates.
* **Professional UI:** Dark-mode optimized Streamlit interface with real-time status updates.
* **Downloadable Reports:** Users can export the final research as a text file.

## 🛠️ Tech Stack
* **Orchestration:** LangGraph, LangChain
* **Frontend:** Streamlit
* **Search Engine:** DuckDuckGo Search API (`ddgs`)
* **Scraping:** Trafilatura
* **Language:** Python 3.x

## 💻 Installation & Usage (Run Locally)

**1. Clone the repository**
```bash
git clone [https://github.com/varuni16/Deep-Reseach-Agent.git](https://github.com/varuni16/Deep-Reseach-Agent.git)
cd Deep-Reseach-Agent
