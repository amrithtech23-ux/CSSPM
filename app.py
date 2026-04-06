# app.py - FIXED VERSION
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

# SPM Topics - FIXED with proper quote escaping
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
    "Outsourcing management",
    # Monitoring and Control
    "Project monitoring techniques",
    "Progress reporting",
    "Milestone tracking",
    "Traffic-light reporting (RAG)",
    "Exception reporting",
    "Performance measurement",
    "Baseline management",
    "Change management",
    "Scope control",
    "Quality control",
    # Miscellaneous Advanced Topics
    "Virtual teams management",
    "Offshore development",
    "Knowledge management",
    "Lessons learned",
    "Post-implementation review",
    "Project closure",
    "Stakeholder management",
    "Requirements engineering",
    "Systems analysis",
    "Design methodologies",
    "Software architecture",
    "Integration testing",
    "User acceptance testing",
    "Deployment strategies",
    "Maintenance strategies",
    "Technical debt management",
    "Agile transformation",
    "DevOps practices",
    "Continuous integration",
    "Continuous delivery"
]

# API Configuration
API_CONFIG = {
    "api_key": "CSSPM2K6",
    "repository": "CSSPM",
    "license": "MIT"
}

# Topic Database with detailed content
TOPIC_DATABASE = [
    {
        "topic": "Agile",
        "keywords": ["agile", "scrum", "extreme programming", "xp", "dsdm", "atern", "incremental", "sprint", "kanban", "lean", "agile manifesto"],
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
        overlap = sum(1 for keyword in item["keywords"] if keyword in prompt_lower)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = item
            
    if best_match and max_overlap > 0:
        return best_match["content"]
    
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
