from pydantic import BaseModel, Field
from typing import Literal, List



class FeatureDetailArabic(BaseModel):

    feature_key: str = Field(
        description=(
            "Stable feature key copied exactly from ModulesAndFeaturesOutput."
        )
    )

    title_ar: str = Field(
        description="عنوان عربي واضح ومختصر للخاصية."
    )

    purpose_ar: str = Field(
        description=(
            "شرح عربي مهني من جملة إلى جملتين يوضح النتيجة المحددة التي "
            "تقدمها الخاصية للمستخدم أو للعمل، وليس مجرد إعادة صياغة عنوانها."
        )
    )

    user_journey_ar: list[str] = Field(
        default_factory=list,
        description=(
            "خطوات استخدام الخاصية من منظور المستخدم والعمل، من خطوتين إلى "
            "خمس خطوات عند وجود تسلسل فعلي. لا تتضمن تفاصيل تقنية."
        )
    )

    business_value_ar: list[str] = Field(
        default_factory=list,
        description=(
            "منفعة أو منفعتان مباشرتان تحققها الخاصية، دون عبارات تسويقية عامة."
        )
    )

class FunctionalModuleDetailArabic(BaseModel):

    module_key: str = Field(
        description="Stable module key copied from ModulesAndFeaturesOutput"
    )

    module_title_ar: str = Field(
        description="عنوان عربي مهني ومختصر للوحدة الوظيفية"
    )

    module_overview_ar: str = Field(
        description=(
            "وصف موجز من جملة إلى جملتين يوضح المجال الوظيفي العام للوحدة "
            "وسبب وجودها، دون شرح خطوات الخصائص."
        )
    )


    features: list[FeatureDetailArabic] = Field(
        default_factory=list,
        description=(
            "الخصائص التابعة للوحدة، بحيث يظهر كل Feature مرة واحدة فقط"
        )
    )

class FunctionalRequirementsGroupArabicOutput(BaseModel):
    group_key: str = Field(
        description=(
            "Stable interface key copied exactly from InterfacesAndUsersOutput"
        )
    )

    group_title_ar: str = Field(
        description="عنوان الواجهة باللغة العربية"
    )

    group_intro_ar: str = Field(
        description=(
            "مقدمة عربية قصيرة توضح دور الواجهة والمستخدمين الذين يتعاملون معها"
        )
    )

    modules: list[FunctionalModuleDetailArabic] = Field(
        default_factory=list
    )

class FunctionalRequirementsArabicOutput(BaseModel):
    key: Literal["functional_requirements"] = "functional_requirements"

    title_ar: Literal[
        "الوحدات الوظيفية التفصيلية"
    ] = "الوحدات الوظيفية التفصيلية"

    introduction_ar: str = Field(
        description=(
            "مقدمة موجزة توضح أن القسم يعرض الوحدات والخصائص الرئيسية "
            "لكل واجهة من واجهات النظام"
        )
    )

    content: list[FunctionalRequirementsGroupArabicOutput] = Field(
        default_factory=list
    )

"========================================================================================"
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

