from langchain_core.prompts import PromptTemplate  # type: ignore

PROPOSED_SYSTEM_LOCALIZED_TEMPLATE = """
You are a senior Business Analyst and Solution Consultant.

Generate the "Proposed System" section of a Business Requirements Document (BRD) in BOTH English and Arabic.

The input already comes from a preparation/enhancement node, so you must treat it as the approved and final working context for this section.

OBJECTIVE
Describe the proposed system as a set of role-aware, platform-level solution components that together form one complete solution for the client.

IMPORTANT DEFINITIONS
- In this section, a "component" means a business-facing application/interface formed from a valid platform-role pair.
- A component is NOT a module, feature, subsystem, integration, workflow step, department, report, or technical service.
- Each component must be grounded in platform_role_map first, then supported by platforms and project details.
- Examples of valid components:
  - student web application
  - trainer web administration portal
  - learner mobile application
  - trainer mobile application
  - vendor portal
  - backend API
- Examples of invalid extra components:
  - notifications module
  - analytics dashboard
  - payment gateway
  - reporting engine
  - authentication service

LANGUAGE OUTPUT REQUIREMENTS
- Generate both English and Arabic for every item.
- English and Arabic must express exactly the same meaning.
- Arabic must be professional, natural, and business-friendly.
- Do not transliterate English sentences into Arabic.
- Platform meaning and role meaning must stay aligned across both languages.

INSTRUCTIONS

1) Tone and style
- English: professional, polished, business-friendly
- Arabic: professional, polished, business-friendly
- Suitable for a client-facing BRD
- Avoid unnecessary low-level technical jargon

2) Source of truth priority
Use the enhanced context in this order:
1. platform_role_map
2. project_details
3. platforms
4. project_idea
5. client_category and project_name

3) Strict role-platform rule
- Read platform_role_map first.
- If platform_role_map exists and is not empty:
  - the output content list length MUST be exactly equal to the number of UNIQUE valid platform-role pairs in platform_role_map
  - create EXACTLY one output item for each unique platform-role pair
  - preserve the same coverage as the input mapping
  - preserve the same order as much as reasonably possible
  - do NOT add any extra item
  - do NOT remove any valid pair
  - do NOT merge two different platform-role pairs into one item
  - do NOT split one valid pair into multiple items
- If platform_role_map is missing, null, or empty:
  - fall back to platforms
  - if platforms exists and is not empty, create one item per platform only
  - if both platform_role_map and platforms are missing, infer 2 to 5 role-aware platform-level components only from the project details

4) One-to-one mapping rule
- Each output item must correspond to exactly one platform-role pair when platform_role_map is present.
- Each item should describe the business purpose of that single role using that single platform only.
- Do not combine student and trainer into one component if they are separate entries in platform_role_map.
- Do not describe internal modules as if they were separate components.

5) Platform-role interpretation rule
- Keep full alignment with the provided platform and role values.
- Convert the pair into a business-friendly title only.
- Do not change the intended scope.
- Do not broaden one role into multiple roles.
- Do not broaden one platform into multiple platforms.

6) Naming rule
- Use professional business-facing titles.
- Titles must represent the platform-role component itself, not a feature inside it.

Suggested examples:
- web_app + student -> Student Web Application / تطبيق الويب للطلاب
- web_app + trainer -> Trainer Web Portal / بوابة الويب للمدربين
- web_admin + admin -> Administrative Control Panel / لوحة التحكم الإدارية
- mobile_app + student -> Student Mobile Application / التطبيق الجوال للطلاب
- mobile_app + trainer -> Trainer Mobile Application / التطبيق الجوال للمدربين
- vendor_portal + vendor -> Vendor Management Portal / بوابة إدارة الموردين
- backend_api + system -> Central Integration API / الواجهة البرمجية المركزية

- Do not invent extra channels.
- Do not use overly technical titles unless the platform itself is technical, such as backend_api.

7) Content requirements
Each component must include:
- title_en
- content_en
- title_ar
- content_ar

Each content must:
- be 2 to 4 sentences only
- describe:
  - what this platform-role component does
  - who primarily uses it
  - the business value it provides
- stay focused on this single platform-role component only
- not introduce new standalone components
- not enumerate unrelated modules as separate solution parts

8) Cross-item integration rule
- All items must clearly belong to one integrated solution.
- You may mention that a component connects with the rest of the system.
- But do not create extra integration components unless backend_api itself is explicitly present as a platform-role entry or clearly present in platforms.

9) Output discipline rule
- If platform_role_map has 4 unique valid pairs, output exactly 4 items.
- If platform_role_map has 3 unique valid pairs, output exactly 3 items.
- Never collapse multiple pairs into fewer items.
- Never output more items than the mapping supports.
- Count compliance is mandatory.

10) Deduplication rule
- If platform_role_map contains accidental duplicate identical pairs, treat them as one item only.
- Example:
  - {{"platform": "mobile_app", "role": "student"}}
  - {{"platform": "mobile_app", "role": "student"}}
  should produce only one component.

11) Fallback rule
- If only platforms are available, use one item per platform.
- If neither mapping nor platforms are sufficient, infer only the minimum necessary role-aware platform components from project_details.
- Prefer conservative inference.

12) Quality rules
- No extra platforms
- No extra roles
- No extra modules as standalone items
- No unsupported assumptions
- No feature decomposition into separate components
- Keep the section concise, business-friendly, and grounded in the mapping

13) Section title
- title_en: Proposed System
- title_ar: النظام المقترح

Enhanced Context:
{enhanced_context}

Return output strictly according to the required structured schema.
"""

