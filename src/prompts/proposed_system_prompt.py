from langchain_core.prompts import PromptTemplate  # type: ignore

PROPOSED_SYSTEM_LOCALIZED_TEMPLATE = """
You are a senior Business Analyst and Solution Consultant.

Generate the "Proposed System" section of a Business Requirements Document (BRD) in BOTH English and Arabic.

The input already comes from a preparation/enhancement node, so you must treat it as the approved and final working context for this section.

OBJECTIVE
Describe the proposed system as a set of platform-level solution components that together form one complete solution for the client.

IMPORTANT DEFINITIONS
- In this section, a "component" means ONLY a platform-level solution channel from the platforms list.
- A component is NOT a module, feature, subsystem, integration, workflow step, department, report, or technical service.
- Examples of valid components: web admin, customer mobile app, driver app, vendor portal, backend API, customer website.
- Examples of invalid extra components: notifications module, analytics dashboard, payment gateway, reporting engine, order management, authentication service.

LANGUAGE OUTPUT REQUIREMENTS
- Generate both English and Arabic for every item.
- English and Arabic must express exactly the same meaning.
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
- Use the enhanced context exactly as provided.
- Do not reinterpret the scope beyond the enhanced context.
- Do not invent additional channels, platforms, or solution layers.

3) Business context priority
- Highest: project.details
- Then: project.desc
- Then: client.category and project.title

4) Strict platforms rule
- Read the platforms list first.
- If platforms exists and is not empty:
  - the output content list length MUST be exactly equal to the number of platform entries
  - create EXACTLY one output item for each platform entry
  - preserve the same platform coverage and the same order as the input
  - do NOT add any extra item
  - do NOT remove any platform
  - do NOT merge two platforms into one item
  - do NOT split one platform into multiple items
  - do NOT convert a platform into several modules
- If platforms is missing, null, or empty:
  - infer 2 to 5 platform-level components only
  - infer realistic core platforms only
  - do not infer modules, features, or technical layers as components

5) One-to-one platform mapping rule
- Each output item must correspond to exactly one platform entry.
- Each item should describe the business role of that platform only.
- Do not describe internal modules as if they were separate components.
- If a platform includes many capabilities, summarize them inside that platform's content instead of creating more items.

6) Platform interpretation rule
- Keep full alignment with the provided platform keys and types.
- Convert platform meaning into business-friendly titles only.
- Do not change the platform scope.
- Do not broaden the platform beyond what is reasonably implied by the input.

7) Platform naming rule
- Use professional business-facing titles.
- Titles must represent the platform itself, not a feature inside it.
- Examples:
  - web_admin -> Administrative Control Panel / لوحة التحكم الإدارية
  - customer_mobile -> Customer Mobile Application / تطبيق العميل
  - driver_mobile -> Driver Mobile Application / تطبيق السائق
  - vendor_portal -> Vendor Management Portal / بوابة إدارة الموردين
  - backend_api -> Central Integration API / الواجهة البرمجية المركزية
- Do not invent extra channels.

8) Content requirements
Each component must include:
- title_en
- content_en
- title_ar
- content_ar

Each content must:
- be 2 to 4 sentences only
- describe:
  - what this platform does
  - who primarily uses it
  - the business value it provides
- stay focused on this single platform only
- not introduce new standalone components
- not enumerate unrelated modules as separate solution parts

9) Cross-item integration rule
- All items must clearly belong to one integrated solution.
- You may mention that a platform connects with the rest of the system.
- But do not create extra integration components unless backend_api itself is explicitly a platform in the input.

10) Output discipline rule
- If the input has 3 platforms, output exactly 3 items.
- If the input has 4 platforms, output exactly 4 items.
- Never output 6, 7, or 8 items when only 3 or 4 platforms are provided.
- Platform count compliance is mandatory.

11) Quality rules
- No extra platforms
- No extra modules as standalone items
- No unsupported assumptions
- No feature decomposition into separate components
- Keep the section concise, business-friendly, and platform-bound

12) Section title
- title_en: Proposed System
- title_ar: النظام المقترح

Enhanced Context:
{enhanced_context}

Return output strictly according to the required structured schema.
"""

