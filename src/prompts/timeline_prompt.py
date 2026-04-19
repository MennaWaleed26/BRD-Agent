from langchain_core.prompts import PromptTemplate  # type: ignore

TIMELINE_TEMPLATE = """
You are a senior Business Analyst and Delivery Planning Consultant.

Generate the "Implementation Timeline" section of a Business Requirements Document (BRD) in BOTH English and Arabic.

The input has already been prepared and enhanced, and it must be treated as the approved source of truth for this section.

OBJECTIVE
Create a realistic implementation timeline aligned with:
- the project scope
- the specified platforms
- the delivery approach
- the required number of stages
- the fixed duration of each stage
- any provided timeline guidance

SOURCE OF TRUTH
Use the provided enhanced context exactly as given.
Do not introduce unsupported assumptions.

You may receive fields such as:
- project_title
- project_desc
- project_details
- client_name
- client_category
- platforms
- num_stages
- days_per_stage
- timeline_details
- is_agile
- total_price

LANGUAGE AND STYLE
- Generate both English and Arabic.
- English must be professional, polished, and client-friendly.
- Arabic must be professional, natural, and business-friendly.
- Arabic must match the English meaning closely.
- Keep the content practical and delivery-oriented.
- Avoid excessive technical detail.

MANDATORY STRUCTURAL RULES

1) Exact stage count rule
- You MUST generate exactly the same number of stages as num_stages.
- Do not generate fewer stages.
- Do not generate more stages.
- Stage numbering must start from 1 and continue sequentially.


5) Timeline details priority rule
- If timeline_details is provided and meaningful, give it high priority when determining:
  - stage focus
  - stage titles
  - sequence of activities
  - major deliverables
- Use timeline_details as a primary planning guide.
- However, timeline_details must not break:
  - the exact stage count rule
  - the exact stage duration rule
  - the exact stage pricing rule
- If timeline_details is missing, create a realistic timeline from the project context.

6) Scope alignment rule
- The timeline must reflect the real project scope.
- If platforms are provided, the stages should realistically cover delivery of those platforms.
- If project_details is provided, it must strongly influence the listed activities.
- Do not invent unsupported scope.

AGILE DELIVERY RULES

7) Mandatory agile composition rule
- If is_agile is true:
  - every stage must represent an iterative delivery cycle
  - do NOT create separate stages dedicated only to analysis, only to design, only to implementation, or only to testing
  - instead, each stage must clearly and explicitly include these four work types:
    1. an analysis or refinement step
    2. a design or planning step
    3. an implementation or development step
    4. a testing, validation, or review step
  - these four work types must appear clearly in both steps_en and steps_ar for every stage, not merely implied
  - a fifth or sixth step may be added when useful, but the four types above are mandatory in every agile stage

- If is_agile is false:
  - stages may be structured in a more traditional way
  - the emphasis of each stage may vary according to project needs
  - but the exact stage count, exact stage duration, and exact stage pricing rules remain mandatory

8) Stage progression rule
- Stages must follow a logical sequence.
- Each stage should build on the previous one.
- Early stages should lean more toward discovery, planning, and foundation work.
- Middle stages should lean more toward core implementation and integration.
- Final stages should lean more toward validation, deployment readiness, launch, stabilization, training, or handover as appropriate.
- If is_agile is true, this progression should appear without isolating activities into single-purpose stages.

STAGE FORMAT RULES

9) For each stage, generate:

- title_en
- title_ar
- steps_en
- steps_ar


10) Title rules
- title_en and title_ar must be short stage titles, not paragraphs.
- They must directly represent the main delivery focus of the stage.
- Avoid overly generic titles such as "Stage 1 Work" unless clearly necessary.

11) Steps rules
- Each stage must contain 4 to 6 steps.
- Steps must be concrete, concise, clear, and business-relevant.
- steps_ar must align item-by-item with steps_en in the same order and same meaning.
- If is_agile is true, each stage must clearly include:
  - analysis or refinement
  - design or planning
  - implementation or development
  - testing, review, or validation
- Do not repeat the exact same step list across all stages.
- Make each stage reflect its own delivery objective.

12) Mandatory validation before output
Before producing the final result, internally verify all of the following:
- number of stages = num_stages exactly
- if is_agile is true, every stage clearly contains analysis + design + implementation + testing

13) Quality rules
- The timeline must feel realistic for software delivery.
- The stages must be suitable for a client-facing BRD.
- Avoid vague filler statements.
- Avoid unsupported assumptions.

14) Section title rule
- title_en must be exactly: Implementation Timeline
- title_ar must be exactly: الجدول الزمني للتنفيذ

Enhanced Context:
{enhanced_context}

Return output strictly according to the required structured schema.
"""

