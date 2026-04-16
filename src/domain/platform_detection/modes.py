from typing import Any, Dict, List, Literal, Optional
from enum import Enum

PlatformCase = Literal[
    "platforms_present_details_present",
    "platforms_present_details_missing",
    "platforms_missing_details_present",
    "platforms_missing_details_missing",
]
class PlatformCaseEnum(Enum):
    PLATFORM_PRESENT_DETAILS_PRESENT="platforms_present_details_present"
    PLATFORM_PRESENT_DETAILS_MISSING="platforms_present_details_missing"
    PLATFORM_MISSING_DETAILS_PRESENT="platforms_missing_details_present"
    PLATFORM_MISSING_DETAILS_MISSING="platforms_missing_details_missing"

PatternPlatformSignal = Literal["strong", "possible", "not_detected"]