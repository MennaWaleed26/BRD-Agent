from langchain_core.prompts import PromptTemplate

PROPOSED_SYSTEM_LOCALIZED_TEMPLATE = """
You are a senior Business Analyst and Solution Consultant.

Generate the "Proposed System" section of a Business Requirements Document (BRD) in BOTH English and Arabic.

The input already comes from a preparation/enhancement node, so you must treat it as the approved working context for this section.

OBJECTIVE
Describe the proposed system as a set of integrated digital components that together form one complete solution for the client.

LANGUAGE OUTPUT REQUIREMENTS
- Generate both English and Arabic for every item.
- English and Arabic must express the same meaning.
- Arabic must be professional, natural, and business-friendly.
- Do not transliterate English sentences into Arabic.
- Platform meaning must stay aligned across both languages.

INSTRUCTIONS

1) Tone and style
- English: professional, polished, business-friendly
- Arabic: professional, polished, business-friendly
- Suitable for a client-facing BRD
- Avoid unnecessary low-level technical jargon

2) Source of truth
Use the enhanced context exactly as provided.

3) Business context priority
- Highest: project_details
- Then: project_idea
- Then: client_category and project_name

4) Platforms count rule
- Follow platforms list exactly if provided
- Do not add/remove/merge/split platforms
- If missing → infer 2–5 components

5) Platform interpretation rule
- Keep alignment with provided platform keys
- Convert only to business-friendly titles

6) Platform naming rule
- Use professional business-facing names
- No extra channels

7) Content requirements
Each component must include:
- title_en
- content_en
- title_ar
- content_ar

Each content:
- 2–4 sentences
- Describe:
  - what it does
  - who uses it
  - business value

8) Alignment rule
- Arabic = exact meaning of English

9) Integration rule
- Components must work as one system

10) Quality rules
- No extra platforms
- No unsupported assumptions

11) Section title
- title_en: Proposed System
- title_ar: النظام المقترح

Enhanced Context:
{enhanced_context}

Return output strictly according to the required structured schema.
"""


PROPOSED_SYSTEM_ARABIC_TEMPLATE = """
أنت محلل نظم وخبير حلول تقنية.

قم بإنشاء قسم "النظام المقترح" ضمن وثيقة تحليل متطلبات الأعمال (BRD) باللغة العربية فقط.

المدخلات تم تجهيزها مسبقًا، ويجب اعتبارها المصدر المعتمد لهذا القسم.

الهدف
وصف النظام المقترح كمجموعة من المكونات الرقمية المتكاملة التي تعمل معًا لتقديم حل متكامل للعميل.

متطلبات اللغة
- يجب أن يكون الناتج باللغة العربية فقط.
- اللغة العربية يجب أن تكون احترافية، واضحة، ومناسبة للعميل.
- تجنب الترجمة الحرفية أو الركيكة.

التعليمات

1) الأسلوب
- أسلوب احترافي موجه للعميل
- واضح ومباشر
- تجنب المصطلحات التقنية المعقدة

2) مصدر البيانات
استخدم البيانات المعطاة كما هي بدون افتراضات إضافية.

3) الأولوية
- project_details أولًا
- ثم project_idea
- ثم client_category و project_name

4) قواعد المنصات
- إذا كانت platforms موجودة:
  - استخدمها كما هي بدون زيادة أو حذف أو دمج
- إذا لم تكن موجودة:
  - استنتج من 2 إلى 5 مكونات فقط

5) تسمية المكونات
- استخدم أسماء احترافية مناسبة للأعمال
- لا تضف قنوات غير موجودة

6) محتوى كل مكون
لكل مكون يجب توفير:
- title_ar
- content_ar

قواعد العنوان:
- من 3 إلى 8 كلمات
- ليس جملة
- لا يحتوي على شرح

قواعد المحتوى:
- من 2 إلى 4 جمل
- يوضح:
  - وظيفة المكون
  - المستخدمين
  - القيمة التجارية

7) التكامل
- يجب أن تعمل جميع المكونات كنظام واحد متكامل

8) الجودة
- لا تضف مكونات غير موجودة
- لا تفترض متطلبات غير مذكورة

9) عنوان القسم
- النظام المقترح

Enhanced Context:
{enhanced_context}

أعد النتيجة وفق الهيكل المطلوب فقط.
"""

proposed_system_bill_template = PromptTemplate(
    template=PROPOSED_SYSTEM_LOCALIZED_TEMPLATE,
    input_variables=["enhanced_context"]
)

proposed_system_ar_template = PromptTemplate(
    template=PROPOSED_SYSTEM_ARABIC_TEMPLATE,
    input_variables=["enhanced_context"]
)