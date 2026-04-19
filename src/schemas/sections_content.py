from pydantic import BaseModel, Field # type: ignore
from typing import List, Annotated,Literal


# =======================================================================
#                                 BILLINGUAL
# =======================================================================


# =========================
# Proposed System
# =========================

class ProposedSystemItemLocalized(BaseModel):
    title_en: str = Field(
        description="Short English title only, 3 to 8 words, not a sentence, not a paragraph."
    )
    content_en: str = Field(
        description="English description in 2 to 4 business-oriented sentences."
    )
    title_ar: str = Field(
        description="عنوان عربي قصير فقط من 3 إلى 8 كلمات، وليس جملة طويلة، وليس فقرة، ويقابل title_en في المعنى."
    )
    content_ar: str = Field(
        description="وصف عربي مهني من 2 إلى 4 جمل، ويعادل content_en في المعنى، وليس عنوانًا."
    )



# =========================
# Timeline
# =========================
class TimelinePhaseLocalizedItem(BaseModel):
    
    
    title_en: str = Field(
        description="Phase title in English, e.g. 'Phase 1 — Analysis and Design' (short, professional title)"
    )
    title_ar: str = Field(
        description="عنوان المرحلة باللغة العربية، عنوان قصير فقط، مثل: 'المرحلة 1 — التحليل والتصميم'"
    )

    # Steps
    steps_en: List[str] = Field(
        default_factory=list,
        description="List of realistic activities or deliverables for this phase in English"
    )
    steps_ar: List[str] = Field(
        default_factory=list,
        description="قائمة بالأنشطة أو المخرجات الواقعية لهذه المرحلة باللغة العربية"
    )
    



