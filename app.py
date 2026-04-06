# app.py - UPDATED VERSION
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

# Custom CSS styling - UPDATED COLORS
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #f9f9f9;
    }
    
    /* Bold borders for all text areas */
    div[data-testid="stTextArea"] textarea {
        border: 3px solid #000000 !important;
        border-radius: 8px !important;
    }
    
    /* User input - Light gray background, bold black text */
    div[data-testid="stTextArea"] textarea {
        background-color: #D3D3D3 !important;
        color: #000000 !important;
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
    
    /* Result display box - Light gray background, bold black text */
    .result-box {
        background-color: #E8E8E8 !important;
        color: #000000 !important;
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

# Extended SPM Topics from knowledge base - AVOIDING DUPLICATES
SPM_TOPICS = [
    # Original topics from sample_topic.txt (1-50)
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
    "UK National Audit Office report on ICT procurement (2004)",
    "Standish Group findings on project success rates",
    "82% of projects late (Standish Group)",
    "43% of projects exceeding budget (Standish Group)",
    "Lack of skills in project management as failure cause",
    "Lack of proven approach to risk management as failure cause",
    "Dictionary definitions of project",
    "Programme management for coordinating concurrent jobs",
    "Exploratory projects and planning difficulty",
    "Provisional planning for uncertain projects",
    "Routine maintenance vs. non-routine projects",
    "Hazy boundary between non-routine project and routine job",
    "Characteristics distinguishing projects",
    "Non-routine tasks as project characteristic",
    "Planning as project characteristic",
    "Specific objectives or specified product as project characteristic",
    "Predetermined time span as project characteristic",
    "Work for someone other than yourself as project characteristic",
    "Involvement of several specialisms as project characteristic",
    "Temporary work group as project characteristic",
    "Several phases as project characteristic",
    "Constrained resources as project characteristic",
    "Project size and coordination difficulty",
    "Temporary sub-organizations as problematic",
    "Expertise loss when team disperses",
    "Brooks' characteristics of difficult software projects",
    "Invisibility of software progress",
    "Software project management as making invisible visible",
    "Complexity of software vs. physical artefacts",
    "Conformity to human client requirements",
    "Organizational stupidity in requirements",
    "Flexibility of software leading to change",
    "In-house projects vs. contracted-out development",
    "Contract management vs. technical project management",
    "Off-the-shelf software as software project",
    "Feasibility study for assessing project worth",
    "Feasibility study as standalone project",
    "Strategic planning exercise for potential developments",
    "Outline plan vs. detailed plan",
    "Planning later stages nearer their start",
    
    # NEW topics from Unit-02 (Business Case & Portfolio Management)
    "Contents of a typical business plan",
    "Project portfolio management overview",
    "Evaluation and selection of projects against strategic criteria",
    "Evaluation and selection of projects against technical criteria",
    "Evaluation and selection of projects against economic criteria",
    "Cost-benefit evaluation techniques for competing proposals",
    "Business risk evaluation in projects",
    "Grouping individual projects into programmes",
    "Managing programme implementation for planned benefits",
    "ICT infrastructure project as platform for subsequent projects",
    "Non-financial benefits (alleviation of pain, preservation of life)",
    "Business case as feasibility study or project justification",
    "Introduction and background in business case",
    "Proposed project description in business case",
    "Market analysis in business case (demand, competitors)",
    "Organizational and operational infrastructure planning",
    "Benefits identification and valuation in business case",
    "Outline implementation plan and milestones",
    "Cost scheduling and uncertainty in early estimates",
    "Financial case analysis methods",
    "Project risk vs. business risk distinction",
    "Portfolio definition, management, and optimization",
    "Warren McFarlan portfolio concept for information systems",
    "Single repository for all current projects",
    "New product development (NPD) vs. renewal projects",
    "NPD projects attracting funding more easily",
    "Portfolio optimization balancing high-risk/high-reward and low-risk/low-reward projects",
    "Below-the-line projects and their impact on official portfolios",
    "Advantages of allowing small ad hoc tasks (quick fixes, user satisfaction)",
    "Margin for non-planned work in resource allocation",
    
    # NEW topics from Unit-03-04 (Planning & Methodologies)
    "Step Wise project planning framework",
    "PRINCE2 project management standards (OGC sponsored)",
    "Step Wise covering only planning stages (not monitoring/control)",
    "Traditional project planning flexibility vs. standardization",
    "Brigette (Brightmouth College payroll) case study",
    "Amanda (IOE annual maintenance contracts) case study",
    "Recording equipment details for annual maintenance contracts",
    "Central coordinator allocating jobs with mobile phone notifications",
    "Outline planning before detailed planning principle",
    "Project selection in portfolio management context",
    "Project scope and objectives identification",
    "Establishing a single project authority for unity of purpose",
    "Stakeholder analysis and identification",
    "Modifying objectives based on stakeholder analysis (Theory W)",
    "Communication methods establishment (communications plan)",
    "BACS (Bankers Automated Clearing Scheme) contact point",
    "Project infrastructure identification",
    "Enterprise architecture for technical strategic decisions",
    "ERP system module for college financial processing",
    "Installation standards and procedures",
    "Change control and configuration management standards",
    "Measurement programme for statistics collection",
    "Timesheets for recording hours on individual tasks",
    "Structured systems analysis and design method",
    "PRINCE2 modelled project management guidelines",
    "Written user agreement before work",
    "Peer review and independent testing",
    "Error log and user problem log",
    "Informal Monday meetings and monthly progress reviews",
    "Project team organization (business analysts vs. developer pool)",
    "Objective-driven vs. product-driven projects",
    "Safety-critical systems (human life threatened)",
    "High-level project risks identification",
    "Iterative approach for analysis reports with marketing analyst feedback",
    "User requirements concerning implementation",
    "BS EN ISO 9001:2000 / TickIT accreditation",
    "Development methodology and life-cycle approach selection",
    "Questionnaire surveys for novel problem domains",
    "Function points for system size estimation",
    "Project products (deliverables and intermediate products)",
    "Product Breakdown Structure (PBS)",
    "Product Description (name, purpose, derivation, composition, form, standards, quality criteria)",
    "Products as persons (trained user)",
    "Common error: identifying activities as products",
    "Product Flow Diagram (PFD)",
    "Oval notation for products used but not created",
    "PFD allowing looping back via rework",
    "Textual description explaining PFD structure",
    "Product instances recognition",
    
    # NEW topics from Unit-05-06-07 (Estimation & Scheduling)
    "Dangers of unrealistic estimates in software projects",
    "Subjective nature of estimating (underestimating small tasks, overestimating large tasks)",
    "Political implications of software estimation",
    "Independent estimating group to avoid political bias",
    "Changing technology as a difficulty in estimation",
    "Lack of homogeneity of project experience",
    "ISO 12207 standard for standardizing estimation terminology",
    "Productivity calculation in SLOC per work-month",
    "Programmer productivity variation (7 to 150 SLOC/day)",
    "Strategic planning estimates for project portfolio management",
    "Feasibility study estimates confirming benefits justify costs",
    "System specification estimates for design proposals",
    "Evaluation of suppliers' proposals using estimates",
    "Parkinson's Law in software estimation",
    "Weinberg's Law (software always late)",
    "Effort vs. duration estimation parameters",
    "Person-month (PM) as effort measurement unit",
    "Project size as independent variable, effort as dependent variable",
    "Source Lines of Code (SLOC) as size metric",
    "Function Points (FP) as size metric",
    "No precise definition of SLOC as a shortcoming",
    "Difficulty estimating SLOC at project start",
    "SLOC as only a code measure (ignores other life cycle activities)",
    "Programmer-dependent nature of SLOC",
    "SLOC does not consider code complexity",
    "Mythical Man-Month concept (Brooks)",
    "Communication overhead increasing as square of team size",
    "Adding manpower to a late project makes it later",
    "Algorithmic models for effort estimation",
    "Expert judgement in estimation",
    "Estimating by analogy (case-based reasoning)",
    "Parkinson method (effort available becomes estimate)",
    "Price to win estimation",
    "Top-down vs. bottom-up estimating",
    "Work Breakdown Structure (WBS) for bottom-up estimating",
    "Procedural code-oriented bottom-up approach",
    "Estimating SLOC of each module",
    "Complexity and technical difficulty factors in estimation",
    "COCOMO II parametric productivity model",
    "COCOMO81 organic, semi-detached, embedded modes",
    "COCOMO II application composition stage",
    "COCOMO II early design stage",
    "COCOMO II post-architecture stage",
    "Object points for application composition estimation",
    "COCOMO II scale factors (precedentedness, flexibility, risk resolution, team cohesion, process maturity)",
    "COCOMO II effort multipliers",
    "Albrecht Function Point Analysis",
    "External input types in function points",
    "External output types in function points",
    "External inquiry types in function points",
    "Logical internal file types in function points",
    "External interface file types in function points",
    "IFPUG file type complexity tables",
    "Technical complexity adjustment (TCA) in function points",
    "Converting function points to lines of code by language",
    "Mark II Function Points (Symons)",
    "COSMIC Full Function Points for real-time systems",
    "COSMIC data movements (entries, exits, reads, writes)",
    "Capers Jones estimating rules of thumb",
    "SLOC to function point equivalence per language",
    "Project duration estimation using function points raised to power 0.4",
    "Rate of requirements creep (2% per month)",
    "Cost estimation from effort and overhead costs",
    "Staffing pattern and Rayleigh-Norden curve",
    "Putnam's staffing pattern for software projects",
    "Effect of schedule compression on effort (Putnam's fourth power law)",
    "Limit of schedule compression (75% of nominal time)",
    "Activity planning objectives (feasibility, resource allocation, costing, motivation, coordination)",
    "Identifying activities (activity-based, product-based, hybrid approaches)",
    "Work Breakdown Structure (WBS) with levels (project, deliverables, components, work-packages, tasks)",
    "Product Breakdown Structure (PBS) in PRINCE2",
    "Product Flow Diagram (PFD) for sequencing",
    "USDP artifacts and workflows",
    "Sequencing vs. scheduling activities",
    "Bar charts (Gantt charts) for project plans",
    "Network planning models (CPM, PERT, precedence networks)",
    "Activity-on-node vs. activity-on-arrow networks",
    "Dummy activities in activity-on-arrow networks",
    "Forward pass for earliest start/finish dates",
    "Backward pass for latest start/finish dates",
    "Total float, free float, and interfering float",
    "Critical path identification",
    "Shortening project duration by reducing critical path activities",
    "Activity standard deviation in PERT",
    "PERT three estimates (optimistic, most likely, pessimistic)",
    "PERT expected duration formula (a + 4m + b)/6",
    "Calculating probability of meeting target dates with PERT",
    "Z-value calculation for target dates",
    "Monte Carlo simulation for risk analysis",
    
    # NEW topics from Unit-08-09-10-11 (Resource Management & Control)
    "Resource allocation in Step Wise framework",
    "Activity schedule indicating planned start and completion dates",
    "Resource schedule showing dates and levels of resource requirements",
    "Cost schedule showing planned cumulative expenditure",
    "Labour as a resource category (project manager, analysts, developers)",
    "Equipment as a resource category (workstations, office equipment)",
    "Materials as a resource category (consumables like disks)",
    "Space as a resource category (office space for additional staff)",
    "Services as a resource category (telecommunications services)",
    "Time as a resource offset against other primary resources",
    "Money as a secondary resource (used to buy other resources)",
    "Identifying resource requirements by considering each activity",
    "Project infrastructure resources (project manager, office space)",
    "Resource requirements list comprehensiveness",
    "Mapping resource requirements onto activity plan",
    "Resource histogram for visualizing resource distribution",
    "Earliest start date scheduling creating peaked resource histograms",
    "Cost of changing resource levels over time (recruitment, familiarization)",
    "Idle staff time between specification and design stages",
    "Smoothing resource histograms by adjusting activity start dates",
    "Splitting non-critical activities to fill resource troughs",
    "Difficulty of splitting tasks in software projects",
    "Resource smoothing by project planning software tools",
    "Prioritizing activities for resource allocation (critical path first)",
    "Total float priority for resource allocation",
    "Burman's priority list for resource allocation",
    "Shortest critical activity priority rule",
    "Critical activities priority rule",
    "Shortest non-critical activity priority rule",
    "Non-critical activity with least float priority rule",
    "Resource smoothing not always possible within planned timescales",
    "Resource constraints creating new critical paths",
    "Resource-linked criticalities in large projects",
    "Cost comparison between additional staff and delayed delivery",
    "Allocating individuals to activities as early as possible",
    "Availability as factor in allocating individuals to tasks",
    "Criticality of activities influencing staff allocation",
    "Risk assessment guiding staff allocation decisions",
    "Allocating most experienced staff to highest risk activities",
    "Project control cycle (monitoring, comparison, revision)",
    "Four types of project shortfall (delays, quality, functionality, costs)",
    "Project steering committee responsibility for progress",
    "Project reporting structures (team leaders to project manager to steering committee)",
    "PRINCE2 Project Assurance function",
    "Categories of reporting (oral/written, formal/informal, regular/ad hoc)",
    "Weekly progress meetings with formal written minutes",
    "End-of-stage review meetings",
    "Exception reports for significant deviations",
    "Change reports for requirement modifications",
    "Objective and tangible information for assessing progress",
    "Checkpoints in activity plan (regular or event-tied)",
    "Weekly reporting for individual developers",
    "Review points or control points for major progress reviews",
    "PRINCE2 End Stage Assessment",
    "Difficulty forecasting partially completed activities",
    "In-activity milestones (e.g., first successful compilation)",
    "Weekly timesheets for resource usage information",
    "99% complete phenomenon in partial completion reporting",
    "Red/amber/green (RAG) traffic-light reporting",
    "Review as cost-effective defect removal mechanism",
    "Review identifying deviation from standards",
    "Review as learning opportunity for participants",
    "Review roles (moderator, recorder, reviewers)",
    "Moderator responsibilities (scheduling, convening, leading review sessions)",
    "Recorder role in documenting defects and effort data",
    "Review process activities (planning, preparation, meeting, rework, follow-up)",
    "Review team size between five and seven members",
    "Author of preceding work product as reviewer",
    "User of work product under review as reviewer",
    "Peers of author as reviewers",
    "Review preparation log for individual defect recording",
    "Review log for defects agreed by author",
    "Review summary report with total defects and time spent",
    "Gantt chart for tracking project progress",
    "Today cursor on Gantt chart for visual progress indication",
    "Slip chart for striking visual indication of schedule variations",
    "Slip line bending indicating variation from plan",
    "Timeline chart for recording target changes over project duration",
    "Planned time vs. elapsed time on timeline chart",
    "Cumulative expenditure chart for cost monitoring",
    "Projected future costs adding to actual expenditure",
    "Earned value analysis originating from US Department of Defence",
    "Planned value (PV) or budgeted cost of work scheduled (BCWS)",
    "Earned value (EV) or budgeted cost of work performed (BCWP)",
    "0/100 technique for earned value assignment",
    "50/50 technique for earned value assignment",
    "75/25 technique for earned value assignment",
    "Milestone technique for earned value assignment",
    "Baseline budget creation for earned value analysis",
    "Actual cost (AC) or actual cost of work performed (ACWP)",
    "Schedule variance (SV = EV - PV)",
    "Time variance (TV) as difference between planned and actual achievement time",
    "Cost variance (CV = EV - AC)",
    "Cost performance index (CPI = EV/AC)",
    "Schedule performance index (SPI = EV/PV)",
    "Estimate at completion (EAC = BAC/CPI)",
    "Time estimate at completion (TEAC = SAC/SPI)",
    "Prioritizing monitoring (critical path activities, high-risk activities)",
    "Activities with no free float requiring close monitoring",
    "Activities using critical resources requiring high monitoring level",
    "Shortening critical path to bring project back on target",
    "Adding resources (especially staff) to speed up critical activities",
    "Increasing use of current resources (overtime, weekend access)",
    "Reallocating staff to critical activities",
    "Reducing scope of functionality to meet deadlines",
    "Reducing quality-related activities (e.g., curtailing system testing)",
    "Reconsidering precedence requirements to overcome constraints",
    "Subdividing activities to start components earlier",
    "Maintaining business case when revising project plans",
    "Exception planning and exception reports in PRINCE2",
    "Change control for requirements modifications",
    "Baselining products to freeze them for further development",
    "Change control procedures (request for change - RFC)",
    "Single authorized channel for change requests",
    "Change control board (CCB) for approving changes",
    "Configuration librarian role in change control",
    "Central repository of master copies of project documentation",
    "Scope creep in system development",
    "Software configuration management (SCM) for tracking changes",
    "Configuration of software product at any point in time",
    "Version as configuration at a specific point in time",
    "Revision as successive states of a configuration item",
    "Baseline as formally reviewed and agreed configuration",
    "Variants as versions intended to coexist (different platforms)",
    "Concurrent access problems without configuration management",
    "Undoing changes with configuration management",
    "System accounting for tracking who made what change",
    "Release management for systematizing new software releases",
    "Open source configuration management tools (SCCS, RCS)",
    "Delta storage for efficient version storage",
    "Check-out and check-in facilities in configuration management",
    "Types of contracts (fixed price, time and materials, fixed price per unit)",
    "Fixed price contracts with known customer expenditure",
    "Time and materials contracts with fixed rate per unit of effort",
    "Fixed price per delivered unit contracts (function point based)",
    "Open tendering process for contractor selection",
    "Restricted tendering process with invited suppliers",
    "Negotiated procedure for single supplier situations",
    "Requirements analysis before approaching suppliers",
    "Mandatory vs. desirable requirements in contract documents",
    "Evaluation plan for proposal assessment",
    "ISO 9126 standard for quality evaluation",
    "Value for money as key contract selection criterion",
    "Whole lifetime costs in contract evaluation",
    "Contract terms (definitions, form of agreement, goods and services)",
    "Ownership of software and copyright in contracts",
    "Escrow agreement for source code protection",
    "Acceptance procedures and acceptance testing in contracts",
    "Liquidated damages and penalty clauses in contracts",
    "Alternative dispute resolution for contract disputes",
    
    # NEW topics from Unit-12-13-14 (Team Management & Quality)
    "Group working enhancement in software projects",
    "Coordination needs analysis for projects",
    "Communication genres for project coordination",
    "Communication plan documentation",
    "Team structures evaluation",
    "Leadership styles in project management",
    "Co-located vs. dispersed teams",
    "Project team as temporary grouping of individuals",
    "Social roles in team effectiveness",
    "Tasks best done by individuals vs. groups",
    "Coordination through communication",
    "Communication genres beyond technologies",
    "Proactive central direction in projects",
    "Tuckman and Jensen team development stages (forming, storming, norming, performing, adjourning)",
    "Team-building exercises and outdoor activities",
    "Belbin team role classification",
    "Chair role in Belbin model",
    "Plant role (idea generator) in Belbin model",
    "Monitor-evaluator role in Belbin model",
    "Shaper role (worrier, directs attention) in Belbin model",
    "Team worker role (jollying people along)",
    "Resource investigator role in Belbin model",
    "Completer-finisher role in Belbin model",
    "Company worker role in Belbin model",
    "Imbalance of role types causing team problems",
    "Two or more shapers without chair causing stormy atmosphere",
    "Plants and specialists without shapers causing no implementation",
    "Additive group tasks (e.g., gang clearing snow)",
    "Compensatory group tasks (pooling judgements)",
    "Disjunctive group tasks (one correct answer)",
    "Conjunctive group tasks (progress by slowest performer)",
    "Social loafing in group tasks",
    "Structured vs. unstructured decisions",
    "Risk and uncertainty in decision making",
    "Faulty heuristics as mental obstacle to decision making",
    "Escalation of commitment in decision making",
    "Information overload as decision obstacle",
    "Participatory decision making with end-users",
    "Group decision making with complementary skills",
    "Brainstorming techniques for group problem solving",
    "JAD (Joint Application Development) for user involvement",
    "Risky shift in group decisions",
    "Delphi technique for expert judgement without face-to-face meetings",
    "Delphi technique advantages for geographically dispersed experts",
    "Team heedfulness and collective mind",
    "Egoless programming concept",
    "Chief programmer team structure",
    "Co-pilot role in chief programmer team",
    "Program clerk role in chief programmer team",
    "New York Times data bank project using chief programmer concept",
    "Program librarian in chief programmer team",
    "Information overload danger for chief programmer",
    "Staff dissatisfaction in chief programmer teams",
    "Scrum software development process",
    "Scrum chief architect role",
    "Scrum sprints (one to four weeks)",
    "Scrum daily meetings (15 minutes)",
    "Scrum teams working in parallel on different sprints",
    "Scrum time-boxed sprints",
    "Scrum closure phase for regression testing and user guides",
    "AG Communications Scrum implementation",
    "Functional department structure",
    "Project department structure",
    "Matrix department structure",
    "Functional format advantages (ease of staffing, job specialization)",
    "Functional format producing good quality documentation",
    "Functional format handling manpower turnover effectively",
    "Technical ladder career path in functional organizations",
    "Project format for task-oriented teams",
    "Strong vs. weak matrix organizations",
    "Multiplicity of authority causing conflicts in matrix",
    "Democratic team structure",
    "Mixed control team structure",
    "Single point failure in chief programmer team",
    "Coordination dependencies in organizations",
    "Shared resources as coordination dependency",
    "Producer-customer (right time) relationships",
    "Task-subtask dependencies",
    "Accessibility (right place) dependencies",
    "Usability (right thing) dependencies",
    "Fit requirements (component integration)",
    "McChesney and Gallagher research on coordination practices",
    "Go-between role in project coordination",
    "Email as principal communication means in projects",
    "Copying emails to keep stakeholders in loop",
    "Dispersed and virtual teams",
    "Flow (deep concentration) for creative work",
    "15 minutes needed to achieve flow state",
    "IBM research on ideal developer workspace (100 square feet, 6-foot partitions)",
    "Noise levels linked to software defects",
    "Home working for software developers",
    "Offshore staff as dispersed team members",
    "Advantages of dispersed working (lower costs, flexible staff, different time zones)",
    "Challenges of dispersed working (specification, coordination, trust)",
    "Communication genres time/place constraints (same time/different time, same place/different place)",
    "Telephone as same time/different place communication",
    "Instant messaging as same time/different place communication",
    "Email as different time/different place communication",
    "Voicemail as different time/different place communication",
    "Documents as different time/different place communication",
    "Early project stages benefiting from same time/same place meetings",
    "Intermediate design stages using teleconferencing",
    "Implementation stages using email for information exchange",
    "Communication plans with stakeholder lists and communication events",
    "Leadership as ability to influence others",
    "Position power (coercive, connection, legitimate, reward)",
    "Personal power (expert, information, referent)",
    "Directive autocrat leadership style",
    "Permissive autocrat leadership style",
    "Directive democrat leadership style",
    "Permissive democrat leadership style",
    "Task-oriented vs. people-oriented management",
    "Task-oriented management effective with inexperienced teams",
    "People-oriented management for mature team members",
    "Software quality importance for users and developers",
    "Quality measurement methods",
    "Process quality monitoring",
    "External quality standards for supplier software",
    "Increasing criticality of software",
    "Accumulating errors during software development",
    "BS ISO/IEC 15939:2007 for measuring process",
    "Direct vs. indirect quality measures",
    "Quality specification components (definition, scale, test, acceptable range, target range)",
    "Reliability measurements (availability, mean time between failures, failure on demand)",
    "Maintainability components (changeability, analysisability)",
    "Garvin's quality dimensions (performance, features, reliability, conformance, durability, serviceability, aesthetics, perceived quality)",
    "McCall's quality model (correctness, reliability, efficiency, integrity, usability, maintainability, flexibility, testability, portability, reusability, interoperability)",
    "Dromey's quality model (correctness, internal characteristics, contextual characteristics, descriptive properties)",
    "Boehm's quality model (as-is utility, maintainability, portability)",
    "ISO 9126 quality characteristics (functionality, reliability, usability, efficiency, maintainability, portability)",
    "Functionality sub-characteristics (suitability, accuracy, interoperability, compliance, security)",
    "Reliability sub-characteristics (maturity, fault tolerance, recoverability, compliance)",
    "Usability sub-characteristics (understandability, learnability, operability, attractiveness, compliance)",
    "Efficiency sub-characteristics (time behaviour, resource utilization, compliance)",
    "Maintainability sub-characteristics (analysisability, changeability, stability, testability, compliance)",
    "Portability sub-characteristics (adaptability, installability, coexistence, replaceability, compliance)",
    "Mapping quality measurements to user satisfaction ratings",
    "Product metrics vs. process metrics",
    "Product vs. process quality management",
    "Entry requirements for process steps",
    "Implementation requirements for process steps",
    "Exit requirements for process steps",
    "BS EN ISO 9001:2000 quality management system",
    "ISO 9000 series for quality systems certification",
    "ISO 9001 describing QMS for product creation",
    "ISO 9004 for process improvement",
    "Stephen Halliday criticism of ISO 9000 standards",
    "Means-ends inversion in quality preoccupation",
    "SEI capability maturity model (CMM)",
    "CMM five maturity levels (Initial, Repeatable, Defined, Managed, Optimizing)"
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
    
    elif any(word in prompt_lower for word in ["business case", "portfolio"]):
        return "💼 **Business Case & Portfolio Management**\n\n**Business Case Components**:\n1. Introduction & background\n2. Proposed project description\n3. Market analysis (demand, competitors)\n4. Organizational infrastructure planning\n5. Benefits identification & valuation\n6. Outline implementation plan\n7. Cost scheduling\n8. Financial case analysis\n\n**Portfolio Management**:\n• Evaluate projects against strategic, technical, and economic criteria\n• Balance high-risk/high-reward with low-risk/low-reward projects\n• Use Warren McFarlan's portfolio concept for IS management\n• Maintain single repository for all current projects\n\n✅ Projects must be evaluated on strategic, technical, and economic grounds."
    
    elif any(word in prompt_lower for word in ["estimate", "estimation", "cocomo", "function point"]):
        return "📊 **Software Estimation Techniques**\n\n**Key Challenges**:\n• Underestimating small tasks, overestimating large tasks\n• Political implications of estimates\n• Changing technology\n• Lack of homogeneous project experience\n\n**Estimation Methods**:\n1. **Expert Judgement** - Delphi technique\n2. **Analogy-Based** - Case-based reasoning (ANGEL tool)\n3. **Algorithmic Models**:\n   - COCOMO II (Application composition, Early design, Post-architecture)\n   - Function Point Analysis (Albrecht, Mark II, COSMIC-FFP)\n   - SLOC-based estimation\n\n**Important Laws**:\n• Parkinson's Law: Work expands to fill time available\n• Weinberg's Law: Software is always late\n• Brooks' Mythical Man-Month: Adding people to late project makes it later\n\n⚠️ Unrealistic estimates are a major danger in software projects."
    
    elif any(word in prompt_lower for word in ["quality", "iso", "testing"]):
        return "✅ **Software Quality Management**\n\n**Quality Models**:\n1. **ISO 9126 Characteristics**:\n   - Functionality, Reliability, Usability, Efficiency, Maintainability, Portability\n\n2. **McCall's Model**:\n   - Correctness, Reliability, Efficiency, Integrity, Usability\n   - Maintainability, Flexibility, Testability, Portability, Reusability, Interoperability\n\n3. **Garvin's Dimensions**:\n   - Performance, Features, Reliability, Conformance, Durability, Serviceability, Aesthetics, Perceived Quality\n\n**Quality Standards**:\n• BS EN ISO 9001:2000 - Quality Management System\n• SEI Capability Maturity Model (CMM) - 5 levels\n• TickIT accreditation for software\n\n**Quality Activities**:\n• Reviews (more cost-effective than testing)\n• Testing (unit, integration, system, acceptance)\n• Configuration management\n• Change control\n\n💡 Quality must be built into the process, not inspected in at the end."
    
    elif any(word in prompt_lower for word in ["team", "leadership", "communication"]):
        return "👥 **Team Management & Leadership**\n\n**Team Development Stages **(Tuckman & Jensen)\n1. **Forming** - Ground rules about behavior\n2. **Storming** - Conflicts and leadership exertion\n3. **Norming** - Group identity emergence\n4. **Performing** - Emphasis on tasks at hand\n5. **Adjourning** - Group disbands\n\n**Belbin Team Roles**:\n• Chair/Coordinator, Plant (idea generator), Monitor-Evaluator\n• Shaper (directs attention), Team Worker, Resource Investigator\n• Completer-Finisher, Company Worker, Specialist\n\n**Leadership Styles**:\n• Directive Autocrat (decides alone, close supervision)\n• Permissive Autocrat (decides alone, subordinates have latitude)\n• Directive Democrat (participative decisions, close supervision)\n• Permissive Democrat (participative decisions, latitude in implementation)\n\n**Communication**:\n• Email is principal means in projects\n• Face-to-face critical in early stages\n• 15 minutes needed to achieve 'flow' state\n• IBM research: 100 sq ft per developer, 6-foot partitions\n\n✅ Task-oriented management for inexperienced teams; People-oriented for mature teams."
    
    elif any(word in prompt_lower for word in ["agile", "scrum", "spiral", "waterfall", "methodology"]):
        return "🔄 **Development Methodologies**\n\n**Traditional Models**:\n1. **Waterfall Model** (Stage-gate):\n   - Limited iteration as strength\n   - Natural milestones at end of each phase\n   - Ideal for well-defined requirements\n\n2. **Spiral Model** (Boehm):\n   - Incremental style with risk handling\n   - Four quadrants per phase\n   - Tailoring number of phases during execution\n   - Buying knowledge to reduce uncertainty\n\n**Agile Methods**:\n1. **Scrum**:\n   - Sprints (1-4 weeks)\n   - Daily meetings (15 minutes)\n   - Teams max 10 developers\n   - Time-boxed sprints\n\n2. **Extreme Programming **(XP)\n   - Collective mind promotion\n   - Continual integration testing\n   - Test cases before code\n   - User representative on hand\n\n3. **DSDM/Atern**:\n   - MoSCoW classification (Must, Should, Could, Won't have)\n   - Time-boxes (2-6 weeks)\n   - Feasibility, Exploration, Engineering, Deployment cycles\n\n✅ Choose methodology based on project uncertainty, requirements stability, and team size."
    
    elif any(word in prompt_lower for word in ["resource", "scheduling", "gantt", "critical path"]):
        return "📅 **Resource Allocation & Scheduling**\n\n**Resource Categories**:\n• Labour (project manager, analysts, developers)\n• Equipment (workstations, office equipment)\n• Materials (consumables)\n• Space (office space)\n• Services (telecommunications)\n• Time & Money (secondary resources)\n\n**Scheduling Techniques**:\n1. **Gantt Charts** - Visual timeline representation\n2. **Critical Path Method **(CPM)\n   - Forward pass (earliest start/finish)\n   - Backward pass (latest start/finish)\n   - Total float, free float, interfering float\n   - Critical path identification\n\n3. **PERT**:\n   - Three estimates (optimistic, most likely, pessimistic)\n   - Expected duration: (a + 4m + b)/6\n   - Probability calculations for target dates\n\n**Resource Smoothing**:\n• Adjust activity start dates using float\n• Split non-critical activities (difficult in software)\n• Prioritize: Critical path first, then by total float\n• Burman's priority list for allocation\n\n⚠️ Resource constraints can create new critical paths."
    
    elif any(word in prompt_lower for word in ["configuration", "change control", "version"]):
        return "🔧 **Configuration & Change Management**\n\n**Configuration Management **(SCM)\n• Configuration: Software product state at any point in time\n• Version: Configuration at specific point\n• Revision: Successive states of configuration item\n• Baseline: Formally reviewed and agreed configuration\n• Variants: Versions intended to coexist (different platforms)\n\n**Change Control Process**:\n1. Request for Change (RFC) through single authorized channel\n2. Assess products affected by proposed change\n3. Change Control Board (CCB) approval\n4. Configuration librarian maintains master copies\n5. Implement change with check-out/check-in\n6. User acceptance testing for new versions\n\n**Tools**:\n• SCCS, RCS (UNIX text file version control)\n• Delta storage for efficient versioning\n• System accounting for tracking changes\n\n⚠️ Scope creep is a major risk - filter changes through CCB.\n✅ BS EN ISO 9001:1994 requires formal change control."
    
    elif any(word in prompt_lower for word in ["contract", "procurement", "outsourcing"]):
        return "📝 **Contracts & Procurement**\n\n**Contract Types**:\n1. **Fixed Price** - Known customer expenditure\n2. **Time & Materials** - Fixed rate per unit of effort\n3. **Fixed Price per Unit** - Function point based\n\n**Tendering Processes**:\n• **Open Tendering** - Any supplier can bid\n• **Restricted Tendering** - Invited suppliers only\n• **Negotiated Procedure** - Single supplier situations\n\n**Contract Evaluation**:\n• Mandatory vs. desirable requirements\n• Value for money as key criterion\n• Whole lifetime costs consideration\n• ISO 9126 for quality evaluation\n\n**Contract Terms**:\n• Definitions, form of agreement, goods and services\n• Ownership of software and copyright\n• Escrow agreement for source code protection\n• Acceptance procedures and testing\n• Liquidated damages and penalty clauses\n• Alternative dispute resolution\n\n⚠️ Requirements analysis essential before approaching suppliers.\n✅ Legal advice essential for substantial contract sums."
    
    elif any(word in prompt_lower for word in ["earned value", "monitoring", "control", "variance"]):
        return "📈 **Earned Value Analysis & Project Control**\n\n**Key Metrics**:\n• **Planned Value **(PV) - Budgeted cost of work scheduled (BCWS)\n• **Earned Value **(EV) - Budgeted cost of work performed (BCWP)\n• **Actual Cost **(AC) - Actual cost of work performed (ACWP)\n• **Budget at Completion **(BAC) - Total planned budget\n\n**Variance Analysis**:\n• **Schedule Variance**: SV = EV - PV (negative = behind schedule)\n• **Cost Variance**: CV = EV - AC (negative = over budget)\n• **Cost Performance Index**: CPI = EV/AC (>1 = better than planned)\n• **Schedule Performance Index**: SPI = EV/PV\n\n**Forecasting**:\n• **Estimate at Completion**: EAC = BAC/CPI\n• **Time Estimate at Completion**: TEAC = SAC/SPI\n\n**Earned Value Assignment Techniques**:\n• 0/100 technique (nothing until complete)\n• 50/50 technique (50% at start, 50% at finish)\n• 75/25 technique\n• Milestone technique\n\n**Project Control Cycle**:\n1. Monitor progress\n2. Compare with plan\n3. Identify shortfalls (delays, quality, functionality, costs)\n4. Revise plan if necessary\n\n✅ Originated from US Department of Defence."
    
    else:
        return f"🔍 **Regarding: \"{prompt}\"**\n\nThis is an important Software Project Management topic. Key considerations:\n\n1. **Understand context** - Is this for academic study or industry application?\n2. **Reference frameworks** - PMBOK, PRINCE2, Agile/Scrum, ISO 12207\n3. **Apply best practices** - Documentation, communication, iterative planning\n4. **Learn from case studies** - Standish Group, UK National Audit Office reports\n\n💡 Would you like me to elaborate on any specific aspect? Try asking about:\n• Risk management strategies\n• Agile vs. Waterfall methodologies\n• Stakeholder communication plans\n• Project charter essentials\n• Estimation techniques (COCOMO, Function Points)\n• Quality management (ISO 9126, CMM)\n• Team leadership styles\n• Configuration management"

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
        **Updated**: {datetime.now().strftime('%Y-%m-%d')}\n
        **Total Topics**: {len(SPM_TOPICS)}
        """)
        
        st.markdown("### 📖 References")
        st.markdown("""
        • Ref 1: GitHub Repo - CSSPM\n
        • Ref 2: B.E. CSE - SPM Topics (400+ concepts)\n
        • Industry: Standish Group, PMBOK, ISO 12207\n
        • Units: Planning, Estimation, Quality, Team Management
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