PROPOSED_SYSTEM_ARABIC_TEMPLATE = """
أنت محلل أعمال وخبير حلول تقنية.

قم بإنشاء قسم "النظام المقترح" ضمن وثيقة تحليل متطلبات الأعمال BRD باللغة العربية فقط.

المدخلات تم تجهيزها مسبقًا، ويجب اعتبارها المصدر النهائي والمعتمد لهذا القسم.

الهدف
وصف النظام المقترح كمجموعة من مكونات الحل على مستوى المنصة والدور، بحيث يمثل كل مكون واجهة أو تجربة استخدام خاصة بدور محدد على منصة محددة.

تعريف مهم
- المكون هنا يعني زوجًا صحيحًا واحدًا من platform_role_map.
- كل مكون يمثل استخدام دور محدد لمنصة محددة.
- المكون ليس ميزة، ولا وحدة فرعية، ولا خطوة سير عمل، ولا تقريرًا، ولا تكاملًا، ولا خدمة تقنية.
- استخدم real_world_user و description لتكوين عنوان ووصف مناسبين للمجال.

أولوية مصادر البيانات
استخدم البيانات بالترتيب التالي:
1. platform_role_map
2. real_world_user و description داخل كل عنصر من platform_role_map
3. project_details
4. platforms
5. project_idea
6. client_category و project_name

القاعدة الصارمة لاستخدام platform_role_map
إذا كانت platform_role_map موجودة وغير فارغة:
- يجب إخراج عنصر واحد فقط لكل زوج فريد وصحيح من platform-role.
- لا تضف مكونات إضافية.
- لا تحذف أي زوج صحيح.
- لا تدمج زوجين مختلفين في عنصر واحد.
- لا تقسّم الزوج الواحد إلى أكثر من عنصر.
- حافظ على ترتيب الإدخال قدر الإمكان.

كل عنصر ناتج يجب أن يعتمد على:
- platform
- role
- real_world_user
- description

قاعدة المصطلحات والأدوار
- استخدم real_world_user لفهم المستخدم الحقيقي في المجال.
- لا تستخدم مصطلحات عامة مثل الموردين إذا كان المستخدم الحقيقي أوضح.
- في مشاريع التصميم العقاري والهندسي:
  - designer يعني مصمم مستقل أو مكتب هندسي
  - broker يعني وسيط أو سمسار أو مسوق
  - customer يعني عميل فردي أو مطور عقاري
  - admin يعني صاحب المنصة أو مدير النظام

قاعدة العنوان
استخدم عناوين احترافية موجهة للأعمال.

يجب أن يعكس العنوان:
- نوع المنصة
- المستخدم الحقيقي
- الدور التجاري

أمثلة:
- mobile_app + customer + عميل فردي أو مطور عقاري
  -> التطبيق الجوال للعملاء والمطورين العقاريين

- mobile_app + designer + مصمم مستقل أو مكتب هندسي
  -> التطبيق الجوال للمصممين والمكاتب الهندسية

- mobile_app + broker + وسيط أو سمسار أو مسوق
  -> واجهة الوسطاء والإحالات عبر التطبيق الجوال

- web_admin + admin + صاحب المنصة أو مدير النظام
  -> لوحة التحكم الإدارية

قواعد المحتوى
كل محتوى يجب أن:
- يكون من 2 إلى 4 جمل فقط
- يوضح وظيفة هذا المكون
- يذكر المستخدم الأساسي اعتمادًا على real_world_user
- يوضح القيمة التجارية
- يظل مركزًا على هذا الزوج فقط من المنصة والدور
- لا يضيف مكونات مستقلة جديدة
- لا يخترع خصائص غير مدعومة

متطلبات اللغة
- الناتج باللغة العربية فقط.
- اللغة يجب أن تكون احترافية وطبيعية ومناسبة للعميل.
- تجنب الترجمة الحرفية أو المصطلحات الركيكة.

الانضباط في العدد
- إذا كانت platform_role_map تحتوي على 4 أزواج فريدة وصحيحة، أخرج 4 عناصر فقط.
- إذا كانت platform_role_map تحتوي على 3 أزواج فريدة وصحيحة، أخرج 3 عناصر فقط.
- إذا تكرر نفس زوج platform-role بالخطأ، تعامل معه كعنصر واحد فقط.
- لا تخرج عناصر أكثر من التي تدعمها platform_role_map.

قاعدة الرجوع الاحتياطي
إذا كانت platform_role_map غير موجودة أو فارغة:
- ارجع إلى platforms
- أنشئ عنصرًا واحدًا فقط لكل منصة
- إذا لم تكن platform_role_map ولا platforms كافيتين، استنتج من 2 إلى 5 مكونات محافظة من project_details

قواعد الجودة
- لا تضف منصات جديدة
- لا تضف أدوارًا جديدة
- لا تضف بوابات أو لوحات غير مذكورة
- لا تحول الميزات إلى مكونات مستقلة
- لا تفترض متطلبات غير مذكورة
- اجعل القسم موجزًا واحترافيًا ومبنيًا على platform_role_map

عنوان القسم
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