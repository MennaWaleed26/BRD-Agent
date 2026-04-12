import json
from sre_constants import ANY
import stat
from typing import Any, Dict, Type, TypeVar
from urllib import response

from langchain_openai import ChatOpenAI # type: ignore
from pydantic import BaseModel # type: ignore

from src.graph.state import GraphState

from src.schemas.preparation import PreparationOutput
from src.schemas.sections_output import (
                                         
    
    ProposedSystemEnglishOutput,
    TechnologyStackEnglishOutput,
    FunctionalRequirementsPlannerOutput,
    FunctionalRequirementsGroupEnglishOutput,
    FunctionalRequirementsEnglishOutput,
    TimelineEnglishOutput,
    BRDEnglishSections,
    BRDArabicSections,
    ProposedSystemLocalizedOutput,
    TechnologyStackLocalizedOutput,
    FunctionalRequirementsLocalizedOutput,
    TimelineLocalizedOutput,
    BRDResponsePayload
)
from src.graph.prompts.proposed_system_prompt import proposed_system_prompt_template
from src.graph.prompts.preparation_prompt import preparation_prompt_template
from src.graph.prompts.timeline_prompt import timeline_prompt_template
from src.graph.prompts.technology_stack_prompt import technology_stack_prompt_template
from src.graph.prompts.functional_req_planner_prompt import functional_requirements_planner_prompt_template
from src.graph.prompts.functional_req_group_prompt import functional_requirements_group_prompt_template
from src.graph.prompts.translation_report_prompt import translate_report_prompt_template
from src.helpers.config import settings

llm = ChatOpenAI(model="gpt-5.4-nano", api_key=settings.OPENAI_API_KEY) # type: ignore

T = TypeVar("T",bound= BaseModel)



def invoke_structured(
    prompt_template: Any,
    prompt_variables: Dict[str, Any],
    output_model: Type[T]
) -> T:
    """
    Invoke an LLM with structured output and normalize the returned value
    into the requested Pydantic model.
    """
    structured_llm = llm.with_structured_output(output_model)
    final_prompt = prompt_template.invoke(prompt_variables)
    response = structured_llm.invoke(final_prompt)
    print("invoke_structured response type:", type(response))
    # Case 1: already the exact Pydantic model
    if isinstance(response, output_model):
        return response

    # Case 2: wrapper object with `.parsed`
    parsed = getattr(response, "parsed", None)
    if parsed is not None:
        if isinstance(parsed, output_model):
            return parsed
        return output_model.model_validate(parsed)

    # Case 3: plain dict
    if isinstance(response, dict):
        return output_model.model_validate(response)

    # Case 4: fallback
    return output_model.model_validate(response)
   
def generate_enhanced_context(
    state:GraphState,
    prompt_template:Any,
    output_model:Type[T],
) ->T:
    """
    Shared helper for English generation nodes.
    """
    context=state["context"]
    return invoke_structured(prompt_template=prompt_template,
                             prompt_variables={"context": context},
                             output_model=output_model) 
def generate_english_section(
    state:GraphState,
    prompt_template:Any,
    output_model:Type[T],
) ->T:
    """
    Shared helper for English generation nodes.
    """
    enhanced_context=state["enhanced_context"]
    return invoke_structured(prompt_template=prompt_template,
                             prompt_variables={"enhanced_context": enhanced_context},
                             output_model=output_model)
    

def generate_functional_requirements_group(
    enhanced_context: Dict[str, Any],
    group_plan: Dict[str, Any],
) -> FunctionalRequirementsGroupEnglishOutput:
    """
    Generate functional requirements for a specific group
    using the shared structured invocation helper.
    """

    response: FunctionalRequirementsGroupEnglishOutput = invoke_structured(
        prompt_template=functional_requirements_group_prompt_template,
        prompt_variables={
            "enhanced_context": enhanced_context,
            "group_plan": group_plan,
        },
        output_model=FunctionalRequirementsGroupEnglishOutput,
    )

    return response
    






def preparation_node(state:GraphState):
    response=generate_enhanced_context(
        state=state,
        prompt_template=preparation_prompt_template,
        output_model=PreparationOutput
    )
    
    return {"enhanced_context":response.model_dump()}


def proposed_system_node(state:GraphState):
    response=generate_english_section(
        state=state,
        prompt_template=proposed_system_prompt_template,
        output_model=ProposedSystemEnglishOutput
        
    )
    
    return {"proposed_system_en":response.model_dump()}

