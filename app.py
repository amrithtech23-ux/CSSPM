# app.py - COMPLETE CORRECTED VERSION WITH STRICT TOPIC SEPARATION
import streamlit as st
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
    .main {
        background-color: #f9f9f9;
    }
    
    div[data-testid="stTextArea"] textarea {
        border: 3px solid #000000 !important;
        border-radius: 8px !important;
        background-color: #D3D3D3 !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    
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
    }
    
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
    
    h1 {
        color: #4169E1 !important;
        font-weight: bold !important;
        text-align: center !important;
    }
</style>
""", unsafe_allow_html=True)

# SPM Topics for suggestions
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
    "Brooks characteristics of difficult software projects",
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
    "UK government spending on ICT contracts vs. roads",
    "Department for Work and Pensions spending over 800 million pounds on ICT",
    "Mismanagement of ICT projects reducing spending on hospitals",
    "Standish Group analysis of 13,522 projects (2003)",
    "Programme management for coordinating activities on concurrent jobs",
    "Exploratory projects making planning difficult",
    "Routine maintenance procedures documented for consistency and newcomers",
    "20 developers disproportionately more difficult than 10 due to coordination",
    "Examples of activities to categorize as projects (newspaper edition, Mars robot, marriage)",
    "Amending financial system for common European currency as project example",
    "Research project into good human-computer interface as project example",
    "Investigation of user problem with computer system as project example",
    "Second-year programming assignment as project example",
    "Writing operating system for new computer as project example",
    "Installing new version of word processing package as project example",
    "Temporary sub-organization cutting across existing unit authority",
    "Project seen as disruptive to others",
    "Brooks No Silver Bullet essay (1987)",
    "Software project management as making invisible visible",
    "Physical systems governed by consistent physical laws",
    "Organizations exhibiting organizational stupidity",
    "Software expected to change to accommodate other components",
    "Client project manager delegating technical decisions to contractors",
    "Book leaning towards technical project managers concerns",
    "Feasibility study as part of strategic planning exercise",
    "PRINCE2 iterative approach to planning",
    "Annex 1 outline of plan content",
    "ISO 12207 suggesting strict sequence",
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
    # Agile and Development Methodologies
    "Agile software development methods",
    "Scrum framework",
    "Extreme Programming (XP)",
    "DSDM Atern (Dynamic Systems Development Method)",
    "Incremental delivery",
    "Waterfall model (stage-gate)",
    "Spiral model (Boehm)",
    "Prototyping approaches",
    "Rapid Application Development (RAD)",
    "MoSCoW classification (Must have, Should have, Could have, Won't have)",
    "Time-boxing in development",
    "Iterative development",
    # Estimation Topics
    "Software estimation techniques",
    "COCOMO II model",
    "Function point analysis",
    "Source lines of code (SLOC) estimation",
    "Expert judgement in estimation",
    "Analogy-based estimation",
    "Delphi technique",
    "Parkinson's Law in estimation",
    "Weinberg's Law (software always late)",
    "Mythical Man-Month concept",
    "Bottom-up vs. top-down estimating",
    "Work Breakdown Structure (WBS)",
    "Effort vs. duration estimation",
    "Person-month as effort unit",
    "Productivity calculation",
    "Algorithmic models for estimation",
    "COSMIC Full Function Points",
    "Mark II Function Points",
    "Capers Jones estimating rules",
    "Putnam's staffing pattern",
    "Rayleigh-Norden curve",
    # Risk Management
    "Risk management strategies",
    "Risk identification techniques",
    "Risk analysis and assessment",
    "Risk mitigation planning",
    "Risk register maintenance",
    "Probability impact matrix",
    "Risk exposure calculation",
    "Proactive vs. reactive risk management",
    "Boehm's top 10 software risks",
    "Risk reduction leverage",
    # Quality Management
    "Software quality management",
    "ISO 9126 quality characteristics",
    "McCall's quality model",
    "Garvin's quality dimensions",
    "CMM (Capability Maturity Model)",
    "Quality assurance activities",
    "Software reviews",
    "Testing strategies",
    "Configuration management",
    "Change control procedures",
    # Team Management
    "Team development stages (Tuckman and Jensen)",
    "Belbin team roles",
    "Leadership styles in project management",
    "Communication in projects",
    "Co-located vs. dispersed teams",
    "Motivation and morale",
    "Group decision making",
    "Brainstorming techniques",
    "JAD (Joint Application Development)",
    "Chief programmer team structure",
    "Scrum team organization",
    "Democratic team structure",
    "Matrix organization",
    "Functional organization",
    "Team structures evaluation",
    "Group working enhancement in software projects",
    "Coordination needs analysis for projects",
    "Communication genres for project coordination",
    "Communication plan documentation",
    "Social roles in team effectiveness",
    "Tasks best done by individuals vs. groups",
    "Coordination through communication",
    "Communication genres beyond technologies",
    "Proactive central direction in projects",
    "Team-building exercises and outdoor activities",
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
    # Planning and Scheduling
    "Project planning frameworks",
    "Step Wise planning",
    "PRINCE2 methodology",
    "Activity planning",
    "Gantt charts",
    "Critical Path Method (CPM)",
    "PERT analysis",
    "Network planning models",
    "Resource allocation",
    "Resource smoothing",
    "Resource histograms",
    "Float calculation (total, free, interfering)",
    "Critical path identification",
    "Precedence networks",
    "Activity-on-node diagrams",
    "Earned value analysis",
    "Schedule variance",
    "Cost variance",
    "Performance indices (CPI, SPI)",
    # Business Case and Portfolio
    "Business case development",
    "Portfolio management",
    "Cost-benefit analysis",
    "Net Present Value (NPV)",
    "Internal Rate of Return (IRR)",
    "Return on Investment (ROI)",
    "Payback period",
    "Discounted cash flow",
    "Risk-adjusted NPV",
    "Sensitivity analysis",
    "Decision trees",
    "Programme management",
    "Benefits management",
    "Strategic project selection",
    # Contracts and Procurement
    "Contract types in software projects",
    "Fixed price contracts",
    "Time and materials contracts",
    "Tendering processes",
    "Supplier selection",
    "Contract negotiation",
    "Service level agreements",
    "Outsourcing management"
]

# API Configuration
API_CONFIG = {
    "api_key": "CSSPM2K6",
    "repository": "CSSPM",
    "license": "MIT"
}

# Comprehensive Topic Database with STRICT keyword matching
# Each topic has unique keywords to prevent conflicts
TOPIC_DATABASE = [
    {
        "topic": "Agile Methods",
        # Keywords specific to Agile - NO generic "team" or "communication"
        "keywords": [
            "agile manifesto", "agile methods", "agile software development", 
            "scrum framework", "scrum roles", "scrum master", "product owner", "product backlog",
            "sprint planning", "sprint review", "sprint retrospective", "daily stand-up", "daily scrum",
            "extreme programming", "xp practices", "pair programming", "test-first development", 
            "continuous integration", "refactoring", "user stories", "on-site customer", 
            "dsdm atern", "dynamic systems development method", "moscow classification", 
            "must have", "should have", "could have", "won't have", 
            "incremental delivery", "time-boxing", "iterative development", 
            "rapid application development", "rad model", 
            "collective code ownership", "small releases", "sustainable pace", "coding standards",
            "ag communications scrum", "scrum chief architect", "scrum closure phase"
        ],
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
• **AG Communications Example**: Three meetings per week, freezing external requirements during sprint

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
        "topic": "Team Structures & Group Working",
        # Keywords specific to Team Management - NO "agile", "scrum", "xp"
        "keywords": [
            "team structures", "group working", "group working enhancement", 
            "coordination needs", "coordination through communication", 
            "communication genres", "communication plan", "social roles", 
            "tasks individuals groups", "proactive central direction", 
            "team-building exercises", "outdoor activities", 
            "imbalance role types", "shapers without chair", "plants specialists", 
            "additive group tasks", "compensatory group tasks", "disjunctive group tasks", "conjunctive group tasks", 
            "social loafing", "structured unstructured decisions", 
            "risk uncertainty decision", "faulty heuristics", "escalation commitment", "information overload decision", 
            "participatory decision making", "group decision complementary", 
            "brainstorming techniques", "jad joint application", "risky shift", 
            "delphi technique expert", "team heedfulness", "collective mind", 
            "egoless programming", "chief programmer team", "co-pilot role", "program clerk", "program librarian", 
            "information overload chief", "staff dissatisfaction chief", 
            "functional department", "project department", "matrix department", 
            "functional format", "technical ladder", "project format", "strong weak matrix", 
            "multiplicity authority", "democratic team", "mixed control team", 
            "single point failure", "coordination dependencies", "shared resources coordination", 
            "producer-customer relationships", "task-subtask dependencies", 
            "accessibility dependencies", "usability dependencies", "fit requirements", 
            "mcchesney gallagher", "go-between role", "email principal communication", 
            "copying emails", "dispersed virtual teams", "dispersed working", "virtual teams", 
            "co-located teams", "co-located vs dispersed", 
            "flow deep concentration", "ibm research workspace", "noise levels defects", 
            "home working", "offshore staff", "advantages dispersed", "challenges dispersed", 
            "communication genres time", "telephone same time", "instant messaging", 
            "email different time", "voicemail", "documents different", 
            "early project stages", "intermediate design", "implementation stages", 
            "communication plans stakeholder", "leadership ability influence", 
            "position power", "personal power", "directive autocrat", "permissive autocrat", 
            "directive democrat", "permissive democrat", "task-oriented people-oriented", 
            "tuckman jensen stages", "forming storming norming performing adjourning", 
            "belbin team roles", "chair role", "plant role", "monitor-evaluator", 
            "shaper role", "team worker", "resource investigator", "completer-finisher", 
            "company worker", "specialist role", "new york times data bank"
        ],
        "content": """👥 **Team Structures and Group Working Enhancement**

