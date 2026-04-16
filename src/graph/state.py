from typing import TypedDict, Optional, Dict, Any

from typing import TypedDict, Dict, Any, Optional



class GraphState(TypedDict):
    """
    LangGraph state for BRD generation.

    Workflow:
    1. Generate each English section
    2. Translate each section to Arabic
    3. Combine into final bilingual response
    """


    context: Dict[str, Any]
    controls: Dict[str, Any]
    enhanced_context: Dict[str, Any]

    functional_requirements_plan: Dict[str, Any]
  
    proposed_system: Dict[str, Any]
 
    technology_stack_en: Dict[str, Any]
    timeline: Dict[str, Any]
   
    
    
    functional_requirements_operations: Dict[str, Any]
    functional_requirements_internal_management: Dict[str, Any]
    functional_requirements_client_experience: Dict[str, Any]
    functional_requirements: Dict[str, Any]


    final_result: Dict[str, Any]