def technology_stack_node(state:GraphState):
    response=generate_english_section(
        state=state,
        prompt_template=technology_stack_prompt_template,
        output_model=TechnologyStackEnglishOutput
    )
    
    return{"technology_stack_en":response.model_dump()}
    
    
def timeline_node(state:GraphState):
    response=generate_english_section(
        state=state,
        prompt_template=timeline_prompt_template,
        output_model=TimelineEnglishOutput
        
    )
    
    return {"timeline_en":response.model_dump()}

def functional_req_planner_node(state:GraphState):
    response=generate_english_section(
        state=state,
        prompt_template=functional_requirements_planner_prompt_template,
        output_model= FunctionalRequirementsPlannerOutput
    )
    return {"functional_requirements_plan":response.model_dump()}

def functional_requirements_operations_node(state:GraphState):
    enhanced_context = state["enhanced_context"]
    group_plan = state["functional_requirements_plan"] ["operations_and_project_lifecycle"]
    
    functional_requirements_operations= generate_functional_requirements_group(
        enhanced_context=enhanced_context,
        group_plan=group_plan
    )
    print("Success: functional_requirements_operations_node")
    
    return {"functional_requirements_operations":functional_requirements_operations.model_dump()}

def  functional_requirements_internal_management_node(state:GraphState):
    enhanced_context=state["enhanced_context"]
    group_plan=state["functional_requirements_plan"] ["internal_business_management"]
    
    functional_requirements_internal_management= generate_functional_requirements_group(
        enhanced_context=enhanced_context,
        group_plan=group_plan
    )
    print("Success: functional_requirements_internal_management_node")
    return {"functional_requirements_internal_management":functional_requirements_internal_management.model_dump()}

def functional_requirements_client_experience_node(state: GraphState) -> Dict[str, Any]:
    enhanced_context = state["enhanced_context"]
    group_plan = state["functional_requirements_plan"]["client_digital_experience"]

    functional_requirements_client_experience= generate_functional_requirements_group(
            enhanced_context=enhanced_context,
            group_plan=group_plan,
        )
    
    print("Success: functional_requirements_client_experience_node")
    return {"functional_requirements_client_experience":functional_requirements_client_experience.model_dump() }


def functional_requirements_merge_node(state: GraphState) -> Dict[str, Any]:
    operations = FunctionalRequirementsGroupEnglishOutput(**state["functional_requirements_operations"])
    internal_management = FunctionalRequirementsGroupEnglishOutput(**state["functional_requirements_internal_management"])
    client_experience = FunctionalRequirementsGroupEnglishOutput(**state["functional_requirements_client_experience"])

    final_output = FunctionalRequirementsEnglishOutput(
        content=[operations, internal_management, client_experience]
    )
    print("Success: functional_requirements_merge_node")
    return {"functional_requirements_en": final_output.model_dump()}

def sections_merge_node(state: GraphState) -> Dict[str, Any]:
    print("sections_merge_node keys:", state.keys())

    english_report = BRDEnglishSections(
        proposed_system=ProposedSystemEnglishOutput(**state["proposed_system_en"]),
        technology_stack=TechnologyStackEnglishOutput(**state["technology_stack_en"]),
        functional_requirements=FunctionalRequirementsEnglishOutput(**state["functional_requirements_en"]),
        timeline=TimelineEnglishOutput(**state["timeline_en"]),
    )
    print("Success: sections_merge_node")
    return {"english_report": english_report.model_dump()}

def translation_node(state:GraphState)-> Dict[str,Any]:
    response=invoke_structured(
        prompt_template=translate_report_prompt_template,
        prompt_variables={
            "english_report":state["english_report"]
        },
        output_model=BRDArabicSections
    )
    return {"arabic_report": response.model_dump()}

def final_response_node(state: GraphState) -> Dict[str, Any]:
    english_report = BRDEnglishSections(**state["english_report"])
    arabic_report = BRDArabicSections(**state["arabic_report"])

    final_response = BRDResponsePayload(
        proposed_system=ProposedSystemLocalizedOutput(
            en=english_report.proposed_system,
            ar=arabic_report.proposed_system,
        ),
        technology_stack=TechnologyStackLocalizedOutput(
            en=english_report.technology_stack,
            ar=arabic_report.technology_stack,
        ),
        functional_requirements=FunctionalRequirementsLocalizedOutput(
            en=english_report.functional_requirements,
            ar=arabic_report.functional_requirements,
        ),
        timeline=TimelineLocalizedOutput(
            en=english_report.timeline,
            ar=arabic_report.timeline,
        ),
    )

    return {"final_response": final_response.model_dump()}