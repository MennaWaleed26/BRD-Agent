from typing import List, Optional
from pydantic import BaseModel, Field # type: ignore

class PlatformDetails(BaseModel):
    platform: str = Field(
        ...,
        description="""
Normalized platform type (channel), not role-specific.
Use only predefined keys such as:
- web_app
- web_admin
- customer_web
- mobile_app
- backend_api
- vendor_portal

This field represents the platform technology/channel only.
Do NOT include role names or descriptions here.
"""
    )

    role: str = Field(
        ...,
        description="""
User role that uses this platform.

Examples:
- student
- trainer
- admin
- customer
- vendor

Each entry represents one role using one platform.
If multiple roles use the same platform, create multiple entries.
"""
    )


class PreparationOutput(BaseModel):
    project_name: str = Field(
        default="",
        description="Clean and normalized project name in English."
    )

    project_idea: str 

    project_details: str 

    client_name: str 

    client_category: str 

    platforms: List[str] = Field(
        default_factory=list,
        description="""
Flat list of UNIQUE platform types (channels).

Examples:
- web_app
- mobile_app
- backend_api

IMPORTANT RULES:
- This list represents platform TYPES only
- DO NOT duplicate entries
- DO NOT include roles
- DO NOT try to represent multiple apps here

Example:
If there are 2 mobile apps (student + trainer),
the list should still contain only:
["mobile_app"]
"""
    )

    tech_stacks: List[str]

    is_agile: Optional[bool]

    num_stages: Optional[int] 

    timeline_details: Optional[str] 

    platform_role_map: List[PlatformDetails] = Field(
        default_factory=list,
        description="""
CRITICAL FIELD: Defines how each platform is used by each role.

This is the MAIN source of truth for platform-role relationships.

RULES:
- Each entry = one role using one platform
- Must include ALL roles interacting with the system
- Must include ALL platforms used by each role

Examples:

[
  {"platform": "web_app", "role": "student"},
  {"platform": "web_app", "role": "trainer"},
  {"platform": "mobile_app", "role": "student"},
  {"platform": "mobile_app", "role": "trainer"}
]

IMPORTANT:
- This field drives downstream system generation
- Be complete and consistent
- Do NOT skip roles
- Do NOT merge roles
"""
    )

# class PreparationOutput(BaseModel):
#     enhanced_context: NormalizedContext