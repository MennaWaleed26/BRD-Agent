from src.ai.Proposal.state import GraphState
from .schema import FunctionalRequirementsArabicOutput
from .prompt import functional_requirements_group_ar_template
from src.ai.llm.invoke import generate_section


class Functional_Requiremenst:
     
    def __init__(self):
          pass


    async def functional_requirements_node(self,state:GraphState,prompt_template, output_model,run_name):
            context = state["context"]
            project_title = context['project_name']
            project_details = context['project_details']

            interfaces_and_users = state.get('interfaces_and_users')
            functional_requirements_plan = state.get('functional_requirements_plan')
            prompt_variables = {"project_title":project_title,"project_details":project_details,
                                "interfaces_and_users":interfaces_and_users, 'functional_requirements_plan':functional_requirements_plan}

            response= await generate_section(
                state=state,
                prompt_template=prompt_template,
                output_model= output_model,
                run_name= run_name,
                prompt_variables=prompt_variables

            )
            return response


    async def functional_requirements_ar(self, state: GraphState):
        

        response= await self.functional_requirements_node(
            state= state ,prompt_template= functional_requirements_group_ar_template, output_model= FunctionalRequirementsArabicOutput,run_name= "Func Req Node"
        )
        return {"functional_requirements":response.model_dump()}


    async def functional_requirements_bill(self,state: GraphState):
        

        response= await self.functional_requirements_node(
            state= state ,prompt_template= functional_requirements_group_ar_template, output_model= FunctionalRequirementsArabicOutput,run_name= "Func Req Node"
        )
        return {"functional_requirements":response.model_dump()}
