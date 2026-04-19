from pydantic import BaseModel, Field # type: ignore
from typing import Literal, Union, List

from src.schemas.sections_content import (
    ProposedSystemItemLocalized,
    TimelinePhaseLocalizedItem,
    TimelinePhaseEnrichedLocalizedItem,
    FunctionalGroupPlanEnglish,
    FunctionalModuleDetailLocalized,
    ProposedSystemItemArabic,
    TimelinePhaseArabicItem,
    TimelinePhaseEnrichedArabicItem,
    FunctionalModuleDetailArabic
)

# =======================================================================
#                                 BILLINGUAL
# =======================================================================


class ProposedSystemLocalizedOutput(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"
    title_en: str = Field(description="English section title")
    title_ar: str = Field(description="Arabic section title")
    content: List[ProposedSystemItemLocalized] = Field(
        default_factory=list,
        description="List of proposed system items with aligned English and Arabic content"
    )

class TimelineLocalizedOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title_en: Literal["Implementation Timeline"] = "Implementation Timeline"
    title_ar: Literal["الجدول الزمني للتنفيذ"] = "الجدول الزمني للتنفيذ"
    content: List[TimelinePhaseLocalizedItem] = Field(
        default_factory=list,
        description="Ordered list of implementation phases in English and Arabic"
    )
class TimelineEnrichedLocalizedOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title_en: Literal["Implementation Timeline"] = "Implementation Timeline"
    title_ar: Literal["الجدول الزمني للتنفيذ"] = "الجدول الزمني للتنفيذ"
    content: List[TimelinePhaseEnrichedLocalizedItem] = Field(
        default_factory=list,
        description="Ordered list of implementation phases in English and Arabic"
    )

class FunctionalRequirementsPlannerOutput(BaseModel):
    key: Literal["functional_requirements_plan"] = "functional_requirements_plan"
    title: Literal["Detailed Functional Units Plan"] = "Detailed Functional Units Plan"

    operations_and_project_lifecycle: FunctionalGroupPlanEnglish
    internal_business_management: FunctionalGroupPlanEnglish
    client_digital_experience: FunctionalGroupPlanEnglish 

class FunctionalRequirementsGroupLocalizedOutput(BaseModel):
    group_key: str = Field(description="Stable internal group key")

    group_title_en: str = Field(
        description="Business-friendly group title in English"
    )
    group_title_ar: str = Field(
        description="عنوان المجموعة باللغة العربية"
    )

    group_intro_en: str = Field(
        description="Short introduction for the group in English"
    )
    group_intro_ar: str = Field(
        description="مقدمة قصيرة للمجموعة باللغة العربية"
    )

    modules: List[FunctionalModuleDetailLocalized] = Field(default_factory=list)

class FunctionalRequirementsLocalizedOutput(BaseModel):
    key: Literal["functional_requirements"] = "functional_requirements"
    title_en: Literal["Detailed Functional Units"] = "Detailed Functional Units"
    title_ar: Literal["الوحدات الوظيفية التفصيلية"] = "الوحدات الوظيفية التفصيلية"

    content: List[FunctionalRequirementsGroupLocalizedOutput] = Field(
        default_factory=list
    )


BRDSectionsLocalized=Union[
    ProposedSystemLocalizedOutput,
    TimelineEnrichedLocalizedOutput,
    FunctionalRequirementsLocalizedOutput
]
class FinalBRDLocalizedOutput(BaseModel):
    sections: List[BRDSectionsLocalized] = Field(default_factory=list) # type: ignore





# =======================================================================
#                                 ARABIC
# =======================================================================


class ProposedSystemArabicOutput(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"

    title_ar: str = Field(
        default="النظام المقترح",
        description="عنوان القسم باللغة العربية"
    )

    content: List[ProposedSystemItemArabic] = Field(
        default_factory=list,
        description="قائمة مكونات النظام المقترح باللغة العربية فقط"
    )


class TimelineArabicOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title_ar: Literal["الجدول الزمني للتنفيذ"] = "الجدول الزمني للتنفيذ"
    content: List[TimelinePhaseArabicItem] = Field(
        default_factory=list,
        description="قائمة مرتبة لمراحل التنفيذ بالعربية"
    )

class TimelineEnrichedArabicOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title_ar: Literal["الجدول الزمني للتنفيذ"] = "الجدول الزمني للتنفيذ"
    content: List[TimelinePhaseEnrichedArabicItem] = Field(
        default_factory=list,
        description="قائمة مرتبة لمراحل التنفيذ بالعربية"
    )
    
class FunctionalRequirementsGroupArabicOutput(BaseModel):
    group_key: str = Field(description="Stable internal group key")


    group_title_ar: str = Field(
        description="عنوان المجموعة باللغة العربية"
    )


    group_intro_ar: str = Field(
        description="مقدمة قصيرة للمجموعة باللغة العربية"
    )

    modules: List[FunctionalModuleDetailArabic] = Field(default_factory=list)

class FunctionalRequirementsArabicOutput(BaseModel):
    key: Literal["functional_requirements"] = "functional_requirements"
    title_ar: Literal["الوحدات الوظيفية التفصيلية"] = "الوحدات الوظيفية التفصيلية"

    content: List[FunctionalRequirementsGroupArabicOutput] = Field(
        default_factory=list
    )

BRDSectionsArabic=Union[
    ProposedSystemArabicOutput,
    TimelineEnrichedArabicOutput,
    FunctionalRequirementsArabicOutput
]
class FinalBRDArabicOutput(BaseModel):
    sections: List[BRDSectionsArabic] = Field(default_factory=list) # type: ignore