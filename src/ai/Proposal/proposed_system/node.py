
from src.ai.Proposal.state import GraphState

from .schema import ProposedSystemLocalizedOutput, ProposedSystemArabicOutput

from .prompt import proposed_system_ar_template, proposed_system_bill_template

from src.ai.llm.invoke import generate_section


class ProposedSystem:
     
    def __init__(self):
          pass
    async def proposed_system_node(self,state:GraphState,prompt_template, output_model,run_name):

    
            interfaces_and_users = state.get("interfaces_and_users")


            prompt_variables = {"interfaces_and_users":interfaces_and_users}
                
            response= await generate_section(
                state=state,
                prompt_template=prompt_template,
                output_model= output_model,
                run_name= run_name,
                prompt_variables=prompt_variables

            )
            return response

    async def proposed_system_ar(self,state:GraphState):
        response= await self.proposed_system_node(state=state,
            prompt_template=proposed_system_ar_template,
            output_model=ProposedSystemArabicOutput,
            run_name="Proposed System Arabic Node")
        
        
        return {"proposed_system":response.model_dump()}

    async def proposed_system_billingual(self,state:GraphState):
        response= await self.proposed_system_node(state=state,
            prompt_template=proposed_system_bill_template,
            output_model=ProposedSystemLocalizedOutput,
            run_name="Proposed System Node")
        
        
        return {"proposed_system":response.model_dump()}
