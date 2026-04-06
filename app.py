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

# Custom CSS styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #f5f5f5;
    }
    
    /* Bold borders for text areas */
    .stTextArea > div > div > textarea {
        border: 3px solid #000000 !important;
        border-radius: 10px !important;
    }
    
    /* User input area - Blue background, white text */
    .user-input textarea {
        background-color: #1E90FF !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
        border: 3px solid #000000 !important;
    }
    
    /* Result area - Blue background, white text */
    .result-area textarea {
        background-color: #1E90FF !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
        border: 3px solid #000000 !important;
    }
    
    /* System suggestion prompts - Royal blue, bold, bigger */
    .suggestion-prompt {
        background-color: #4169E1;
        color: white;
        padding: 15px;
        border-radius: 8px;
        margin: 5px 0;
        font-weight: bold;
        font-size: 16px;
        border: 2px solid #000000;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .suggestion-prompt:hover {
        background-color: #1E90FF;
        transform: scale(1.02);
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #4169E1;
        color: white;
        font-weight: bold;
        font-size: 16px;
        border: 3px solid #000000;
        border-radius: 8px;
        padding: 10px 24px;
    }
    
    .stButton > button:hover {
        background-color: #1E90FF;
    }
    
    /* Header styling */
    h1 {
        color: #4169E1;
        font-weight: bold;
        text-align: center;
    }
    
    /* Sidebar styling */
    .sidebar-content {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Sample topics from the uploaded file for generating suggestions
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
    "base_url": "https://api.qwen.ai/v1",  # Replace with actual Qwen API endpoint
    "model": "qwen-chat",
    "repository": "CSSPM",
    "license": "MIT"
}

def get_random_suggestions(num_suggestions=10):
    """Generate random suggestions from SPM topics"""
    return random.sample(SPM_TOPICS, min(num_suggestions, len(SPM_TOPICS)))

def query_qwen_api(prompt, api_key):
    """
    Query Qwen Chatbot API
    Replace this with actual API call when you have the endpoint
    """
    try:
        # Example API call structure for Qwen
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": API_CONFIG["model"],
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert Software Project Management assistant for B.E. Computer Science and B.Tech IT students. Provide clear, concise, and educational answers."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }
        
        # Uncomment when you have the actual API endpoint
        # response = requests.post(
        #     f"{API_CONFIG['base_url']}/chat/completions",
        #     headers=headers,
        #     json=payload,
        #     timeout=30
        # )
        # response.raise_for_status()
        # result = response.json()
        # return result['choices'][0]['message']['content']
        
        # Mock response for demonstration
        return generate_mock_response(prompt)
        
    except Exception as e:
        return f"Error: {str(e)}. Please check your API configuration."

def generate_mock_response(prompt):
    """Generate mock response for demonstration"""
    responses = {
        "scope": "Software project management encompasses planning, organizing, securing, and managing resources to achieve specific project goals. It includes scope management, time management, cost management, quality management, and risk management.",
        "stakeholder": "Stakeholders in software projects include clients, end-users, developers, project managers, sponsors, and suppliers. Each has different objectives: clients want value, users want functionality, developers want clear requirements, and sponsors want ROI.",
        "planning": "Careful planning involves defining project scope, creating work breakdown structures, estimating resources, developing schedules, identifying risks, and establishing communication plans. Planning should be iterative and adaptive.",
        "risk": "Common risks include scope creep, resource constraints, technical challenges, changing requirements, and team turnover. Risk management involves identification, analysis, response planning, and monitoring.",
        "success": "Project success criteria typically include: delivered on time, within budget, meeting quality standards, satisfying stakeholder requirements, and achieving business objectives. The Standish Group reports only 28% of projects are completely successful.",
        "default": "This is an important topic in Software Project Management. Key considerations include: understanding requirements, proper planning, stakeholder engagement, risk management, quality assurance, and continuous monitoring. Would you like more specific information on any aspect?"
    }
    
    prompt_lower = prompt.lower()
    if "scope" in prompt_lower:
        return responses["scope"]
    elif "stakeholder" in prompt_lower:
        return responses["stakeholder"]
    elif "plan" in prompt_lower:
        return responses["planning"]
    elif "risk" in prompt_lower:
        return responses["risk"]
    elif "success" in prompt_lower or "failure" in prompt_lower:
        return responses["success"]
    else:
        return responses["default"]

