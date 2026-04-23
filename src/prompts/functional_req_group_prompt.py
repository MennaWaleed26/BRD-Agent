from langchain_core.prompts import PromptTemplate  # type: ignore


FUNCTIONAL_REQUIREMENTS_GROUP_TEMPLATE = """
You are a senior Business Analyst and Solution Architect.

Generate one grouped part of the "Detailed Functional Units" section of a Business Requirements Document (BRD) in BOTH English and Arabic.

The input already comes from:
1) a preparation/enhancement node
2) a functional requirements planning node

OBJECTIVE
Generate one complete functional group containing:
- group title in English and Arabic
- group intro in English and Arabic
- multiple modules
- multiple features inside each module

WRITING RULES
- Generate both English and Arabic for all textual fields.
- English must be professional, polished, and business-friendly.
- Arabic must be professional, natural, and business-friendly.
- Keep the writing suitable for a client-facing BRD.
- Avoid unnecessary low-level jargon.
- Arabic must match the English meaning (not literal translation).
- Do not place paragraph text inside title fields.

CLIENT-FOCUSED INTELLIGENCE RULE
- Always explain features in a way that highlights their value to the client or end user.
- Clearly communicate WHY the feature exists, not only WHAT it does.
- When relevant, briefly indicate how the feature improves usability, efficiency, revenue, or user engagement.

REAL-WORLD BEHAVIOR RULE
- Reflect realistic system behavior where applicable.
- Include practical scenarios such as delays, failures, user mistakes, or alternative flows when relevant.
- Avoid purely ideal or static descriptions.

CONSISTENCY RULES
- Respect the exact module and feature structure provided in the group plan.
- Do not add or remove modules/features.
- You may refine wording, but preserve intent.

DOMAIN ADAPTATION RULES
- Adapt content to the actual project category and product behavior.
- Do not force business-management patterns unless supported.
- Keep domain language natural and specific.

PRODUCT BEHAVIOR RULE
- The output must reflect real product behavior, not generic system templates.

CONCISENESS RULE
- Avoid repeating the same idea in multiple sentences.
- Prefer clear and direct explanations over extended elaboration.
- Keep descriptions informative but not verbose.

VARIETY RULE
- Avoid repeating the same explanation phrases across features.
- Use varied wording while keeping clarity and professionalism.

USER JOURNEY DEPTH RULE
- For client-facing features, ensure the description reflects actual user interaction steps and system responses.
- Avoid generic UI descriptions; focus on real usage scenarios.

MODULE RULE
For each module:
- generate title_en and title_ar
- generate a short intro in both English and Arabic
- ensure intro explains the role of the module in the overall system

FEATURE RULE
For each feature, generate:
- title_en
- title_ar
- description_en
- description_ar
- technical_implementation_en
- technical_implementation_ar
- additional_ideas_en
- additional_ideas_ar

DESCRIPTION RULE
- Explain what the feature does AND why it matters.
- Keep it clear, practical, and client-friendly.
- Avoid vague or generic descriptions.

TECHNICAL IMPLEMENTATION RULE
- Provide 3 to 5 structured steps.
- Keep them implementation-aware but NOT developer-level.
- Focus on system behavior and logic, not code.
- For core features → more clarity
- For optional features → lighter detail

ADDITIONAL IDEAS RULE
- Provide 0 to 3 meaningful enhancements.
- Only include ideas that realistically add value.


EXPLANATION BALANCE RULE
- Avoid being too generic.
- Avoid being too technical.
- Aim for “client-understandable but system-aware” explanation level.

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

الهدف
إنشاء مجموعة وظيفية كاملة تتضمن:
- عنوان المجموعة
- مقدمة المجموعة
- عدة وحدات
- عدة خصائص داخل كل وحدة

قواعد الكتابة
- يجب أن تكون اللغة العربية احترافية وطبيعية ومناسبة للعميل.
- يجب أن تكون الصياغة واضحة وسهلة الفهم لغير التقنيين.
- تجنب المصطلحات التقنية المعقدة غير الضرورية.
- لا تستخدم ترجمة حرفية، بل صياغة طبيعية تعكس المعنى.
- النص موجه للعميل وليس للمطور.

قاعدة التركيز على القيمة (CLIENT-FOCUSED INTELLIGENCE)
- يجب توضيح قيمة كل خاصية للعميل أو المستخدم النهائي.
- لا تكتفِ بشرح ما تفعله الخاصية، بل وضّح لماذا هي مهمة.
- يمكن الإشارة إلى تأثيرها على تجربة المستخدم أو الكفاءة أو الإيرادات عند الحاجة.

قاعدة السلوك الواقعي للنظام (REAL-WORLD BEHAVIOR)
- يجب أن يعكس الوصف سلوك النظام في الواقع.
- عند الحاجة، أشر إلى حالات مثل التأخير أو الأخطاء أو البدائل.
- تجنب الوصف المثالي أو النظري فقط.

قاعدة الالتزام بالخطة (CONSISTENCY)
- التزم تمامًا ببنية الوحدات والخصائص كما وردت في خطة المجموعة.
- لا تضف أو تحذف عناصر.
- يمكنك تحسين الصياغة فقط مع الحفاظ على نفس المعنى.

قاعدة التكيف مع المجال (DOMAIN ADAPTATION)
- صِغ المحتوى بما يتناسب مع نوع المشروع وسلوك المنتج.
- لا تفرض أنماط أنظمة إدارية أو تجارية إلا إذا كانت مدعومة بالسياق.

قاعدة سلوك المنتج (PRODUCT BEHAVIOR)
- يجب أن يعكس الوصف سلوك منتج حقيقي، وليس قالبًا عامًا لأنظمة تقليدية.

قاعدة الاختصار (CONCISENESS)
- تجنب تكرار نفس الفكرة في أكثر من جملة.
- استخدم صياغة مباشرة وواضحة.
- اجعل الوصف مختصرًا لكنه غني بالمعلومة.

قاعدة التنويع (VARIETY)
- تجنب تكرار نفس العبارات التفسيرية بين الخصائص.
- استخدم تنوعًا في الصياغة مع الحفاظ على الوضوح والاحترافية.

قاعدة عمق رحلة المستخدم (USER JOURNEY DEPTH)
- في الخصائص الموجهة للمستخدم، وضّح خطوات التفاعل الفعلي مع النظام.
- ركّز على ما يحدث أثناء الاستخدام وليس فقط الشكل أو الواجهة.
- تجنب الوصف العام لواجهة المستخدم.

قاعدة شرح القرارات (DECISION EXPLANATION)
- إذا كانت الخاصية تتضمن حسابات أو قرارات من النظام، وضّح بشكل مبسط العوامل المؤثرة فيها.
- اجعل الشرح مفهومًا لغير التقنيين.

قاعدة الوحدات
لكل وحدة:
- title_ar
- intro_ar (يجب أن يوضح دور الوحدة داخل النظام بشكل واضح)

قاعدة الخصائص
لكل خاصية:
- title_ar
- description_ar
- technical_implementation_ar
- additional_ideas_ar

قاعدة الوصف
- اشرح ما الذي تقوم به الخاصية ولماذا هي مهمة.
- اجعل الوصف عمليًا ومرتبطًا باستخدام فعلي.
- تجنب العبارات العامة أو غير المحددة.

قاعدة التنفيذ الفني
- قدم من 3 إلى 5 خطوات واضحة.
- ركّز على منطق النظام وسلوكه، وليس على تفاصيل برمجية.
- اجعل المستوى مناسبًا لفهم العميل.

قاعدة الأفكار الإضافية
- قدم من 0 إلى 3 أفكار فقط.
- يجب أن تضيف قيمة حقيقية للنظام.


قاعدة التوازن
- لا تجعل الوصف عامًا جدًا.
- ولا تقنيًا بشكل زائد.
- الهدف: شرح واضح + فهم لسلوك النظام + مناسب للعميل.

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