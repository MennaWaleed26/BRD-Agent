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

    # normalized input from backend
    context: Dict[str, Any]
    enhanced_context: Dict[str, Any]

    functional_requirements_plan: Dict[str, Any]
    # english generated sections
    proposed_system_en: Dict[str, Any]
    technology_stack_en: Dict[str, Any]
    timeline_en: Dict[str, Any]
    
    functional_requirements_operations: Dict[str, Any]
    functional_requirements_internal_management: Dict[str, Any]
    functional_requirements_client_experience: Dict[str, Any]
    functional_requirements_en: Dict[str, Any]


    english_report: Dict[str, Any]
    arabic_report: Dict[str, Any]

    final_response: Dict[str, Any]