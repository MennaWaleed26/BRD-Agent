from src.llm.invoke import generate_enhanced_context, extract_interfaces_and_actors, generate_section 
from src.schemas.preparation import PreparationOutput
from src.prompts.proposal_prompts.preparation_prompt import preparation_prompt_template
from src.graph.state import GraphState
from src.prompts.proposal_prompts.functional_req_planner_prompt import functional_requirements_planner_prompt_template
from src.prompts.proposal_prompts import interfaces_actors_prompt_template
from src.schemas.sections_output import FunctionalRequirementsPlannerOutput
from src.schemas import SystemInterface
from typing import Literal


async def preparation_node(state:GraphState):
    response= await generate_enhanced_context(
        state=state,
        prompt_template=preparation_prompt_template,
        output_model=PreparationOutput,

    )
    
    return {"enhanced_context":response.model_dump()}

async def interfaces_actors_node(state:GraphState):

    response = await extract_interfaces_and_actors(
        state = state,
        prompt_template = interfaces_actors_prompt_template,
        output_model = SystemInterface
    )

    return {"interfaces_and_users": response.model_dump()}

async def router_after_timeline_validation(state:GraphState)-> Literal[
    "next_node",
    "timeline_generate_node",
    "timeline_fallback_node",
]:
    if state.get("timeline_validated") is not None:
        return "next_node"

    if state.get("timeline_retry_count", 0) < 3:
        return "timeline_generate_node"

    return "timeline_fallback_node"



async def functional_req_planner_node(state:GraphState):
    context =  state.get("context")

    project_title = context.get("project_name")
    project_description = context.get("project_idea")
    project_details = context.get("project_details")
    project_understanding = state.get('enhanced_context')
    interfaces_and_users = state.get("interfaces_and_users")

    prompt_variables = {"project_title":project_title, "project_description":project_description,
                         "project_details":project_details, "project_understanding":project_understanding, "interfaces_and_users":interfaces_and_users}

    response= await generate_section(
        state=state,
        prompt_template=functional_requirements_planner_prompt_template,
        output_model= FunctionalRequirementsPlannerOutput,
        run_name="Func Req Planner Node",
        prompt_variables = prompt_variables

    )
    return {"functional_requirements_plan":response.model_dump()}


async def router_node(state:GraphState):
    
    context=state.get("context",{})
    languages=context.get("languages",[])
    
    if len(languages)==1 and languages[0] in ["arabic","ar"]:
        
        return "arabic_branch"

    return "bilingual_branch"