**1. Team Development Stages (Tuckman & Jensen):**
• **Forming**: Ground rules about behavior, team members get acquainted
• **Storming**: Conflicts emerge, leadership exertion, power struggles
• **Norming**: Group identity emerges, cohesion develops
• **Performing**: Emphasis on tasks at hand, high productivity
• **Adjourning**: Group disbands, project completion

**2. Belbin Team Role Classification:**
• **Chair/Coordinator**: Clarifies goals, promotes decisions, delegates
• **Plant**: Creative, solves difficult problems, generates ideas
• **Monitor-Evaluator**: Strategic, sees all options, judges accurately
• **Shaper**: Challenging, thrives on pressure, directs attention
• **Team Worker**: Cooperative, diplomatic, jollies people along
• **Resource Investigator**: Extrovert, explores opportunities, develops contacts
• **Completer-Finisher**: Painstaking, delivers on time, checks details
• **Company Worker/Implementer**: Disciplined, turns ideas into actions
• **Specialist**: Technical knowledge, professional dedication

**Team Role Imbalances:**
⚠️ Two or more Shapers without Chair → Stormy atmosphere
⚠️ Plants and Specialists without Shapers → No implementation
⚠️ 30% of subjects unclassifiable in Belbin's research

**3. Group Task Types:**
• **Additive Tasks**: Gang clearing snow - combined effort
• **Compensatory Tasks**: Pooling judgments - averaging estimates
• **Disjunctive Tasks**: One correct answer - group as good as best member
• **Conjunctive Tasks**: Progress by slowest - requires cooperation

**Social Loafing Prevention:**
✅ Make individual contributions identifiable
✅ Keep group sizes small
✅ Make tasks meaningful and challenging
✅ Increase group cohesion
✅ Provide individual feedback

**4. Decision Making in Groups:**

**Structured vs. Unstructured Decisions:**
• **Structured**: Routine, rule-based, clear procedures
• **Unstructured**: Complex, requires creativity, incomplete information

**Group Decision Making:**
✅ More likely accepted than imposed decisions
✅ Complementary skills and perspectives
❌ Time-consuming process
❌ Unduly influenced by dominant personalities
❌ Conformity to group norms (risky shift)

**Participatory Decision Making:**
• JAD (Joint Application Development) for user involvement
• Prototyping for end-user engagement
• Brainstorming techniques for creative solutions

**Delphi Technique:**
• Expert judgement without face-to-face meetings
• Steps: Cooperation → Problem presentation → Recommendations → Collation → Recirculation → Comments → Consensus
• Advantages for geographically dispersed experts
• Time-consuming but avoids groupthink

**5. Team Structures:**

**Chief Programmer Team:**
• **Chief Programmer**: Senior-level programmer, single unifying intellect
• **Co-pilot**: Alternative chief, provides backup
• **Program Clerk**: Documentation, configuration management
• **Program Librarian**: Master copies, version control
• **Tester**: Independent testing
• **Editor**: Documentation preparation
• **Temporary Members**: Specialists for particular problems
• **Example**: New York Times data bank project

**Advantages:**
✅ Design consistency for large complex systems
✅ Reduced number of programmers but increased productivity
✅ Clear hierarchy and responsibility

**Disadvantages:**
❌ Single point failure risk
❌ Information overload danger for chief
❌ Staff dissatisfaction
❌ Difficulty finding outstanding programmers

**Democratic Team:**
• No formal hierarchy
• Manager provides administrative leadership
• Different members provide technical leadership
• Higher morale and job satisfaction
• Lower manpower turnover
• Suitable for research-oriented projects (<6 developers)
• Less productive for small simple projects
• Overhead for large team sizes

**Mixed Control Team:**
• Dashed lines for communication
• Solid arrows for reporting
• Democratic at senior level for problem decomposition
• Democratic at programmer level for solutions
• Suitable for large team sizes

**6. Departmental Structures:**

**Functional Organization:**
• Based on staff specialization
• Verticals: Banking, embedded, telecom
• Functional groups: Database, networking, testing
• **Advantages**: Ease of staffing, job specialization, quality documentation, handles turnover
• **Disadvantages**: Partially completed product passing between teams, idling in initial phases, pressure in later phases
• Technical ladder career path
• Rarely adopted by industry (paradox)

**Project Organization:**
• Task-oriented teams
• Facilitates career as business analysts/managers
• Team members dedicated to single project

**Matrix Organization:**
• **Strong Matrix**: Functional managers assign workers
• **Weak Matrix**: Project manager controls budget, can reject workers
• **Advantages**: Resource flexibility, technical excellence
• **Disadvantages**: Multiplicity of authority, conflicts, firefighting mode

**7. Coordination in Teams:**

**Coordination Dependencies:**
• **Shared Resources**: Coordination dependency
• **Producer-Customer**: Right time relationships (PFD)
• **Task-Subtask**: Forced by technical nature
• **Accessibility**: Right place dependencies
• **Usability**: Right thing dependencies (fitness for purpose)
• **Fit Requirements**: Component integration

**Coordination Practices (McChesney & Gallagher):**
• Go-between role for coordination
• Email as principal communication means
• Copying emails to keep stakeholders in loop
• Email volume can overwhelm staff

**8. Communication in Projects:**

**Communication Genres:**
• Beyond technologies - organizational conventions
• **Same Time/Same Place**: Face-to-face meetings (early stages)
• **Same Time/Different Place**: Telephone, instant messaging
• **Different Time/Different Place**: Email, voicemail, documents

**Best Communication Modes:**
• **Early Stages**: Same time/same place meetings critical
• **Intermediate Design**: Teleconferencing
• **Implementation**: Email for information exchange
• **Regular Face-to-Face**: Supplies rhythm to project

**Communication Plan Components:**
• What (event/type)
• Who/target audience
• Purpose
• When/frequency
• Type/method
• Responsibility

**9. Dispersed and Virtual Teams:**

**Advantages:**
✅ Lower costs
✅ Flexible staff
✅ Different time zones (24-hour development)
✅ Access to global talent

**Challenges:**
❌ Carefully specified requirements needed
❌ Formally expressed procedures
❌ Payment methods modified (fixed price, piece-rate)
❌ Lack of trust in remote co-workers
❌ Thorough quality assessment required
❌ Different time zones causing communication problems
❌ Specification, coordination, trust issues

**Home Working:**
• 77% of businesses allowed home working (2004)
• Broadband channels reduce coordination problems
• Graphic designer as intermittent specialist for web projects
• Offshore staff as dispersed team members

**10. Flow and Workspace:**

**Flow State (Deep Concentration):**
• 15 minutes uninterrupted effort needed
• Every interruption destroys flow
• 15 minutes recovery needed after interruption

**IBM Research on Ideal Workspace:**
• 100 square feet dedicated space per developer
• 30 square feet work surface
• Partitions at least 6 feet high for noise protection
• Noise levels linked to software defects (DeMarco & Lister)

**11. Leadership Styles:**

**Leadership Axes:**
• **Directive vs. Permissive**
• **Autocratic vs. Democratic**
• **Task-oriented vs. People-oriented**

