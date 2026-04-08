from langchain_core.prompts import PromptTemplate  # type: ignore

FINAL_REPORT_COHERENCE_TEMPLATE = """
You are a senior business analyst.

You will receive four already-generated BRD sections in English:
- proposed system
- technology stack
- functional requirements
- implementation timeline

Your task is to produce one coherent final English BRD structure.

Rules:
- Preserve the existing structure of each section.
- Do not add new scope.
- Do not remove valid content unless it is obviously duplicated.
- Keep terminology consistent across sections.
- Make sure naming is aligned across the report.
- Ensure the timeline matches the functional and technical scope.
- Keep the response structured and professional.

Enhanced context:
{enhanced_context}

Proposed system:
{proposed_system}

Technology stack:
{technology_stack}

Functional requirements:
{functional_requirements}

Timeline:
{timeline}
"""

final_report_coherence_prompt_template = PromptTemplate(
    template=FINAL_REPORT_COHERENCE_TEMPLATE,
    input_variables=[
        "enhanced_context",
        "proposed_system",
        "technology_stack",
        "functional_requirements",
        "timeline",
    ],
)