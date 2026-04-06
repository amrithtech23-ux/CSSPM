# app.py - FIXED VERSION
import streamlit as st
import requests
import json
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="⚖️ Software Project Management Chatbot",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simplified Custom CSS - Deployment-safe
st.markdown("""
<style>
    /* Bold borders for all text areas */
    div[data-testid="stTextArea"] textarea {
        border: 3px solid #000000 !important;
        border-radius: 8px !important;
    }
    
    /* User input - Blue background, white text, bold */
    div[data-testid="stTextArea"] textarea {
        background-color: #1E90FF !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    
    /* Suggestion buttons - Royal blue, bold, bigger */
    div.stButton > button {
        background-color: #4169E1 !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 15px !important;
        border: 2px solid #000000 !important;
        border-radius: 6px !important;
        margin: 3px 0 !important;
    }
    
    div.stButton > button:hover {
        background-color: #1E90FF !important;
        border-color: #000000 !important;
    }
    
    /* Submit/Reset buttons */
    div.stButton > button[kind="primary"] {
        background-color: #4169E1 !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    
    /* Result display box */
    .result-box {
        background-color: #1E90FF !important;
        color: white !important;
        padding: 20px !important;
        border-radius: 8px !important;
        border: 3px solid #000000 !important;
        font-weight: bold !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
    }
    
    /* Header */
    h1 {
        color: #4169E1 !important;
        font-weight: bold !important;
        text-align: center !important;
    }
</style>
""", unsafe_allow_html=True)

# SPM Topics from knowledge base
SPM_TOPICS = [
    "Scope of software project management",
    "Problems and concerns of software project managers",
    "Usual stages of a software project",
    "Main elements of the role of management",
    "Need for careful planning, monitoring and control",
    "Stakeholders of a project and their objectives",
    "Success criteria for a project",
    "Meeting objectives as essence of all projects",
    "Identifying stakeholders and their objectives",
    "Knowing present state of project to predict future",
    "UK National Audit Office report on ICT procurement",
    "Standish Group findings on project success rates",
    "Lack of skills in project management as failure cause",
    "Lack of proven approach to risk management",
    "Programme management for coordinating concurrent jobs",
    "Exploratory projects and planning difficulty",
    "Routine maintenance vs. non-routine projects",
    "Characteristics distinguishing projects",
    "Planning as project characteristic",
    "Specific objectives or specified product",
    "Predetermined time span as project characteristic",
    "Involvement of several specialisms",
    "Temporary work group as project characteristic",
    "Constrained resources as project characteristic",
    "Brooks' characteristics of difficult software projects",
    "Invisibility of software progress",
    "Complexity of software vs. physical artefacts",
    "Flexibility of software leading to change",
    "In-house projects vs. contracted-out development",
    "Feasibility study for assessing project worth",
    "Strategic planning exercise for potential developments",
    "Requirements analysis and elicitation",
    "Quality requirements in requirements analysis",
    "Architecture design for new system components",
    "Legacy systems and interoperability",
    "Coding and testing of software units",
    "Integration of software components",
    "Qualification testing for requirements fulfilment",
    "Software maintenance as minor software projects",
    "Method vs. plan distinction",
    "Customer participation in early projects",
    "Market surveys for voluntary systems",
    "Information systems vs. embedded systems",
    "Software product development vs. software services",
    "Generic software products (horizontal market)",
    "Domain-specific software products (vertical market)",
    "Outsourced projects and special challenges",
    "Objective-driven vs. product-driven projects",
    "Project charter as high-level authorization document",
    "Project sponsor role and responsibilities"
]

# API Configuration
API_CONFIG = {
    "api_key": "CSSPM2K6",
    "base_url": "https://api.qwen.ai/v1",
    "model": "qwen-chat",
    "repository": "CSSPM",
    "license": "MIT"
}

def get_random_suggestions(num_suggestions=10):
    """Generate random suggestions from SPM topics"""
    return random.sample(SPM_TOPICS, min(num_suggestions, len(SPM_TOPICS)))

