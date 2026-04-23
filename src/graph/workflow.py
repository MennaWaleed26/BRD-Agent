from langgraph.graph import StateGraph, START, END

from src.graph.state import GraphState
from .nodes import (
    preparation_node,
    functional_req_planner_node,
    router_node,
    
    bilingual_entry_node,
    proposed_system_billingual,
    timeline_billingual,
    validate_timeline_bi,
    timeline_fallback_bi_node,
    finish_timeline_bi_node,
    functional_requirements_operations_billingual,
    functional_requirements_internal_management_billingual,
    functional_requirements_client_experience_billingual,
    functional_requirements_merge_billingual,
    Final_BRD_billingual,
    
    arabic_entry_node,
    proposed_system_ar,
    timeline_ar,
    validate_timeline_ar,
    router_after_timeline_validation,
    timeline_fallback_ar_node,
    finish_timeline_ar_node,
    functional_requirements_operations_ar,
    functional_requirements_client_experience_ar,
    functional_requirements_internal_management_ar,
    functional_requirements_merge_ar,
    Final_BRD_ar
)


def create_brd_graph():
    
    workflow=StateGraph(GraphState)
    
    workflow.add_node("preparation", preparation_node)
    workflow.add_node("functional_req_planner", functional_req_planner_node)
    
    
    
    workflow.add_node("bilingual_entry_point", bilingual_entry_node)
    
    workflow.add_node("proposed_system_bi", proposed_system_billingual)
    workflow.add_node("timeline_bi", timeline_billingual)
    workflow.add_node("validate_timeline_bi",validate_timeline_bi)
    workflow.add_node("timeline_fallback_bi_node",timeline_fallback_bi_node)
    workflow.add_node("finish_timeline_bi_node",finish_timeline_bi_node)
    workflow.add_node("functional_requirements_operations_bi", functional_requirements_operations_billingual)
    workflow.add_node("functional_requirements_internal_management_bi",functional_requirements_internal_management_billingual)
    workflow.add_node("functional_requirements_client_experience_bi",functional_requirements_client_experience_billingual)
    workflow.add_node("functional_requirements_merge_bi",functional_requirements_merge_billingual)
    workflow.add_node("final_brd_bi",Final_BRD_billingual)



    workflow.add_node("arabic_entry_point", arabic_entry_node)
    
    workflow.add_node("proposed_system_ar", proposed_system_ar)
    workflow.add_node("timeline_ar", timeline_ar)
    workflow.add_node("validate_timeline_ar",validate_timeline_ar)
    workflow.add_node("timeline_fallback_ar_node",timeline_fallback_ar_node)
    workflow.add_node("finish_timeline_ar_node",finish_timeline_ar_node)
    workflow.add_node("functional_requirements_operations_ar", functional_requirements_operations_ar)
    workflow.add_node("functional_requirements_internal_management_ar",functional_requirements_internal_management_ar)
    workflow.add_node("functional_requirements_client_experience_ar",functional_requirements_client_experience_ar)
    workflow.add_node("functional_requirements_merge_ar",functional_requirements_merge_ar)
    workflow.add_node("final_brd_ar",Final_BRD_ar)
    
    
    



 
    # workflow.add_edge(START, "preparation")
    # workflow.add_edge("preparation", "proposed_system_ar")
    # workflow.add_edge("proposed_system_ar", END)
    
    
    # workflow.add_conditional_edges("functional_req_planner",router_node,{
    #     "arabic_branch":"arabic_entry_point",
    #     "bilingual_branch":"bilingual_entry_point"
    # })
    
    
    # workflow.add_edge("bilingual_entry_point","proposed_system_bi")
    # workflow.add_edge("bilingual_entry_point","timeline_bi")
    # workflow.add_edge("bilingual_entry_point","functional_requirements_operations_bi")
    # workflow.add_edge("bilingual_entry_point","functional_requirements_internal_management_bi")
    # workflow.add_edge("bilingual_entry_point","functional_requirements_client_experience_bi")
    # workflow.add_edge(["functional_requirements_operations_bi", "functional_requirements_internal_management_bi",
    #                    "functional_requirements_client_experience_bi"]
    #                   ,"functional_requirements_merge_bi")
    # workflow.add_edge([
    #     "proposed_system_bi",
    #     "timeline_bi",
    #     "functional_requirements_merge_bi"
    # ],"final_brd_bi")
    # workflow.add_edge("final_brd_bi",END)
    
    

    # workflow.add_edge("arabic_entry_point","timeline_ar")
    # workflow.add_edge("timeline_ar","validate_timeline_ar")
    # workflow.add_conditional_edges("validate_timeline_ar",router_after_timeline_validation,{
    #     "next_node": "finish_timeline_ar_node",
    #     "timeline_generate_node": "timeline_ar",
    #     "timeline_fallback_ar_node": "timeline_fallback_ar_node",
    # })
    # workflow.add_edge("timeline_fallback_ar_node", "finish_timeline_ar_node")


    # workflow.add_edge("finish_timeline_ar_node",END)
    
    
    
    
    
    workflow.add_edge(START, "preparation")
    workflow.add_edge("preparation", "functional_req_planner")
    workflow.add_conditional_edges("functional_req_planner",router_node,{
        "arabic_branch":"arabic_entry_point",
        "bilingual_branch":"bilingual_entry_point"
    })
    
    
    workflow.add_edge("bilingual_entry_point","proposed_system_bi")
    workflow.add_edge("bilingual_entry_point","timeline_bi")
    workflow.add_edge("timeline_bi","validate_timeline_bi")
    workflow.add_conditional_edges("validate_timeline_bi",router_after_timeline_validation,{
        "next_node":"finish_timeline_bi_node",
        "timeline_generate_node":"timeline_bi",
        "timeline_fallbacki_node":"timeline_fallback_bi_node"
    })
    workflow.add_edge("timeline_fallback_bi_node","finish_timeline_bi_node")
    workflow.add_edge("bilingual_entry_point","functional_requirements_operations_bi")
    workflow.add_edge("bilingual_entry_point","functional_requirements_internal_management_bi")
    workflow.add_edge("bilingual_entry_point","functional_requirements_client_experience_bi")
    workflow.add_edge(["functional_requirements_operations_bi", "functional_requirements_internal_management_bi",
                       "functional_requirements_client_experience_bi"]
                      ,"functional_requirements_merge_bi")
    workflow.add_edge([
        "proposed_system_bi",
        "finish_timeline_bi_node",
        "functional_requirements_merge_bi"
    ],"final_brd_bi")
    workflow.add_edge("final_brd_bi",END)
    
    
    workflow.add_edge("arabic_entry_point","proposed_system_ar")
    workflow.add_edge("arabic_entry_point","timeline_ar")
    workflow.add_edge("timeline_ar","validate_timeline_ar")
    workflow.add_conditional_edges("validate_timeline_ar",router_after_timeline_validation,{
        "next_node": "finish_timeline_ar_node",
        "timeline_generate_node": "timeline_ar",
        "timeline_fallback_node": "timeline_fallback_ar_node",
    })
    workflow.add_edge("timeline_fallback_ar_node", "finish_timeline_ar_node")
    workflow.add_edge("arabic_entry_point","functional_requirements_operations_ar")
    workflow.add_edge("arabic_entry_point","functional_requirements_internal_management_ar")
    workflow.add_edge("arabic_entry_point","functional_requirements_client_experience_ar")
    workflow.add_edge(["functional_requirements_operations_ar", "functional_requirements_internal_management_ar",
                       "functional_requirements_client_experience_ar"]
                      ,"functional_requirements_merge_ar")
    workflow.add_edge([
        "proposed_system_ar",
        "finish_timeline_ar_node",
        "functional_requirements_merge_ar"
    ],"final_brd_ar")
    workflow.add_edge("final_brd_ar",END)


    return workflow.compile()

brd_graph = create_brd_graph()

