from typing import TypedDict, Optional, Dict, Any

from typing import TypedDict, Dict, Any, Optional

from src.schemas.sections_output import (
    ProposedSystemEnglishOutput,
    TechnologyStackEnglishOutput,
    FunctionalUnitsEnglishOutput,
    TimelineEnglishOutput,
    ProposedSystemArabicOutput,
    TechnologyStackArabicOutput,
    FunctionalUnitsArabicOutput,
    TimelineArabicOutput,
)
from src.schemas.response import BRDResponsePayload


class GraphState(TypedDict ):
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
    proposed_system_en: Optional[ProposedSystemEnglishOutput]
    technology_stack_en: Optional[TechnologyStackEnglishOutput]
    functional_units_en: Optional[FunctionalUnitsEnglishOutput]
    timeline_en: Optional[TimelineEnglishOutput]

    # arabic translated sections
    proposed_system_ar: Optional[ProposedSystemArabicOutput]
    technology_stack_ar: Optional[TechnologyStackArabicOutput]
    functional_units_ar: Optional[FunctionalUnitsArabicOutput]
    timeline_ar: Optional[TimelineArabicOutput]

    # final response payload
    final_response: Optional[BRDResponsePayload]