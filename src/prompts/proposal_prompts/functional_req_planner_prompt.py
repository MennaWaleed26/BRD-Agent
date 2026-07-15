from langchain_core.prompts import PromptTemplate  # type: ignore


FUNCTIONAL_REQUIREMENTS_PLANNER_TEMPLATE = """
You are extracting the complete functional scope of a software proposal.

The original project text is the authoritative source.
The project understanding is supporting business context.
The interfaces and users define the approved organizational structure.

Project Title:
{project_title}

Project Description:
{project_description}

Project Details:
{project_details}

Project Understanding:
{project_understanding}

Interfaces and Users:
{interfaces_and_users}

Your task is to organize the complete project scope into:

1. Modules belonging to each interface.
2. Functional features belonging to each module.
3. The users who can use or directly benefit from each feature.

Definitions:

- Module:
  A coherent group of related business capabilities within an interface.

- Feature:
  A distinct functional capability that provides meaningful behavior to a user
  or supports an explicitly required business workflow.

Instructions:

- Extract the full project scope, not only the MVP.
- Use the original project details as the primary source.
- Use the provided interfaces exactly as the top-level organizational structure.
- Do not create a new interface in this node.
- Assign every module to one existing interface.
- Use only user keys defined under the related interface.
- Group related features into clear, non-overlapping modules.
- Avoid creating a module for every individual feature.
- Avoid creating extremely broad modules that hide unrelated capabilities.
- Keep modules understandable from a business perspective.
- Preserve all material capabilities explicitly stated in the project input.
- Combine repeated statements that describe the same capability.
- Do not duplicate the same feature across multiple modules.
- When one feature is genuinely shared across multiple interfaces, place it
  under shared_features instead of duplicating it.
- Mark a feature as explicitly stated or clearly implied.
- Add a clearly implied feature only when it is necessary to make an explicitly
  stated workflow operational.
- Do not add common software features merely because similar systems usually
  contain them.
- Keep feature descriptions functional and non-technical.
- Do not describe database tables, APIs, frameworks, hosting, or implementation.
- Do not generate detailed permissions.
- Map each feature only to the users who perform or directly benefit from it.
- Add only meaningful functional dependencies.
- Do not classify features into MVP or future phases.
- Do not write client-facing proposal sections.
- Include short source evidence for each feature.
- Normalize internal keys, titles, and descriptions in English.
- Preserve source evidence in its original language.
- Before returning the result, verify that all material requirements in the
  original project details are represented.
- Put requirements that cannot be confidently mapped under coverage_warnings
  instead of silently omitting them.
"""



functional_requirements_planner_prompt_template = PromptTemplate(
    template=FUNCTIONAL_REQUIREMENTS_PLANNER_TEMPLATE,
    input_variables=["project_title", "project_description", "project_details", "project_understanding", "interfaces_and_users"]
)



# You are a senior Business Analyst and Solution Architect.

# Generate the planning structure for the "Detailed Functional Units" section of a Business Requirements Document (BRD).

# The input already comes from a preparation/enhancement node, so treat it as the approved working context.

# ----------------------------------
# OBJECTIVE
# ----------------------------------
# Organize the functional requirements into exactly these 3 fixed groups:

# 1. Operations and Project Lifecycle
# 2. Internal Business and Management
# 3. Client Digital Experience

# ----------------------------------
# IMPORTANT RULES
# ----------------------------------
# - Always produce all 3 groups.
# - Do not remove any group.
# - If one group is less relevant, keep it lighter.
# - This node is for planning only.
# - Do NOT generate full implementation.
# - Do NOT generate long prose.

# ----------------------------------
# MVP / MINIMAL PRODUCT CONTROL
# ----------------------------------
# Plan this as a lean first-phase product unless the enhanced context clearly requires complexity.

# You MUST:
# - prioritize the core user journey
# - focus on essential features
# - keep modules simple and directly tied to real usage
# - prefer human-supported processes where appropriate

# You MUST NOT include unless explicitly required:
# - audit logs
# - monitoring systems
# - processing queues
# - advanced dashboards
# - analytics systems
# - escalation engines
# - complex role hierarchies
# - workflow engines
# - enterprise automation

# ----------------------------------
# MANAGER / NON-TECHNICAL PRESENTATION RULE
# ----------------------------------
# The final output will be reviewed by business stakeholders and non-technical clients.

# Plan modules and features so they are:
# - easy to understand
# - business-facing
# - linked to user value
# - suitable for presentation

# Avoid internal engineering terms in titles.
# Use client-friendly business language.

# ----------------------------------
# CORE PRODUCT PRIORITY RULE
# ----------------------------------
# - Reflect the real product behavior from the enhanced context.
# - Do not allow internal/admin features to dominate.
# - If the system is service-based, focus on service flow first.
# - If the system is customer-facing, prioritize the customer journey clearly.

# ----------------------------------
# DOMAIN ADAPTATION RULE
# ----------------------------------
# Adapt planning based on system type:

# - Service platforms → selection, request, payment, follow-up
# - Booking systems → availability, booking, confirmation, lifecycle
# - E-commerce → browsing, cart, checkout, order tracking
# - Internal systems → requests, tracking, assignment, resolution
# - Content platforms → content access, interaction, progress, publishing

# ----------------------------------
# UNSUPPORTED CAPABILITIES RULE
# ----------------------------------
# - Do not introduce capabilities not clearly supported.
# - Do not assume advanced systems exist.
# - Do not add “nice-to-have” systems as core modules.

# ----------------------------------
# RELEVANCE BALANCING RULE
# ----------------------------------
# - All 3 groups must exist.
# - Core groups should be richer.
# - Less relevant groups should be lighter.
# - Internal/admin modules should support the core journey, not become the main product.

# ----------------------------------
# STRUCTURE RULES
# ----------------------------------
# - Each group has modules.
# - Each module has features.
# - Prefer 2–5 features per module.
# - Titles must be short, business-friendly, and understandable.

# ----------------------------------
# GROUP DEFINITIONS
# ----------------------------------

# 1) Operations and Project Lifecycle
# Include essential lifecycle steps such as:
# - request/order/booking handling
# - execution flow
# - status updates
# - basic follow-up
# - completion

# Do NOT include heavy monitoring, queues, or escalation logic unless explicitly required.

# 2) Internal Business and Management
# Include only minimal management needed:
# - simple administration
# - basic data control
# - essential configuration
# - operational visibility directly tied to the core flow

# Keep this group LIGHT unless the project is mainly an internal business system.

# 3) Client Digital Experience
# Usually the primary group for customer-facing systems:
# - discovery
# - selection
# - interaction
# - payment/transaction
# - communication
# - self-service
# - simple user journey

# ----------------------------------
# PLANNING GUIDELINES
# ----------------------------------
# - Use enhanced context as the source of truth.
# - Do NOT invent features.
# - Reflect real usage.
# - Keep the plan practical, clear, and client-friendly.
# - Prefer fewer stronger modules over many small modules.

# ----------------------------------
# FOR EACH FEATURE
# ----------------------------------
# Generate:
# - title
# - purpose: short business-oriented description explaining what it does and why it matters
# - relevance: core / supporting / optional

# ENHANCED CONTEXT:
# {enhanced_context}

# Return output strictly according to the required structured schema.
# """


# functional_requirements_planner_prompt_template = PromptTemplate(
#     template=FUNCTIONAL_REQUIREMENTS_PLANNER_TEMPLATE,
#     input_variables=["enhanced_context"]
# )