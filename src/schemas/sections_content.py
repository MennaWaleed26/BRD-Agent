from pydantic import BaseModel, Field # type: ignore
from typing import List, Annotated,Literal

from src.schemas.common import LocalizedText

class ProposedSystemItemtLang(BaseModel):
    """Structured content for one language of the proposed system section."""
    title: str = Field(description="Title of this proposed platform or subsystem")
    content: str = Field(description="Description of this proposed platform or subsystem")
    technologies_used: List[str] = Field(
        default_factory=list,
        description=
        "List of referenced technologies used to build this item (this platform or subsystem)"
    )
    
class TechnologyStackContentLang(BaseModel):
    title: str = Field(
        description="Business-friendly subsection title aligned to a platform or major solution area"
    )
    content: str = Field(
        description="A concise professional paragraph describing why the selected technologies are suitable and what business or operational advantages they provide"
    )
    technologies_used: List[str] = Field(
        default_factory=list,
        description="List of actual technologies only, minimum 1 and maximum 4 items"
    )

class TimelinePhaseLang(BaseModel):
    phase_number: int = Field(
        description="Sequential phase number starting from 1"
    )
    title: str = Field(
        description="Phase title in English, such as 'Phase 1 — Analysis and Design'"
    )
    duration: str = Field(
        description="Phase duration written exactly like '2 weeks' or '10 days'"
    )
    duration_count: int = Field(
        description="Numeric duration of the phase"
    )
    duration_type: Literal["days", "weeks"] = Field(
        description="Duration unit for the phase"
    )
    steps: List[str] = Field(
        description="List of realistic activities or deliverables for this phase"
    )
class FeatureOutline(BaseModel):
    title:str=Field(description="Short feature title")
    purpose:str=Field(description="short business purpose of the feature")

class ModuleOutline(BaseModel):
    title: str = Field(description="Business-friendly module title")
    intro: str = Field(description="Short module introduction")
    features: List[FeatureOutline] = Field(default_factory=list)

class FunctionalGroupPlan(BaseModel):
    group_key: str = Field(description="Stable internal group key")
    group_title: str = Field(description="Business-friendly group title")
    group_intro: str = Field(description="Short group introduction")
    modules: List[ModuleOutline] = Field(default_factory=list)




# =========================
# Group generation schemas
# =========================

class FeatureDetail(BaseModel):
    title: str = Field(description="Feature title")
    description: str = Field(description="Business-friendly explanation of the feature")
    technical_implementation: List[str] = Field(
        default_factory=list,
        description="Concrete implementation-oriented steps"
    )
    additional_ideas: List[str] = Field(
        default_factory=list,
        description="Optional ideas that add future value"
    )
    technologies_used: List[str] = Field(
        default_factory=list,
        description="Actual technologies only, up to 4 items"
    )



class FunctionalModuleDetail(BaseModel):
    title: str = Field(description="Module title")
    intro: str = Field(description="Short module introduction")
    features: List[FeatureDetail] = Field(default_factory=list)








class GenericContentLang(BaseModel):
    """
    Temporary generic content model for sections whose final structure
    will be designed later, like functional_units و timeline.
    """
    title: str = Field(description="Short internal title for the section content")
    content: str = Field(description="Main descriptive content")