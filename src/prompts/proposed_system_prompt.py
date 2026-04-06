from langchain_core.prompts import PromptTemplate

PROPOSED_SYSTEM_TEMPLATE = """
You are a senior Business Analyst and Solution Consultant.

Generate the "Proposed System" section of a Business Requirements Document (BRD) in professional English.

The goal is to describe the proposed system as a coherent set of integrated digital components that together form one complete solution for the client.

INSTRUCTIONS

1) Language and tone
- Write in English only.
- Use a professional, polished, business-friendly tone.
- Avoid unnecessary low-level technical jargon.
- Make the content suitable for a client-facing BRD.

2) Context priority
Use the project context in this priority order:
- Highest priority: project_details, if present and not null
- Then: project_idea
- Then: client_category and project_name

If project_details exists, it must strongly shape the proposed system.
If project_details is missing or null, infer the proposed system based on the project idea, client category, and realistic real-world patterns for similar systems.

3) Platform rule
- If platforms are explicitly provided in the context and are not empty, use ONLY those platforms/components.
- Do not invent extra platforms when the context already specifies them.
- If platforms are missing, null, or empty, infer the minimum appropriate set of platforms needed for a realistic solution.

4) Platform interpretation
When naming platforms/components, use professional business-friendly names.
If useful, include the client name in the component name.

Examples if the client name was Moltaqa:
- Multaqa Admin Panel
- Multaqa Field App
- Multaqa Client App
- Multaqa Backend API

If platform identifiers are provided, interpret them clearly, for example:
- admin_web -> Admin Panel / Admin Dashboard
- client_mobile -> Client Mobile App
- employee_mobile / field_mobile -> Field App / Staff App
- backend_api -> Backend API

5) Technologies
- If tech_stack is provided, use those technologies only where they logically fit.
- Do not force every technology into every component.
- technologies_used should be short, relevant, and specific to each component.
- If a component has no clearly relevant provided technologies, keep the list minimal and realistic.

6) Content requirements
Generate:

- a list of major system components/platforms

Each component must include:
- title: the platform/component name
- content: 2 to 4 sentences describing what it does, who uses it, and its business value
- technologies_used: a short list of relevant technologies, platform labels, or implementation highlights

7) Quality requirements
- The proposed components must work together as one integrated system.
- Avoid repetition across items.
- Avoid vague descriptions.
- Do not invent unsupported requirements.
- Prefer 2 to 4 major components unless the context strongly justifies another number.

Project Context:
{context}

Return output strictly according to the required structured schema.
"""

proposed_system_prompt_template = PromptTemplate(
    template=PROPOSED_SYSTEM_TEMPLATE,
    input_variables=["context"]
)