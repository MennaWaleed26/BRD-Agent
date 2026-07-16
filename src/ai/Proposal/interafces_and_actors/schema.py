from pydantic import BaseModel, Field
from typing import Literal

class InterfaceUser(BaseModel):
    key: str = Field(
        ...,
        description=(
            "Stable English snake_case key for the user type, "
            "such as employee, provider, customer, broker, or hr_staff."
        ),
    )

    title: str = Field(
        ...,
        description="Concise normalized English title for internal use.",
    )

    real_world_user: str = Field(
        ...,
        description=(
            "The user title using the terminology and language found "
            "in the project input."
            " make this in arabic and infer it from the arabic project details"
        ),
    )

    description: str = Field(
        ...,
        description=(
            "Brief explanation of who this user is and their relationship "
            "with the interface."
        ),
    )

    capabilities: list[str] = Field(
        default_factory=list,
        description=(
            "High-level actions this user can perform through this interface. "
            "Do not include detailed technical permissions."
        ),
    )

    source_evidence: list[str] = Field(
        default_factory=list,
        description=(
            "Short evidence from the project input supporting this user "
            "and their capabilities."
            "make this in arabic and infer it from the arabic project details"
        ),
    )


class SystemInterface(BaseModel):
    key: str = Field(
        ...,
        description=(
            "Stable English snake_case interface key, such as "
            "customer_portal, provider_portal, or employee_mobile_app."
        ),
    )

    title: str = Field(
        ...,
        description="Normalized English interface title for internal use.",
    )

    real_world_title: str = Field(
        ...,
        description=(
            "Client-facing interface title using terminology from the input. make this in arabic and infer it from the arabic project details"
        ),
    )


    description: str = Field(
        ...,
        description=(
            "High-level purpose of the interface. "
            "Do not enumerate detailed modules or features."
        ),
    )



    users: list[InterfaceUser] = Field(
        default_factory=list,
        description=(
            "The users who interact with this interface and the high-level "
            "actions available to each user."
        ),
    )

    source_evidence: list[str] = Field(
        default_factory=list,
        description=(
            "Evidence supporting the existence and purpose of this interface. make this in arabic and infer it from the arabic project details"
        ),
    )


class InterfacesAndUsersOutput(BaseModel):
    interfaces: list[SystemInterface] = Field(default_factory=list)

