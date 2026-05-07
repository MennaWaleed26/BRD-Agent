from typing import List, Optional
from pydantic import BaseModel, Field # type: ignore

class PlatformDetails(BaseModel):
    platform: str = Field(
        ...,
        description="""
        Normalized platform type / delivery channel only.

        Use predefined platform keys only, such as:
        - web_app
        - web_admin
        - customer_web
        - mobile_app
        - backend_api
        - vendor_portal

        This field represents the technical platform or channel.
        It must NOT include:
        - role names
        - user types
        - business descriptions
        - duplicated app names

        Correct:
        - mobile_app
        - web_admin

        Wrong:
        - customer_mobile_app
        - designer_mobile_app
        - broker_dashboard
        - admin_for_owner

        If multiple roles use the same mobile app, repeat the same platform value in platform_role_map with different roles.
        """
    )

    role: str = Field(
        ...,
        description="""
        Normalized internal system role that uses this platform.

        This should be a clean, stable role key used by downstream generation.

        Examples:
        - customer
        - designer
        - broker
        - admin
        - student
        - trainer
        - vendor

        Rules:
        - Use one normalized role per entry.
        - Do NOT merge multiple roles in one value.
        - Do NOT use long descriptions here.
        - Do NOT use domain-specific phrases here; put them in real_world_user.
        - Prefer precise domain roles over generic roles when possible.

        For design/real-estate projects:
        Use:
        - customer
        - designer
        - broker
        - admin

        Avoid:
        - vendor
        - supplier
        if the real-world user is actually a designer or engineering office.
        """
    )

    real_world_user: str = Field(
        ...,
        description="""
        Domain-specific real-world user represented by this role.

        This field explains who the user actually is in the business context.
        It should use business/domain language, not generic platform terminology.

        Examples:
        - عميل فردي أو مطور عقاري
        - مصمم مستقل أو مكتب هندسي
        - وسيط أو سمسار أو مسوق
        - صاحب المنصة أو مدير النظام
        - طالب
        - مدرب
        - مسؤول نظام

        Rules:
        - Be specific to the project domain.
        - Mention all real-world user types covered by the role.
        - Do NOT use vague generic terms if the domain provides clearer terms.
        - Do NOT replace domain users with generic labels such as supplier/vendor unless the user explicitly means that.
        """
    )

    description: str = Field(
        ...,
        description="""
        Clear description of what this role does through this platform/interface.

        This field should describe the purpose, main actions, and business value of the interface.

        Include:
        - what the user can do
        - what workflow this interface supports
        - why this interface matters to the business

        Rules:
        - Keep it concise but informative.
        - Use the project domain language.
        - Do NOT invent features not implied by the user request.
        - Do NOT describe another role's responsibilities.
        - Do NOT create a separate platform just because a role has a different experience.

        Example:
        For a designer using mobile_app:
        "Interface for independent designers and engineering offices to receive suitable design requests, review details, submit offers or accept work, communicate with customers, upload design files, and track execution stages."
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
        CRITICAL FIELD: Main source of truth for platform-role relationships.

        Each entry defines:
        - which platform/channel is used
        - which normalized role uses it
        - who that role represents in the real world
        - what this interface is used for

        RULES:
        - Each entry = one role using one platform.
        - Include ALL roles that interact with the system.
        - Include ALL platform-role combinations explicitly mentioned or strongly implied.
        - If multiple roles use the same platform, create multiple entries with the same platform and different roles.
        - Do NOT duplicate the same platform-role pair.
        - Do NOT skip secondary but important roles such as broker, marketer, mediator, reviewer, or admin.
        - Do NOT invent extra platforms not found in the input.
        - Do NOT convert a role-specific experience into a new platform unless the user explicitly requested it.

        Correct example:
        [
        {
            "platform": "mobile_app",
            "role": "customer",
            "real_world_user": "عميل فردي أو مطور عقاري",
            "description": "Creates design requests, uploads files, sets budget/city, tracks project status, and communicates with designers."
        },
        {
            "platform": "mobile_app",
            "role": "designer",
            "real_world_user": "مصمم مستقل أو مكتب هندسي",
            "description": "Receives suitable requests, reviews details, submits offers or accepts work, uploads design files, and tracks execution stages."
        },
        {
            "platform": "mobile_app",
            "role": "broker",
            "real_world_user": "وسيط أو سمسار أو مسوق",
            "description": "Tracks referred customers/designers, follows projects generated from referrals, and monitors commission entitlements."
        },
        {
            "platform": "web_admin",
            "role": "admin",
            "real_world_user": "صاحب المنصة أو مدير النظام",
            "description": "Monitors platform activity, manages users and permissions, reviews projects, configures commissions, and oversees operations."
        }
        ]

        IMPORTANT:
        This field drives downstream proposed-system generation.
        Downstream nodes must not invent platforms or roles outside this map unless explicitly instructed.
        """)
# class PreparationOutput(BaseModel):
#     enhanced_context: NormalizedContext