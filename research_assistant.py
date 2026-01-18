import warnings
from typing import TypedDict, Dict, List
from langgraph.graph import StateGraph, START, END
from tools import perform_search, scrape_url 

warnings.filterwarnings("ignore")

# 1. SHARED STATE
class ResearchState(TypedDict):
    topic: str
    sections: Dict[str, dict] 
    final_report: str

# 2. SEARCH AGENT
def search_agent(state: ResearchState):
    topic = state['topic']
    
    missions = {
        "overview": f"{topic} comprehensive overview definition",
        "details": f"{topic} key facts technical details statistics architecture",
        "updates": f"{topic} latest news updates outcome 2024 2025"
    }
    
    found_data = {}
    
    for section, query in missions.items():
        candidates = perform_search(query, max_results=3)
        if candidates:
            found_data[section] = {"candidates": candidates, "best_content": ""}
    
    return {"sections": found_data}

# 3. SUMMARIZER AGENT
def summarizer_agent(state: ResearchState):
    sections = state['sections']
    
    for key, data in sections.items():
        candidates = data.get('candidates', [])
        best_content = ""
        final_url = ""
        
        for candidate in candidates:
            url = candidate['url']
            content = scrape_url(url) # Using the tool
            
            if content:
                best_content = content
                final_url = url
                break
        
        if not best_content and candidates:
            best_content = f"**[Summary from Search]:** {candidates[0]['snippet']}"
            final_url = candidates[0]['url']
            
        sections[key]['best_content'] = best_content
        sections[key]['final_url'] = final_url
            
    return {"sections": sections}

# 4. SYNTHESIS AGENT
def synthesis_agent(state: ResearchState):
    s = state['sections']
    topic = state['topic']
    
    def get_data(key):
        return s.get(key, {}).get('best_content', 'Data not available.')

    def get_source(key):
        return s.get(key, {}).get('final_url', 'N/A')

    final_output = f"""
    DEEP RESEARCH REPORT: {topic.upper()}
    
    1. OVERVIEW & INTRODUCTION
    --------------------------
    {get_data('overview')}
    
    (Source: {get_source('overview')})
    
    
    2. KEY DETAILS & DEEP DIVE
    --------------------------
    {get_data('details')}
    
    (Source: {get_source('details')})
    
    
    3. LATEST UPDATES & FINDINGS
    ----------------------------
    {get_data('updates')}
    
    (Source: {get_source('updates')})
    
    
    """
    return {"final_report": final_output}

# 5. GRAPH SETUP
workflow = StateGraph(ResearchState)
workflow.add_node("Search", search_agent)
workflow.add_node("Summarize", summarizer_agent)
workflow.add_node("Synthesis", synthesis_agent)

workflow.add_edge(START, "Search")
workflow.add_edge("Search", "Summarize")
workflow.add_edge("Summarize", "Synthesis")
workflow.add_edge("Synthesis", END)

app = workflow.compile()