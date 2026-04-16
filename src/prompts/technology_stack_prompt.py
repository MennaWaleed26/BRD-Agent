from langchain_core.prompts import PromptTemplate  # type: ignore

TECHNOLOGY_STACK_TEMPLATE = """
You are a senior Business Analyst and Solution Architect.

Generate the "Technologies Used" section of a Business Requirements Document (BRD) in professional English.

The input already comes from a preparation/enhancement node, so you must treat it as the approved working context for this section.

OBJECTIVE
Describe the selected technologies used across the proposed solution in a business-friendly way.

This section is NOT the same as the "Proposed System" section.
Here, each subsection should focus on the technology choices for a platform or solution area, and briefly explain why these technologies are suitable and what advantages they provide.

SOURCE OF TRUTH
Use the enhanced context exactly as provided.
Field names in the context may include:
- project_name
- project_idea
- project_details
- client_name
- client_category
- platforms
- tech_stacks
- is_agile
- deadline_count
- deadline_type

INSTRUCTIONS

1) Language and tone
- Write in English only.
- Use a professional, polished, business-friendly tone.
- Keep the content suitable for a client-facing BRD.
- Avoid unnecessary low-level technical jargon.

2) Section purpose
- This section must explain the chosen technologies and their practical value.
- Do NOT describe the full business workflow of the platform.
- Do NOT repeat the same type of content from the Proposed System section.
- Focus on technology suitability, stability, scalability, usability, maintainability, integration capability, performance, security, or similar practical strengths.

3) Subsection structure
- Generate subsections aligned to the main solution areas or provided platforms.
- If platforms are provided and not empty:
  - align the subsections to those platforms only
  - do NOT add extra subsections beyond the provided platforms
  - do NOT merge two provided platforms into one subsection
  - the number of generated subsections must exactly equal the number of provided platforms
- If platforms are missing or empty:
  - infer a realistic set of 2 to 5 subsections based on the project context

4) Title rule
- Each subsection title should be business-friendly and similar in style to the corresponding platform title from the Proposed System section.
- However, the content must focus on the selected technologies, not on describing the platform itself.
- Titles may include the client name if that improves quality.

Examples:
- Mobile Application
- Admin Dashboard
- Delivery Operations App
- Backend Integration Layer

5) Technologies rule
- Use only technologies from tech_stacks.
- technologies_used must contain ONLY actual technologies.
- Do NOT include platform keys such as web_admin, customer_mobile, or delivery_app.
- Each subsection must contain only the technologies that are clearly necessary and strongly relevant for that area.
- Do NOT try to fill the list to 4 items by default.
- Use the smallest sufficient number of technologies.
- 1 technology is allowed if it is enough.
- 2 technologies are preferred when they clearly represent the main implementation choice.
- 3 to 4 technologies should be used only when there is a strong and realistic reason.
- The number of technologies may vary between subsections.
- Avoid making all subsections have the same number of technologies unless the context stron

6) Content rule
For each subsection:
- write one concise professional paragraph
- explain what the selected technologies are suitable for
- mention short practical benefits such as:
  - cross-platform delivery
  - responsive web experience
  - maintainability
  - scalability
  - secure access
  - fast integration
  - stable performance
  - efficient notifications
- keep the paragraph concise and specific
- avoid repeating identical benefits across all subsections

7) Quality rules
- Keep the section clear, elegant, and client-friendly.
- Avoid overly technical implementation detail.
- Avoid inventing unsupported technologies.
- Avoid repeating the exact same wording in every subsection.
- Keep the technology choices coherent and realistic.
- Vary the subsection technology lists naturally according to the needs of each area.
- Do not create artificial uniformity across all subsections.

Enhanced Context:
{enhanced_context}

Return output strictly according to the required structured schema.
"""

technology_stack_prompt_template = PromptTemplate(
    template=TECHNOLOGY_STACK_TEMPLATE,
    input_variables=["enhanced_context"]
)