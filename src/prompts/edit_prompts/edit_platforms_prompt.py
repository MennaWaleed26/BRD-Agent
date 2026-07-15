from langchain_core.prompts import PromptTemplate  # type: ignore


# =======================================================================
# 1. EDIT CLASSIFIER PROMPT
# =======================================================================

EDIT_CLASSIFIER_TEMPLATE = """
You are a senior Business Analyst.

Your task is to classify a user's requested edit for the "Proposed System" section of a BRD.

INPUTS:
- Enhanced Context: the current approved project understanding
- Original Content: the current Proposed System section in Arabic
- Edit Content: the user's requested change

CLASSIFICATION MODES:

MODE A = Content Revision
Use Mode A when the edit only affects:
- wording, tone, or phrasing
- titles or labels
- ordering of existing items
- shortening or expanding descriptions
- presentation style
- section-local clarification that does NOT change project facts, platforms, roles, or scope

MODE B = Structural Update
Use Mode B when the edit affects:
- platforms
- user roles
- platform_role_map
- project scope
- target users
- delivery channels
- core business facts
- any change that should logically affect other BRD sections, such as functional requirements or timeline

IMPORTANT CLASSIFICATION RULE:
If the edit adds, removes, or changes a platform, role, or platform-role relationship, classify it as MODE B even if the user only mentions the Proposed System section.
MIXED EDIT RULE:
If the edit contains both content refinement and structural changes, classify as Mode B.
Structural changes take priority over wording-only changes.

AFFECTED ENTITIES RULE:
For Mode A, affected_entities usually includes:
- proposed_system
- tone
- wording
- title
depending on the edit.

For Mode B, affected_entities should include all relevant items, such as:
- proposed_system
- enhanced_context
- platforms
- platform_role_map
- project_details
- functional_requirements
- timeline
- technology_stack, if technology/platform impact is likely

DECISION TEST:
Ask yourself:
1. Does the edit change the truth of the project?
2. Would this edit affect functional requirements or timeline?
3. Does this edit add/remove a platform or role?

If yes to any of these, choose MODE B.

Enhanced Context:
{enhanced_context}

Original Content:
{original_content}

User Edit:
{edit_content}

Return the classification according to the required schema.
"""

edit_classifier_template = PromptTemplate(
    template=EDIT_CLASSIFIER_TEMPLATE,
    input_variables=["enhanced_context", "original_content", "edit_content"]
)


# =======================================================================
# 2. MODE A REVISION PROMPT
# =======================================================================

MODE_A_REVISION_TEMPLATE = """
You are a senior Business Analyst.

Revise the "Proposed System" section based on the user's requested edit.

INPUTS:
Enhanced Context:
{enhanced_context}

Original Proposed System in Arabic:
{original_content}

User Edit:
{edit_content}

PRIORITY ORDER:
1. Apply the User Edit exactly.
2. Preserve unchanged parts from the original content as much as possible.
3. Maintain consistency with the Enhanced Context.
4. Preserve the required output schema.

MODE A PURPOSE:
This is a section-level revision only.
It is NOT a structural regeneration task.

RULES:
1. Maintain Arabic language only.
2. Do not regenerate from scratch unless the edit clearly requires broad rewriting.
3. Preserve existing components unless the user explicitly asks to rename, reorder, shorten, or rephrase them.
4. Do not add new platforms.
5. Do not add new roles.
6. Do not create new platform-role mappings.
7. Do not add new business capabilities.
8. Do not change project facts.
9. Do not change the number of components unless the user explicitly requests it and the request does not conflict with the Enhanced Context.
10. Keep the wording professional, clear, and suitable for a client-facing BRD.

STRUCTURAL SAFETY:
If the requested edit requires adding/removing platforms, roles, or platform-role mappings, do not invent a workaround.
Stay consistent with the current Enhanced Context and revise only what can be revised safely within Mode A.

OUTPUT:
Return the revised Proposed System strictly according to the ProposedSystemArabicOutput schema.
"""

mode_a_revision_template = PromptTemplate(
    template=MODE_A_REVISION_TEMPLATE,
    input_variables=["enhanced_context", "original_content", "edit_content"]
)


# =======================================================================
# 3. MODE B CONTEXT UPDATE PROMPT
# =======================================================================

MODE_B_CONTEXT_UPDATE_TEMPLATE = """
You are a senior Solution Architect.

A user has requested a structural change to the project.
Your task is to update the Enhanced Context so it reflects the user's new facts.

INPUTS:
Enhanced Context:
{enhanced_context}

Original Proposed System in Arabic:
{original_content}

User Edit:
{edit_content}

PRIORITY ORDER:
1. User Edit is the new source of truth.
2. Preserve unaffected parts of the Enhanced Context.
3. Remove outdated facts that conflict with the User Edit.
4. Keep the context internally consistent.

FIELDS TO UPDATE WHEN AFFECTED:
- project_details
- project_idea, if the edit changes the project concept
- platforms
- platform_role_map
- tech_stacks, only if the edit clearly affects technology
- timeline_details, only if the edit clearly affects timeline assumptions
- other context fields only when necessary

PLATFORM RULES:
- platforms must be a unique flat list of normalized platform keys.
- Do not duplicate platform keys.
- If the same platform is used by multiple roles, represent that in platform_role_map, not by duplicating platforms.
- Remove platform keys that are no longer valid after the edit.
- Add platform keys that are explicitly required by the edit.

PLATFORM_ROLE_MAP RULES:
- platform_role_map is critical.
- Each item represents one role using one platform.
- Add all required role-platform pairs created by the user edit.
- Remove pairs that conflict with the user edit.
- Do not keep mappings for removed platforms.
- Do not invent unsupported roles.
- Normalize role names clearly, such as:
  - customer
  - student
  - trainer
  - admin
  - vendor
  - staff
  - system

SCOPE CONTROL:
- Do not expand the project beyond the user's requested change.
- Do not add extra platforms just because they are common.
- Do not add extra roles just because they are typical.
- Do not add new features unless needed to express the user's structural change in project_details.

CONSISTENCY CHECK BEFORE OUTPUT:
Before returning, ensure:
1. platforms contains no duplicates.
2. every platform in platform_role_map exists in platforms.
3. no removed platform remains in platform_role_map.
4. project_details reflects the new structure.
5. unchanged business facts remain stable.

OUTPUT:
Return the updated context strictly according to the PreparationOutput schema.
"""

mode_b_context_update_template = PromptTemplate(
    template=MODE_B_CONTEXT_UPDATE_TEMPLATE,
    input_variables=["enhanced_context", "original_content", "edit_content"]
)