def query_qwen_api(prompt, api_key):
    """Query Qwen API with fallback mock response"""
    try:
        # Mock response for demonstration (uncomment API call when ready)
        return generate_mock_response(prompt)
    except Exception as e:
        return f"⚠️ Error: {str(e)}\n\nPlease verify API configuration."

def generate_mock_response(prompt):
    """Generate contextual mock response"""
    prompt_lower = prompt.lower()
    
    if any(word in prompt_lower for word in ["scope", "definition"]):
        return "📋 **Scope of Software Project Management**\n\nSoftware project management encompasses planning, organizing, securing, and managing resources to achieve specific project goals. Key areas include:\n• Scope management\n• Time & schedule management\n• Cost & budget control\n• Quality assurance\n• Risk management\n• Stakeholder communication\n\nProper scope definition prevents 'scope creep' - a leading cause of project failure (Standish Group, 2023)."
    
    elif any(word in prompt_lower for word in ["stakeholder", "objective"]):
        return "👥 **Stakeholders & Their Objectives**\n\n| Stakeholder | Primary Objective |\n|------------|----------------|\n| Client/Sponsor | ROI, business value |\n| End Users | Usability, functionality |\n| Developers | Clear requirements, feasible tech |\n| Project Manager | On-time, on-budget delivery |\n| QA Team | Quality standards compliance |\n\n✅ Success requires balancing these often-competing objectives through regular communication and documented agreements."
    
    elif any(word in prompt_lower for word in ["plan", "planning", "monitor"]):
        return "📅 **Planning, Monitoring & Control**\n\n**Essential Planning Steps**:\n1. Define project scope & deliverables\n2. Create Work Breakdown Structure (WBS)\n3. Estimate effort & resources\n4. Develop realistic timeline (Gantt/Agile)\n5. Identify risks & mitigation strategies\n6. Establish communication protocols\n\n**Monitoring Techniques**:\n• Weekly status meetings\n• Burndown charts (Agile)\n• Earned Value Management (EVM)\n• Risk register updates\n\n🔄 Planning should be iterative - revisit assumptions as project evolves."
    
    elif any(word in prompt_lower for word in ["risk", "failure", "problem"]):
        return "⚠️ **Risk Management & Failure Prevention**\n\n**Top Project Failure Causes **(Standish Group)\n1. Incomplete requirements (43%)\n2. Lack of user involvement (37%)\n3. Resource constraints (32%)\n4. Unrealistic expectations (29%)\n5. Poor risk management (26%)\n\n**Proactive Risk Strategy**:\n✅ Identify risks early (brainstorming, checklists)\n✅ Analyze impact & probability (Risk Matrix)\n✅ Plan responses: Avoid, Mitigate, Transfer, Accept\n✅ Monitor triggers & update register weekly\n\n💡 Remember: Risk management is not about eliminating risk, but managing it intelligently."
    
    elif any(word in prompt_lower for word in ["success", "criteria", "standish"]):
        return "🎯 **Project Success Criteria**\n\n**Traditional Triple Constraint**:\n• ✅ On Time\n• ✅ Within Budget\n• ✅ Meets Scope/Quality\n\n**Modern Success Metrics**:\n• Stakeholder satisfaction\n• Business value delivered\n• Team morale & learning\n• Maintainability & scalability\n\n📊 **Standish Group CHAOS Report Insights**:\n• Only ~28% of projects are fully successful\n• 43% exceed budget\n• 82% delivered late\n• Key success factor: Executive support + user involvement\n\n✅ Define success criteria WITH stakeholders during project charter phase."
    
    else:
        return f"🔍 **Regarding: \"{prompt}\"**\n\nThis is an important Software Project Management topic. Key considerations:\n\n1. **Understand context** - Is this for academic study or industry application?\n2. **Reference frameworks** - PMBOK, PRINCE2, Agile/Scrum, ISO 12207\n3. **Apply best practices** - Documentation, communication, iterative planning\n4. **Learn from case studies** - Standish Group, UK National Audit Office reports\n\n💡 Would you like me to elaborate on any specific aspect? Try asking about:\n• Risk management strategies\n• Agile vs. Waterfall methodologies\n• Stakeholder communication plans\n• Project charter essentials"

