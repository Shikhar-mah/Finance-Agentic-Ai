"""
This is Finance Ai Agent. It's purpose is to:
    1. Fetch the news for the requested stock/information
    2. Analyse the news that was fetched
    3. Based on the analysis providing a suggestion response to the client

Overview of the Project/How the code Flows:
    1. We give it an api key, through .env file, based on the platform we are using.
    2. Test the .env file using Load_dotenv() function
    3. Providing an llm based on our needs. Here we have provided it the "llama-3.3-70b-versatile"
       with 70 billion parameters through the Groq.com api.
    4. Next we create two agents based on our needs, 
        i. Web search agent: It searches the web scraping for any relevant information based on the
           prompt it is provided.
           It has access to duckduckgo search tools which helps it searching the internet for
           relevant results.
        ii. Short term financial advisor agent: Based on the search results fetched it does an analyses on them and
           provides the user with a relevant short term investment risks and suggestion. 
        iii. Long Term Financial advisor agent: Based on the search results fetched it does an analyses on them and
           provides the user with a relevant short term investment risks and suggestion.
           Both the Short term and the long term agents have access to the YfinanceTools() tool. This helps them 
           make better financial decisions.
        iv. Orchestrator agent: This is the heart of our entire process. This agent helps in delegating the tasks
           to the right agent. 
    5. Now we combine the four agents using a "Team" library so that it can decide easily. It's  
       task is to assign the relevant tasks to the appropriate AI agent.
    6. Then we give it the prompt. It provides us with the relevant result according to that.

"""


import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.team import Team

# Load environment variables from .env file
load_dotenv()

# Configure the LLM model 
# I'm using Groq with llama-3.3-70b-versatile - capable of handling
# multi-agent tasks with financial analysis. It has some daily free responses as well
llm = Groq(
    id="llama-3.3-70b-versatile", 
    temperature=0 # Zero temperature for deterministic, consistent financial analysis
)


# ============================================================================
# AGENT 1: WEB SEARCH AGENT
# ============================================================================
web_search_agent = Agent(
    name="Web Search Agent",
    description=(
        "this agent specializes in gathering real-time financial data, news, and market "
        "information from the web. Your primary job is to collect data "
        "for the entire analysis pipeline."
    ),
    model=llm,
    tools=[DuckDuckGoTools()],  # Web search capability for real-time data
    instructions=[
        "Search for the most recent and relevant financial news/articles (last 7 days preferred)",
        "Focus on credible sources: financial news outlets, official company announcements, market analyses"
    ],
    markdown=True,  # Output formatted in Markdown for better readability
)


# ============================================================================
# AGENT 2: SHORT-TERM FINANCIAL ADVICE AGENT
# ============================================================================
short_term_financialAdvice_agent = Agent(
    name="Short-Term Financial Advice Agent",
    description=(
        "this agent specializes in short-term investment analysis (days to weeks). It focuses on "
        "technical indicators, market sentiment, news impact, and momentum-based "
        "trading opportunities."
    ),
    model=llm,
    tools=[YFinanceTools()],  # Access to real-time stock data and technical indicators
    instructions=[
        "Analyze data for SHORT-TERM trading perspective (days to 3 months maximum)"
    ],
    markdown=True,
)


# ============================================================================
# AGENT 3: LONG-TERM FINANCIAL ADVICE AGENT
# ============================================================================
long_term_financialAdvice_agent = Agent(
    name="Long-Term Financial Advice Agent",
    description=(
        "This agent specializes in long-term investment analysis (months to years). Focuses on "
        "fundamental analysis, company health, industry trends, growth potential, "
        "and value investing principles."
    ),
    model=llm,
    tools=[YFinanceTools()],  # Access to financial statements and fundamental data
    instructions=[
        "Analyze data for LONG-TERM investment perspective (3 months to 5+ years)",
        "Focus on fundamental analysis: P/E ratios, P/B ratios, debt-to-equity, ROE, ROIC"
    ],
    markdown=True,
)


