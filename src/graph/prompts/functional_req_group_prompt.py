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
- Avoid unnecessary low-level jargon, but remain technically clear.
- Arabic must match the English meaning and scope.
- Do not copy English text into Arabic fields.
- Do not place paragraph text inside title fields.

CONSISTENCY RULES
- Respect the exact module and feature structure provided in the group plan.
- Do not add extra modules not present in the group plan.
- Do not remove planned modules.
- Do not remove planned features.
- You may refine wording, but preserve the planned intent.

MODULE RULE
For each module:
- generate title_en and title_ar
- generate a short intro in both English and Arabic
- generate all planned features for that module

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
- technologies_used

TITLE RULES
- All titles must be short headings, not paragraphs.
- Arabic titles must be concise and professional.
- title_ar must correspond directly to title_en in meaning.
- Never repeat description text inside title_ar.

DESCRIPTION RULE
- Explain what the feature does and why it is useful.
- Keep it practical, specific, and business-friendly.
- description_ar must match description_en in meaning.

TECHNICAL IMPLEMENTATION RULE
- Provide 3 to 5 concrete implementation-oriented steps.
- Keep them realistic and sequential where possible.
- Do not make them overly code-level.
- Do not make them vague.
- technical_implementation_ar must align item-by-item with technical_implementation_en.

ADDITIONAL IDEAS RULE
- Provide 0 to 3 useful additional ideas.
- They should add business value or future extensibility.
- Do not invent unrealistic features.
- additional_ideas_ar must align item-by-item with additional_ideas_en.

TECHNOLOGIES RULE
- Use only technologies from enhanced_context.tech_stacks when clearly relevant.
- technologies_used must contain actual technologies only.
- Do not include platform keys.
- Use the smallest sufficient set.
- 1 to 3 technologies is preferred.
- 4 is allowed only when clearly justified.
- The number of technologies may vary naturally across features.
- Keep technology names in English.

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

المدخلات الواردة تأتي مسبقًا من:
1) عقدة التحضير/التحسين
2) عقدة تخطيط المتطلبات الوظيفية

الهدف
إنشاء مجموعة وظيفية كاملة تتضمن:
- عنوان المجموعة باللغة العربية
- مقدمة المجموعة باللغة العربية
- عدة وحدات فرعية
- عدة خصائص داخل كل وحدة

قواعد الكتابة
- يجب أن يكون جميع النص الناتج باللغة العربية فقط.
- يجب أن تكون العربية احترافية وطبيعية ومناسبة للأعمال.
- يجب أن يكون الأسلوب مناسبًا لوثيقة BRD موجهة للعميل.
- تجنب المصطلحات التقنية المعقدة غير الضرورية، مع الحفاظ على الوضوح.
- لا تضع نصوصًا وصفية طويلة داخل حقول العناوين.
- لا تستخدم أسلوب الترجمة الحرفية أو الصياغة الركيكة.

قواعد الالتزام بالخطة
- التزم تمامًا ببنية الوحدات والخصائص كما هي واردة في خطة المجموعة.
- لا تضف وحدات غير موجودة في خطة المجموعة.
- لا تحذف أي وحدة مخططة.
- لا تحذف أي خاصية مخططة.
- يمكنك تحسين الصياغة فقط مع الحفاظ على نفس المعنى المقصود.

قاعدة الوحدات
لكل وحدة فرعية يجب إنشاء:
- title_ar
- intro_ar
- جميع الخصائص المخططة لهذه الوحدة

قاعدة الخصائص
لكل خاصية يجب إنشاء:
- title_ar
- description_ar
- technical_implementation_ar
- additional_ideas_ar
- technologies_used

قواعد العناوين
- جميع العناوين يجب أن تكون عناوين قصيرة وليست فقرات.
- يجب أن تكون العناوين العربية موجزة واحترافية.
- لا تكرر نص الوصف داخل العنوان.
- اجعل العنوان معبرًا مباشرة عن الوظيفة.

قواعد الوصف
- وضّح ما الذي تقوم به الخاصية ولماذا هي مفيدة.
- اجعل الوصف عمليًا ومحددًا ومناسبًا للأعمال.
- تجنب العموميات غير المفيدة.

قواعد التنفيذ الفني
- قدّم من 3 إلى 5 خطوات تنفيذية عملية.
- يجب أن تكون الخطوات واقعية ومتسلسلة قدر الإمكان.
- لا تجعلها على مستوى الشفرة البرمجية التفصيلية.
- لا تجعلها مبهمة أو عامة جدًا.

قواعد الأفكار الإضافية
- قدّم من 0 إلى 3 أفكار إضافية مفيدة عند الحاجة.
- يجب أن تضيف قيمة تجارية أو توسعًا مستقبليًا منطقيًا.
- لا تضف أفكارًا غير واقعية أو غير مدعومة بالسياق.
- إذا لم توجد أفكار مناسبة، يمكن أن تكون القائمة فارغة.

قواعد التقنيات
- استخدم فقط التقنيات الواردة في enhanced_context.tech_stacks عند الحاجة الواضحة.
- يجب أن يحتوي technologies_used على أسماء تقنيات فعلية فقط.
- لا تضع مفاتيح المنصات ضمن technologies_used.
- استخدم أقل عدد كافٍ من التقنيات.
- يفضل استخدام 1 إلى 3 تقنيات.
- يسمح باستخدام 4 فقط إذا كان ذلك مبررًا بوضوح.
- قد يختلف عدد التقنيات بشكل طبيعي بين الخصائص.
- اكتب أسماء التقنيات باللغة الإنجليزية.

السياق المحسن:
{enhanced_context}

خطة المجموعة:
{group_plan}

أعد النتيجة وفق الهيكل المطلوب فقط.
"""

functional_requirements_group_ar_template = PromptTemplate(
    template=FUNCTIONAL_REQUIREMENTS_GROUP_AR_TEMPLATE,
    input_variables=["enhanced_context", "group_plan"]
)