**Leadership Styles:**
• **Directive Autocrat**: Decides alone, close supervision
• **Permissive Autocrat**: Decides alone, subordinates have latitude
• **Directive Democrat**: Participative decisions, close supervision
• **Permissive Democrat**: Participative decisions, latitude

**Power Types:**
• **Position Power**: Coercive, Connection, Legitimate, Reward
• **Personal Power**: Expert, Information, Referent

**Management Orientation:**
• **Task-oriented**: Effective with inexperienced teams, uncertainty
• **People-oriented**: Valued as group members mature, staff control work
• **Best**: High in both orientations

**12. Team Heedfulness and Collective Mind:**

**Collective Mind:**
• Appearance from shared understanding
• Familiarity and good communications
• Football team analogy
• Programs as common property (Weinberg)
• Peer code reviews based on egoless programming

**XP Practices Promoting Collective Mind:**
• Less formal communication methods
• Continual integration testing

**Team Building:**
• Outdoor activities
• Joint assignment as purpose
• Social roles beyond technical roles
• Judgement and decision-making tasks better by groups

**Key Success Factors:**
✅ Clear role definitions
✅ Balanced team composition
✅ Effective communication channels
✅ Appropriate leadership style
✅ Trust and mutual respect
✅ Shared goals and objectives
✅ Regular feedback and adjustment"""
    },
    {
        "topic": "Waterfall Model",
        "keywords": [
            "waterfall model", "stage-gate model", "classical model", "sequential development", 
            "linear model", "cascade model", "limited iteration", "natural milestones", 
            "well-defined requirements", "h.d. bennington waterfall", "reopening completed activities", 
            "business case review", "stage-gate", "ideal well-defined", "escaping end activity", 
            "activities grouped differently", "alternative approaches"
        ],
        "content": """📊 **Waterfall Model (Classical/Stage-Gate Model)**

**Overview:**
First described by H.D. Bennington (1956), the Waterfall model is a linear, sequential approach where each phase must be completed before the next begins.

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
❌ Reopening completed activities plays havoc with dates

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
        "topic": "Spiral Model",
        "keywords": [
            "spiral model", "boehm model", "risk-driven model", "boehm spiral", 
            "four quadrants", "incremental style risk", "tailoring phases", 
            "buying knowledge", "prototyping spiral", "ieee computer 1988", 
            "phases not fixed", "spiral quadrants", "risk handling spiral"
        ],
        "content": """🌀 **Spiral Model (Boehm's Risk-Driven Model)**

**Overview:**
Developed by Barry Boehm (IEEE Computer, 1988), the Spiral model combines iterative development with systematic risk management.

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
• **Phases Not Fixed**: Varies by project

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
        "topic": "Estimation Techniques",
        "keywords": [
            "software estimation", "cocomo", "function point", "sloc estimation", 
            "expert judgement estimation", "analogy-based estimation", "delphi technique estimation", 
            "parkinson's law estimation", "weinberg's law", "mythical man-month", 
            "bottom-up top-down", "wbs estimation", "effort duration estimation", 
            "person-month effort", "productivity calculation", "algorithmic models", 
            "cosmic full function", "mark ii function", "capers jones", "putnam staffing", 
            "rayleigh-norden", "unrealistic estimates", "subjective estimating", 
            "political implications estimation", "independent estimating", 
            "changing technology estimation", "lack homogeneity", "iso 12207 estimation", 
            "productivity sloc", "programmer productivity variation", "strategic planning estimates", 
            "feasibility study estimates", "system specification estimates", "suppliers proposals estimates", 
            "effort vs duration", "project size independent", "source lines code", 
            "function points size", "no precise sloc", "difficulty estimating sloc", 
            "sloc code measure", "programmer-dependent sloc", "sloc complexity", 
            "communication overhead", "adding manpower late", "expert judgement", 
            "estimating analogy", "parkinson method", "price to win", "work breakdown structure", 
            "procedural code-oriented", "estimating sloc module", "complexity technical difficulty", 
            "cocomo ii parametric", "cocomo81 organic", "cocomo ii application", 
            "cocomo ii early", "cocomo ii post-architecture", "object points application", 
            "cocomo ii scale", "cocomo ii effort", "albrecht function", "external input", 
            "external output", "external inquiry", "logical internal file", "external interface file", 
            "ifpug file", "technical complexity adjustment", "converting function points", 
            "mark ii symons", "cosmic real-time", "cosmic data movements", "capers jones rules", 
            "sloc function point", "project duration function", "requirements creep", 
            "cost estimation effort", "staffing pattern", "putnam's staffing", "schedule compression", 
            "limit schedule compression"
        ],
        "content": """📊 **Software Estimation Techniques**

**Key Challenges:**
• **Underestimating small tasks, overestimating large tasks**
• **Political implications**: Estimates used for bidding, commitment
• **Changing technology**: Difficult to predict productivity
• **Lack of homogeneity**: Project experience varies widely
• **Subjective nature**: Estimator's comfort zone affects accuracy

**Important Laws:**
• **Parkinson's Law**: Work expands to fill time available
• **Weinberg's Law**: Software is always late
• **Brooks' Mythical Man-Month**: Adding people to late project makes it later
• **Communication overhead**: Increases as square of team size n(n-1)/2

**Estimation Parameters:**
• **Effort**: Person-months (PM) or work-months (WM)
• **Duration**: Calendar time to completion
• **Size**: Independent variable (SLOC, Function Points)
• **Productivity**: Dependent variable (SLOC/PM)

**Size Metrics:**

