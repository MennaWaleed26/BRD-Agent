import json
import re
from typing import Any, Dict, Optional
from .modes import PlatformCase,PlatformCaseEnum,PatternPlatformSignal
from .patterns import STRONG_HINT_PATTERNS,POSSIBLE_HINT_PATTERNS


def normalize_text(value:Optional[str])->str:
    if not value:
        return ""
    return re.sub(r"\s+", " ", value).strip() #converts multiple spaces → one space
                                              # removes tabs/newlines
                                              # trims edges
                                            
def has_meaningful_text(value: Optional[str], min_len: int = 5) -> bool:
    return len(normalize_text(value)) >= min_len

def get_project_deatils(context):
    
    project_deatils=context.get("project_details","")
    return normalize_text(project_deatils)

def get_platforms(context):
    platforms=context.get("platforms",[])
    return platforms

def get_safe_platform_case(context) -> PlatformCase:
    """
    Only uses safe structural facts:
    - whether details exist
    - whether platforms exist
    """
    details= get_project_deatils(context=context)
    platforms=get_platforms(context=context)
    
    has_details= has_meaningful_text(value=details)
    has_platforms=len(platforms)>0
    
    if has_platforms and has_details:
        return PlatformCaseEnum.PLATFORM_PRESENT_DETAILS_PRESENT.value
    if has_platforms and not has_details:
        return PlatformCaseEnum.PLATFORM_PRESENT_DETAILS_MISSING.value
    if not has_platforms and has_details:
        return PlatformCaseEnum.PLATFORM_MISSING_DETAILS_PRESENT.value
    return PlatformCaseEnum.PLATFORM_MISSING_DETAILS_MISSING.value

def detect_pattern_platform_signal(details:str)->PatternPlatformSignal:
    
    if not has_meaningful_text(value=details):
        return "not_detected"
    
    strong_hits=0
    possible_hits=0
    
    for pattern in STRONG_HINT_PATTERNS:
        if re.search(pattern, details, flags=re.IGNORECASE):
            strong_hits += 1

    for pattern in POSSIBLE_HINT_PATTERNS:
        if re.search(pattern, details, flags=re.IGNORECASE):
            possible_hits += 1

    if strong_hits >= 1:
        return "strong"
    if possible_hits >= 1:
        return "possible"
    return "not_detected"

def build_preparation_controls(context):
    case= get_safe_platform_case(context=context)
    details= get_project_deatils(context=context)
    platforms=get_platforms(context=context)
    
    return {
        "platform_case":case,
        "details_present":has_meaningful_text(details),
        "platforms_provided":len(platforms)>0,
        "platforms_provided_count":len(platforms),
        "pattern_platform_signal":detect_pattern_platform_signal(details=details),
        "control_notes": [
            "Pattern-based platform signal is heuristic only.",
            "It may miss typos, abbreviations, mixed language, or noisy user text.",
            "Do not treat 'not_detected' as proof that project.details has no platform meaning.",
            "If project.details is present and platforms are missing, inspect project.details semantically before deciding whether to extract platforms or infer them from the project context.",
        ],
    }
    
def build_preparation_prompt_inputs(context) :
    controls = build_preparation_controls(context)
    return {
        "context":context,
        "controls":controls 
    }
