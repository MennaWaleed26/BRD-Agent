
from typing import Any, Dict
from src.graph.state import GraphState
from src.graph.nodes.base_nodes import BaseNodes
from src.schemas.sections_output import (
                                         
    
    ProposedSystemLocalizedOutput,
    TimelineLocalizedOutput,
    FunctionalRequirementsGroupLocalizedOutput,
    FunctionalRequirementsLocalizedOutput,
    FinalBRDLocalizedOutput,
    
)
from src.prompts.proposed_system_prompt import proposed_system_bill_template
from src.prompts.timeline_prompt import timeline_prompt_template
from src.prompts.functional_req_group_prompt import functional_requirements_group_prompt_template




base_node=BaseNodes()


async def bilingual_entry_node(state: GraphState):
    return {}


async def proposed_system_billingual(state:GraphState):
    response= await base_node.proposed_system_node(state=state,
        prompt_template=proposed_system_bill_template,
        output_model=ProposedSystemLocalizedOutput,
        run_name="Proposed System Node")
    
    
    return {"proposed_system":response.model_dump()}


# async def technology_stack_node(state:GraphState):
#     response= await generate_english_section(
#         state=state,
#         prompt_template=technology_stack_prompt_template,
#         output_model=TechnologyStackEnglishOutput,
#         run_name="Technology Stach node"
#     )
    
#     return{"technology_stack_en":response.model_dump()}
    
    
async def timeline_billingual(state:GraphState):
    response= await base_node.timeline_node(
        state=state,
        prompt_template=timeline_prompt_template,
        output_model=TimelineLocalizedOutput,
        run_name="Timeline Node"
    )
    
    return {"timeline":response.model_dump()}





async def functional_requirements_operations_billingual(state:GraphState):
    enhanced_context = state["enhanced_context"]
    group_plan = state["functional_requirements_plan"] ["operations_and_project_lifecycle"]
    
    functional_requirements_operations= await base_node.functional_requirements_operations_node(
        state=state,
        enhanced_context=enhanced_context,
        group_plan=group_plan,
        output_model=FunctionalRequirementsGroupLocalizedOutput,
        run_name="Func Req Operations Node",
        prompt_template=functional_requirements_group_prompt_template
    )
    

    print("Success: functional_requirements_operations_node")
    
    return {"functional_requirements_operations":functional_requirements_operations.model_dump()}



async def  functional_requirements_internal_management_billingual(state:GraphState):
    enhanced_context=state["enhanced_context"]
    group_plan=state["functional_requirements_plan"] ["internal_business_management"]
    
    functional_requirements_internal_management= await base_node.functional_requirements_internal_management_node(state,
        enhanced_context=enhanced_context,
        group_plan=group_plan,
        output_model=FunctionalRequirementsGroupLocalizedOutput,
        run_name="Func Req Internal Management Node",
        prompt_template=functional_requirements_group_prompt_template) 
    

    print("Success: functional_requirements_internal_management_node")
    
    return {"functional_requirements_internal_management":functional_requirements_internal_management.model_dump()}


async def functional_requirements_client_experience_billingual(state: GraphState) -> Dict[str, Any]:
    enhanced_context = state["enhanced_context"]
    group_plan = state["functional_requirements_plan"]["client_digital_experience"]

    functional_requirements_client_experience= await base_node.functional_requirements_client_experience_node(state,
            enhanced_context=enhanced_context,
            group_plan=group_plan,
            output_model=FunctionalRequirementsGroupLocalizedOutput,
            run_name="Func Req Client Experience Node",
            prompt_template=functional_requirements_group_prompt_template)
 
    
    print("Success: functional_requirements_client_experience_node")
    return {"functional_requirements_client_experience":functional_requirements_client_experience.model_dump() }


async def functional_requirements_merge_billingual(state: GraphState) -> Dict[str, Any]:

    keys=["functional_requirements_operations","functional_requirements_internal_management","functional_requirements_client_experience"]

    result=await base_node.functional_requirements_merge_node(state=state,
                                                              validate_model=FunctionalRequirementsGroupLocalizedOutput,
                                                              output_model=FunctionalRequirementsLocalizedOutput,
                                                              keys=keys)

    return {"functional_requirements": result.model_dump()}


async def Final_BRD_billingual(state:GraphState):

    keys=["proposed_system","timeline","functional_requirements"]

    result= await base_node.Final_BRD_node(state=state,output_schema=FinalBRDLocalizedOutput,keys=keys)

    return {
        "final_result": result.model_dump()
    }

