
from typing import Any, Dict
from src.graph.state import GraphState
from src.graph.nodes.base_nodes import BaseNodes
from src.schemas.sections_output import (
                                         
    
    ProposedSystemArabicOutput,
    TimelineArabicOutput,
    FunctionalRequirementsGroupArabicOutput,
    FunctionalRequirementsArabicOutput,
    FinalBRDArabicOutput,
    
)
from src.prompts.proposed_system_prompt import proposed_system_ar_template
from src.prompts.timeline_prompt import timeline_arabic_prompt_template
from src.prompts.functional_req_group_prompt import functional_requirements_group_ar_template
from src.graph.validators.timeline_enricher import enrich_timeline_ar_stages


class SectionValidationError(Exception):
    pass

base_node=BaseNodes()

async def arabic_entry_node(state: GraphState):
    return {}



async def proposed_system_ar(state:GraphState):
    response= await base_node.proposed_system_node(state=state,
        prompt_template=proposed_system_ar_template,
        output_model=ProposedSystemArabicOutput,
        run_name="Proposed System Arabic Node")
    
    
    return {"proposed_system":response.model_dump()}

async def timeline_ar(state:GraphState):
    response= await base_node.timeline_node(
        state=state,
        prompt_template=timeline_arabic_prompt_template,
        output_model=TimelineArabicOutput,
        run_name="Timeline Arabic Node"
    )
    
    enriched_timeline= enrich_timeline_ar_stages(state["context"], raw_timeline_output=response.model_dump())

    
    return {"timeline":enriched_timeline}

# async def validate_timeline_ar(state:GraphState):
#     timeline=state.get("timeline")
#     context=state["context"]
#     try:
#         expected_stages=context["num_stages"]
#         actual_stages =len(timeline.get("content")) # type: ignore
#         if actual_stages != expected_stages:
#             raise SectionValidationError(
#                 f"Expected {expected_stages} but got {actual_stages}"
#             )
#         return {
#             "timeline_validated":timeline,
#             "timeline_error": None 
#         }
        
#     except Exception as e :
        
#         return {
#             "timeline_validated":None,
#             "timeline_error": str(e),
#             "timeline_retry_count": state.get("timeline_retry_count",0)+1
#         }
    
    
async def functional_requirements_operations_ar(state:GraphState):
    enhanced_context = state["enhanced_context"]
    group_plan = state["functional_requirements_plan"] ["operations_and_project_lifecycle"]
    
    functional_requirements_operations= await base_node.functional_requirements_operations_node(
        state=state,
        enhanced_context=enhanced_context,
        group_plan=group_plan,
        output_model=FunctionalRequirementsGroupArabicOutput,
        run_name="Func Req Operations Node",
        prompt_template=functional_requirements_group_ar_template
    )
    

    print("Success: functional_requirements_operations_node")
    
    return {"functional_requirements_operations":functional_requirements_operations.model_dump()}

async def  functional_requirements_internal_management_ar(state:GraphState):
    enhanced_context=state["enhanced_context"]
    group_plan=state["functional_requirements_plan"] ["internal_business_management"]
    
    functional_requirements_internal_management= await base_node.functional_requirements_internal_management_node(state,
        enhanced_context=enhanced_context,
        group_plan=group_plan,
        output_model=FunctionalRequirementsGroupArabicOutput,
        run_name="Func Req Internal Management Node",
        prompt_template=functional_requirements_group_ar_template) 
    

    print("Success: functional_requirements_internal_management_node")
    
    return {"functional_requirements_internal_management":functional_requirements_internal_management.model_dump()}


async def functional_requirements_client_experience_ar(state: GraphState) -> Dict[str, Any]:
    enhanced_context = state["enhanced_context"]
    group_plan = state["functional_requirements_plan"]["client_digital_experience"]

    functional_requirements_client_experience= await base_node.functional_requirements_client_experience_node(state,
            enhanced_context=enhanced_context,
            group_plan=group_plan,
            output_model=FunctionalRequirementsGroupArabicOutput,
            run_name="Func Req Client Experience Node",
            prompt_template=functional_requirements_group_ar_template)
 
    
    print("Success: functional_requirements_client_experience_node")
    return {"functional_requirements_client_experience":functional_requirements_client_experience.model_dump() }


async def functional_requirements_merge_ar(state: GraphState) -> Dict[str, Any]:

    keys=["functional_requirements_operations","functional_requirements_internal_management","functional_requirements_client_experience"]

    result=await base_node.functional_requirements_merge_node(state=state,
                                                              validate_model=FunctionalRequirementsGroupArabicOutput,
                                                              output_model=FunctionalRequirementsArabicOutput,
                                                              keys=keys)

    return {"functional_requirements": result.model_dump()}


async def Final_BRD_ar(state:GraphState):

    keys=["proposed_system","timeline","functional_requirements"]

    result= await base_node.Final_BRD_node(state=state,output_schema=FinalBRDArabicOutput,keys=keys)

    return {
        "final_result": result.model_dump()
    }

