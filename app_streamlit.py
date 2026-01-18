import streamlit as st
import time
from research_assistant import app

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Deep Research Agent",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CUSTOM CSS (WHITE TEXT FIX)
# ==========================================
st.markdown("""
    <style>
    /* Main Title Styling */
    .main-header {
        text-align: center;
        color: #4A90E2;
        font-family: 'Helvetica', sans-serif;
        margin-bottom: 20px;
    }
    
    /* FORCE WHITE TEXT
       Targeting paragraphs, divs, lists, and headers inside Markdown 
    */
    .stMarkdown p, .stMarkdown div, .stMarkdown li, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        font-family: 'Georgia', serif !important;
        font-size: 16px !important;
        line-height: 1.6 !important;
        color: #ffffff !important; /* <--- FIXED: Changed from #2c3e50 to WHITE */
    }
    
    /* Optional: Style the container border to look good in dark mode */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #444;
        border-radius: 10px;
        padding: 20px;
        background-color: transparent; /* Let the dark theme background show through */
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        font-weight: bold;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. SIDEBAR
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6165/6165576.png", width=80)
    st.title("Research Config")
    st.markdown("---")
    topic = st.text_input("Research Topic", placeholder="e.g., Quantum Computing 2025")
    run_btn = st.button("🚀 Start Research", type="primary")

# ==========================================
# 4. MAIN CONTENT
# ==========================================
st.markdown("<h1 class='main-header'>🕵️‍♂️ Deep Research Agent</h1>", unsafe_allow_html=True)

if run_btn and topic:
    result_container = st.container()
    
    with st.status("🤖 Agents are working...", expanded=True) as status:
        st.write("🕵️‍♂️ **Search Agent:** Analyzing topic...")
        time.sleep(0.5)
        st.write("📝 **Summarizer Agent:** Reading and cleaning text...")
        
        try:
            initial_state = {"topic": topic, "sections": {}, "final_report": ""}
            result = app.invoke(initial_state)
            
            st.write("✍️ **Synthesis Agent:** Compiling report...")
            status.update(label="✅ Research Complete!", state="complete", expanded=False)
            
            # Display Result
            with result_container:
                st.success("Report generated successfully!")
                st.markdown("### 📄 Final Report")
                
                # Use simple container with border
                with st.container(border=True):
                    st.markdown(result['final_report'])
                
                # Download Button
                st.download_button(
                    label="📥 Download Report as Text",
                    data=result['final_report'],
                    file_name=f"{topic.replace(' ', '_')}_Research.txt",
                    mime="text/plain"
                )
                
        except Exception as e:
            status.update(label="❌ Error", state="error")
            st.error(f"Error: {e}")

elif run_btn:
    st.warning("⚠️ Please enter a topic.")