from src.ai.Proposal.state import GraphState
from .prompt import interfaces_actors_prompt_template
from  .schema import InterfacesAndUsersOutput
from src.ai.llm.invoke import generate_section


async def interfaces_actors_node(state:GraphState):
    
    context =  state.get("context")
    project_title = context.get("project_name")
    project_description = context.get("project_idea")
    project_details = context.get("project_details")

    
    prompt_variables = {"project_title": project_title, "project_description":project_description,
                                                "project_details":project_details}

    response= await generate_section(
        state=state,
        prompt_template=interfaces_actors_prompt_template,
        output_model= InterfacesAndUsersOutput,
        run_name="Interfaces and Actors extraction node",
        prompt_variables = prompt_variables

    )

    return {"interfaces_and_users": response.model_dump()}