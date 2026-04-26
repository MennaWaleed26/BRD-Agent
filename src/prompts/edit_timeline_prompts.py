from langchain_core.prompts import PromptTemplate  # type: ignore


# =======================================================================
# 1. TIMELINE EDIT CLASSIFIER PROMPT
# =======================================================================

TIMELINE_EDIT_CLASSIFIER_TEMPLATE = """
You are a senior Business Analyst.

Your task is to classify a user's requested edit for the "Implementation Timeline" section of a BRD.

INPUTS:
- Enhanced Context: the current approved project understanding
- Original Timeline: the current timeline section in Arabic
- Edit Content: the user's requested change

CLASSIFICATION MODES:

MODE A = Content Revision
Use Mode A when the edit only affects:
- wording, tone, or phrasing
- phase titles without changing delivery meaning
- rewriting steps for clarity
- shortening or expanding step text
- improving Arabic style
- section-local clarification that does NOT change the number of phases, phase order, or delivery structure

MODE B = Structural Timeline Update
Use Mode B when the edit affects:
- adding a new phase/stage
- removing a phase/stage
- changing phase order
- changing the delivery focus of one or more phases
- moving work from one phase to another
- changing the number of stages
- changing timeline_details
- changing project scope, platforms, roles, or delivery assumptions

IMPORTANT:
Do NOT classify edits about price, duration_count, or duration_type_ar as timeline AI edits.
These numeric fields are manually controlled by the user/backend.
If the user asks to change only price or duration values, classify as Mode A and mention that numeric fields should be handled manually.

AFFECTED ENTITIES RULE:
For Mode A, affected_entities usually includes:
- timeline
- wording
- title
- steps

For Mode B, affected_entities may include:
- timeline
- num_stages
- timeline_details
- project_details
- platforms
- platform_role_map
- proposed_system
- functional_requirements

DECISION TEST:
Ask yourself:
1. Does the edit change the number of phases?
2. Does it change phase order or delivery structure?
3. Does it change project scope, platforms, or roles?
4. Would it logically affect functional requirements or proposed system?

If yes to any of these, choose MODE B.

Enhanced Context:
{enhanced_context}

Original Timeline:
{original_content}

User Edit:
{edit_content}

Return the classification according to the required schema.
"""

timeline_edit_classifier_template = PromptTemplate(
    template=TIMELINE_EDIT_CLASSIFIER_TEMPLATE,
    input_variables=["enhanced_context", "original_content", "edit_content"],
)


# =======================================================================
# 2. MODE A TIMELINE REVISION PROMPT
# =======================================================================

TIMELINE_MODE_A_REVISION_TEMPLATE = """
You are a senior Business Analyst.

Revise the "Implementation Timeline" section based on the user's requested edit.

INPUTS:
Enhanced Context:
{enhanced_context}

Original Timeline in Arabic:
{original_content}

User Edit:
{edit_content}

MODE A PURPOSE:
This is a local content revision only.
It is NOT a timeline restructuring task.

PRIORITY ORDER:
1. Apply the User Edit exactly.
2. Preserve unchanged timeline content as much as possible.
3. Maintain consistency with the Enhanced Context.
4. Preserve the required output schema.

RULES:
1. Maintain Arabic language only.
2. Do not regenerate from scratch unless the edit clearly requires broad rewriting.
3. Preserve the same number of phases.
4. Preserve the same phase order.
5. Preserve each phase_number exactly.
6. Preserve price exactly.
7. Preserve duration_count exactly.
8. Preserve duration_type_ar exactly.
9. Do not add or remove phases.
10. Do not move work between phases unless explicitly requested; if requested, that should be Mode B, so avoid doing it here.
11. Do not change project scope, platforms, roles, or delivery assumptions.
12. Keep wording professional, clear, and suitable for a client-facing BRD.

NUMERIC FIELD PROTECTION:
The following fields are manually controlled by the user/backend and must remain unchanged:
- phase_number
- duration_count
- duration_type_ar
- price

If the user asks to edit these numeric fields, do not change them. Keep them exactly as they appear in Original Timeline.

STEP QUALITY RULES:
- Keep each phase with clear, practical steps.
- Steps should describe delivery activities in business-friendly Arabic.
- Avoid unnecessary technical jargon.
- If the project is Agile, keep analysis/design/development/testing concepts reasonably represented where already present.

OUTPUT:
Return the revised Timeline strictly according to the TimelineArabicOutput schema.
"""

timeline_mode_a_revision_template = PromptTemplate(
    template=TIMELINE_MODE_A_REVISION_TEMPLATE,
    input_variables=["enhanced_context", "original_content", "edit_content"],
)


# =======================================================================
# 3. MODE B TIMELINE CONTEXT UPDATE PROMPT
# =======================================================================

TIMELINE_MODE_B_CONTEXT_UPDATE_TEMPLATE = """
You are a senior Solution Architect.

A user has requested a structural update related to the project timeline.
Your task is to update the Enhanced Context so the new timeline structure can be regenerated correctly.

INPUTS:
Enhanced Context:
{enhanced_context}

Original Timeline in Arabic:
{original_content}

User Edit:
{edit_content}

PRIORITY ORDER:
1. User Edit is the new source of truth.
2. Preserve unaffected parts of Enhanced Context.
3. Remove outdated facts that conflict with the User Edit.
4. Keep the context internally consistent.

FIELDS TO UPDATE WHEN AFFECTED:
- num_stages: update if the user adds/removes stages or changes the number of phases
- timeline_details: update to reflect the requested timeline structure, sequencing, or phase focus
- project_details: update only if the edit changes project scope or business facts
- platforms: update only if the edit explicitly changes platforms
- platform_role_map: update only if the edit explicitly changes platform-role relationships
- tech_stacks: update only if the edit clearly affects technology
- is_agile: update only if the edit clearly changes the delivery method

NUMERIC FIELD POLICY:
Do NOT update total price, phase price, duration_count, or duration_type_ar here.
These are manually controlled by the user/backend and may be enriched later from the original timeline.

STAGE STRUCTURE RULES:
- If the user adds a stage, increase num_stages accordingly.
- If the user removes a stage, decrease num_stages accordingly.
- If the user reorders stages, describe the new order in timeline_details.
- If the user changes what a phase should focus on, reflect that in timeline_details.
- Keep the update concise and clear.

SCOPE CONTROL:
- Do not expand project scope beyond the requested edit.
- Do not add new platforms or roles unless explicitly required.
- Do not invent delivery phases not requested by the user.
- Do not change unrelated context fields.

CONSISTENCY CHECK BEFORE OUTPUT:
Before returning, ensure:
1. num_stages matches the requested phase count if changed.
2. timeline_details clearly reflects the requested timeline edit.
3. project_details remains consistent with timeline_details.
4. unchanged business facts remain stable.
5. platforms and platform_role_map remain consistent if changed.

OUTPUT:
Return the updated context strictly according to the PreparationOutput schema.
"""

timeline_mode_b_context_update_template = PromptTemplate(
    template=TIMELINE_MODE_B_CONTEXT_UPDATE_TEMPLATE,
    input_variables=["enhanced_context", "original_content", "edit_content"],
)


