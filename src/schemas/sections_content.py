from pydantic import BaseModel, Field # type: ignore
from typing import List, Annotated,Literal

from src.schemas.common import LocalizedText


# =========================
# Proposed System
# =========================

class ProposedSystemItemEnglish(BaseModel):
    """Structured content for one language of the proposed system section."""
    title: str = Field(description="Title of this proposed platform or subsystem")
    content: str = Field(description="Description of this proposed platform or subsystem")
    technologies_used: List[str] = Field(
        default_factory=list,
        description=
        "List of referenced technologies used to build this item (this platform or subsystem)"
    )
    
class ProposedSystemItemArabic(BaseModel):
    title: str = Field(
        description="عنوان هذا النظام الفرعي أو المنصة المقترحة باللغة العربية"
    )
    content: str = Field(
        description="وصف هذا النظام الفرعي أو المنصة المقترحة باللغة العربية"
    )
    technologies_used: List[str] = Field(
        default_factory=list,
        description="قائمة بالتقنيات المستخدمة فعليًا، وتبقى أسماؤها بالإنجليزية عند الحاجة"
    )

# =========================
# Technology Stack
# =========================

   
class TechnologyStackContentEnglish(BaseModel):
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
    
class TechnologyStackContentArabic(BaseModel):
    title: str = Field(
        description="عنوان فرعي مهني باللغة العربية مرتبط بمنصة أو مجال حل رئيسي"
    )
    content: str = Field(
        description="فقرة عربية مهنية ومختصرة توضح سبب ملاءمة التقنيات المختارة وما المزايا التشغيلية أو التجارية التي تقدمها"
    )
    technologies_used: List[str] = Field(
        default_factory=list,
        description="أسماء التقنيات الفعلية فقط، وتبقى بالإنجليزية عند الحاجة"
    )

# =========================
# Timeline
# =========================

class TimelinePhaseEnglish(BaseModel):
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
        default_factory=list,
        description="List of realistic activities or deliverables for this phase"
    )
    
class TimelinePhaseArabic(BaseModel):
    phase_number: int = Field(
        description="رقم المرحلة بشكل تسلسلي يبدأ من 1"
    )
    title: str = Field(
        description="عنوان المرحلة باللغة العربية مثل: المرحلة 1 — التحليل والتصميم"
    )
    duration: str = Field(
        description="مدة المرحلة باللغة العربية مثل: 'أسبوعان' أو '10 أيام'"
    )
    duration_count: int = Field(
        description="القيمة الرقمية لمدة المرحلة"
    )
    duration_type: Literal["أيام", "أسابيع"] = Field(
        description="وحدة مدة المرحلة باللغة العربية"
    )
    steps: List[str] = Field(
        default_factory=list,
        description="قائمة بالأنشطة أو المخرجات الواقعية لهذه المرحلة باللغة العربية"
    )
    
# =========================
# Functional Requirements Plan
# =========================

class FeatureOutlineEnglish(BaseModel):
    title: str = Field(description="Short feature title in English")
    purpose: str = Field(description="Short business purpose of the feature in English")


class FeatureOutlineArabic(BaseModel):
    title: str = Field(description="عنوان مختصر للميزة باللغة العربية")
    purpose: str = Field(description="الغرض التجاري المختصر من الميزة باللغة العربية")


class ModuleOutlineEnglish(BaseModel):
    title: str = Field(description="Business-friendly module title in English")
    intro: str = Field(description="Short module introduction in English")
    features: List[FeatureOutlineEnglish] = Field(default_factory=list)


class ModuleOutlineArabic(BaseModel):
    title: str = Field(description="عنوان الوحدة بشكل مهني باللغة العربية")
    intro: str = Field(description="مقدمة قصيرة للوحدة باللغة العربية")
    features: List[FeatureOutlineArabic] = Field(default_factory=list)


class FunctionalGroupPlanEnglish(BaseModel):
    group_key: str = Field(description="Stable internal group key")
    group_title: str = Field(description="Business-friendly group title in English")
    group_intro: str = Field(description="Short group introduction in English")
    modules: List[ModuleOutlineEnglish] = Field(default_factory=list)


class FunctionalGroupPlanArabic(BaseModel):
    group_key: str = Field(description="مفتاح داخلي ثابت للمجموعة")
    group_title: str = Field(description="عنوان مهني للمجموعة باللغة العربية")
    group_intro: str = Field(description="مقدمة قصيرة للمجموعة باللغة العربية")
    modules: List[ModuleOutlineArabic] = Field(default_factory=list)


# =========================
# Functional Requirements Details
# =========================

class FeatureDetailEnglish(BaseModel):
    title: str = Field(description="Feature title in English")
    description: str = Field(description="Business-friendly explanation of the feature in English")
    technical_implementation: List[str] = Field(
        default_factory=list,
        description="Concrete implementation-oriented steps in English"
    )
    additional_ideas: List[str] = Field(
        default_factory=list,
        description="Optional ideas in English that add future value"
    )
    technologies_used: List[str] = Field(
        default_factory=list,
        description="Actual technologies only, up to 4 items"
    )


class FeatureDetailArabic(BaseModel):
    title: str = Field(description="عنوان الميزة باللغة العربية")
    description: str = Field(description="شرح مهني واضح للميزة باللغة العربية")
    technical_implementation: List[str] = Field(
        default_factory=list,
        description="خطوات تنفيذ تقنية واضحة باللغة العربية"
    )
    additional_ideas: List[str] = Field(
        default_factory=list,
        description="أفكار إضافية اختيارية باللغة العربية تضيف قيمة مستقبلية"
    )
    technologies_used: List[str] = Field(
        default_factory=list,
        description="أسماء التقنيات الفعلية فقط، وتبقى بالإنجليزية عند الحاجة"
    )


class FunctionalModuleDetailEnglish(BaseModel):
    title: str = Field(description="Module title in English")
    intro: str = Field(description="Short module introduction in English")
    features: List[FeatureDetailEnglish] = Field(default_factory=list)


class FunctionalModuleDetailArabic(BaseModel):
    title: str = Field(description="عنوان الوحدة باللغة العربية")
    intro: str = Field(description="مقدمة قصيرة للوحدة باللغة العربية")
    features: List[FeatureDetailArabic] = Field(default_factory=list)