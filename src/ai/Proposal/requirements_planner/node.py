from src.ai.llm.invoke import  generate_section 
from src.ai.Proposal.state import GraphState
from .prompt import functional_requirements_planner_prompt_template
from .schema import FunctionalRequirementsPlannerOutput
from src.ai.Proposal.state import GraphState



async def functional_req_planner_node(state:GraphState):
    context =  state.get("context")

    project_title = context.get("project_name")
    project_description = context.get("project_idea")
    project_details = context.get("project_details")
    # project_understanding = state.get('enhanced_context')
    interfaces_and_users = state.get("interfaces_and_users")

    prompt_variables = {"project_title":project_title, "project_description":project_description,
                         "project_details":project_details, "interfaces_and_users":interfaces_and_users}

    response= await generate_section(
        state=state,
        prompt_template=functional_requirements_planner_prompt_template,
        output_model= FunctionalRequirementsPlannerOutput,
        run_name="Func Req Planner Node",
        prompt_variables = prompt_variables

    )
    return {"functional_requirements_plan":response.model_dump()}