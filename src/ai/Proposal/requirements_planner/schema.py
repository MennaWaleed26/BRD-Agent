from pydantic import BaseModel, Field

class SystemFeature(BaseModel):
    key: str = Field(
        ...,
        description=(
            "Stable English snake_case key for the feature, such as "
            "'submit_service_request' or 'upload_documents'."
        ),
    )


    outcome: str = Field(
        description=(
            "The specific user or business result delivered by this feature. "
            "It must add information beyond the parent module purpose and must "
            "not merely restate the feature title."
        )
    )

    interaction_summary: str = Field(
        description=(
            "A concise summary of what the user does and what the system "
            "produces or changes. Keep it functional and non-technical."
        )
    )


    user_keys: list[str] = Field(
        default_factory=list,
        description=(
            "Keys of the users who can use or benefit directly from this feature. "
            "Use only user keys defined under the related interface."
        ),
    )


    source_evidence: list[str] = Field(
        default_factory=list,
        description=(
            "Short evidence from the original project input supporting the feature."
        ),
    )

    dependency_keys: list[str] = Field(
        default_factory=list,
        description=(
            "Keys of features that must exist before this feature can work. "
            "Include only meaningful functional dependencies."
        ),
    )


class SystemModule(BaseModel):
    key: str
    title: str

    purpose: str = Field(
        description=(
            "Concise explanation of the broader business capability covered "
            "by this module. Explain why the module exists. Do not describe "
            "individual feature behavior."
        )
    )

    features: list[SystemFeature] = Field(default_factory=list)


class InterfaceModules(BaseModel):
    interface_key: str = Field(
        ...,
        description=(
            "The key of the interface to which these modules belong. "
            "It must match an interface from InterfacesAndUsersOutput."
        ),
    )

    modules: list[SystemModule] = Field(default_factory=list)

class FunctionalRequirementsPlannerOutput(BaseModel):
    interfaces: list[InterfaceModules] = Field(default_factory=list)


    ambiguities: list[str] = Field(
        default_factory=list,
        description=(
            "Material uncertainties that affect feature boundaries or scope."
        ),
    )
