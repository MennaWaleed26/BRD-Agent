# from src.graph.workflow import brd_graph
from src.schemas.request_models import BRDRequestModel # type: ignore
from src.services.NormalizeService import normalize_request
from src.graph.workflow import brd_graph


class BRDService:
    
    async def generate_brd(self,payload:BRDRequestModel):
            final_state=None
            context=normalize_request(raw_request=payload)
            initial_state={"context":context.to_dict()}
            print(initial_state)
            
            # final_output=brd_graph.invoke(initial_state)
            # final_output = brd_graph.invoke(initial_state)
            for event in brd_graph.stream(initial_state, stream_mode="updates"):
                print(event)          # debugging
                final_state = event   # keep last update
            return final_state

