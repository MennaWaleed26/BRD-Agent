from typing import Any, Dict, Type, TypeVar
from langchain_openai import ChatOpenAI # type: ignore
from pydantic import BaseModel # type: ignore

from src.graph.state import GraphState


from src.helpers.config import settings


llm = ChatOpenAI(model="gpt-5.4-nano", api_key=settings.OPENAI_API_KEY) # type: ignore

T = TypeVar("T",bound= BaseModel)



async def invoke_structured_async(
    prompt_template: Any,
    prompt_variables: Dict[str, Any],
    output_model: Type[T],
    run_name: str = "unknown"

    
) -> T:
    """
    Invoke an LLM with structured output and normalize the returned value
    into the requested Pydantic model.
    """
    structured_llm = llm.with_structured_output(output_model).with_config({"run_name":run_name})
    final_prompt = prompt_template.invoke(prompt_variables)
    response = await structured_llm.ainvoke(final_prompt)
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
   
async def generate_enhanced_context(
    state:GraphState,
    prompt_template:Any,
    output_model:Type[T],
) ->T:
    """
    Shared helper for English generation nodes.
    """
    context=state["context"]
    controls=state["controls"]
    result= await invoke_structured_async(prompt_template=prompt_template,
                             prompt_variables={"context": context, "controls":controls},
                             output_model=output_model) 
    return result 

async def generate_section(
    state:GraphState,
    prompt_template:Any,
    output_model:Type[T],
    run_name:str="unknown"
) ->T:
    """
    Shared helper for English generation nodes.
    """
    enhanced_context=state["enhanced_context"]
    result= await invoke_structured_async(prompt_template=prompt_template,
                             prompt_variables={"enhanced_context": enhanced_context},
                             output_model=output_model,
                             run_name=run_name)
    return result
    

async def generate_functional_requirements_group(
    enhanced_context: Dict[str, Any],
    group_plan: Dict[str, Any],
    output_model,
    prompt_template,
    run_name:str ="Unknown",
    
) :
    """
    Generate functional requirements for a specific group
    using the shared structured invocation helper.
    """

    response = await invoke_structured_async(
        prompt_template=prompt_template,
        prompt_variables={
            "enhanced_context": enhanced_context,
            "group_plan": group_plan,
        },
        output_model=output_model,
        run_name=run_name
    )

    return response
    



