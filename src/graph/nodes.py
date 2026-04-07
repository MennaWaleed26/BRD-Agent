import json
from sre_constants import ANY
import stat
from typing import Any, Dict, Type, TypeVar
from urllib import response

from langchain_openai import ChatOpenAI # type: ignore
from pydantic import BaseModel # type: ignore

from src.graph.state import GraphState
from src.schemas.response import BRDResponsePayload
from src.schemas.preparation import PreparationOutput
from src.schemas.sections_output import (
                                         
    ProposedSystemEnglishOutput,
    ProposedSystemArabicOutput,
    ProposedSystemSection,
    ProposedSystemSectionContent,
    TechnologyStackEnglishOutput,
    TechnologyStackArabicOutput,
    TechnologyStackSection,
    TechnologyStackSectionContent,
    FunctionalUnitsEnglishOutput,
    FunctionalUnitsArabicOutput,
    FunctionalUnitsSection,
    TimelineEnglishOutput,
    TimelineArabicOutput,
    TimelineSection,
    GenericSectionContent,
)
from src.graph.prompts.proposed_system_prompt import proposed_system_prompt_template
from src.graph.prompts.preparation_prompt import preparation_prompt_template
from src.graph.prompts.timeline_prompt import timeline_prompt_template
from src.graph.prompts.technology_stack_prompt import technology_stack_prompt_template
from src.helpers.config import settings

llm = ChatOpenAI(model="gpt-5.4-nano", api_key=settings.OPENAI_API_KEY) # type: ignore

T = TypeVar("T",bound= BaseModel)



def invoke_structured(
    prompt_template:Any,
    prompt_variables:Dict[str,Any],
    output_model:Type[T]
)->T:
    
    """
    Invoke an LLM with structured output using the given prompt template and output model.
    """
    structured_llm=llm.with_structured_output(output_model)
    final_prompt=prompt_template.invoke(prompt_variables)
    return structured_llm.invoke(final_prompt)
   
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
    
    return {"proposed_system_en":response}

def technology_stack_node(state:GraphState):
    response=generate_english_section(
        state=state,
        prompt_template=technology_stack_prompt_template,
        output_model=TechnologyStackEnglishOutput
    )
    
    return{"technology_stack_en":response}
    
    
def timeline_node(state:GraphState):
    response=generate_english_section(
        state=state,
        prompt_template=timeline_prompt_template,
        output_model=TimelineEnglishOutput
        
    )
    
    return {"timeline_en":response}