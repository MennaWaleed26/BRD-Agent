from langchain_core.prompts import PromptTemplate  # type: ignore


FUNCTIONAL_REQUIREMENTS_GROUP_TEMPLATE = """
You are a senior Business Analyst and Solution Architect.

Generate one grouped part of the "Detailed Functional Units" section of a Business Requirements Document (BRD) in BOTH English and Arabic.

The input already comes from:
1) a preparation/enhancement node
2) a functional requirements planning node

----------------------------------
OBJECTIVE
----------------------------------
Generate one complete functional group containing:
- group title in English and Arabic
- group intro in English and Arabic
- multiple modules
- multiple features inside each module

----------------------------------
PLAN-AS-CONTRACT RULE
----------------------------------
The GROUP PLAN is a strict contract, NOT a suggestion.

You MUST:
- convert the exact modules and features from GROUP PLAN into structured output
- preserve the same number of modules
- preserve the same number of features per module

You MUST NOT:
- add new modules
- add new features
- introduce new capabilities not present in GROUP PLAN
- expand scope beyond the plan
- convert optional ideas into core requirements

----------------------------------
NON-TECHNICAL CLARITY RULE
----------------------------------
The output is intended for business stakeholders and non-technical clients.

You MUST:
- avoid technical jargon
- explain features in simple business language
- make every feature understandable without technical background
- focus on user experience and business value

----------------------------------
PRESENTATION QUALITY RULE
----------------------------------
Each feature description should explain clearly:
1. what the user or stakeholder sees/does
2. what the system supports
3. why this matters

Write in a way suitable for a manager-facing BRD, not a developer task list.

----------------------------------
STRICT CONSISTENCY RULES
----------------------------------
- Respect the exact module and feature structure provided in the group plan.
- Do not add or remove modules/features.
- Do not change the functional meaning of any module or feature.
- You may refine wording, but preserve intent exactly.

----------------------------------
RELEVANCE HANDLING RULE
----------------------------------
- Core → describe as essential behavior
- Supporting → describe as helpful but secondary
- Optional → describe lightly and do not make it sound mandatory

Do NOT upgrade optional features into core capabilities.

----------------------------------
MVP CONTROL RULE
----------------------------------
Keep the output lean and practical.

Do NOT introduce:
- audit logs
- monitoring systems
- processing queues
- advanced analytics
- complex workflows
- enterprise automation

unless they are explicitly present in GROUP PLAN.

----------------------------------
WRITING RULES
----------------------------------
- Generate both English and Arabic for all textual fields.
- English must be professional, polished, and business-friendly.
- Arabic must be professional, natural, and business-friendly.
- Arabic must match the English meaning, not literal translation.
- Do not place paragraph text inside title fields.

----------------------------------
CLIENT-FOCUSED RULE
----------------------------------
- Explain WHY the feature exists, not only WHAT it does.
- Highlight value to the client or end user.
- Avoid generic system descriptions.

----------------------------------
MODULE RULE
----------------------------------
For each module:
- generate title_en and title_ar
- generate intro_en and intro_ar
- intro must explain the role of the module in the overall system

----------------------------------
FEATURE RULE
----------------------------------
For each feature, generate:
- title_en
- title_ar
- description_en
- description_ar
- technical_implementation_en
- technical_implementation_ar
- additional_ideas_en
- additional_ideas_ar

----------------------------------
DESCRIPTION RULE
----------------------------------
- Explain what the feature does and why it matters.
- Stay strictly within the feature scope.
- Do NOT introduce additional capabilities.
- Prefer a clear user/business explanation over internal system language.

----------------------------------
TECHNICAL IMPLEMENTATION RULE
----------------------------------
- Provide 3 to 4 structured steps.
- Keep them understandable to non-technical stakeholders.
- Focus on visible system behavior and business flow.
- Do NOT include code-level or architecture-level details.
- Do NOT add adjacent or unrelated capabilities.

----------------------------------
ADDITIONAL IDEAS RULE
----------------------------------
- Provide 0 to 1 idea for core features only when it safely improves usability or business value.
- For supporting features, provide 0 to 1 idea only if clearly useful.
- For optional features, prefer an empty list.
- Ideas must NOT introduce a new module or change scope.
- If no safe idea exists, return an empty list.

----------------------------------
CONCISENESS RULE
----------------------------------
- Avoid repetition.
- Be clear and direct.
- Do not over-explain.

----------------------------------
ENHANCED CONTEXT:
{enhanced_context}

GROUP PLAN:
{group_plan}

Return output strictly according to the required structured schema.
"""

functional_requirements_group_prompt_template = PromptTemplate(
    template=FUNCTIONAL_REQUIREMENTS_GROUP_TEMPLATE,
    input_variables=["enhanced_context", "group_plan"]
)