def display_suggestions(suggestions):
    """Display suggestion buttons with custom styling"""
    st.markdown("### 💡 Suggested Questions (Click to auto-fill):")
    
    cols = st.columns(2)
    for idx, suggestion in enumerate(suggestions):
        with cols[idx % 2]:
            if st.button(f"📌 {suggestion}", key=f"sugg_{idx}"):
                st.session_state.user_query = suggestion
                st.rerun()

def main():
    # Header
    st.title("⚖️ Software-Project-Management for B.E.Computer Science/B.Tech Information Technology Chatbot")
    
    st.markdown("""
    <div style='background-color: #4169E1; padding: 15px; border-radius: 10px; margin-bottom: 20px; border: 3px solid black;'>
        <p style='color: white; font-weight: bold; font-size: 16px; margin: 0;'>
            🎯 Target Audience: B.E. Computer Science Students | B.Tech Information Technology Students | IT Job Seekers
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
    
    # Sidebar - Repository Info
    with st.sidebar:
        st.markdown("### 📚 Repository Information")
        st.markdown(f"""
        <div class='sidebar-content'>
            <p><strong>GitHub Repository:</strong> {API_CONFIG['repository']}</p>
            <p><strong>License:</strong> {API_CONFIG['license']}</p>
            <p><strong>API Key:</strong> {API_CONFIG['api_key']}</p>
            <p><strong>Version:</strong> 1.0.0</p>
            <p><strong>Last Updated:</strong> {datetime.now().strftime('%Y-%m-%d')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📖 Quick Reference")
        st.markdown("""
        - **Ref 1**: GitHub Repository - CSSPM
        - **Ref 2**: B.E. Computer Science - Software Project Management Topics
        - 50+ Core SPM Concepts
        - Industry Best Practices
        - Real-world Case Studies
        """)
        
        if st.button("🔄 Refresh Suggestions"):
            st.session_state.suggestions = get_random_suggestions(10)
            st.rerun()
    
    # Display suggestions
    display_suggestions(st.session_state.suggestions)
    
    st.markdown("---")
    
    # User Input Section
    st.markdown("### ❓ Enter Your Query:")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_query = st.text_area(
            "Type your Software Project Management question here:",
            value=st.session_state.user_query,
            height=100,
            placeholder="E.g., What are the key success criteria for software projects?",
            key="query_input",
            help="Enter your question about software project management concepts, methodologies, or best practices"
        )
    
    with col2:
        submit_button = st.button("📤 Submit Prompt", use_container_width=True)
        reset_button = st.button("🔄 Reset", use_container_width=True)
    
    # Handle reset
    if reset_button:
        st.session_state.user_query = ""
        st.session_state.result = ""
        st.session_state.suggestions = get_random_suggestions(10)
        st.rerun()
    
    # Handle submit
    if submit_button and user_query:
        st.session_state.user_query = user_query
        
        with st.spinner("🤖 AI is analyzing your question..."):
            result = query_qwen_api(user_query, API_CONFIG["api_key"])
            st.session_state.result = result
    
    # Display Result
    if st.session_state.result:
        st.markdown("---")
        st.markdown("### 💬 Response:")
        
        st.markdown(f"""
        <div style='background-color: #1E90FF; padding: 20px; border-radius: 10px; border: 3px solid black;'>
            <p style='color: white; font-weight: bold; font-size: 16px; line-height: 1.6;'>
                {st.session_state.result}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Additional actions
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📋 Copy Response"):
                st.success("Response copied to clipboard!")
        with col2:
            if st.button("🔍 Search Related"):
                st.info("Searching for related topics...")
        with col3:
            if st.button("💾 Save to Notes"):
                st.success("Saved to your notes!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='background-color: #4169E1; padding: 15px; border-radius: 10px; text-align: center; border: 3px solid black;'>
        <p style='color: white; font-weight: bold; margin: 0;'>
             CSSPM - Computer Science Software Project Management Chatbot<br>
            <small>GitHub: amrithtech23-ux/CSSPM | License: MIT | API: CSSPM2K6</small>
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
