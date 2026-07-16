from src.ai.Proposal.state import GraphState

async def arabic_entry_node(state: GraphState):
    return {}


async def bilingual_entry_node(state: GraphState):
    return {}


async def router_node(state:GraphState):
    
    context=state.get("context",{})
    languages=context.get("languages",[])
    
    if len(languages)==1 and languages[0] in ["arabic","ar"]:
        
        return "arabic_branch"

    return "bilingual_branch"

