from pydantic import BaseModel, Field # type: ignore
from typing import Literal, Union, List

from src.schemas.common import LocalizedText
from src.schemas.sections_content import (
    ProposedSystemItemEnglish,
    ProposedSystemItemArabic,
    TechnologyStackContentEnglish,
    TechnologyStackContentArabic,
    TimelinePhaseEnglish,
    TimelinePhaseArabic,
    FunctionalGroupPlanEnglish,
    FunctionalGroupPlanArabic,
    FunctionalModuleDetailEnglish,
    FunctionalModuleDetailArabic,
)

# =========================
# English-only generation outputs
# =========================

class ProposedSystemEnglishOutput(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"
    title: str = Field(description="English section title")
    content: List[ProposedSystemItemEnglish] = Field(
        default_factory=list,
        description="List of proposed system items in English"
    )


class TechnologyStackEnglishOutput(BaseModel):
    key: Literal["technology_stack"] = "technology_stack"
    title: Literal["Technologies Used"] = "Technologies Used"
    content: List[TechnologyStackContentEnglish] = Field(
        default_factory=list,
        description="Ordered list of technology subsections in English"
    )


class FunctionalRequirementsPlannerOutput(BaseModel):
    key: Literal["functional_requirements_plan"] = "functional_requirements_plan"
    title: Literal["Detailed Functional Units Plan"] = "Detailed Functional Units Plan"

    operations_and_project_lifecycle: FunctionalGroupPlanEnglish
    internal_business_management: FunctionalGroupPlanEnglish
    client_digital_experience: FunctionalGroupPlanEnglish


class FunctionalRequirementsGroupEnglishOutput(BaseModel):
    group_key: str = Field(description="Stable internal group key")
    group_title: str = Field(description="Business-friendly group title in English")
    group_intro: str = Field(description="Short introduction for the group in English")
    modules: List[FunctionalModuleDetailEnglish] = Field(default_factory=list)


class FunctionalRequirementsEnglishOutput(BaseModel):
    key: Literal["functional_requirements"] = "functional_requirements"
    title: Literal["Detailed Functional Units"] = "Detailed Functional Units"
    content: List[FunctionalRequirementsGroupEnglishOutput] = Field(default_factory=list)


class TimelineEnglishOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title: Literal["Implementation Timeline"] = "Implementation Timeline"
    content: List[TimelinePhaseEnglish] = Field(
        default_factory=list,
        description="Ordered list of implementation phases in English"
    )


EnglishSectionOutput = Union[
    ProposedSystemEnglishOutput,
    TechnologyStackEnglishOutput,
    FunctionalRequirementsEnglishOutput,
    TimelineEnglishOutput,
]


# =========================
# Arabic-only translation outputs
# =========================

class ProposedSystemArabicOutput(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"
    title: str = Field(description="Arabic section title")
    content: List[ProposedSystemItemArabic] = Field(default_factory=list)


class TechnologyStackArabicOutput(BaseModel):
    key: Literal["technology_stack"] = "technology_stack"
    title: str = Field(description="Arabic section title")
    content: List[TechnologyStackContentArabic] = Field(default_factory=list)


class FunctionalRequirementsGroupArabicOutput(BaseModel):
    group_key: str = Field(description="مفتاح داخلي ثابت للمجموعة")
    group_title: str = Field(description="عنوان المجموعة باللغة العربية")
    group_intro: str = Field(description="مقدمة قصيرة للمجموعة باللغة العربية")
    modules: List[FunctionalModuleDetailArabic] = Field(default_factory=list)


class FunctionalRequirementsArabicOutput(BaseModel):
    key: Literal["functional_requirements"] = "functional_requirements"
    title: str = Field(description="Arabic section title")
    content: List[FunctionalRequirementsGroupArabicOutput] = Field(default_factory=list)


class TimelineArabicOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title: str = Field(description="Arabic section title")
    content: List[TimelinePhaseArabic] = Field(
        default_factory=list,
        description="قائمة مرتبة بمراحل التنفيذ باللغة العربية"
    )


# =========================
# Merged report schemas
# =========================

class BRDEnglishSections(BaseModel):
    proposed_system: ProposedSystemEnglishOutput
    technology_stack: TechnologyStackEnglishOutput
    functional_requirements: FunctionalRequirementsEnglishOutput
    timeline: TimelineEnglishOutput


class BRDArabicSections(BaseModel):
    proposed_system: ProposedSystemArabicOutput
    technology_stack: TechnologyStackArabicOutput
    functional_requirements: FunctionalRequirementsArabicOutput
    timeline: TimelineArabicOutput


# =========================
# Localized wrappers
# =========================

class ProposedSystemLocalizedOutput(BaseModel):
    en: ProposedSystemEnglishOutput
    ar: ProposedSystemArabicOutput


class TechnologyStackLocalizedOutput(BaseModel):
    en: TechnologyStackEnglishOutput
    ar: TechnologyStackArabicOutput


class FunctionalRequirementsLocalizedOutput(BaseModel):
    en: FunctionalRequirementsEnglishOutput
    ar: FunctionalRequirementsArabicOutput


class TimelineLocalizedOutput(BaseModel):
    en: TimelineEnglishOutput
    ar: TimelineArabicOutput


class BRDResponsePayload(BaseModel):
    proposed_system: ProposedSystemLocalizedOutput
    technology_stack: TechnologyStackLocalizedOutput
    functional_requirements: FunctionalRequirementsLocalizedOutput
    timeline: TimelineLocalizedOutput