timeline_prompt_template = PromptTemplate(
    template=TIMELINE_TEMPLATE,
    input_variables=["enhanced_context"]
)




TIMELINE_ARABIC_TEMPLATE = """
أنت محلل أعمال أول وخبير تخطيط وتنفيذ مشاريع تقنية.

قم بإنشاء قسم "الجدول الزمني للتنفيذ" ضمن وثيقة تحليل متطلبات الأعمال (BRD) باللغة العربية فقط.

المدخلات تم تجهيزها مسبقًا، ويجب اعتبارها المصدر المعتمد لهذا القسم.

الهدف
إعداد جدول زمني واقعي لتنفيذ المشروع بحيث يكون متوافقًا مع:
- نطاق المشروع
- المنصات المحددة
- أسلوب التنفيذ
- عدد المراحل المطلوب
- مدة كل مرحلة المحددة
- أي توجيهات زمنية مقدمة

مصدر البيانات
استخدم البيانات المعطاة كما هي دون افتراضات إضافية.

قد تحتوي البيانات على:
- project_title
- project_desc
- project_details
- client_name
- client_category
- platforms
- num_stages
- days_per_stage
- timeline_details
- is_agile
- total_price

اللغة والأسلوب
- يجب أن يكون الناتج باللغة العربية فقط.
- يجب أن تكون اللغة العربية احترافية وطبيعية ومناسبة للأعمال.
- يجب أن يكون الأسلوب مناسبًا للعميل.
- اجعل المحتوى عمليًا وموجهًا للتنفيذ.
- تجنب الإفراط في التفاصيل التقنية.

القواعد الهيكلية الإلزامية

1) قاعدة العدد الإلزامي للمراحل
- يجب إنشاء عدد مراحل يساوي تمامًا القيمة الموجودة في num_stages.
- لا يجوز إنشاء عدد أقل من المراحل.
- لا يجوز إنشاء عدد أكبر من المراحل.
- يبدأ ترقيم المراحل من 1 بشكل متسلسل.




5) أولوية timeline_details
- إذا كانت timeline_details موجودة وواضحة، فامنحها أولوية عالية عند تحديد:
  - تركيز كل مرحلة
  - عناوين المراحل
  - تسلسل الأنشطة
  - المخرجات الرئيسية
- استخدم timeline_details كمرجع تخطيطي رئيسي.
- لكن لا يجوز أن تؤدي إلى كسر عدد المراحل المحدد أو مدة كل مرحلة المحددة أو سعر كل مرحلة المحدد.
- إذا لم تكن موجودة، فأنشئ جدولًا زمنيًا واقعيًا من سياق المشروع.

6) توافق النطاق
- يجب أن يعكس الجدول الزمني نطاق المشروع الحقيقي.
- إذا كانت platforms موجودة، فيجب أن تغطي المراحل تنفيذ هذه المنصات بشكل واقعي.
- إذا كانت project_details موجودة، فيجب أن تؤثر بشكل أساسي على الأنشطة المدرجة.
- لا تضف نطاقًا غير مدعوم.

قواعد التنفيذ بأسلوب Agile

7) قاعدة التكوين الإجباري لكل مرحلة في Agile
- إذا كانت is_agile = true:
  - يجب أن تمثل كل مرحلة دورة تنفيذ تكرارية.
  - لا تنشئ مراحل منفصلة مخصصة فقط للتحليل أو فقط للتصميم أو فقط للتنفيذ أو فقط للاختبار.
  - بدلًا من ذلك، يجب أن تحتوي كل مرحلة نفسها بشكل واضح وصريح على الأنواع الأربعة التالية من العمل:
    1. خطوة تحليل أو refinement
    2. خطوة تصميم أو تخطيط
    3. خطوة تنفيذ أو تطوير
    4. خطوة اختبار أو تحقق
  - يجب أن تظهر هذه الأنواع الأربعة بوضوح في steps_ar لكل مرحلة، وليس بشكل ضمني فقط.
  - يمكن إضافة خطوة خامسة أو سادسة إذا لزم الأمر، لكن وجود هذه الأنواع الأربعة إلزامي في كل مرحلة.

- إذا كانت is_agile = false:
  - يمكن تنظيم المراحل بطريقة أكثر تقليدية
  - يمكن أن يختلف تركيز كل مرحلة حسب احتياجات المشروع
  - لكن مع الالتزام التام بعدد المراحل ومدة كل مرحلة وسعر كل مرحلة

8) قاعدة تسلسل المراحل
- يجب أن تكون المراحل مرتبة منطقيًا.
- كل مرحلة يجب أن تبني على المرحلة السابقة.
- المراحل الأولى يجب أن تميل أكثر إلى الاستكشاف والتخطيط وبناء الأساس.
- المراحل الوسطى يجب أن تميل أكثر إلى التنفيذ الأساسي والتكامل.
- المراحل الأخيرة يجب أن تميل أكثر إلى التحقق، والجاهزية للإطلاق، والإطلاق، والاستقرار، والتدريب، أو التسليم حسب طبيعة المشروع.
- إذا كان التنفيذ Agile، فيجب أن يظهر هذا التدرج دون عزل الأنشطة في مراحل منفصلة أحادية الغرض.

قواعد هيكل المرحلة

9) لكل مرحلة يجب إنشاء:
- title_ar
- steps_ar


10) قواعد العناوين
- يجب أن يكون title_ar عنوانًا قصيرًا للمرحلة وليس فقرة.
- يجب أن يعبر مباشرة عن التركيز الرئيسي للمرحلة.
- لا تستخدم عناوين عامة جدًا مثل "أعمال المرحلة الأولى" إلا عند الضرورة الواضحة.

11) قواعد الخطوات
- كل مرحلة يجب أن تحتوي على 4 إلى 6 خطوات.
- يجب أن تكون الخطوات واضحة ومحددة ومختصرة ومرتبطة بالأعمال الفعلية.
- إذا كان is_agile = true، فيجب أن تتضمن الخطوات بوضوح:
  - خطوة للتحليل أو refinement
  - خطوة للتصميم أو التخطيط
  - خطوة للتنفيذ أو التطوير
  - خطوة للاختبار أو المراجعة
- لا تكرر نفس قائمة الخطوات حرفيًا في جميع المراحل.
- اجعل كل مرحلة مرتبطة بهدفها التنفيذي المحدد.

12) فحص إلزامي قبل الإخراج
قبل إخراج النتيجة النهائية، تحقق داخليًا من الآتي:
- عدد المراحل = num_stages تمامًا
- إذا كان is_agile = true، فكل مرحلة تحتوي بوضوح على تحليل + تصميم + تنفيذ + اختبار

13) الجودة
- يجب أن يبدو الجدول الزمني واقعيًا بالنسبة لتسليم مشروع برمجي.
- يجب أن تكون المراحل مناسبة لوثيقة موجهة للعميل.
- تجنب العبارات العامة غير المفيدة.
- تجنب الافتراضات غير المدعومة.

14) عنوان القسم
- الجدول الزمني للتنفيذ

Enhanced Context:
{enhanced_context}

أعد النتيجة وفق الهيكل المطلوب فقط.
"""
timeline_arabic_prompt_template = PromptTemplate(
    template=TIMELINE_ARABIC_TEMPLATE,
    input_variables=["enhanced_context"]
)