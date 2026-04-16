from langchain_core.prompts import PromptTemplate  # type: ignore

FUNCTIONAL_REQUIREMENTS_PLANNER_TEMPLATE = """
You are a senior Business Analyst and Solution Architect.

Generate the planning structure for the "Detailed Functional Units" section of a Business Requirements Document (BRD).

The input already comes from a preparation/enhancement node, so you must treat it as the approved working context.

OBJECTIVE
Organize the functional requirements into exactly these 3 fixed groups:

1. Operations and Project Lifecycle
2. Internal Business and Management
3. Client Digital Experience

IMPORTANT RULES
- You must always produce all 3 groups.
- Do not remove any of the 3 groups.
- If one group is less relevant for the project, keep it lighter, but still present.
- This node is only for planning and decomposition.
- Do NOT generate full technical implementation.
- Do NOT generate long prose.
- Do NOT generate the final section text.

STRUCTURE RULES
- Each group must contain one or more modules.
- Each module must contain multiple features whenever realistically possible.
- A module is a major functional area.
- A feature is a specific capability inside a module.
- Prefer 2 to 5 features per module where appropriate.
- Use concise business-friendly titles.

GROUP DEFINITIONS
1) Operations and Project Lifecycle
Include operational capabilities such as:
- request intake
- project lifecycle tracking
- scheduling
- site visits
- media uploads
- notifications
- execution follow-up

2) Internal Business and Management
Include internal business capabilities such as:
- CRM
- roles and permissions
- task management
- quotations
- invoices
- dashboards
- reporting
- internal administration

3) Client Digital Experience
Include client-facing digital capabilities such as:
- client login and authentication
- project tracking
- approvals
- galleries
- appointments
- payments visibility
- in-app communication
- client self-service
- AI-enhanced client experience if supported by context

PLANNING GUIDELINES
- Use the enhanced context as the source of truth.
- Respect the project scope, platforms, and project details.
- Keep the module distribution balanced and coherent.
- Do not create too many tiny modules.
- Do not invent unsupported major capabilities.

FOR EACH FEATURE
Generate:
- title
- purpose

ENHANCED CONTEXT:
{enhanced_context}

Return output strictly according to the required structured schema.
"""

functional_requirements_planner_prompt_template = PromptTemplate(
    template=FUNCTIONAL_REQUIREMENTS_PLANNER_TEMPLATE,
    input_variables=["enhanced_context"]
)