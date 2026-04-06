# app.py - STRICT FILTERING & COMPLETE TOPIC COVERAGE
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

# Custom CSS styling - UPDATED COLORS (Light Gray Background, Black Text)
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

# Extended SPM Topics from knowledge base - FOR RANDOM SUGGESTIONS
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
    "Boundary between design and planning",
    "Design decisions about product form",
    "ISO 12207 software development activities",
    "Requirements analysis and elicitation",
    "Quality requirements in requirements analysis",
    "System vs. software requirements",
    "Architecture design for new system components",
    "Legacy systems and interoperability",
    "Detailed design of software units",
    "Coding and testing of software units",
    "Integration of software components",
    "Qualification testing for requirements fulfilment",
    "Installation process for new system",
    "Standing data setup in installation",
    "Acceptance support for problem resolution",
    "Software maintenance as minor software projects",
    "Plans based on methods of work",
    "Method vs. plan distinction",
    "Methodologies as groups of methods",
    "Building height estimation exercise",
    "Changes in software project characteristics over decades",
    "Writing software from scratch in early years",
    "Programming paradigms inhibiting code reuse",
    "Customization of existing software as current norm",
    "Small percentage of new code written today",
    "Project durations shrinking to few months",
    "Customer participation in early projects",
    "Customer representatives in development team today",
    "Compulsory vs. voluntary users",
    "Market surveys for voluntary systems",
    "Focus groups for voluntary systems",
    "Prototype evaluation for voluntary systems",
    "Information systems vs. embedded systems",
    "Embedded systems as real-time or industrial systems",
    "Software product development vs. software services projects",
    "Generic software products (horizontal market)",
    "Domain-specific software products (vertical market)",
    "Examples of generic products (Windows, Oracle)",
    "Examples of domain-specific products (BANCS, FINACLE, AspenPlus)",
    "Growth of available code base",
    "Outsourced projects and special challenges",
    "Indian software companies in outsourcing",
    "Generic product revenue stream vs. one-time outsourcing revenue",
    "Objective-driven vs. product-driven projects",
    "Two-stage objective-driven then product-driven projects",
    "Preliminary design at fixed fee",
    "Project charter as high-level authorization document",
    "Project charter outlining objectives, deliverables, resources",
    "Project sponsor role (champion, monitor, remove obstacles)",
    "Project charter as unchanging document",
    "Project plan as dynamic document",
    "Risk management plan as dynamic document",
    "Work breakdown structure as dynamic document",
    "Project charter contents (objectives, scope, schedule, stakeholders, budget, risks)",
    "Stakeholder categories (internal to team, external within organization, external to both)",
    "Theory W (win-win) of Boehm and Ross",
    "Communication plan creation at project start",
    "Project owners controlling financing",
    "Objectives as shared intentions for project",
    "Objectives as postconditions (success statements)",
    "Project steering committee for setting objectives",
    "Sub-objectives and goals in project management",
    "SMART criteria for objectives (Specific, Measurable, Achievable, Relevant, Time-constrained)",
    "Measures of effectiveness (e.g., mean time between failures)",
    "Predictive measures (e.g., errors in code inspections)",
    "Business case and cost-benefit analysis",
    "Business model for generating benefits",
    "Project success vs. failure distinction",
    "Project objectives vs. business objectives",
    "Project success as benefits exceeding costs",
    "Delay reducing time for benefits generation",
    "Broader view including business issues",
    "Market surveys to reduce business risks",
    "Competitor analysis to reduce business risks",
    "Focus groups to reduce business risks",
    "Prototyping to reduce business risks",
    "Technical learning benefits across successive projects",
    "Reusable code as software asset",
    "Customer relationships built over multiple projects",
    "Management activities (planning, organizing, staffing, directing, monitoring, controlling, innovating, representing)",
    "Principal project management processes",
    "Project initiation stage (initial plan)",
    "Project monitoring and control",
    "Project closing stage",
    "Estimation of cost, duration, effort",
    "Scheduling based on effort and duration",
    "Staffing plans",
    "Risk management (identification, analysis, abatement planning)",
    "Quality assurance plan",
    "Configuration management plan",
    "Plan revision iterations during project",
    "Management control cycle",
    "Modelling consequences of potential solutions",
    "Project plan as dynamic with constant adjustment",
    "Software development life cycle vs. project management life cycle",
    "Project life cycle as generic term",
    "W5HH principle of Barry Boehm",
    "Bidding processes (RFQ, RFP, RFI, RFT)",
    "Statement of work in RFQ",
    "Gold plating and scope creep",
    "Technical students impatience with project management studies",
    "UK government spending on ICT contracts vs. roads (£2.3 billion vs. £1.4 billion)",
    "Department for Work and Pensions spending over £800 million on ICT",
    "Mismanagement of ICT projects reducing spending on hospitals",
    "Standish Group analysis of 13,522 projects (2003)",
    "Programme management for coordinating activities on concurrent jobs",
    "Exploratory projects making planning difficult",
    "Routine maintenance procedures documented for consistency and newcomers",
    "20 developers disproportionately more difficult than 10 due to coordination",
    "Examples of activities to categorize as projects (newspaper edition, Mars robot, marriage, etc.)",
    "Amending financial system for common European currency as project example",
    "Research project into good human-computer interface as project example",
    "Investigation of user problem with computer system as project example",
    "Second-year programming assignment as project example",
    "Writing operating system for new computer as project example",
    "Installing new version of word processing package as project example",
    "Temporary sub-organization cutting across existing unit authority",
    "Project seen as disruptive to others",
    "Brooks' "No Silver Bullet" essay (1987)",
    "Software project management as making invisible visible",
    "Physical systems governed by consistent physical laws",
    "Organizations exhibiting "organizational stupidity"",
    "Software expected to change to accommodate other components",
    "Client project manager delegating technical decisions to contractors",
    "Book leaning towards technical project managers' concerns",
    "Feasibility study as part of strategic planning exercise",
    "PRINCE2 iterative approach to planning",
    "Annex 1 outline of plan content",
    "ISO 12207 suggesting strict sequence (alternative iterative approaches in Chapter 4)",
    "Ambulance dispatch transaction time example",
    "Training as system requirement (not specifically software)",
    "Resource requirements for application development costs",
    "Legacy systems interoperability in architecture design",
    "Second architecture design process mapping software requirements to components",
    "Integration combining hardware platforms and user interactions",
    "Setting system parameters during installation",
    "User training during installation",
    "Brightmouth College payroll project conversion stages",
    "Off-the-shelf package project vs. writing from scratch differences",
    "Feasibility study steps for customizing existing product",
    "Devising test cases for each requirement",
    "Creating test scripts and expected results",
    "Comparing actual and expected results",
    "Plan identifying start/end dates, who, tools, materials, information",
    "Output from one method as input to another",
    "Object-oriented design as methodology example",
    "Building height estimation exercise (planning vs. execution)",
    "Programming paradigms hardly supporting code reuse in early days",
    "Dynamically linking library routines for code reuse",
    "Frameworks supporting code reuse",
    # Unit-02 Topics
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
    # Unit-03-04 Topics
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
    # Unit-05-06-07 Topics
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
    # Unit-08-09-10-11 Topics
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
    # Unit-12-13-14 Topics
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