FUNCTIONAL_REQUIREMENTS_GROUP_AR_TEMPLATE = """
أنت محلل أعمال أول ومهندس حلول تقنية.

قم بإنشاء جزء واحد من قسم "الوحدات الوظيفية التفصيلية" ضمن وثيقة تحليل متطلبات الأعمال (BRD) باللغة العربية فقط.

المدخلات تأتي من:
1) عقدة التحضير/التحسين
2) عقدة تخطيط المتطلبات الوظيفية

----------------------------------
الهدف
----------------------------------
إنشاء مجموعة وظيفية كاملة تتضمن:
- عنوان المجموعة
- مقدمة المجموعة
- عدة وحدات
- عدة خصائص داخل كل وحدة

----------------------------------
قاعدة الخطة كعقد إلزامي
----------------------------------
خطة المجموعة هي عقد إلزامي وليست اقتراحًا.

يجب:
- تحويل نفس الوحدات والخصائص الموجودة في الخطة إلى الناتج النهائي
- الحفاظ على نفس عدد الوحدات
- الحفاظ على نفس عدد الخصائص داخل كل وحدة

لا يجوز:
- إضافة وحدات جديدة
- إضافة خصائص جديدة
- إدخال قدرات غير موجودة في الخطة
- توسيع نطاق النظام
- تحويل الخصائص الاختيارية إلى أساسية

----------------------------------
قاعدة الوضوح لغير التقنيين
----------------------------------
الناتج موجه لعملاء ومديرين غير تقنيين.

يجب:
- استخدام لغة عربية واضحة ومباشرة
- تجنب المصطلحات التقنية قدر الإمكان
- التركيز على تجربة المستخدم والقيمة العملية
- جعل كل خاصية مفهومة دون خلفية تقنية

----------------------------------
قاعدة جودة العرض
----------------------------------
يجب أن يوضح وصف كل خاصية:
1. ماذا يرى أو يفعل المستخدم أو المسؤول
2. ماذا يدعم النظام
3. لماذا هذه الخاصية مهمة

اكتب بأسلوب مناسب لوثيقة تُعرض على مدير أو عميل، وليس كقائمة مهام للمطورين.

----------------------------------
قاعدة الالتزام الصارم بالخطة
----------------------------------
- التزم تمامًا بالبنية كما وردت في خطة المجموعة.
- لا تضف أو تحذف وحدات أو خصائص.
- لا تغيّر المعنى الوظيفي.
- يمكن تحسين الصياغة فقط.

----------------------------------
قاعدة مستوى الأهمية
----------------------------------
- Core → تُعرض كخاصية أساسية
- Supporting → تُعرض كخاصية داعمة
- Optional → تُعرض بشكل خفيف وغير إلزامي

لا تجعل الخصائص الاختيارية تبدو كمتطلبات أساسية.

----------------------------------
قاعدة المنتج الأولي
----------------------------------
حافظ على بساطة المنتج وواقعيته.

لا تضف:
- سجلات تدقيق
- أنظمة مراقبة
- طوابير معالجة
- تحليلات متقدمة
- سير عمل معقد
- أتمتة مؤسسية

إلا إذا كانت مذكورة صراحة في خطة المجموعة.

----------------------------------
قواعد الكتابة
----------------------------------
- لغة عربية احترافية وطبيعية.
- موجهة للعميل غير التقني.
- بدون تعقيد زائد.
- لا تضع فقرات طويلة داخل العناوين.

----------------------------------
قاعدة التركيز على القيمة
----------------------------------
- اشرح لماذا الخاصية مهمة.
- وضّح قيمتها للعميل أو المستخدم.
- تجنب الوصف العام.

----------------------------------
قاعدة الوحدات
----------------------------------
لكل وحدة:
- title_ar
- intro_ar

يجب أن توضح المقدمة دور الوحدة في النظام.

----------------------------------
قاعدة الخصائص
----------------------------------
لكل خاصية:
- title_ar
- description_ar
- technical_implementation_ar
- additional_ideas_ar

----------------------------------
قاعدة الوصف
----------------------------------
- اشرح ماذا تفعل الخاصية ولماذا هي مهمة.
- ابقَ داخل نطاق الخاصية فقط.
- لا تضف قدرات جديدة.
- ركز على ما يفهمه العميل أو المستخدم.

----------------------------------
قاعدة التنفيذ الفني
----------------------------------
- قدم من 3 إلى 4 خطوات.
- اجعل الخطوات مفهومة لغير التقنيين.
- ركّز على سلوك النظام وتدفق العمل.
- لا تذكر تفاصيل برمجية أو معمارية.
- لا تضف وظائف جديدة.

----------------------------------
قاعدة الأفكار الإضافية
----------------------------------
- قدم من 0 إلى 1 فكرة للخصائص الأساسية فقط إذا كانت تحسن تجربة الاستخدام أو القيمة العملية بأمان.
- للخصائص الداعمة: قدم فكرة واحدة فقط إذا كانت مفيدة بوضوح.
- للخصائص الاختيارية: يفضل إرجاع قائمة فارغة.
- لا تستخدم الأفكار الإضافية لإدخال خاصية جديدة أو تغيير نطاق النظام.
- إذا لم توجد فكرة آمنة ومفيدة، أعد قائمة فارغة.

----------------------------------
قاعدة الاختصار
----------------------------------
- تجنب التكرار.
- اجعل النص واضحًا ومباشرًا.
- لا تبالغ في الشرح.

----------------------------------
السياق:
{enhanced_context}

خطة المجموعة:
{group_plan}

أعد النتيجة وفق الهيكل المطلوب فقط.
"""
functional_requirements_group_ar_template = PromptTemplate(
    template=FUNCTIONAL_REQUIREMENTS_GROUP_AR_TEMPLATE,
    input_variables=["enhanced_context", "group_plan"]
)