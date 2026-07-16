from src.ai.Proposal.state import GraphState
from .schema import FinalBRDArabicOutput, FinalBRDLocalizedOutput

class MergeProposal:
     
    def __init__(self):
          pass
    async def Final_BRD_node(self,state,output_schema,keys):

            sections=[]

            for key in keys:
                v=state.get(key)
                if v :
                    sections.append(v)
            result = output_schema(sections=sections)

            return result


    async def Final_BRD_ar(self, state:GraphState):

        keys=["proposed_system","timeline_validated","functional_requirements"]

        result= await self.Final_BRD_node(state=state,output_schema=FinalBRDArabicOutput,keys=keys)

        return {
            "final_result": result.model_dump()
        }

    async def Final_BRD_billingual(self, state:GraphState):

        keys=["proposed_system","timeline","functional_requirements"]

        result= await self.Final_BRD_node(state=state,output_schema=FinalBRDLocalizedOutput,keys=keys)

        return {
            "final_result": result.model_dump()
        }