class TimelinePhaseEnrichedLocalizedItem(BaseModel):
    
    phase_number: int = Field(
        description="Sequential phase number starting from 1"
    )
    title_en: str = Field(
        description="Phase title in English, e.g. 'Phase 1 — Analysis and Design' (short, professional title)"
    )
    title_ar: str = Field(
        description="عنوان المرحلة باللغة العربية، عنوان قصير فقط، مثل: 'المرحلة 1 — التحليل والتصميم'"
    )
    # Structured duration
    duration_count: int = Field(
        description="Numeric duration of the phase"
    )
    duration_type_en: Literal["days", "weeks"] = Field(
        description="Duration unit in English"
    )
    duration_type_ar: Literal["أيام", "أسابيع"] = Field(
        description="مدة المرحلة باللغة العربية"
    )
    steps_en: List[str] = Field(
        default_factory=list,
        description="List of realistic activities or deliverables for this phase in English"
    )
    steps_ar: List[str] = Field(
        default_factory=list,
        description="قائمة بالأنشطة أو المخرجات الواقعية لهذه المرحلة باللغة العربية"
    )
    price:int =Field(
        description="the total price devided the number of stages as all stages have the same price"
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
# Functional Requirements Plan
# =========================

class FeatureOutlineEnglish(BaseModel):
    title: str = Field(description="Short feature title in English")
    purpose: str = Field(description="Short business purpose of the feature in English")




class ModuleOutlineEnglish(BaseModel):
    title: str = Field(description="Business-friendly module title in English")
    intro: str = Field(description="Short module introduction in English")
    features: List[FeatureOutlineEnglish] = Field(default_factory=list)




class FunctionalGroupPlanEnglish(BaseModel):
    group_key: str = Field(description="Stable internal group key")
    group_title: str = Field(description="Business-friendly group title in English")
    group_intro: str = Field(description="Short group introduction in English")
    modules: List[ModuleOutlineEnglish] = Field(default_factory=list)




# =========================
# Functional Requirements Details
# =========================

class FeatureDetailLocalized(BaseModel):
    title_en: str = Field(
        description="Short feature title in English"
    )
    title_ar: str = Field(
        description="عنوان عربي قصير للميزة، وليس فقرة"
    )

    description_en: str = Field(
        description="Business-friendly explanation of the feature in English"
    )
    description_ar: str = Field(
        description="شرح مهني واضح للميزة باللغة العربية، ويطابق المعنى الإنجليزي"
    )

    technical_implementation_en: List[str] = Field(
        default_factory=list,
        description="Concrete implementation-oriented steps in English"
    )
    technical_implementation_ar: List[str] = Field(
        default_factory=list,
        description="خطوات تنفيذ واضحة بالعربية، وتطابق technical_implementation_en بالترتيب والمعنى"
    )

    additional_ideas_en: List[str] = Field(
        default_factory=list,
        description="Optional ideas in English that add future value"
    )
    additional_ideas_ar: List[str] = Field(
        default_factory=list,
        description="أفكار إضافية اختيارية بالعربية تضيف قيمة مستقبلية، وتطابق المعنى الإنجليزي"
    )

    technologies_used: List[str] = Field(
        default_factory=list,
        description="Actual technologies only, keep technology names in English, usually 1 to 4 items"
    )


class FunctionalModuleDetailLocalized(BaseModel):
    title_en: str = Field(
        description="Module title in English"
    )
    title_ar: str = Field(
        description="عنوان الوحدة باللغة العربية، قصير وواضح"
    )

    intro_en: str = Field(
        description="Short module introduction in English"
    )
    intro_ar: str = Field(
        description="مقدمة قصيرة للوحدة باللغة العربية، وتطابق intro_en في المعنى"
    )

    features: List[FeatureDetailLocalized] = Field(default_factory=list)


# =======================================================================
#                                 ARABIC
# =======================================================================


# =========================
# Proposed System
# =========================

class ProposedSystemItemArabic(BaseModel):

    title_ar: str = Field(
        description="عنوان عربي قصير فقط من 3 إلى 8 كلمات، وليس جملة طويلة، وليس فقرة"
    )
    content_ar: str = Field(
        description="وصف عربي مهني من 2 إلى 4 جمل،"
    )
    
    
# =========================
# Timeline
# =========================

class TimelinePhaseArabicItem(BaseModel):

    title_ar: str = Field(
        description="عنوان المرحلة باللغة العربية، عنوان قصير فقط، مثل: 'المرحلة 1 — التحليل والتصميم'"
    )

    steps_ar: List[str] = Field(
        default_factory=list,
        description="قائمة بالأنشطة أو المخرجات الواقعية لهذه المرحلة باللغة العربية"
    )

    
class TimelinePhaseEnrichedArabicItem(BaseModel):
    phase_number: int = Field(
        description="Sequential phase number starting from 1"
    )

    title_ar: str = Field(
        description="عنوان المرحلة باللغة العربية، عنوان قصير فقط، مثل: 'المرحلة 1 — التحليل والتصميم'"
    )


    duration_count: int = Field(
        description="Numeric duration of the stage"
    )

    duration_type_ar: Literal["أيام", "أسابيع"] = Field(
        description="مدة المرحلة باللغة العربية"
    )

    steps_ar: List[str] = Field(
        default_factory=list,
        description="قائمة بالأنشطة أو المخرجات الواقعية لهذه المرحلة باللغة العربية"
    )
    price:int =Field(
        description="سعر كل مرحلة"
    )


# =========================
# Functional Requirements Details
# =========================

  
class FeatureDetailArabic(BaseModel):

    title_ar: str = Field(
        description="عنوان عربي قصير للميزة، وليس فقرة"
    )


    description_ar: str = Field(
        description="شرح مهني واضح للميزة باللغة العربية"
    )

 
    technical_implementation_ar: List[str] = Field(
        default_factory=list,
        description="خطوات تنفيذ واضحة بالعربية"
    )


    additional_ideas_ar: List[str] = Field(
        default_factory=list,
        description="أفكار إضافية اختيارية بالعربية تضيف قيمة مستقبلية"
    )

    technologies_used: List[str] = Field(
        default_factory=list,
        description="Actual technologies only, keep technology names in English, usually 1 to 4 items"
    )


class FunctionalModuleDetailArabic(BaseModel):

    title_ar: str = Field(
        description="عنوان الوحدة باللغة العربية، قصير وواضح"
    )

    intro_ar: str = Field(
        description="مقدمة قصيرة للوحدة باللغة العربية، وتطابق intro_en في المعنى"
    )

    features: List[FeatureDetailArabic] = Field(default_factory=list)
