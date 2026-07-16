from pydantic import BaseModel, Field
from typing import List, Literal


class ProposedSystemItemArabic(BaseModel):

    interface_key: str = Field(
        description=(
            "Stable interface key copied exactly from InterfacesAndUsersOutput"
        )
    )

    title_ar: str = Field(
        description=(
            "عنوان عربي قصير وواضح من 2 إلى 6 كلمات يمثل الواجهة، "
            "وليس اسم مستخدم أو دورًا"
        )
    )

    content_ar: str = Field(
        description=(
            "وصف عربي مهني من 2 إلى 4 جمل يوضح الغرض من الواجهة، "
            "المستخدمين المستفيدين منها، وأهم ما تتيحه بصورة عامة"
        )
    )


class ProposedSystemArabicOutput(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"

    title_ar: Literal["النظام المقترح"] = "النظام المقترح"

    overview_ar: str = Field(
        description=(
            "مقدمة عربية قصيرة من جملتين إلى ثلاث تصف الحل المقترح "
            "وكيف تتكامل واجهاته لتحقيق أهداف المشروع"
        )
    )

    content: list[ProposedSystemItemArabic] = Field(
        default_factory=list,
        description=(
            "عنصر واحد فقط لكل واجهة معتمدة، وبالترتيب نفسه الوارد "
            "في مخرجات InterfacesAndUsersOutput"
        )
    )

"=============================================================================================="


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

class ProposedSystemLocalizedOutput(BaseModel):
    key: Literal["proposed_system"] = "proposed_system"
    title_en: str = Field(description="English section title")
    title_ar: str = Field(description="Arabic section title")
    content: List[ProposedSystemItemLocalized] = Field(
        default_factory=list,
        description="List of proposed system items with aligned English and Arabic content"
    )