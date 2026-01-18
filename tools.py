import re
import trafilatura
from ddgs import DDGS


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def clean_text(text: str, limit: int = 3000) -> str:
    """Cleans raw web text, removes ads/nav, and ensures complete sentences."""
    if not text: return ""
    
    text = re.sub(r'\[.*?\]', '', text)
    lines = text.split('\n')
    clean_lines = []
    
    for line in lines:
        l = line.strip()
        if len(l) < 50: continue 
        if l.startswith("|"): continue 
        if any(x in l.lower() for x in ["table of contents", "subscribe", "cookies", "sign up", "read more"]):
            continue
        clean_lines.append(l)
    
    full_text = " ".join(clean_lines)
    
    # Smart Truncate
    if len(full_text) > limit:
        cut_text = full_text[:limit]
        last_period = cut_text.rfind(".")
        if last_period != -1:
            full_text = cut_text[:last_period+1]
        else:
            full_text = cut_text
            
    return full_text

def perform_search(query: str, max_results: int = 3):
    """
    Searches DuckDuckGo and returns TOP 3 candidates.
    """
    candidates = []
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5, backend="lite"))
            
            for r in results:
                url = r.get('href', '').lower()
                if url.endswith('.pdf'): continue
                
                candidates.append({
                    "title": r.get('title'),
                    "url": r.get('href'),
                    "snippet": r.get('body')
                })
                if len(candidates) >= max_results:
                    break
    except Exception as e:
        print(f"Error searching for '{query}': {e}")
        
    return candidates

def scrape_url(url: str):
    """
    Tries to scrape. Returns None if failed/blocked.
    """
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            text = trafilatura.extract(downloaded)
            if text:
                cleaned = clean_text(text)
                if len(cleaned) > 200:
                    return cleaned
    except:
        return None
    return None