**1. Source Lines of Code (SLOC):**
• **Advantages**: Objective, easy to count post-development
• **Disadvantages**:
  - No precise definition
  - Difficult to estimate at project start
  - Only measures code (ignores other activities)
  - Programmer-dependent
  - Doesn't consider complexity
  - Excludes comment lines (writer's view)

**2. Function Points (FP):**
• **Albrecht FP Types**:
  - External Inputs
  - External Outputs
  - External Inquiries
  - Logical Internal Files
  - External Interface Files
• **Technical Complexity Adjustment (TCA)**: 14 factors
• **Disadvantages**: TCA produces less accurate estimates

• **Mark II FP**: Weighted sum (2.5 total)
  - Industry averages: 0.58, 1.66, 0.26

• **COSMIC-FFP**: For real-time/embedded systems
  - Data movements: Entries, Exits, Reads, Writes
  - ISO/IEC 19761:2003 standard

**Estimation Methods:**

**1. Expert Judgement:**
• Delphi technique for combining opinions
• Steps: Cooperation → Problem presentation → Recommendations → Collation → Recirculation → Comments → Consensus
• Advantages for geographically dispersed experts

**2. Analogy-Based Estimation:**
• Case-based reasoning
• ANGEL software tool for automated selection
• Euclidean distance calculation for project similarity

**3. Algorithmic Models:**

**COCOMO II (Constructive Cost Model):**
• **Three Stages**:
  - **Application Composition**: High-productivity tools, object points
  - **Early Design**: 13 parameters, rough estimates (±400%)
  - **Post-Architecture**: 23 parameters, final construction

• **Scale Factors (Exponent Drivers)**:
  - **PREC** (Precedentedness)
  - **FLEX** (Development Flexibility)
  - **RESL** (Architecture/Risk Resolution)
  - **TEAM** (Team Cohesion)
  - **PMAT** (Process Maturity)

**COCOMO81 Modes:**
• **Organic**: Small teams, familiar environment
• **Semi-detached**: Intermediate
• **Embedded**: Tight constraints

**4. Bottom-Up Estimating:**
• Work Breakdown Structure (WBS)
• Identify tasks (1-2 person-weeks)
• Estimate each module SLOC
• Forced when no historical data

**5. Top-Down Estimating:**
• Overall project estimate
• Allocate to components

**6. Parkinson Method:**
• Effort available becomes estimate
• Scope-setting rather than prediction

**7. Price to Win:**
• Price identification, not prediction
• Design to cost acceptable

**Productivity Calculation:**
• Industry average: 10 SLOC/day
• Variation: 7 to 150 SLOC/day
• Organization productivity from multiple projects
• ISBSG database for benchmarks

**Duration Estimation:**
• **Capers Jones Rules**:
  - Function points^0.4 for duration in months
  - Requirements creep: 2% per month
  
**Putnam's Staffing Pattern:**
• Rayleigh-Norden curve adaptation
• Peak staffing during product delivery (TD)
• **Fourth Power Law**: Schedule compression effect
• **75% Limit**: Maximum schedule compression (Boehm)

**Cost Estimation:**
• Effort × Manpower cost/month
• Overhead costs: Hardware, software, space, services
• Employer contributions (social security, pension)

**Re-estimating:**
• Step Wise: Progressive refinement
• Design stage confirms feasibility
• System specification for design proposals
• Evaluation of supplier proposals

**Key Considerations:**
⚠️ Estimates are management goals, not predictions (Boehm)
⚠️ Developers more committed to self-set targets
⚠️ Consistency essential in SLOC definition
⚠️ Person-month accounts for holidays/breaks
⚠️ Men and months tradable only without dependencies
⚠️ Training cannot be partitioned among team members

**Improving Accuracy:**
✅ Use multiple methods and compare
✅ Maintain historical database
✅ Calibrate models to organization
✅ Involve developers in estimation
✅ Document assumptions
✅ Track actual vs. estimated
✅ Account for requirements creep (2%/month)"""
    },
    {
        "topic": "Risk Management",
        "keywords": [
            "risk management", "risk identification", "risk analysis", "risk mitigation", 
            "risk register", "probability impact matrix", "risk exposure", 
            "proactive reactive risk", "boehm top 10 risks", "risk reduction leverage", 
            "uncertain event objectives", "risk components future", "lyytinen mathiassen ropponen", 
            "checklists brainstorming", "personnel schedules", "wrong functions", "gold-plating", 
            "potential damage probability", "qualitative risk assessment", 
            "acceptance avoidance reduction", "mitigation transfer", "rrl calculation", 
            "risk register content", "top project failure", "incomplete requirements", 
            "lack user involvement", "resource constraints", "unrealistic expectations", 
            "poor risk management", "identify brainstorming checklists", "analyze impact probability", 
            "plan responses avoid", "mitigate transfer accept", "monitor triggers update", 
            "risk exposure formula", "key risks personnel", "schedule slippage", "technical risks", 
            "business risks", "risk management intelligently"
        ],
        "content": """⚠️ **Risk Management & Failure Prevention**

**Risk Definition:**
• Uncertain event or condition that affects project objectives
• Components: Future, Cause and Effect
• Can have positive or negative impact

**Risk Framework (Lyytinen, Mathiassen, Ropponen):**
• **Actors**: People involved
• **Technology**: Technical components
• **Structure**: Organizational aspects
• **Tasks**: Work to be performed

**Top Project Failure Causes (Standish Group):**
1. **Incomplete requirements** (43%)
2. **Lack of user involvement** (37%)
3. **Resource constraints** (32%)
4. **Unrealistic expectations** (29%)
5. **Poor risk management** (26%)

**Proactive vs. Reactive Risk Management:**
• **Proactive**: Identify and address before occurrence
• **Reactive**: Respond after risk materializes

**Risk Management Process:**

**1. Risk Identification:**
**Boehm's Top 10 Software Risks:**
1. Personnel shortages
2. Unrealistic schedules and budgets
3. Developing wrong software functions
4. Developing wrong user interface
5. Gold-plating (unnecessary features)
6. Continuous requirements changes
7. Shortcomings of externally performed tasks
8. Shortcomings of externally furnished components
9. Real-time performance shortfalls
10. Straining computer science capabilities

**Identification Techniques:**
• **Checklists**: Based on historical data
• **Brainstorming**: Team collaboration
• **Risk Matrix**: Categorization tool

**2. Risk Analysis and Assessment:**

**Risk Exposure Formula:**
Risk Exposure = Potential Damage × Probability

**Probability Impact Matrix:**
• **Qualitative Assessment**: High/Medium/Low
• **Importance**: Separate from likelihood
• **Separately assessed** dimensions

**Example Risks:**
• Client rejects proposed look and feel
• Warehouse unable to deal with increased demand
• Online payment security problems
• Response times deterring purchasers

**3. Risk Planning Strategies:**

**Risk Reduction Leverage (RRL):**
RRL = (Risk Exposure Before - Risk Exposure After) / Cost of Risk Reduction

**Response Strategies:**
• **Acceptance**: Acknowledge and monitor
• **Avoidance**: Eliminate the threat
• **Reduction**: Reduce probability or impact
• **Mitigation**: Minimize consequences
• **Transfer**: Shift to third party (insurance, outsourcing)

**Risk Reduction Plans:**
• Design reviews
• Additional testing
• Staff training
• Prototyping
• Contingency planning

**4. Risk Register:**

**Content:**
• Risk description
• Category (technical, schedule, cost, etc.)
• Probability
• Impact
• Risk exposure
• Response strategy
• Action plan
• Owner
• Status
• Triggers

**Maintenance:**
• Update weekly
• Monitor triggers
• Track effectiveness of responses
• Add new risks as identified

**Key Risk Categories:**

**Project Risks:**
• Personnel shortages
• Schedule slippage
• Wrong functions (gold-plating)
• Technical risks (new technology)
• Resource constraints

**Business Risks:**
• Market changes
• Competitor actions
• Regulatory changes
• Economic conditions

**Risk Management Best Practices:**
✅ Identify risks early
✅ Analyze impact and probability
✅ Plan responses proactively
✅ Monitor triggers and update register weekly
✅ Communicate risks to stakeholders
✅ Maintain contingency budget
✅ Review risks at each milestone

**Remember:**
💡 Risk management is not about eliminating risk, but managing it intelligently
💡 Some risk is inevitable and necessary for innovation
💡 Early identification reduces cost of mitigation
💡 Regular monitoring prevents surprises"""
    },
    {
        "topic": "Quality Management",
        "keywords": [
            "software quality", "iso 9126", "mccall quality", "garvin quality", 
            "cmm capability", "quality assurance", "software reviews", "testing strategies", 
            "configuration management quality", "change control quality", "quality measurement", 
            "process quality monitoring", "external quality standards", "increasing criticality", 
            "accumulating errors", "bs iso iec 15939", "direct indirect quality", 
            "quality specification", "reliability measurements", "maintainability components", 
            "garvin dimensions", "mccall model", "dromey quality", "boehm quality", 
            "functionality suitability", "reliability maturity", "usability understandability", 
            "efficiency time", "maintainability analysisability", "portability adaptability", 
            "correctness reliability", "integrity usability", "flexibility testability", 
            "reusability interoperability", "internal characteristics", "contextual characteristics", 
            "descriptive properties", "as-is utility", "maintainability portability", 
            "quality characteristics", "compliance security", "fault tolerance recoverability", 
            "learnability operability", "attractiveness compliance", "resource utilization", 
            "changeability stability", "installability coexistence", "replaceability compliance", 
            "mapping quality measurements", "product metrics", "process metrics", 
            "product process quality", "entry requirements", "implementation requirements", 
            "exit requirements", "bs en iso 9001", "iso 9000 series", "iso 9001 qms", 
            "iso 9004 improvement", "stephen halliday", "means-ends inversion", 
            "sei capability maturity", "cmm five levels", "initial repeatable", 
            "defined managed optimizing", "quality specifications", "system unavailable", 
            "availability mtbf", "changeability analysisability", "analysisability ease", 
            "performance features", "conformance durability", "serviceability aesthetics", 
            "perceived quality", "operational characteristics", "ease fixing", "ease porting", 
            "nested menus", "attractiveness games", "replaceability upwards", 
            "downwards compatibility", "coexistence sharing", "judge importance", 
            "select external", "map measurements", "identify internal", 
            "internal external mapping", "validation correlation", "qualitative indicators", 
            "quantitative measurements", "combining ratings", "presence quality", 
            "efficiency portability", "mandatory quality", "importance weighting", 
            "weighted scores", "product comparison", "review effectiveness", "defects inspection", 
            "average defect", "failures detected", "latent defects", "product-based pr", 
            "predicting final", "errors entering", "errors caused", "development step", 
            "test data", "repeating test", "tests successful", "quality control", 
            "quality assurance", "identical iso", "ce marks", "quality manual", 
            "change control system", "management responsibility", "resources trained", 
            "effective communications", "design outcomes", "adequate measures", 
            "controlled conditions", "measurement demonstrate", "uvw company", "lisa software", 
            "project engineer", "separate systems", "fault correction", "process improvement", 
            "psp personal"
        ],
        "content": """✅ **Software Quality Management**

**Increasing Criticality of Software:**
• Software failures can threaten human life
• Accumulating errors during development
• Quality essential for users and developers

**Quality Measurement (BS ISO/IEC 15939:2007):**
• **Direct Measures**: Observable attributes
• **Indirect Measures**: Derived from other measures

**Quality Specification Components:**
1. Definition
2. Scale
3. Test
4. Acceptable range
5. Target range

**Quality Models:**

**1. Garvin's Eight Quality Dimensions:**
1. **Performance**: Primary operating characteristics
2. **Features**: Bells and whistles
3. **Reliability**: Probability of failure
4. **Conformance**: Meeting specifications
5. **Durability**: Product life
6. **Serviceability**: Speed and courtesy of repair
7. **Aesthetics**: Look, feel, sound, taste, smell
8. **Perceived Quality**: Reputation and brand image

**2. McCall's Quality Model:**

**Three High-Level Parameters:**
• **Product Operation**: Correctness, Reliability, Efficiency, Integrity, Usability
• **Product Revision**: Maintainability, Flexibility, Testability
• **Product Transition**: Portability, Reusability, Interoperability

**Characteristics:**
• **Correctness**: Extent to which program satisfies specifications
• **Reliability**: Extent to which program performs as expected
• **Efficiency**: Amount of computing resources required
• **Integrity**: Control of unauthorized access
• **Usability**: Effort required to learn and operate
• **Maintainability**: Effort required to locate and fix errors
• **Flexibility**: Effort required to modify program
• **Testability**: Effort required to test program
• **Portability**: Effort required to convert to different platform
• **Reusability**: Extent to which program can be reused
• **Interoperability**: Effort required to couple with another system

**3. Dromey's Quality Model:**

**Four High-Level Properties:**
1. **Correctness**: Absence of defects
2. **Internal Characteristics**: Maintainability, complexity
3. **Contextual Characteristics**: Reliability, efficiency, usability
4. **Descriptive Properties**: Documentation, structure

**4. Boehm's Quality Model:**
• **As-is Utility**: Fitness for current use
• **Maintainability**: Ease of modification
• **Portability**: Ease of transfer to different platform
• Based on wider range of attributes
• Greater focus on maintainability

**5. ISO 9126 Quality Characteristics:**

**Six Main Characteristics:**

**1. Functionality:**
• Suitability: Appropriateness for specified tasks
• Accuracy: Correctness of results
• Interoperability: Interaction with other systems
• Compliance: Adherence to standards
• Security: Protection of data and access

**2. Reliability:**
• Maturity: Frequency of failure due to faults
• Fault Tolerance: Ability to withstand faults
• Recoverability: Ability to recover from failure
• Compliance: Adherence to reliability standards

**3. Usability:**
• Understandability: Ease of understanding
• Learnability: Ease of learning
• Operability: Ease of operation
• Attractiveness: Visual appeal (games, entertainment)
• Compliance: Usability standards adherence

**4. Efficiency:**
• Time Behavior: Response and processing times
• Resource Utilization: Amount of resources used
• Compliance: Efficiency standards

**5. Maintainability:**
• Analysisability: Ease of identifying failure causes
• Changeability: Ease of modification
• Stability: Low risk of unexpected effects
• Testability: Ease of testing modifications
• Compliance: Maintainability standards

**6. Portability:**
• Adaptability: Adaptation to different environments
• Installability: Ease of installation
• Coexistence: Sharing resources without data passing
• Replaceability: Upwards compatibility
• Compliance: Portability standards

**Note:**
• Interoperability ≠ Compatibility
• Learnability vs. Operability trade-off (nested menus)
• Replaceability implies upwards, not downwards compatibility
• Stability = low risk from modifications

**Mapping Quality Measurements:**

**Process:**
1. Judge importance of each quality characteristic for application
2. Select external quality measurements relevant to priorities
3. Map measurements onto user satisfaction ratings
4. Identify internal measurements and intermediate products
5. Validate correlation between internal and external measurements

**Challenges:**
• Internal to external mapping least convincing
• Presence of one quality to detriment of another
• Efficiency at expense of portability
• Combining ratings difficult

**Approaches:**
• **Mandatory Levels**: Minimum ratings for acceptance
• **Weighted Scores**: Importance weighting, sum for overall score
• **Qualitative Indicators**: Early stages (checklists, expert judgement)
• **Quantitative Measurements**: Near completion

**Quality Metrics:**

**Product Metrics:**
• Defect density
• Number of latent defects per LOC
• Average failures during testing per LOC

**Process Metrics:**
• Review effectiveness (defects per inspection hour)
• Average defect correction time
• Entry/Implementation/Exit requirements compliance

**Quality Activities:**

**1. Software Reviews:**
• More cost-effective than testing for defect removal
• Identifies deviation from standards
• Learning opportunity for participants
• Suggests time/space efficient algorithms

**Review Candidates:**
• Requirements specification
• Design documents
• User interface specification
• Test plans and cases
• Configuration management plan

**2. Testing Strategies:**
• Unit testing
• Integration testing
• System testing
• Acceptance testing

**3. Configuration Management:**
• Version control
• Change control
• Baseline management

**Quality Standards:**

**BS EN ISO 9001:2000:**
• Identical to ISO 9001:2000
• Quality Management System (QMS) requirements
• **Key Elements**:
  - Quality manual documenting procedures
  - Change control system for QMS documentation
  - Management responsibility
  - Resources (trained staff, infrastructure)
  - Effective communications
  - Design verification, validation, documentation
  - Purchased component quality measures
  - Controlled production conditions
  - Measurement for conformance demonstration

**ISO 9000 Series:**
• **ISO 9001**: QMS for product creation
• **ISO 9004**: Process improvement
• **ISO 25000**: New standard in development

**Criticism (Stephen Halliday, Observer):**
• Means-ends inversion in quality preoccupation
• Focus on process over product

**SEI Capability Maturity Model (CMM):**

**Five Maturity Levels:**
1. **Initial**: Chaotic, ad hoc processes
2. **Repeatable**: Basic project management established
3. **Defined**: Standard processes documented
4. **Managed**: Processes monitored and measured
5. **Optimizing**: Continuous process improvement

**Progression:**
• Level 3 to Level 4 through monitoring
• PSP (Personal Software Process) for individuals

**Example Scenario:**
**UVW Company (Machine Tool Equipment):**
• Lisa: Software Team Leader (6 designers)
• Project Engineer: Not primarily software specialist
• Separate Systems Testing Group
• Fault correction and adaptive maintenance not tested by Systems Testing Group

**Quality Specifications Example:**
• System unavailable for one whole day (disk drive)
• System not available until 10am (batch processing)
• Calculate availability and MTBF from data

**Maintainability:**
• Changeability + Analysisability
• Analysisability: Ease of identifying failure causes

**Key Principles:**
✅ Quality must be built into process, not inspected in at end
✅ Each development step before error found increases rework
✅ Errors enter at any stage
✅ Predicting final quality from intermediate attributes difficult
✅ Process metrics convenient for PRINCE2
✅ Quality control vs. quality assurance distinction

**Best Practices:**
✅ Define quality specifications early
✅ Use appropriate models for application type
✅ Combine qualitative and quantitative measures
✅ Regular reviews and testing
✅ Configuration management
✅ Continuous process improvement
✅ Staff training and competence development
✅ Lessons learned from previous projects"""
    },
    {
        "topic": "Business Case & Portfolio",
        "keywords": [
            "business case", "portfolio management", "npv", "irr", "roi", 
            "cost-benefit", "payback period", "investment", "net present value", 
            "internal rate of return", "return on investment", "discounted cash flow", 
            "risk-adjusted npv", "sensitivity analysis", "decision trees", 
            "programme management", "benefits management", "strategic project selection", 
            "warren mcfarlan", "npd renewal projects", "below-the-line projects", 
            "ad hoc tasks", "margin non-planned work", "technical assessment", 
            "development costs", "setup costs", "operational costs", "cash flow forecasting", 
            "decommissioning costs", "ignoring inflation", "quarterly monthly cash flow", 
            "net profit criterion", "payback period calculation", "payback ignoring post-breakeven", 
            "roi formula", "disadvantages roi", "npv considering profitability timing", 
            "discount rate selection", "risk premium", "present value formula", 
            "discount factor table", "npv calculation year 0", "difficulty selecting discount rate", 
            "discount rate target return", "irr percentage measure", "irr calculated discount rate", 
            "irr deficiency absolute size", "multiple irr solutions", "funding cash flow problems", 
            "project risk matrix importance likelihood", "probability-weighted expected value", 
            "buyright payroll example", "cost-benefit portfolio evaluation", "sensitivity analysis varying", 
            "decision tree sequential risk", "expected value decision trees", "dc ferns programme", 
            "business cycle programmes", "strategic programmes", "infrastructure programmes", 
            "research development programmes", "innovative partnerships", "programme manager project manager", 
            "programme manager personal relationship", "programme manager maximize resource", 
            "project manager impersonal relationship", "programme management monitoring", 
            "strategic programme management", "ogc guidelines programme", "programme mandate", 
            "programme director appointment", "programme champion", "programme brief business case", 
            "preliminary vision statement", "vision statement refinement", "blueprint structural operational", 
            "business models new processes", "organizational structure blueprint", 
            "data information requirements blueprint", "benefit profiles estimating", 
            "tangible benefits delivery", "stakeholder map communication", 
            "preliminary programme portfolio", "financial plan budget", 
            "dependency diagrams programme", "tranches projects", "project briefs planning", 
            "reservations programme management", "super-project trap", "programme structure expense process", 
            "bureaucratic obstruction control", "programmes evolution modification", 
            "different forms programme management", "benefits management definition", 
            "mandatory compliance benefit", "quality service benefit", "productivity benefit", 
            "motivated workforce benefit", "internal management benefits", "risk reduction benefit", 
            "economy cost reduction", "revenue enhancement acceleration", "strategic fit benefit", 
            "benefits inter-linked", "quantified valued benefits", "quantified not valued", 
            "identified not quantified", "disbenefits", "tests genuine benefits", 
            "business change managers", "benefits monitored project environment", 
            "developers users jointly responsible", "projects evaluated strategic technical economic", 
            "benefits precisely quantifiable", "money received future worth less", 
            "uncertainty future returns lowering", "discounted cash flow present value", 
            "decision trees choosing alternative", "insurance company claims settlement", 
            "stress claims staff", "shortages qualified repair", "brightmouth college off-shelf programmer", 
            "irr calculation investment return", "roi calculation cost profit", 
            "payback period cost inflows", "increase discount rate affecting irr", 
            "irr equal discount rate npv", "payback period maintenance contract", 
            "npv calculation discount rate", "roi not computing discounted net", 
            "roi not computing time period", "bidding costs uk government", 
            "suppliers accommodating contract", "customer bargaining position", 
            "contract department participation", "notifying unsuccessful candidates", 
            "wto eu rules notification", "legal advice substantial contract", 
            "two-stage tendering process", "memorandum agreement suppliers", 
            "demonstrations controlled suppliers", "visits operational sites", 
            "projects decision process initiation", "single project justified benefits", 
            "projects enabling strategic objectives", "medical diagnosis system benefit", 
            "business case multiple potential projects", "management plan section business case", 
            "health-check milestones", "uncertainties costs requirements", 
            "project risk business risk business case", "b de royck portfolio", 
            "too many projects resources", "projects completed organization benefits", 
            "portfolio definition portfolio management", "warren mcfarlan harvard", 
            "setting new warehouse non-ict", "new information system recording insurance", 
            "continuous development new goods", "renewal projects inherently risky", 
            "tracking actual project performance", "rigorous screening new projects", 
            "e-commerce site sales competitors", "automating processes cost cutting", 
            "full-time staff part-time routine", "developers called away support", 
            "only projects certain cost level", "b s bichlefiet eskerod portfolio", 
            "quick fixes systems externally", "reducing higher management work", 
            "first-line managers judgement", "organizational policy limiting technical", 
            "bank investment minimum return", "new sales order processing benefit", 
            "file conversion costs setup", "recruitment costs setup", "staff training costs setup", 
            "brightmouth college payroll costs", "quantified not valued benefits examples", 
            "identified not valued benefits examples", "decommissioning costs product life", 
            "funding development expenditure", "bankruptcy unplanned negative cash", 
            "table project net profit investment", "risk investing single project", 
            "bulk income occurring late", "estimates distant future reliable", 
            "payback period simple calculate", "roi bearing relationship bank", 
            "roi taking account compounding", "100 today better 100 next year", 
            "91 now equivalent 100 one year", "83 now equivalent 100 two years", 
            "discount factor table rates", "initial investment year 0 discounted", 
            "later cash flows end year", "project npv discount rate", 
            "same net profit roi different npv", "discount rate reflecting borrowing", 
            "software projects risky lending", "same discount rate compared projects", 
            "ranking projects sensitive discount", "table projects cash flows discount", 
            "positive npv projects selection", "irr directly comparable interest", 
            "project worthwhile capital borrowed", "project worthwhile capital investable", 
            "microsoft excel irr function", "irr indicating absolute size", 
            "project npv irr vs npv irr", "multiple irr solutions take lowest", 
            "repaying interest borrowed money", "future earnings risky project", 
            "project financial framework organization", "risk identification quantification", 
            "project risk matrix checklist", "importance likelihood separately assessed", 
            "client rejects proposed look", "warehouse unable deal increased", 
            "online payment security problems", "response times deterring purchasers", 
            "risk premiums high medium low", "cost-benefit approach evaluating", 
            "assigning probabilities scenarios", "averaging negative positive outcomes", 
            "worst-case scenarios averaging", "successful projects offset less", 
            "sensitivity analysis varying parameters", "recalculating expected costs", 
            "passive bystander assumption risk", "decision limiting affecting future", 
            "competitor bankruptcy rumours", "replacing system time revenue", 
            "replacing system deferring projects", "extending existing system npv", 
            "market expanding turning loss", "replacing system npv market expands", 
            "replacing system npv market loss", "likelihood market increasing", 
            "probability market increasing", "decision point denoted decision tree", 
            "programmes providing benefits possible"
        ],
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

**1. Payback Period:**
• Time to recover initial investment
• **Advantages**: Simple to calculate, not sensitive to small errors
• **Disadvantages**: Ignores post-breakeven income, ignores timing of cash flows

**2. Return on Investment (ROI):**
• Formula: (Average annual profit / Total investment) × 100
• **Advantages**: Easy to understand
• **Disadvantages**: Ignores timing of cash flows, no relation to interest rates, doesn't account for compounding

**3. Net Present Value (NPV):**
• Considers profitability and timing of cash flows
• **Formula**: Value in year t / (1 + r)^t
• **Discount Rate**: Reflects borrowing costs plus risk premium
• **Advantages**: Accounts for time value of money (£100 today > £100 next year)
• **Disadvantages**: Difficulty selecting appropriate discount rate
• **Decision Rule**: Positive NPV projects considered for selection

**4. Internal Rate of Return (IRR):**
• Percentage measure, directly comparable with interest rates
• Calculated as discount rate producing NPV of zero
• **Advantages**: Easy to compare with cost of capital
• **Disadvantages**: Does not indicate absolute size of return, multiple IRR solutions possible (take lowest value)
• **Decision Rule**: Project worthwhile if capital borrowed for less than IRR

**Portfolio Management:**

**Warren McFarlan Portfolio Concept:**
• Evaluate projects against strategic, technical, and economic criteria
• Balance high-risk/high-reward with low-risk/low-reward projects
• Maintain single repository for all current projects

**Portfolio Optimization:**
• Too many projects started relative to resources → missed dates
• Projects must be completed for organization to reap benefits
• NPD projects attract funding more easily than renewal projects
• Below-the-line projects impact official portfolios

**Benefits Management:**
• **Tangible Benefits**: Quantified and valued (e.g., cost reduction)
• **Intangible Benefits**: Quantified but not valued (e.g., customer satisfaction)
• **Disbenefits**: Negative impacts (e.g., overtime costs)
• **Tests for Genuine Benefits**: Explain, see consequences, attribute, measure

**Programme Management:**
• Grouping individual projects into programmes for coordinated benefits
• **Programme Mandate**: Formal triggering document
• **Programme Brief**: Outlines business case and vision
• **Blueprint**: Structural and operational changes
• **Tranches**: Coherent groups delivering stepwise benefits

**Risk-Adjusted Evaluation:**
• **Sensitivity Analysis**: Varying parameters by ±5%
• **Decision Trees**: Sequential risk-based decisions
• **Expected Value**: Probability-weighted outcomes
• **Risk Premiums**: Added to discount rate for high-risk projects

**Key Principles:**
✅ Projects evaluated on strategic, technical, economic grounds
✅ Money received in future worth less than money now
✅ Uncertainty lowers real value of future returns
✅ Not all benefits precisely quantifiable in financial values
✅ Developers and users jointly responsible for benefits delivery
✅ Benefits cannot normally be monitored in project environment

**Common Pitfalls:**
⚠️ Ignoring inflation in cash flow estimates
⚠️ Focusing only on net profit (ignores investment size)
⚠️ Assuming passive bystander in risk analysis
⚠️ Averaging out worst-case scenarios
⚠️ Bureaucratic obstruction in programme management
⚠️ Super-project trap (programmes becoming too large)

**Best Practices:**
✅ Use multiple evaluation techniques (NPV, IRR, Payback)
✅ Perform sensitivity analysis on key assumptions
✅ Maintain risk register for portfolio projects
✅ Regularly review and re-prioritize portfolio
✅ Ensure strategic alignment of all projects
✅ Track actual benefits vs. planned benefits
✅ Use decision trees for complex sequential decisions"""
    },
    {
        "topic": "Configuration Management",
        "keywords": [
            "configuration management", "change control", "version control", "scm", 
            "baseline management", "variant management", "release management", 
            "software configuration management", "change control board", "ccb", 
            "request for change", "rfc", "configuration librarian", "central repository", 
            "scope creep", "baselining products", "configuration items", "versioning numbering", 
            "revision numbering", "variants operating systems", "concurrent access problems", 
            "undoing changes configuration", "comparing versions", "fixing bug variant", 
            "controlled pre-controlled uncontrolled", "reserve operation", "sccs rcs", 
            "delta storage", "check-out check-in", "bs en iso 9001 change control", 
            "manual change management overwhelmed", "configuration management tool", 
            "configuration items work products", "versioning identification", 
            "revision identification", "variants unix windows", "novice enterprise professional", 
            "concurrent access", "undoing changes", "comparing today yesterday", 
            "fixing bug one variant", "controlled work products", "reserve operation private", 
            "ccb reviewing changes restore", "ccb functions project manager", 
            "sccs rcs unix text", "deltas storing changes baseline", 
            "check-out check-in facilities", "types contracts", "fixed price contracts", 
            "time materials contracts", "fixed price per unit", "open tendering", 
            "restricted tendering", "negotiated procedure", "requirements analysis suppliers", 
            "mandatory desirable requirements", "evaluation plan proposal", 
            "iso 9126 quality evaluation", "value money contract selection", 
            "whole lifetime costs evaluation", "contract terms definitions", 
            "ownership software copyright", "escrow agreement source code", 
            "acceptance procedures testing", "liquidated damages penalty", 
            "alternative dispute resolution"
        ],
        "content": """🔧 **Configuration & Change Management**

**Configuration Management (SCM):**
• **Configuration**: Software product state at any point in time
• **Version**: Configuration at specific point
• **Revision**: Successive states of configuration item
• **Baseline**: Formally reviewed and agreed configuration
• **Variants**: Versions intended to coexist (different platforms)
• **Configuration Items**: Work products under configuration control

**Change Control Process:**
1. Request for Change (RFC) through single authorized channel
2. Assess products affected by proposed change
3. Change Control Board (CCB) approval
4. Configuration librarian maintains master copies
5. Implement change with check-out/check-in
6. User acceptance testing for new versions

**Change Control Board (CCB):**
• Reviews changes before restore
• Functions discharged by project manager for small projects
• Filters within client community before RFC generation
• Prevents bureaucratic bottleneck from too many RFCs
• Allows project manager allowance for minor changes

**Configuration Librarian:**
• Central repository of master copies of project documentation
• System accounting for tracking who made what change
• Release management for systematizing new software releases

**Tools:**
• **SCCS, RCS**: UNIX text file version control
• **Delta Storage**: Efficient version storage (changes between baselines)
• **Check-out/Check-in**: Facilities for controlled access

**Key Concepts:**

**Versioning vs. Revision:**
• **Versioning**: Numbering scheme for specific configuration identification
• **Revision**: Numbering scheme for work product state identification
• **Variants**: For different operating systems (Unix, Windows)
  - Novice version, enterprise version, professional version

**Baselining:**
• Baselining products as foundation for further development
• Freeze products for further development
• Re-estimating system size at key milestones for scope control

**Scope Creep Prevention:**
• Filter changes through CCB
• Single authorized channel for requests for change
• Assess products affected by proposed change
• Large number of small changes having accumulative effect

**Concurrent Access:**
• Concurrent access problems without configuration management
• Undoing changes requiring configuration management
• Comparing today's version with yesterday's version
• Fixing bug in one variant needing fix in all versions

**Work Product Control:**
• Controlled, pre-controlled, and uncontrolled work products
• Reserve operation for getting private copy of module
• Recompiling and testing after code modification
• User acceptance testing for new versions
• Operational release authorization by user

**Standards:**
• BS EN ISO 9001:1994 requiring formal change control
• Manual change management overwhelmed with multiple variants
• Configuration management tool deployment for systematic SCM

**Contract Types:**
• **Fixed Price**: Known customer expenditure
• **Time & Materials**: Fixed rate per unit of effort
• **Fixed Price per Unit**: Function point based

**Tendering Processes:**
• **Open Tendering**: Any supplier can bid
• **Restricted Tendering**: Invited suppliers only
• **Negotiated Procedure**: Single supplier situations

**Contract Evaluation:**
• Mandatory vs. desirable requirements
• Value for money as key criterion
• Whole lifetime costs consideration
• ISO 9126 for quality evaluation

**Contract Terms:**
• Definitions, form of agreement, goods and services
• Ownership of software and copyright
• Escrow agreement for source code protection
• Acceptance procedures and testing
• Liquidated damages and penalty clauses
• Alternative dispute resolution

**Key Principles:**
✅ Configuration management essential for team coordination
✅ Change control prevents scope creep
✅ Baselines provide stable reference points
✅ Version control enables parallel development
✅ CCB ensures changes are evaluated properly
✅ Documentation must be kept up to date

**Best Practices:**
✅ Implement SCM early in project
✅ Define clear versioning scheme
✅ Use automated tools for version control
✅ Regular backups of configuration items
✅ Train team on SCM procedures
✅ Audit configuration items periodically
✅ Integrate SCM with change control process
✅ Monitor scope creep through RFC tracking"""
    },
    {
        "topic": "Planning & Scheduling",
        "keywords": [
            "project planning", "step wise planning", "prince2 methodology", 
            "activity planning", "gantt charts", "critical path method", "cpm", 
            "pert analysis", "network planning models", "resource allocation", 
            "resource smoothing", "resource histograms", "float calculation", 
            "critical path identification", "precedence networks", "activity-on-node", 
            "earned value analysis", "schedule variance", "cost variance", 
            "performance indices", "cpi", "spi", "work breakdown structure", 
            "product breakdown structure", "product flow diagram", "usdp artifacts", 
            "sequencing scheduling activities", "bar charts", "activity-on-arrow", 
            "dummy activities", "forward pass", "backward pass", "total float", 
            "free float", "interfering float", "shortening project duration", 
            "activity standard deviation", "pert three estimates", "pert expected duration", 
            "probability meeting target dates", "z-value calculation", "monte carlo simulation", 
            "resource allocation step wise", "activity schedule planned start", 
            "resource schedule dates levels", "cost schedule planned cumulative", 
            "labour resource category", "equipment resource category", "materials resource", 
            "space resource category", "services resource category", "time resource offset", 
            "money secondary resource", "identifying resource requirements", 
            "project infrastructure resources", "resource requirements list", 
            "mapping resource requirements", "resource histogram visualizing", 
            "earliest start date scheduling", "cost changing resource levels", 
            "idle staff time specification", "smoothing resource histograms", 
            "splitting non-critical activities", "difficulty splitting tasks", 
            "resource smoothing software tools", "prioritizing activities allocation", 
            "total float priority allocation", "burman's priority list", 
            "shortest critical activity priority", "critical activities priority", 
            "shortest non-critical priority", "non-critical least float priority", 
            "resource smoothing possible timescales", "resource constraints critical paths", 
            "resource-linked criticalities", "cost comparison additional staff", 
            "allocating individuals activities", "availability factor allocating", 
            "criticality activities influencing", "risk assessment guiding allocation", 
            "allocating experienced staff risk", "project control cycle monitoring", 
            "four types project shortfall", "project steering committee progress", 
            "project reporting structures", "prince2 project assurance", 
            "categories reporting oral written", "weekly progress meetings minutes", 
            "end-of-stage review meetings", "exception reports deviations", 
            "change reports requirement modifications", "objective tangible information", 
            "checkpoints activity plan", "weekly reporting developers", 
            "review points control points", "prince2 end stage assessment", 
            "difficulty forecasting partially completed", "in-activity milestones", 
            "weekly timesheets resource usage", "99% complete phenomenon", 
            "red amber green rag reporting", "review cost-effective defect removal", 
            "review identifying deviation standards", "review learning opportunity", 
            "review roles moderator recorder", "moderator responsibilities scheduling", 
            "recorder role documenting defects", "review process activities planning", 
            "review team size five seven", "author preceding work reviewer", 
            "user work product reviewer", "peers author reviewers", 
            "review preparation log defect", "review log defects agreed", 
            "review summary report total defects", "gantt chart tracking progress", 
            "today cursor gantt chart", "slip chart schedule variations", 
            "slip line bending variation", "timeline chart target changes", 
            "planned time elapsed time", "cumulative expenditure chart cost", 
            "projected future costs actual", "earned value analysis originating", 
            "planned value pv bcws", "earned value ev bcwp", "0/100 technique earned", 
            "50/50 technique earned", "75/25 technique earned", "milestone technique earned", 
            "baseline budget earned value", "actual cost ac acwp", 
            "schedule variance sv ev pv", "time variance tv planned actual", 
            "cost variance cv ev ac", "cost performance index cpi ev ac", 
            "schedule performance index spi ev pv", "estimate completion eac bac cpi", 
            "time estimate completion teac sac spi", "prioritizing monitoring critical", 
            "activities free float monitoring", "activities critical resources monitoring", 
            "shortening critical path target", "adding resources speed critical", 
            "increasing use current resources", "reallocating staff critical activities", 
            "reducing scope functionality deadlines", "reducing quality-related activities", 
            "reconsidering precedence requirements", "subdividing activities start earlier", 
            "maintaining business case revising", "exception planning exception reports", 
            "change control requirements modifications", "baselining products freeze"
        ],
        "content": """📅 **Project Planning & Scheduling**

**Planning Steps:**
1. Define scope & deliverables
2. Create Work Breakdown Structure (WBS)
3. Estimate effort & resources
4. Develop realistic timeline
5. Identify risks & mitigation
6. Establish communication protocols

**Scheduling Techniques:**

**1. Gantt Charts:**
• Visual timeline representation
• Named after Henry Gantt (1861-1919)
• Shading activity bars for reported progress
• Today cursor for visual progress indication
• Combines sequencing and scheduling

**2. Critical Path Method (CPM):**
• Developed by DuPont Chemical Company (1958)
• **Forward Pass**: Earliest start/finish dates
• **Backward Pass**: Latest start/finish dates
• **Float Calculation**:
  - Total Float: Time activity can be delayed without delaying project
  - Free Float: Time activity can be delayed without delaying successor
  - Interfering Float: Total Float - Free Float
• **Critical Path Identification**: Path with zero total float
• **Shortening Duration**: Reduce critical path activities

**3. PERT Analysis:**
• **Three Estimates**: Optimistic (a), Most Likely (m), Pessimistic (b)
• **Expected Duration**: (a + 4m + b) / 6
• **Activity Standard Deviation**: (b - a) / 6
• **Probability Calculations**: Z-value for target dates
• **Monte Carlo Simulation**: Risk analysis for schedule uncertainty

**4. Network Planning Models:**
• **Precedence Networks**: Activity-on-node
  - Single start node rule
  - Single end node rule
  - Links have no duration
  - No loops allowed
• **Activity-on-Arrow Networks**:
  - Nodes as events (zero duration)
  - Dummy activities for logical dependencies
  - Sequential node numbering
  - Dangling activities avoided

**Resource Allocation:**

**Resource Categories:**
• Labour (project manager, analysts, developers)
• Equipment (workstations, office equipment)
• Materials (consumables like disks)
• Space (office space for additional staff)
• Services (telecommunications services)
• Time & Money (secondary resources)

**Resource Histograms:**
• Visualizing resource distribution
• Earliest start date scheduling creates peaked histograms
• Ideal histogram: Initial build-up and staged run-down

**Resource Smoothing:**
• Adjust activity start dates using float
• Split non-critical activities (difficult in software)
• Prioritize: Critical path first, then by total float
• **Burman's Priority List**:
  - Critical activities
  - Non-critical activities with least float
  - Shortest non-critical activities
• Resource constraints can create new critical paths

**Earned Value Analysis:**
• Originated from US Department of Defence
• **Key Metrics**:
  - Planned Value (PV) / BCWS: Budgeted cost of work scheduled
  - Earned Value (EV) / BCWP: Budgeted cost of work performed
  - Actual Cost (AC) / ACWP: Actual cost of work performed
  - Budget at Completion (BAC)
• **Variance Analysis**:
  - Schedule Variance (SV) = EV - PV (negative = behind schedule)
  - Cost Variance (CV) = EV - AC (negative = over budget)
• **Performance Indices**:
  - Cost Performance Index (CPI) = EV / AC (>1 = better than planned)
  - Schedule Performance Index (SPI) = EV / PV
• **Forecasting**:
  - Estimate at Completion (EAC) = BAC / CPI
  - Time Estimate at Completion (TEAC) = SAC / SPI
• **Earned Value Assignment Techniques**:
  - 0/100 technique (nothing until complete)
  - 50/50 technique (50% at start, 50% at finish)
  - 75/25 technique
  - Milestone technique

**Project Control Cycle:**
1. Monitor progress
2. Compare with plan
3. Identify shortfalls (delays, quality, functionality, costs)
4. Revise plan if necessary

**Reporting:**
• **Traffic-Light (RAG)**: Red/Amber/Green status
• **Slip Charts**: Visual indication of schedule variations
• **Timeline Charts**: Recording target changes over duration
• **Cumulative Expenditure**: Comparing actual vs. planned

**Key Principles:**
✅ Planning is iterative and progressive
✅ Resource constraints affect schedule
✅ Critical path determines project duration
✅ Earned value provides objective progress measurement
✅ Regular reporting keeps stakeholders informed
✅ Exception reporting for significant deviations

**Best Practices:**
✅ Use WBS for detailed planning
✅ Identify critical path early
✅ Monitor critical activities closely
✅ Use float wisely for resource smoothing
✅ Perform earned value analysis regularly
✅ Update plans based on actual progress
✅ Communicate changes promptly
✅ Maintain baseline for comparison"""
    }
]

