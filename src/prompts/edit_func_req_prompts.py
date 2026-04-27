from langchain_core.prompts import PromptTemplate  # type: ignore


FUNCTIONAL_EDIT_CLASSIFIER_TEMPLATE = """
You are a senior Business Analyst.

Classify the user's requested edit for the "Functional Requirements" section.

MODE A = Content Revision
Use Mode A when the edit only affects:
- wording
- tone
- phrasing
- shortening or expanding descriptions
- improving clarity
- rewriting titles without changing meaning
- refining technical implementation wording
- adding polish without adding/removing features or modules

MODE B = Functional Structure Update
Use Mode B when the edit affects:
- adding a feature
- removing a feature
- adding a module
- removing a module
- moving a feature between modules/groups
- changing the meaning of an existing feature
- adding a new functional capability
- changing scope, roles, platforms, or user journeys

IMPORTANT:
If the edit changes platforms, roles, platform_role_map, or project scope, still classify as Mode B.
In this case, affected_entities should include proposed_system and timeline as possibly impacted.

Enhanced Context:
{enhanced_context}

Original Functional Requirements:
{original_content}

User Edit:
{edit_content}

Return the classification according to the required schema.
"""

functional_edit_classifier_template = PromptTemplate(
    template=FUNCTIONAL_EDIT_CLASSIFIER_TEMPLATE,
    input_variables=["enhanced_context", "original_content", "edit_content"],
)


FUNCTIONAL_MODE_A_REVISION_TEMPLATE = """
You are a senior Business Analyst.

Revise the Functional Requirements section based on the user's edit.

MODE A PURPOSE:
This is a text-only/content refinement task.

INPUTS:
Enhanced Context:
{enhanced_context}

Original Functional Requirements:
{original_content}

User Edit:
{edit_content}

RULES:
1. Maintain Arabic language.
2. Apply the user edit exactly.
3. Preserve all existing groups, modules, and features.
4. Do NOT add new groups.
5. Do NOT add new modules.
6. Do NOT add new features.
7. Do NOT remove any existing feature.
8. Do NOT change the functional meaning.
9. Improve only wording, clarity, tone, titles, descriptions, implementation steps, or additional ideas as requested.
10. Preserve the output schema exactly.

Return the revised Functional Requirements strictly according to the FunctionalRequirementsArabicOutput schema.
"""

functional_mode_a_revision_template = PromptTemplate(
    template=FUNCTIONAL_MODE_A_REVISION_TEMPLATE,
    input_variables=["enhanced_context", "original_content", "edit_content"],
)


FUNCTIONAL_MODE_B_REVISION_TEMPLATE = """
You are a senior Business Analyst and Solution Architect.

Revise the Functional Requirements section based on a structural functional edit.

MODE B PURPOSE:
The user wants to change the functional structure, such as adding/removing/changing features or modules.

INPUTS:
Enhanced Context:
{enhanced_context}

Original Functional Requirements:
{original_content}

User Edit:
{edit_content}

PRIORITY ORDER:
1. Apply the user edit as the highest priority.
2. Preserve existing functional requirements as much as possible.
3. Keep consistency with the enhanced context.
4. Keep the output suitable for a client-facing BRD.
5. Preserve the required output schema.

RULES:
1. Maintain Arabic language.
2. Do NOT rewrite the entire section unnecessarily.
3. If adding a feature:
   - place it in the most relevant existing module if possible.
   - create a new module only if no existing module fits.
4. If removing a feature:
   - remove only the requested feature.
   - keep surrounding modules/features unchanged.
5. If moving a feature:
   - move it to the most appropriate group/module.
   - do not duplicate it.
6. If adding a module:
   - add only the requested module and relevant features.
   - do not invent unrelated features.
7. Do NOT add platforms, roles, or scope not supported by the enhanced context unless the user explicitly requested them.
8. If the user requests a platform/scope change, update the functional requirements as much as possible, but do not attempt to regenerate proposed system or timeline here.
9. Keep feature descriptions clear for non-technical clients.
10. Keep implementation steps practical, business-friendly, and not code-level.
11. Preserve group structure unless the edit explicitly requires moving content.
12. Do not over-engineer.

OUTPUT:
Return the revised Functional Requirements strictly according to the FunctionalRequirementsArabicOutput schema.
"""

functional_mode_b_revision_template = PromptTemplate(
    template=FUNCTIONAL_MODE_B_REVISION_TEMPLATE,
    input_variables=["enhanced_context", "original_content", "edit_content"],
)