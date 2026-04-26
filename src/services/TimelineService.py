# from enum import Enum
# from pydantic import BaseModel,Field
# from typing import List
# from src.llm.invoke import invoke_structured_async
# from src.prompts.edit_timeline import
# from src.prompts.proposed_system_prompt import proposed_system_ar_template
# from src.schemas.preparation import PreparationOutput
# from src.schemas.sections_output import ProposedSystemArabicOutput



# class EditMode(str,Enum):
#     A="A"
#     B="B"

# class TimelineEditClassification(BaseModel):

#     mode: EditMode
#     reason :str
#     affected_entities: List[str]= Field(default_factory=list)

# class TimelineService:

#     def __init__(self):
#         pass

#     async def get_total_price(self,enhanced_context,original_content):
#         current_stages=enhanced_context.get("num_stages",0)
#         stage_price=original_content.get("content",[])[0].get("price")
#         total_price=current_stages*stage_price
#         return current_stages, total_price
#     async def modify_timeline(self,enhanced_context,original_content,edit_content):
#         classification= await invoke_structured_async(
#             prompt_template= edit_classifier_template,
#             prompt_variables={"enhanced_context": enhanced_context,
#                               "original_content":original_content,
#                               "edit_content": edit_content
#                               },
#                               output_model=TimelineEditClassification,
#                               run_name="edit_classifier"
#         )

#         if classification.mode == EditMode.A:
#             # Mode A: Revision (Local)
#             revised_section = await invoke_structured_async(
#                 prompt_template=mode_a_revision_template,
#                 prompt_variables={
#                     "enhanced_context": enhanced_context.model_dump(),
#                     "original_content": original_content.model_dump(),
#                     "edit_content": edit_content
#                 },
#                 output_model=ProposedSystemArabicOutput,
#                 run_name="proposed_system_mode_a_revision"
#             )

#             return {
#                 "mode": "A",
#                 "classification_reason": classification.reason,
#                 "affected_entities": classification.affected_entities,
#                 "updated_context": None,
#                 "proposed_system": revised_section.model_dump()
#             }
#         else:
#             updated_enhanced_context = await invoke_structured_async(
#                 prompt_template=mode_b_context_update_template,
#                 prompt_variables={
#                     "enhanced_context": enhanced_context.model_dump(),
#                     "original_content": original_content.model_dump(),
#                     "edit_content": edit_content
#                 },
#                 output_model=PreparationOutput,
#                 run_name="proposed_system_mode_b_context_update"
#             )

#             regenerated_proposed_system = await invoke_structured_async(
#                 prompt_template=proposed_system_ar_template,
#                 prompt_variables={
#                     "enhanced_context": updated_enhanced_context.model_dump()
#                 },
#                 output_model=ProposedSystemArabicOutput,
#                 run_name="proposed_system_mode_b_regeneration"
#             )

#             return {
#                 "mode": "B",
#                 "classification_reason": classification.reason,
#                 "affected_entities": classification.affected_entities,
#                 "updated_context": updated_enhanced_context.model_dump(),
#                 "proposed_system": regenerated_proposed_system.model_dump(),
#             }

# timeline_service=TimelineService()