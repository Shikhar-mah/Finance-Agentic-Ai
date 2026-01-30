# 📊 Agentic Financial Advisor using Agno

An **agent-based AI financial analysis system** built using the **Agno framework**, designed to provide structured, explainable **short-term and long-term investment insights** by coordinating multiple specialized AI agents.

This project demonstrates how agent orchestration, tool integration, and modular design can be applied to real-world financial decision support systems.

---

## 🚀 Features

* 🧠 **Multi-Agent Architecture** with clear role separation
* 🌐 **Real-time financial news retrieval** using web search tools
* 📈 **Short-term trading analysis** based on technical indicators and sentiment
* 🏦 **Long-term investment analysis** using fundamental metrics
* 🧩 **Central Orchestrator Agent** enforcing a deterministic workflow
* 📑 **Well-structured, explainable Markdown reports**
* 🔍 Transparent agent outputs for debugging and evaluation

---

## 🏗️ System Architecture

The system consists of **four specialized agents** coordinated through an Agno `Team`.

### 1. Web Search Agent

* Fetches the latest financial news and market context
* Uses **DuckDuckGoTools**
* Ensures all analysis is based on recent and credible information

### 2. Short-Term Financial Advice Agent

* Focuses on **short-term trading opportunities** (days to weeks)
* Analyzes momentum, sentiment, and technical signals
* Uses **YFinanceTools**

### 3. Long-Term Financial Advice Agent

* Performs **fundamental and strategic analysis** (months to years)
* Evaluates company health, valuation metrics, and growth potential
* Uses **YFinanceTools**

### 4. Orchestrator Agent

* Acts as the **central controller**
* Delegates tasks in a fixed order
* Combines all agent outputs into a unified investment report
* Highlights conflicts between short-term and long-term perspectives

---

## 🔄 Execution Flow

```
User Query
   ↓
Financial Advice Team
   ↓
Orchestrator Agent
   ↓
Web Search Agent (News & Market Context)
   ↓
Parallel Execution
   ├── Short-Term Agent (Technical Analysis)
   └── Long-Term Agent (Fundamental Analysis)
   ↓
Orchestrator Agent (Synthesis)
   ↓
Final Structured Financial Report
```

---

## 🧰 Tech Stack

* **Framework:** Agno
* **LLM:** Groq – `llama-3.3-70b-versatile`
* **Search Tools:** DuckDuckGoTools
* **Market Data:** YFinanceTools
* **Language:** Python
* **Environment Management:** python-dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install agno python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Running the Project

Execute the main script:

```bash
python main.py
```

Example query used in the project:

```text
Get me comprehensive analysis of NVIDIA stock including current news, short-term trading advice, and long-term investment strategy
```

The system will stream responses and display outputs from each agent for transparency.

---

## 📄 Output Format

The final response includes:

* Executive Summary
* Current Market Context
* Short-Term Trading Outlook
* Long-Term Investment Strategy
* Integrated Risk Assessment
* Final Combined Recommendation

All outputs are rendered in **Markdown** for readability.

---

## 📌 Key Design Highlights

* **Deterministic workflow** using zero-temperature LLM configuration
* **Parallel agent execution** for efficiency
* **Single source of truth** via shared market data
* **Explainable AI decisions** through agent-level outputs

---

## 🔮 Future Enhancements

* Real-time streaming market data
* Portfolio-level optimization
* Advanced risk modeling
* Backtesting of strategies
* Persistent memory for long-term market tracking
* User-defined risk profiles

---

## ⚠️ Disclaimer

This project is for **educational and experimental purposes only**.
It does **not** constitute financial advice. Always consult a licensed financial advisor before making investment decisions.
