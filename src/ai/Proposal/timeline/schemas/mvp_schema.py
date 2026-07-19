from pydantic import create_model, BaseModel, Field
from typing import List, Literal


MVP_TITLE_DESCRIPTION = """
        Short, business-friendly Arabic stage title.

        The title should describe the primary delivery milestone of the stage,
        not a technical task or a numbered label.

        Adapt the title naturally to the project's execution plan and the current stage.

        Examples of style (not fixed sequence):

        - تأسيس المشروع وإطلاق النسخة الأولية
        - استكمال الخصائص الأساسية
        - تطوير الوظائف الإدارية
        - التكامل والاختبارات
        - الإطلاق النهائي
        """





class TimelinePhaseArabicItem(BaseModel):

    title_ar: str = Field(
    description=MVP_TITLE_DESCRIPTION)

    steps_ar: List[str] = Field(
        default_factory=list,
        description="قائمة بالأنشطة أو المخرجات الواقعية لهذه المرحلة باللغة العربية"
    )


class MVPTimelineArabicOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title_ar: Literal["الجدول الزمني للتنفيذ"] = "الجدول الزمني للتنفيذ"
    content: List[TimelinePhaseArabicItem] = Field(
        default_factory=list,
        description="قائمة مرتبة لمراحل التنفيذ بالعربية"
    )

    
class TimelinePhaseEnrichedArabicItem(BaseModel):
    phase_number: int = Field(
        description="Sequential phase number starting from 1"
    )

    title_ar: str = Field(
        description=MVP_TITLE_DESCRIPTION
    )


    duration_count: int = Field(
        description="Numeric duration of the stage"
    )

    duration_type_ar: Literal["آسابيع","آيام","ايام","اسابيع","أيام", "أسابيع"] = Field(
        description="مدة المرحلة باللغة العربية"
    )

    steps_ar: List[str] = Field(
        default_factory=list,
        description="قائمة بالأنشطة أو المخرجات الواقعية لهذه المرحلة باللغة العربية"
    )
    price:float =Field(
        description="سعر كل مرحلة"
    )


class MVPTimelineEnrichedArabicOutput(BaseModel):
    key: Literal["timeline"] = "timeline"
    title_ar: Literal["الجدول الزمني للتنفيذ"] = "الجدول الزمني للتنفيذ"
    content: List[TimelinePhaseEnrichedArabicItem] = Field(
        default_factory=list,
        description="قائمة مرتبة لمراحل التنفيذ بالعربية"
    )
  