from pydantic import BaseModel, Field
from typing import Literal, Union, List

from src.schemas.common import LocalizedText
from src.schemas.sections_content import (
    ProposedSystemItemtLang,
    TechnologyStackContentLang,
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
    title: str = Field(description="English section title")
    content: TechnologyStackContentLang = Field(
        description="Structured English content for technology stack"
    )


class FunctionalUnitsEnglishOutput(BaseModel):
    key: Literal["functional_units"] = "functional_units"
    title: str = Field(description="English section title")
    content: GenericContentLang = Field(
        description="Structured English content for functional units"
    )


class TimelineEnglishOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title: str = Field(description="English section title")
    content: GenericContentLang = Field(
        description="Structured English content for timeline"
    )


EnglishSectionOutput = Union[
    ProposedSystemEnglishOutput,
    TechnologyStackEnglishOutput,
    FunctionalUnitsEnglishOutput,
    TimelineEnglishOutput,
]


# ---------------------------
# Arabic-only translation outputs
# ---------------------------

class ProposedSystemArabicOutput(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"
    title: str = Field(description="Arabic section title")
    content: List[ProposedSystemItemtLang] = Field(
        default_factory=list,
        description="Structured Arabic content for proposed system"
    )


class TechnologyStackArabicOutput(BaseModel):
    key: Literal["technology_stack"] = "technology_stack"
    title: str = Field(description="Arabic section title")
    content: TechnologyStackContentLang = Field(
        description="Structured Arabic content for technology stack"
    )


class FunctionalUnitsArabicOutput(BaseModel):
    key: Literal["functional_units"] = "functional_units"
    title: str = Field(description="Arabic section title")
    content: GenericContentLang = Field(
        description="Structured Arabic content for functional units"
    )


class TimelineArabicOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title: str = Field(description="Arabic section title")
    content: GenericContentLang = Field(
        description="Structured Arabic content for timeline"
    )


ArabicSectionOutput = Union[
    ProposedSystemArabicOutput,
    TechnologyStackArabicOutput,
    FunctionalUnitsArabicOutput,
    TimelineArabicOutput,
]


# ---------------------------
# Final bilingual section outputs
# ---------------------------

class ProposedSystemSectionContent(BaseModel):
    en: List[ProposedSystemItemtLang] 
    ar: List[ProposedSystemItemtLang] 


class TechnologyStackSectionContent(BaseModel):
    en: TechnologyStackContentLang
    ar: TechnologyStackContentLang


class GenericSectionContent(BaseModel):
    en: GenericContentLang
    ar: GenericContentLang


class ProposedSystemSection(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"
    title: LocalizedText = Field(
        default_factory=lambda: LocalizedText(
            en="Proposed System",
            ar="النظام المقترح",
        )
    )
    content: ProposedSystemSectionContent


class TechnologyStackSection(BaseModel):
    key: Literal["technology_stack"] = "technology_stack"
    title: LocalizedText = Field(
        default_factory=lambda: LocalizedText(
            en="Technologies Used",
            ar="التقنيات المستخدمة",
        )
    )
    content: TechnologyStackSectionContent


class FunctionalUnitsSection(BaseModel):
    key: Literal["functional_units"] = "functional_units"
    title: LocalizedText = Field(
        default_factory=lambda: LocalizedText(
            en="Functional Units",
            ar="الوحدات الوظيفية",
        )
    )
    content: GenericSectionContent


class TimelineSection(BaseModel):
    key: Literal["timeline"] = "timeline"
    title: LocalizedText = Field(
        default_factory=lambda: LocalizedText(
            en="Timeline",
            ar="الجدول الزمني",
        )
    )
    content: GenericSectionContent


BRDSection = Union[
    ProposedSystemSection,
    TechnologyStackSection,
    FunctionalUnitsSection,
    TimelineSection,
]