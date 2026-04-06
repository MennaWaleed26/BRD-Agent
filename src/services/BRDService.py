# from src.graph.workflow import brd_graph
from src.schemas.request_models import BRDRequestModel # type: ignore
from src.services.NormalizeService import normalize_request
class BRDService:
    
    async def generate_brd(self,payload:BRDRequestModel):
                
            context=normalize_request(raw_request=payload)
            initial_state={"context":context.to_dict()}
            
            # final_output=brd_graph.invoke(initial_state)
            return initial_state


