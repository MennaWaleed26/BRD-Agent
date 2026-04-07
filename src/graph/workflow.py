from langgraph.graph import StateGraph, START, END  # type: ignore
from src.graph.state import GraphState
from src.graph.nodes import (
    proposed_system_node,
    preparation_node,
    technology_stack_node,
    timeline_node,
    functional_req_planner_node
)

def create_brd_graph():
    
    workflow=StateGraph(GraphState)
    
    workflow.add_node("proposed_system", proposed_system_node)
    workflow.add_node("preparation_node", preparation_node)
    workflow.add_node("technology_stack_node", technology_stack_node)
    workflow.add_node("timeline_node", timeline_node)
    workflow.add_node("functional_req_planner_node", functional_req_planner_node)
    
    # workflow.add_edge(START, "proposed_system")
    workflow.add_edge(START, "preparation_node")
    workflow.add_edge("preparation_node", "functional_req_planner_node")
    workflow.add_edge("functional_req_planner_node",END)
    
    return workflow.compile()

brd_graph = create_brd_graph()