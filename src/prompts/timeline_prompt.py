from langchain_core.prompts import PromptTemplate  # type: ignore

TIMELINE_TEMPLATE = """
You are a senior Business Analyst and Delivery Planning Consultant.

Generate the "Implementation Timeline" section of a Business Requirements Document (BRD) in BOTH English and Arabic.

The input has already been prepared and enhanced, and it must be treated as the approved source of truth for this section.

----------------------------------
OBJECTIVE
----------------------------------
Create a realistic implementation timeline aligned with:
- the project scope
- the specified platforms
- the delivery approach
- the required number of stages
- any provided timeline guidance

----------------------------------
SOURCE OF TRUTH
----------------------------------
Use the provided enhanced context exactly as given.
Do not introduce unsupported assumptions.

You may receive:
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
- timeline_error

----------------------------------
ERROR CORRECTION RULE (NEW – MATCH ARABIC)
----------------------------------
- If timeline_error exists and is not empty:
  - it represents a validation failure from a previous attempt
  - you MUST treat it as a mandatory correction note
  - you MUST regenerate the entire timeline after fixing the issue
  - you MUST NOT repeat the same error
  - error correction must be fully applied without breaking other rules

----------------------------------
LANGUAGE AND STYLE
----------------------------------
- Generate both English and Arabic
- English must be professional and client-friendly
- Arabic must be natural, professional, and business-oriented
- Arabic must match the English meaning closely
- Avoid excessive technical detail
- Keep content practical and delivery-oriented

----------------------------------
MANDATORY STRUCTURAL RULES
----------------------------------

1) Exact stage count rule
- You MUST generate exactly num_stages
- Do NOT generate fewer or more
- Numbering must start from 1 and be sequential

----------------------------------

2) Timeline details priority rule
- If timeline_details is provided:
  - use it as primary guidance for:
    - stage focus
    - stage titles
    - sequence of activities
- It must NOT break:
  - stage count rule

----------------------------------

3) Scope alignment rule
- Timeline must reflect actual project scope
- If platforms exist:
  - stages must realistically cover platform delivery
- If project_details exist:
  - they must strongly influence activities
- Do NOT invent scope

----------------------------------
AGILE DELIVERY RULES
----------------------------------

4) Mandatory agile composition rule
If is_agile = true:
- each stage MUST include ALL:
  1. analysis/refinement
  2. design/planning
  3. implementation/development
  4. testing/review

- These must appear clearly in BOTH:
  - steps_en
  - steps_ar

- You may add extra steps, but these four are mandatory

If is_agile = false:
- stages may vary in focus
- but must still respect structure rules

----------------------------------

5) Stage progression rule
- Stages must follow a logical flow
- Each stage builds on previous

- Early stages → discovery, planning
- Middle stages → implementation, integration
- Final stages → validation, readiness, launch, stabilization

- In Agile, this progression must appear WITHOUT isolating work types

----------------------------------
STAGE FORMAT RULES
----------------------------------

6) For each stage generate:
- title_en
- title_ar
- steps_en
- steps_ar

----------------------------------

7) Title rules
- Titles must be short
- Must reflect stage focus clearly
- Avoid generic titles

----------------------------------

8) Steps rules
- Each stage must have 4–6 steps
- Steps must be:
  - clear
  - concise
  - business-relevant

- steps_ar must match steps_en line-by-line

- If Agile:
  each stage MUST include:
  - analysis
  - design
  - implementation
  - testing

- Do NOT repeat identical steps across stages

----------------------------------

9) Mandatory validation before output
Before generating final result:
- verify stage count = num_stages
- if is_agile = true:
  every stage includes:
    analysis + design + implementation + testing

- if timeline_error exists:
  ensure it is fully resolved

----------------------------------

10) Quality rules
- Timeline must be realistic
- Suitable for client-facing BRD
- Avoid vague or filler content
- Avoid unsupported assumptions

----------------------------------

11) Section title
- title_en: Implementation Timeline
- title_ar: الجدول الزمني للتنفيذ

----------------------------------

Enhanced Context:
{enhanced_context}

----------------------------------

Validation Error From Previous Attempt:
{timeline_error}

----------------------------------

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
- timeline_error

تعليمات تصحيح الإخراج السابق
- إذا كانت timeline_error موجودة وغير فارغة، فهذا يعني أن المحاولة السابقة فشلت في التحقق.
- في هذه الحالة، اعتبر timeline_error ملاحظة تصحيح إلزامية يجب معالجتها بالكامل في هذه المحاولة.
- أعد إنشاء القسم بالكامل بعد تصحيح الخطأ المذكور.
- لا تكرر نفس الخطأ السابق.
- يجب أن يكون تصحيح الخطأ جزءًا أساسيًا من هذه المحاولة دون الإخلال بباقي القواعد.

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
- يبدأ ترتيب المراحل من 1 بشكل متسلسل.

2) أولوية timeline_details
- إذا كانت timeline_details موجودة وواضحة، فامنحها أولوية عالية عند تحديد:
  - تركيز كل مرحلة
  - عناوين المراحل
  - تسلسل الأنشطة
  - المخرجات الرئيسية
- استخدم timeline_details كمرجع تخطيطي رئيسي.
- إذا لم تكن موجودة، فأنشئ جدولًا زمنيًا واقعيًا من سياق المشروع.
- لا يجوز أن تؤدي timeline_details إلى كسر عدد المراحل المطلوب.

3) توافق النطاق
- يجب أن يعكس الجدول الزمني نطاق المشروع الحقيقي.
- إذا كانت platforms موجودة، فيجب أن تغطي المراحل تنفيذ هذه المنصات بشكل واقعي.
- إذا كانت project_details موجودة، فيجب أن تؤثر بشكل أساسي على الأنشطة المدرجة.
- لا تضف نطاقًا غير مدعوم.

قواعد التنفيذ بأسلوب Agile

4) قاعدة التكوين الإجباري لكل مرحلة في Agile
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
  - لكن مع الالتزام التام بعدد المراحل المطلوب

5) قاعدة تسلسل المراحل
- يجب أن تكون المراحل مرتبة منطقيًا.
- كل مرحلة يجب أن تبني على المرحلة السابقة.
- المراحل الأولى يجب أن تميل أكثر إلى الاستكشاف والتخطيط وبناء الأساس.
- المراحل الوسطى يجب أن تميل أكثر إلى التنفيذ الأساسي والتكامل.
- المراحل الأخيرة يجب أن تميل أكثر إلى التحقق، والجاهزية للإطلاق، والإطلاق، والاستقرار، والتدريب، أو التسليم حسب طبيعة المشروع.
- إذا كان التنفيذ Agile، فيجب أن يظهر هذا التدرج دون عزل الأنشطة في مراحل منفصلة أحادية الغرض.

قواعد هيكل المرحلة

6) لكل مرحلة يجب إنشاء:
- title_ar
- steps_ar

7) قواعد العناوين
- يجب أن يكون title_ar عنوانًا قصيرًا للمرحلة وليس فقرة.
- يجب أن يعبر مباشرة عن التركيز الرئيسي للمرحلة.
- لا تستخدم عناوين عامة جدًا مثل "أعمال المرحلة الأولى" إلا عند الضرورة الواضحة.

8) قواعد الخطوات
- كل مرحلة يجب أن تحتوي على 4 إلى 6 خطوات.
- يجب أن تكون الخطوات واضحة ومحددة ومختصرة ومرتبطة بالأعمال الفعلية.
- إذا كان is_agile = true، فيجب أن تتضمن الخطوات بوضوح:
  - خطوة للتحليل أو refinement
  - خطوة للتصميم أو التخطيط
  - خطوة للتنفيذ أو التطوير
  - خطوة للاختبار أو المراجعة
- لا تكرر نفس قائمة الخطوات حرفيًا في جميع المراحل.
- اجعل كل مرحلة مرتبطة بهدفها التنفيذي المحدد.

9) فحص إلزامي قبل الإخراج
قبل إخراج النتيجة النهائية، تحقق داخليًا من الآتي:
- عدد المراحل = num_stages تمامًا
- إذا كان is_agile = true، فكل مرحلة تحتوي بوضوح على تحليل + تصميم + تنفيذ + اختبار
- إذا كانت timeline_error موجودة، فقد تم تصحيحها بالكامل في هذه المحاولة

10) الجودة
- يجب أن يبدو الجدول الزمني واقعيًا بالنسبة لتسليم مشروع برمجي.
- يجب أن تكون المراحل مناسبة لوثيقة موجهة للعميل.
- تجنب العبارات العامة غير المفيدة.
- تجنب الافتراضات غير المدعومة.

11) عنوان القسم
- الجدول الزمني للتنفيذ

Enhanced Context:
{enhanced_context}

Validation Error From Previous Attempt:
{timeline_error}

أعد النتيجة وفق الهيكل المطلوب فقط.
"""

timeline_arabic_prompt_template = PromptTemplate(
    template=TIMELINE_ARABIC_TEMPLATE,
    input_variables=["enhanced_context","timeline_error"]
)