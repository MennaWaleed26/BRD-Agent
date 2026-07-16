from pydantic import BaseModel, Field
from typing import List, Literal





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

    duration_type_ar: Literal["ايام","اسابيع","أيام", "أسابيع"] = Field(
        description="مدة المرحلة باللغة العربية"
    )

    steps_ar: List[str] = Field(
        default_factory=list,
        description="قائمة بالأنشطة أو المخرجات الواقعية لهذه المرحلة باللغة العربية"
    )
    price:float =Field(
        description="سعر كل مرحلة"
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
  
"=============================================================================================="

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
    price:float =Field(
        description="the total price devided the number of stages as all stages have the same price"
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