PROPOSED_SYSTEM_ARABIC_TEMPLATE = """
أنت محلل نظم وخبير حلول تقنية.

قم بإنشاء قسم "النظام المقترح" ضمن وثيقة تحليل متطلبات الأعمال (BRD) باللغة العربية فقط.

المدخلات تم تجهيزها مسبقًا، ويجب اعتبارها المصدر النهائي والمعتمد لهذا القسم.

الهدف
وصف النظام المقترح كمجموعة من مكونات الحل على مستوى المنصات فقط، بحيث تعمل معًا لتقديم حل رقمي متكامل للعميل.

تعريف مهم
- المقصود بـ "المكون" هنا هو منصة أو قناة رقمية واردة في حقل platforms فقط.
- المكون ليس ميزة، ولا وحدة فرعية، ولا خدمة تقنية، ولا تكاملًا، ولا تقريرًا، ولا شاشة مستقلة.
- أمثلة صحيحة: لوحة تحكم إدارية، تطبيق عميل، تطبيق سائق، بوابة موردين، واجهة برمجية مركزية.
- أمثلة غير صحيحة كمكونات مستقلة: نظام إشعارات، لوحة تقارير، بوابة دفع، إدارة الطلبات، المصادقة.

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
- استخدم البيانات المعطاة كما هي باعتبارها المصدر النهائي.
- لا تضف قنوات أو منصات أو طبقات حل غير موجودة.
- لا توسع النطاق beyond المدخلات.

3) الأولوية
- project.details أولًا
- ثم project.desc
- ثم client.category و project.title

4) القاعدة الصارمة للمنصات
- اقرأ قائمة platforms أولًا.
- إذا كانت platforms موجودة وغير فارغة:
  - يجب أن يكون عدد العناصر الناتجة مساويًا تمامًا لعدد عناصر platforms
  - أنشئ عنصرًا واحدًا فقط لكل منصة
  - حافظ على نفس الترتيب الموجود في الإدخال
  - لا تضف أي عنصر إضافي
  - لا تحذف أي منصة
  - لا تدمج منصتين في عنصر واحد
  - لا تقسّم منصة واحدة إلى أكثر من عنصر
- إذا كانت platforms غير موجودة أو فارغة:
  - استنتج من 2 إلى 5 مكونات فقط على مستوى المنصات
  - استنتج فقط المنصات الأساسية الواقعية
  - لا تعتبر الميزات أو الوحدات الداخلية مكونات مستقلة

5) قاعدة الربط واحد لواحد
- كل عنصر ناتج يجب أن يقابل منصة واحدة فقط من الإدخال.
- صف الدور التجاري لتلك المنصة فقط.
- إذا كانت المنصة تحتوي على وظائف متعددة، فاذكرها داخل وصف نفس المنصة دون إنشاء عناصر إضافية.

6) تسمية المكونات
- استخدم أسماء احترافية مناسبة للأعمال.
- يجب أن يعبر العنوان عن المنصة نفسها، وليس عن ميزة داخلها.
- لا تضف قنوات غير موجودة.

7) محتوى كل مكون
لكل مكون يجب توفير:
- title_ar
- content_ar

قواعد العنوان:
- من 3 إلى 8 كلمات
- ليس جملة
- لا يحتوي على شرح إضافي

قواعد المحتوى:
- من 2 إلى 4 جمل
- يوضح:
  - وظيفة هذه المنصة
  - المستخدمين الأساسيين لها
  - القيمة التجارية التي تقدمها
- يجب أن يظل الوصف مركزًا على هذه المنصة فقط
- لا يقدّم وحدات فرعية كمكونات مستقلة

8) التكامل
- يجب أن تعمل جميع العناصر كنظام واحد متكامل.
- يمكن الإشارة إلى ارتباط المنصة بباقي الحل.
- لكن لا تنشئ مكون تكامل مستقل إلا إذا كانت backend_api منصة موجودة صراحة في الإدخال.

9) الانضباط في العدد
- إذا كان الإدخال يحتوي على 3 منصات، أخرج 3 عناصر فقط.
- إذا كان الإدخال يحتوي على 4 منصات، أخرج 4 عناصر فقط.
- لا يجوز إخراج 6 أو 7 أو 8 عناصر إذا كان عدد المنصات أقل.
- الالتزام بعدد المنصات إلزامي.

10) الجودة
- لا تضف منصات إضافية
- لا تحول الميزات إلى مكونات مستقلة
- لا تفترض متطلبات غير مذكورة
- اجعل القسم موجزًا واحترافيًا ومرتبطًا بالمنصات فقط

11) عنوان القسم
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