# from src.graph.workflow import brd_graph
from src.schemas.request_models import BRDRequestModel # type: ignore
from src.services.NormalizeService import normalize_request
from src.graph.workflow import brd_graph


class BRDService:
    async def generate_brd(self, payload: BRDRequestModel):
        context = normalize_request(raw_request=payload)
        initial_state = {"context": context.to_dict()}

        final_state = brd_graph.invoke(initial_state)
        print(final_state.keys())
        return final_state["final_response"]