def get_random_suggestions(num_suggestions=10):
    """Generate random suggestions from SPM topics"""
    return random.sample(SPM_TOPICS, min(num_suggestions, len(SPM_TOPICS)))

def query_qwen_api(prompt, api_key):
    """Query Qwen API with fallback mock response"""
    try:
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
• Team structures and group working
• Waterfall model
• Spiral model
• Risk management
• Estimation techniques (COCOMO, Function Points)
• Quality management (ISO 9126, CMM)
• Leadership styles
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
                if hasattr(st, 'rerun'):
                    st.rerun()
                else:
                    st.experimental_rerun()

def main():
    st.title("⚖️ Software-Project-Management for B.E.Computer Science/B.Tech Information Technology Chatbot")
    
    st.markdown("""
    <div style='background-color: #4169E1; padding: 12px; border-radius: 8px; margin: 15px 0; border: 3px solid black; text-align: center;'>
        <p style='color: white; font-weight: bold; font-size: 15px; margin: 0;'>
            🎯 Target: B.E. Computer Science | B.Tech IT Students | IT Job Seekers
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'user_query' not in st.session_state:
        st.session_state.user_query = ""
    if 'result' not in st.session_state:
        st.session_state.result = ""
    if 'suggestions' not in st.session_state:
        st.session_state.suggestions = get_random_suggestions(10)
    
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
    
    display_suggestions(st.session_state.suggestions)
    st.markdown("---")
    
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
    
    if reset_clicked:
        st.session_state.user_query = ""
        st.session_state.result = ""
        st.session_state.suggestions = get_random_suggestions(10)
        if hasattr(st, 'rerun'):
            st.rerun()
        else:
            st.experimental_rerun()
    
    if submit_clicked and user_query.strip():
        st.session_state.user_query = user_query.strip()
        
        with st.spinner("🤖 AI is analyzing..."):
            result = query_qwen_api(user_query, API_CONFIG["api_key"])
            st.session_state.result = result
    
    if st.session_state.result:
        st.markdown("---")
        st.markdown("### 💬 Response:")
        st.markdown(f'<div class="result-box">{st.session_state.result}</div>', unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.button("📋 Copy", disabled=True, help="Manual copy: Select text + Ctrl+C")
        with c2:
            st.button("🔍 Related", disabled=True, help="Feature coming soon")
        with c3:
            st.button("💾 Save", disabled=True, help="Feature coming soon")
    
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
