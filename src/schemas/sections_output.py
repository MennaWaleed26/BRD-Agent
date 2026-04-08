from pickle import LIST

from pydantic import BaseModel, Field # type: ignore
from typing import Literal, Union, List

from src.schemas.common import LocalizedText
from src.schemas.sections_content import (
    ProposedSystemItemtLang,
    TechnologyStackContentLang,
    TimelinePhaseLang,
    FunctionalGroupPlan,
    FunctionalModuleDetail,
    GenericContentLang,
)


# ---------------------------
# English-only generation outputs
# ---------------------------

class ProposedSystemEnglishOutput(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"
    title: str = Field(description="English section title")
    content: List[ProposedSystemItemtLang] = Field(
        default_factory=list,
        description="List of proposed system items in english"
    )


class TechnologyStackEnglishOutput(BaseModel):
    key: Literal["technology_stack"] = "technology_stack"
    title: Literal["Technologies Used"] = "Technologies Used"
    content: List[TechnologyStackContentLang] = Field(
        description="Ordered list of technology subsections"
    )

class FunctionalRequirementsPlannerOutput(BaseModel):
    key: Literal["functional_requirements_plan"] = "functional_requirements_plan"
    title: Literal["Detailed Functional Units Plan"] = "Detailed Functional Units Plan"

    operations_and_project_lifecycle: FunctionalGroupPlan
    internal_business_management: FunctionalGroupPlan
    client_digital_experience: FunctionalGroupPlan

class FunctionalRequirementsGroupOutput(BaseModel):
    group_key: str = Field(description="Stable internal group key")
    group_title: str = Field(description="Business-friendly group title")
    group_intro: str = Field(description="Short introduction for the group")
    modules: List[FunctionalModuleDetail] = Field(default_factory=list)


class FunctionalRequirementsEnglishOutput(BaseModel):
    key: Literal["functional_requirements"] = "functional_requirements"
    title: Literal["Detailed Functional Units"] = "Detailed Functional Units"
    content: List[FunctionalRequirementsGroupOutput] = Field(default_factory=list)


class TimelineEnglishOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title: Literal["Implementation Timeline"] = "Implementation Timeline"
    content: List[TimelinePhaseLang] = Field(
        description="Ordered list of implementation phases"
    )

EnglishSectionOutput = Union[
    ProposedSystemEnglishOutput,
    TechnologyStackEnglishOutput,
    FunctionalRequirementsEnglishOutput,
    TimelineEnglishOutput,
]


class ProposedSystemArabicOutput(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"
    title: str = Field(description="Arabic section title")
    content: List[ProposedSystemItemtLang] = Field(default_factory=list)


class TechnologyStackArabicOutput(BaseModel):
    key: Literal["technology_stack"] = "technology_stack"
    title: str = Field(description="Arabic section title")
    content: List[TechnologyStackContentLang] = Field(default_factory=list)


class FunctionalRequirementsArabicOutput(BaseModel):
    key: Literal["functional_requirements"] = "functional_requirements"
    title: str = Field(description="Arabic section title")
    content: List[FunctionalRequirementsGroupOutput] = Field(default_factory=list)


class TimelineArabicOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title: str = Field(description="Arabic section title")
    content: List[TimelinePhaseLang] = Field(default_factory=list)



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
    
# # ---------------------------
# # Arabic-only translation outputs
# # ---------------------------

# class ProposedSystemArabicOutput(BaseModel):
#     key: Literal["proposed_system"] = "proposed_system"
#     title: str = Field(description="Arabic section title")
#     content: List[ProposedSystemItemtLang] = Field(
#         default_factory=list,
#         description="Structured Arabic content for proposed system"
#     )


# class TechnologyStackArabicOutput(BaseModel):
#     key: Literal["technology_stack"] = "technology_stack"
#     title: str = Field(description="Arabic section title")
#     content: TechnologyStackContentLang = Field(
#         description="Structured Arabic content for technology stack"
#     )


# class FunctionalUnitsArabicOutput(BaseModel):
#     key: Literal["functional_units"] = "functional_units"
#     title: str = Field(description="Arabic section title")
#     content: GenericContentLang = Field(
#         description="Structured Arabic content for functional units"
#     )


# class TimelineArabicOutput(BaseModel):
#     key: Literal["timeline"] = "timeline"
#     title: str = Field(description="Arabic section title")
#     content: GenericContentLang = Field(
#         description="Structured Arabic content for timeline"
#     )


# ArabicSectionOutput = Union[
#     ProposedSystemArabicOutput,
#     TechnologyStackArabicOutput,
#     FunctionalUnitsArabicOutput,
#     TimelineArabicOutput,
# ]


# # ---------------------------
# # Final bilingual section outputs
# # ---------------------------

# class ProposedSystemSectionContent(BaseModel):
#     en: List[ProposedSystemItemtLang] 
#     ar: List[ProposedSystemItemtLang] 


# class TechnologyStackSectionContent(BaseModel):
#     en: TechnologyStackContentLang
#     ar: TechnologyStackContentLang


# class GenericSectionContent(BaseModel):
#     en: GenericContentLang
#     ar: GenericContentLang


# class ProposedSystemSection(BaseModel):
#     key: Literal["proposed_system"] = "proposed_system"
#     title: LocalizedText = Field(
#         default_factory=lambda: LocalizedText(
#             en="Proposed System",
#             ar="النظام المقترح",
#         )
#     )
#     content: ProposedSystemSectionContent


# class TechnologyStackSection(BaseModel):
#     key: Literal["technology_stack"] = "technology_stack"
#     title: LocalizedText = Field(
#         default_factory=lambda: LocalizedText(
#             en="Technologies Used",
#             ar="التقنيات المستخدمة",
#         )
#     )
#     content: TechnologyStackSectionContent


# class FunctionalUnitsSection(BaseModel):
#     key: Literal["functional_units"] = "functional_units"
#     title: LocalizedText = Field(
#         default_factory=lambda: LocalizedText(
#             en="Functional Units",
#             ar="الوحدات الوظيفية",
#         )
#     )
#     content: GenericSectionContent


# class TimelineSection(BaseModel):
#     key: Literal["timeline"] = "timeline"
#     title: LocalizedText = Field(
#         default_factory=lambda: LocalizedText(
#             en="Timeline",
#             ar="الجدول الزمني",
#         )
#     )
#     content: GenericSectionContent


# BRDSection = Union[
#     ProposedSystemSection,
#     TechnologyStackSection,
#     FunctionalUnitsSection,
#     TimelineSection,
# ]