# ============================================================================
# AGENT 4: ORCHESTRATOR AGENT
# ============================================================================
orchestrator_agent = Agent(
    name="Financial Analysis Orchestrator",
    description=(
        "Master coordinator that manages the entire financial analysis workflow. "
        "This agent receives user queries, decomposes them into subtasks, delegates "
        "to specialized agents, and synthesizes their outputs into a comprehensive report."
    ),
    model=llm,
    instructions=[
        "FOLLOW THIS EXACT WORKFLOW FOR EVERY FINANCIAL ANALYSIS QUERY:",
        "",
        "STEP 1 - DATA COLLECTION:",
        "   - Delegate to Web Search Agent to gather current news and market data",
        "   - Ensure it collects: recent news, price data, market sentiment",
        "   - Wait for and store the complete web search results",
        "",
        "STEP 2 - PARALLEL ANALYSIS:",
        "   - Simultaneously delegate to both Short-Term and Long-Term Financial Advice Agents",
        "   - Provide BOTH agents with the complete web search results",
        "   - Instruct Short-Term agent to focus on immediate technical factors",
        "   - Instruct Long-Term agent to focus on fundamental and strategic factors",
        "",
        "STEP 3 - SYNTHESIS:",
        "   - Collect outputs from all three specialized agents",
        "   - Combine insights into a unified comprehensive analysis",
        "   - Structure the final report with clear sections:",
        "       1. Executive Summary",
        "       2. Current Market Context (from Web Search Agent)",
        "       3. Short-Term Outlook & Trading Strategy",
        "       4. Long-Term Outlook & Investment Strategy",
        "       5. Integrated Risk Assessment",
        "       6. Final Combined Recommendation",
        "",
        "GENERAL RULES:",
        "   - Always use ALL THREE specialized agents for complete financial analysis",
        "   - Never skip any agent in the workflow",
        "   - Ensure recommendations from different time horizons are clearly distinguished",
        "   - Highlight any conflicts between short-term and long-term views",
        "   - Present final output in professional, well-structured Markdown format",
        "   - Include clear headers, bullet points, and tables for readability"
    ],
    markdown=True,
)


# ============================================================================
# AGENT 5: FINANCIAL ADVICE TEAM
# ============================================================================
financial_advice_team = Team(
    name="Comprehensive Financial Advisory Team",
    members=[
        orchestrator_agent,           # Master coordinator
        web_search_agent,             # Data collection specialist
        short_term_financialAdvice_agent,  # Short-term analysis specialist
        long_term_financialAdvice_agent    # Long-term analysis specialist
    ],
    model=llm,
    instructions=(
        "This is a coordinated team for comprehensive financial analysis. "
        "The Orchestrator Agent is the team lead and MUST be used for every query. "
        ""
        "TEAM PROTOCOL:"
        "1. All user queries are first handled by the Orchestrator Agent"
        "2. Orchestrator decomposes the query and delegates to appropriate specialists"
        "3. Web Search Agent always runs first to gather current data"
        "4. Both Short-Term and Long-Term agents analyze the same data from different perspectives"
        "5. Orchestrator synthesizes all outputs into a unified report"
        ""
        "RESPONSE FORMAT REQUIREMENTS:"
        "- Use clear hierarchical headers (##, ###)"
        "- Include executive summary at the beginning"
        "- Separate short-term and long-term analyses clearly"
        "- Use tables for financial metrics"
        "- Include risk disclosures and limitations"
        "- Cite sources for all external data"
    ),

    # Team-level settings
    show_members_responses=True,  # Show outputs from all agents for transparency
    markdown=True
)


# ============================================================================
# EXECUTION EXAMPLE
# ============================================================================

# Example query for NVIDIA analysis
query = "Get me comprehensive analysis of NVIDIA stock including current news, short-term trading advice, and long-term investment strategy"
    
response = financial_advice_team.print_response(
        query,
        stream=True,  # Stream response for better user experience
        show_members_responses=True  # Show individual agent contributions
)