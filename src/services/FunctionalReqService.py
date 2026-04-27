from enum import Enum
from pydantic import BaseModel, Field
from typing import List
from src.schemas.preparation import PreparationOutput
from src.schemas.sections_output import FunctionalRequirementsArabicOutput
from src.llm.invoke import invoke_structured_async
from src.prompts.edit_func_req_prompts import (functional_edit_classifier_template,
                                               functional_mode_a_revision_template,
                                               functional_mode_b_revision_template)

class EditMode(str,Enum):
    A="A"
    B="B"
    
class FunctionalReqEditClassification(BaseModel):

    mode: EditMode
    reason :str
    affected_entities: List[str]= Field(default_factory=list)
    
class FunctionalReqService:
    
    def __init__(self) -> None:
        pass
    
    async def modify_functional_req(self,enhanced_context:PreparationOutput,
                                    original_content:FunctionalRequirementsArabicOutput,
                                    edit_content:str):
        classification = await invoke_structured_async(functional_edit_classifier_template,prompt_variables={
            "enhanced_context":enhanced_context,
            "original_content":original_content,
            "edit_content":edit_content
        },
        output_model=FunctionalReqEditClassification,
        run_name="functional_requirements_edit_classifier",
        )
        
        if classification.mode == EditMode.A:
            
            revised_section=await invoke_structured_async(functional_mode_a_revision_template,prompt_variables={
                "enhanced_context":enhanced_context.model_dump(),
                "original_content":original_content.model_dump(),
                "edit_content":edit_content
                },
                output_model=FunctionalRequirementsArabicOutput,
                run_name="functional_requirements_mode_a_revision",
                )
            
            return {
                "mode": "A",
                "classification_reason": classification.reason,
                "affected_entities": classification.affected_entities,
                "updated_context": None,
                "functional_requirement": revised_section.model_dump(),
            }
        elif classification.mode ==EditMode.B:
            
            revised_section= await invoke_structured_async(
            prompt_template=functional_mode_b_revision_template,
            prompt_variables={
                "enhanced_context": enhanced_context.model_dump(),
                "original_content": original_content.model_dump(),
                "edit_content": edit_content,
            },
            output_model=FunctionalRequirementsArabicOutput,
            run_name="functional_requirements_mode_b_revision",
        )
            
            return {
                "mode": "B",
                "classification_reason": classification.reason,
                "affected_entities": classification.affected_entities,
                "updated_context": None,
                "functional_requirement": revised_section.model_dump(),
            }
            
            
    
functional_req_service=FunctionalReqService()