# TOPIC DATABASE - STRICT FILTERING & SCALABLE
# This dictionary maps keywords to specific topic content.
# It ensures that searching for "agile" returns ONLY agile content.
TOPIC_DATABASE = [
    {
        "topic": "Agile",
        "keywords": ["agile", "scrum", "extreme programming", "xp", "dsdm", "atern", "incremental", "sprint", "kanban", "lean"],
        "content": """🔄 **Agile Software Development Methods**

**Agile Manifesto Principles:**
• Individuals and interactions over processes and tools
• Working software over comprehensive documentation
• Customer collaboration over contract negotiation
• Responding to change over following a plan

**1. Scrum Framework:**
• **Sprints**: Time-boxed iterations (1-4 weeks)
• **Daily Stand-up**: 15-minute meetings for progress tracking
• **Scrum Roles**: Product Owner, Scrum Master, Development Team
• **Product Backlog**: Prioritized list of features
• **Sprint Planning**: Selecting work for upcoming sprint
• **Sprint Review**: Demonstrating completed work
• **Sprint Retrospective**: Process improvement discussion
• **Time-boxed**: Fixed duration sprints
• **Team Size**: Maximum 10 developers per team
• **Closure Phase**: Regression testing and user guides

**2. Extreme Programming (XP):**
• **Collective Code Ownership**: Programs as common property
• **Pair Programming**: Two developers working together
• **Test-First Development**: Test cases written before code
• **Continuous Integration**: Frequent code integration and testing
• **Refactoring**: Continuously improving code structure
• **User Stories**: Requirements from customer perspective
• **On-site Customer**: User representative always available
• **Small Releases**: Frequent delivery of working software
• **Sustainable Pace**: 40-hour work week recommended
• **Coding Standards**: Consistent code style across team

**3. DSDM/Atern (Dynamic Systems Development Method):**
• **MoSCoW Prioritization**:
  - Must have (critical requirements)
  - Should have (important but not vital)
  - Could have (desirable but not necessary)
  - Won't have (agreed to omit for now)
• **Time-boxes**: Fixed periods of 2-6 weeks
• **Four Cycles**:
  - Feasibility: Foundation with business case
  - Exploration: Exploratory prototypes
  - Engineering: Converting design to components
  - Deployment: Getting application into operational use
• **User Involvement**: Active participation throughout
• **Empowered Teams**: Decision-making authority
• **Frequent Delivery**: Regular increments of functionality

**4. Incremental Delivery:**
• **Breaking System**: Into small, deliverable components
• **Early Benefits**: Each increment delivers value
• **Feedback Loop**: Early increments improve later stages
• **Reduced Gold-plating**: Focus on essential features
• **Value-to-Cost Ratio**: Prioritizing high-value increments
• **Open Technology Plan**: Standard language, OS, DBMS
• **Risk Reduction**: Shorter time spans reduce change risk
• **Cash Flow Improvement**: Early ROI from early delivery

**Agile Advantages:**
✅ Adapts to changing requirements
✅ Early and continuous delivery
✅ Close customer collaboration
✅ Self-organizing teams
✅ Sustainable development pace

**Agile Challenges:**
⚠️ Requires experienced, motivated team
⚠️ Customer must be actively involved
⚠️ Less predictable timelines
⚠️ Documentation may be minimal
⚠️ Not ideal for safety-critical systems

**Best Suited For:**
• New product development for competitive markets
• Projects with uncertain or evolving requirements
• Small to medium-sized teams (<10 developers)
• Rapidly changing technology environments
• Projects where speed to market is critical"""
    },
    {
        "topic": "Waterfall",
        "keywords": ["waterfall", "cascade", "sequential", "linear", "stage-gate", "traditional model"],
        "content": """📊 **Waterfall Model (Classical/Stage-Gate Model)**

**Overview:**
The Waterfall model is a linear, sequential approach to software development where each phase must be completed before the next begins.

**Phases of Waterfall:**
1. **Requirements Analysis**: Gather and document all requirements
2. **System Design**: Create architecture and design specifications
3. **Implementation (Coding)**: Write actual code
4. **Testing**: Verify system meets requirements
5. **Deployment**: Install and make operational
6. **Maintenance**: Fix bugs and make enhancements

**Key Characteristics:**
• **Limited Iteration**: Each phase completed once (strength)
• **Natural Milestones**: Clear end points for each phase
• **Sequential Flow**: No overlapping of phases
• **Documentation-Heavy**: Extensive documentation at each stage
• **Stage-Gate Reviews**: Business case reviewed at phase ends
• **Well-Defined Requirements**: Ideal when requirements are stable

**Advantages:**
✅ Simple and easy to understand
✅ Clear milestones and deliverables
✅ Easy to manage and control
✅ Works well for stable requirements
✅ Good documentation produced
✅ Suitable for regulated industries

**Disadvantages:**
❌ Inflexible to changing requirements
❌ Working software produced late
❌ High risk and uncertainty
❌ Difficult to go back to previous phases
❌ Customer sees product only at end
❌ Not suitable for complex/uncertain projects

**Best Suited For:**
• Projects with well-defined, stable requirements
• Short projects with low uncertainty
• Projects using familiar technology
• Safety-critical systems requiring documentation
• Projects with fixed scope and budget
• Regulatory compliance environments

**When to Avoid:**
⚠️ Requirements likely to change
⚠️ High uncertainty or complexity
⚠️ Need for early delivery
⚠️ Customer wants frequent feedback
⚠️ Innovative or research-oriented projects"""
    },
    {
        "topic": "Spiral",
        "keywords": ["spiral", "boehm model", "risk-driven model", "prototyping"],
        "content": """🌀 **Spiral Model (Boehm's Risk-Driven Model)**

**Overview:**
Developed by Barry Boehm (1988), the Spiral model combines iterative development with systematic risk management.

**Four Quadrants per Phase:**
1. **Determine Objectives**: Identify goals, alternatives, constraints
2. **Evaluate Alternatives**: Identify and resolve risks
3. **Develop and Test**: Develop next level of product
4. **Plan Next Phase**: Review and plan next iteration

**Key Characteristics:**
• **Incremental Style**: Builds system in increments
• **Risk Handling**: Primary focus on risk reduction
• **Tailorable Phases**: Number of phases varies by project
• **Prototyping**: Buying knowledge to reduce uncertainty
• **Customer Involvement**: Regular reviews at each spiral
• **Flexible**: Can escape at end of any activity

**Advantages:**
✅ High risk management focus
✅ Early prototyping reduces uncertainty
✅ Customer feedback at each iteration
✅ Suitable for large, complex projects
✅ Flexible and adaptable
✅ Good for mission-critical systems

**Disadvantages:**
❌ Complex and expensive
❌ Requires risk assessment expertise
❌ Not suitable for small projects
❌ Can go on indefinitely
❌ Difficult to manage
❌ Documentation-heavy

**Best Suited For:**
• Large-scale, complex projects
• Mission-critical systems
• Projects with high risk
• Long-term projects
• Projects requiring extensive prototyping"""
    },
    {
        "topic": "Estimation",
        "keywords": ["estimate", "estimation", "cocomo", "function point", "sloc", "delphi", "size", "effort", "cost"],
        "content": """📊 **Software Estimation Techniques**

**Key Challenges:**
• Underestimating small tasks, overestimating large tasks
• Political implications of estimates
• Changing technology
• Lack of homogeneous project experience

**Estimation Methods:**
1. **Expert Judgement** - Delphi technique
2. **Analogy-Based** - Case-based reasoning (ANGEL tool)
3. **Algorithmic Models**:
   - COCOMO II (Application composition, Early design, Post-architecture)
   - Function Point Analysis (Albrecht, Mark II, COSMIC-FFP)
   - SLOC-based estimation

**Important Laws:**
• Parkinson's Law: Work expands to fill time available
• Weinberg's Law: Software is always late
• Brooks' Mythical Man-Month: Adding people to late project makes it later

**COCOMO II Details:**
• **Scale Factors**: Precedentedness, Flexibility, Risk Resolution, Team Cohesion, Process Maturity
• **Effort Multipliers**: Product Reliability, Reusability, Platform Difficulty, Personnel Capability, etc.
• **Stages**: Application Composition, Early Design, Post-Architecture

**Function Point Analysis:**
• **Albrecht FP**: External Inputs, Outputs, Inquiries, Internal Files, Interface Files
• **Mark II FP**: Weighted sum of data movements
• **COSMIC-FFP**: Entries, Exits, Reads, Writes for real-time systems

⚠️ Unrealistic estimates are a major danger in software projects."""
    },
    {
        "topic": "Risk Management",
        "keywords": ["risk", "danger", "threat", "probability", "mitigation", "contingency", "uncertainty"],
        "content": """⚠️ **Risk Management & Failure Prevention**

**Top Project Failure Causes (Standish Group):**
1. Incomplete requirements (43%)
2. Lack of user involvement (37%)
3. Resource constraints (32%)
4. Unrealistic expectations (29%)
5. Poor risk management (26%)

**Proactive Risk Strategy:**
✅ **Identify**: Brainstorming, checklists, risk matrix
✅ **Analyze**: Impact vs. Probability (High/Medium/Low)
✅ **Plan Responses**:
   - **Avoid**: Eliminate the threat
   - **Mitigate**: Reduce probability/impact
   - **Transfer**: Shift to third party (insurance, outsourcing)
   - **Accept**: Acknowledge and monitor
✅ **Monitor**: Update risk register weekly

**Risk Exposure Formula:**
Risk Exposure = Potential Damage × Probability

**Key Risks:**
• Personnel shortages
• Schedule slippage
• Wrong functions (gold-plating)
• Technical risks (new technology)
• Business risks (market changes)

💡 Remember: Risk management is not about eliminating risk, but managing it intelligently."""
    },
    {
        "topic": "Quality Management",
        "keywords": ["quality", "iso", "testing", "review", "cmm", "reliability", "maintainability"],
        "content": """✅ **Software Quality Management**

**Quality Models:**
1. **ISO 9126 Characteristics**:
   - Functionality, Reliability, Usability, Efficiency, Maintainability, Portability

2. **McCall's Model**:
   - Correctness, Reliability, Efficiency, Integrity, Usability
   - Maintainability, Flexibility, Testability, Portability, Reusability, Interoperability

3. **Garvin's Dimensions**:
   - Performance, Features, Reliability, Conformance, Durability, Serviceability, Aesthetics, Perceived Quality

**Quality Standards:**
• BS EN ISO 9001:2000 - Quality Management System
• SEI Capability Maturity Model (CMM) - 5 levels (Initial to Optimizing)
• TickIT accreditation for software

**Quality Activities:**
• **Reviews**: More cost-effective than testing (peer review, walkthroughs)
• **Testing**: Unit, Integration, System, Acceptance
• **Configuration Management**: Version control, change control
• **Metrics**: Defect density, review effectiveness, test coverage

💡 Quality must be built into the process, not inspected in at the end."""
    },
    {
        "topic": "Team Management",
        "keywords": ["team", "leadership", "communication", "belbin", "tuckman", "motivation", "virtual"],
        "content": """👥 **Team Management & Leadership**

**Team Development Stages (Tuckman & Jensen):**
1. **Forming** - Ground rules about behavior
2. **Storming** - Conflicts and leadership exertion
3. **Norming** - Group identity emergence
4. **Performing** - Emphasis on tasks at hand
5. **Adjourning** - Group disbands

**Belbin Team Roles:**
• **Chair/Coordinator**: Clarifies goals, promotes decisions
• **Plant**: Creative, solves difficult problems
• **Monitor-Evaluator**: Strategic, sees all options
• **Shaper**: Challenging, thrives on pressure
• **Team Worker**: Cooperative, diplomatic
• **Resource Investigator**: Extrovert, explores opportunities
• **Completer-Finisher**: Painstaking, delivers on time
• **Company Worker**: Disciplined, turns ideas into actions
• **Specialist**: Technical knowledge

**Leadership Styles:**
• **Directive Autocrat**: Decides alone, close supervision
• **Permissive Autocrat**: Decides alone, subordinates have latitude
• **Directive Democrat**: Participative decisions, close supervision
• **Permissive Democrat**: Participative decisions, latitude in implementation

**Communication:**
• Email is principal means in projects
• Face-to-face critical in early stages
• 15 minutes needed to achieve 'flow' state
• IBM research: 100 sq ft per developer, 6-foot partitions

✅ Task-oriented management for inexperienced teams; People-oriented for mature teams."""
    },
    {
        "topic": "Project Planning",
        "keywords": ["plan", "planning", "schedule", "gantt", "pert", "cpm", "wbs", "float", "critical path"],
        "content": """📅 **Project Planning & Scheduling**

**Planning Steps:**
1. Define scope & deliverables
2. Create Work Breakdown Structure (WBS)
3. Estimate effort & resources
4. Develop realistic timeline
5. Identify risks & mitigation
6. Establish communication protocols

**Scheduling Techniques:**
1. **Gantt Charts**: Visual timeline representation
2. **Critical Path Method (CPM)**:
   - Forward pass (earliest start/finish)
   - Backward pass (latest start/finish)
   - Total float, free float, interfering float
   - Critical path identification
3. **PERT**:
   - Three estimates (optimistic, most likely, pessimistic)
   - Expected duration: (a + 4m + b)/6
   - Probability calculations for target dates

**Resource Smoothing:**
• Adjust activity start dates using float
• Split non-critical activities (difficult in software)
• Prioritize: Critical path first, then by total float
• Burman's priority list for allocation

⚠️ Resource constraints can create new critical paths."""
    },
    {
        "topic": "Configuration Management",
        "keywords": ["configuration", "change control", "version", "scm", "baseline", "variant", "release"],
        "content": """🔧 **Configuration & Change Management**

**Configuration Management (SCM):**
• **Configuration**: Software product state at any point in time
• **Version**: Configuration at specific point
• **Revision**: Successive states of configuration item
• **Baseline**: Formally reviewed and agreed configuration
• **Variants**: Versions intended to coexist (different platforms)

**Change Control Process:**
1. Request for Change (RFC) through single authorized channel
2. Assess products affected by proposed change
3. Change Control Board (CCB) approval
4. Configuration librarian maintains master copies
5. Implement change with check-out/check-in
6. User acceptance testing for new versions

**Tools:**
• SCCS, RCS (UNIX text file version control)
• Delta storage for efficient versioning
• System accounting for tracking changes

⚠️ Scope creep is a major risk - filter changes through CCB.
✅ BS EN ISO 9001:1994 requires formal change control."""
    },
    {
        "topic": "Business Case",
        "keywords": ["business case", "portfolio", "npv", "irr", "roi", "cost-benefit", "payback", "investment"],
        "content": """💼 **Business Case & Portfolio Management**

**Business Case Components:**
1. Introduction & background
2. Proposed project description
3. Market analysis (demand, competitors)
4. Organizational infrastructure planning
5. Benefits identification & valuation
6. Outline implementation plan
7. Cost scheduling
8. Financial case analysis

**Financial Metrics:**
• **NPV (Net Present Value)**: Considers timing of cash flows
• **IRR (Internal Rate of Return)**: Percentage return
• **ROI (Return on Investment)**: Average annual profit / total investment
• **Payback Period**: Time to recover initial investment

**Portfolio Management:**
• Evaluate projects against strategic, technical, and economic criteria
• Balance high-risk/high-reward with low-risk/low-reward projects
• Use Warren McFarlan's portfolio concept for IS management
• Maintain single repository for all current projects

✅ Projects must be evaluated on strategic, technical, and economic grounds."""
    }
]

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
    """Generate contextual mock response using STRICT TOPIC MAPPING"""
    prompt_lower = prompt.lower()
    
    # Check against TOPIC DATABASE for strict filtering
    best_match = None
    max_overlap = 0
    
    for item in TOPIC_DATABASE:
        # Count how many keywords match the prompt
        overlap = sum(1 for keyword in item["keywords"] if keyword in prompt_lower)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = item
            
    # If a topic is found, return its content
    if best_match and max_overlap > 0:
        return best_match["content"]
    
    # Fallback for unmatched queries
    return f"""🔍 **Regarding: "{prompt}"**

This is an important Software Project Management topic. 

**Key Considerations:**
1. **Understand context** - Academic study or industry application?
2. **Reference frameworks** - PMBOK, PRINCE2, Agile/Scrum, ISO 12207
3. **Apply best practices** - Documentation, communication, iterative planning
4. **Learn from case studies** - Standish Group, UK National Audit Office

💡 **Try asking about specific topics:**
• Agile methods (Scrum, XP, DSDM)
• Waterfall model
• Spiral model
• Risk management
• Estimation techniques (COCOMO, Function Points)
• Quality management (ISO 9126, CMM)
• Team leadership styles
• Configuration management
• Earned value analysis
• Stakeholder management
• Project planning & scheduling
• Business case & portfolio management"""

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