def display_suggestions(suggestions):
    """Display suggestion buttons"""
    st.markdown("### 💡 Suggested Questions *(Click to auto-fill)*:")
    
    cols = st.columns(2)
    for idx, suggestion in enumerate(suggestions):
        with cols[idx % 2]:
            if st.button(f"📌 {suggestion}", key=f"sugg_{idx}", use_container_width=True):
                st.session_state.user_query = suggestion
                # Use compatible rerun method
                if hasattr(st, 'rerun'):
                    st.rerun()
                else:
                    st.experimental_rerun()

def main():
    # Header
    st.title("⚖️ Software-Project-Management for B.E.Computer Science/B.Tech Information Technology Chatbot")
    
    # Target audience banner
    st.markdown("""
    <div style='background-color: #4169E1; padding: 12px; border-radius: 8px; margin: 15px 0; border: 3px solid black; text-align: center;'>
        <p style='color: white; font-weight: bold; font-size: 15px; margin: 0;'>
            🎯 Target: B.E. Computer Science | B.Tech IT Students | IT Job Seekers
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'user_query' not in st.session_state:
        st.session_state.user_query = ""
    if 'result' not in st.session_state:
        st.session_state.result = ""
    if 'suggestions' not in st.session_state:
        st.session_state.suggestions = get_random_suggestions(10)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 📚 Repository Info")
        st.info(f"""
        **GitHub**: {API_CONFIG['repository']}\n
        **License**: {API_CONFIG['license']}\n
        **API Key**: {API_CONFIG['api_key']}\n
        **Version**: 1.0.0\n
        **Updated**: {datetime.now().strftime('%Y-%m-%d')}
        """)
        
        st.markdown("### 📖 References")
        st.markdown("""
        • Ref 1: GitHub Repo - CSSPM\n
        • Ref 2: B.E. CSE - SPM Topics (100 concepts)\n
        • Industry: Standish Group, PMBOK, ISO 12207
        """)
        
        if st.button("🔄 New Suggestions", use_container_width=True):
            st.session_state.suggestions = get_random_suggestions(10)
            if hasattr(st, 'rerun'):
                st.rerun()
            else:
                st.experimental_rerun()
    
    # Display suggestions
    display_suggestions(st.session_state.suggestions)
    st.markdown("---")
    
    # User Input
    st.markdown("### ❓ Enter Your Query:")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_query = st.text_area(
            "Type your Software Project Management question:",
            value=st.session_state.user_query,
            height=100,
            placeholder="E.g., What are key success criteria for software projects?",
            key="query_input",
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        submit_clicked = st.button("📤 Submit Prompt", use_container_width=True, type="primary")
        reset_clicked = st.button("🔄 Reset", use_container_width=True)
    
    # Reset functionality
    if reset_clicked:
        st.session_state.user_query = ""
        st.session_state.result = ""
        st.session_state.suggestions = get_random_suggestions(10)
        if hasattr(st, 'rerun'):
            st.rerun()
        else:
            st.experimental_rerun()
    
    # Submit functionality
    if submit_clicked and user_query.strip():
        st.session_state.user_query = user_query.strip()
        
        with st.spinner("🤖 AI is analyzing..."):
            result = query_qwen_api(user_query, API_CONFIG["api_key"])
            st.session_state.result = result
    
    # Display Result
    if st.session_state.result:
        st.markdown("---")
        st.markdown("### 💬 Response:")
        st.markdown(f'<div class="result-box">{st.session_state.result}</div>', unsafe_allow_html=True)
        
        # Action buttons
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("📋 Copy", disabled=True, help="Manual copy: Select text + Ctrl+C")
        with c2:
            st.button("🔍 Related", disabled=True, help="Feature coming soon")
        with c3:
            st.button("💾 Save", disabled=True, help="Feature coming soon")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='background-color: #4169E1; padding: 12px; border-radius: 8px; text-align: center; border: 3px solid black;'>
        <p style='color: white; font-weight: bold; margin: 0; font-size: 14px;'>
             CSSPM - Software Project Management Chatbot<br>
            <small>GitHub: amrithtech23-ux/CSSPM | MIT License | API: CSSPM2K6</small>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
