from langchain_core.prompts import PromptTemplate  # type: ignore

from langchain_core.prompts import PromptTemplate  # type: ignore

TIMELINE_TEMPLATE = """
You are a senior Business Analyst and Delivery Planning Consultant.

Generate the "Implementation Timeline" section of a Business Requirements Document (BRD) in BOTH English and Arabic.

The input already comes from a preparation/enhancement node, so you must treat it as the approved working context for this section.

OBJECTIVE
Create a realistic implementation timeline that is aligned with:
- the project scope
- the provided platforms
- the delivery approach
- the required number of stages
- the fixed duration of each stage
- any provided timeline guidance

SOURCE OF TRUTH
Use the enhanced context exactly as provided.

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
- Arabic must express the same meaning as English.
- Keep the content practical and delivery-oriented.
- Avoid excessive technical detail.

CRITICAL STRUCTURE RULES

1) Exact stage count rule
- You MUST generate exactly the same number of stages as num_stages.
- Do not generate fewer stages.
- Do not generate more stages.
- Stage numbering must start from 1 and continue sequentially.

2) Exact stage duration rule
- Each stage MUST have the same duration count equal to constraints.deadline.days_per_stage.
- All stages must use the same duration type: days.
- duration_count for every stage must equal days_per_stage exactly.
- duration_en for every stage must be a readable English string such as "20 days".
- duration_ar for every stage must be a readable Arabic string such as "20 أيام".
- duration_type_en must be exactly "days".
- duration_type_ar must be exactly "أيام".

3) Total timeline rule
- The total timeline is fixed by:
  num_stages × days_per_stage
- Do not exceed it.
- Do not shorten it.
- The generated stages must fully comply with this fixed structure.

4) Timeline details priority rule
- If timeline_details is provided and meaningful, give it high priority when determining:
  - stage focus
  - stage titles
  - sequence of activities
  - major deliverables
- Use timeline_details as a strong planning guide.
- However, timeline_details must not break the exact stage count rule or exact stage duration rule.
- If timeline_details is missing, create a realistic timeline from the project context.

5) Scope alignment rule
- The timeline must reflect the actual project scope.
- If platforms are provided, the stages should realistically cover the delivery of those platforms.
- If project_details is provided, it must strongly influence the listed activities.
- Do not invent unsupported scope.

AGILE DELIVERY RULES

6) Agile stage composition rule
- If is_agile is true:
  - every stage must represent an agile delivery cycle or sprint-like stage
  - DO NOT create separate dedicated stages only for analysis, only for design, only for implementation, or only for testing
  - instead, each stage should include a practical mix of:
    - analysis or refinement
    - design or solution planning
    - implementation
    - testing or validation
  - each stage should still have a clear delivery focus and meaningful output
  - stages should show iterative progress across the project

- If is_agile is false:
  - you may structure stages in a more traditional manner
  - stages may emphasize different delivery activities depending on project needs
  - but still keep the exact stage count and exact stage duration

7) Stage progression rule
- Stages must follow a logical order.
- Each stage should build on the previous one.
- Early stages should focus more on discovery, planning, and foundation work.
- Middle stages should focus more on core implementation and integration.
- Final stages should focus more on validation, deployment readiness, launch, stabilization, training, or handover as appropriate.
- If agile is true, these emphases should exist without isolating activities into separate single-purpose stages.

PHASE/STAGE FORMAT RULES

8) For each stage, generate:
- phase_number
- title_en
- title_ar
- duration_count
- duration_type_en
- duration_type_ar
- steps_en
- steps_ar
- price

9) Title rules
- title_en and title_ar must be short stage titles, not paragraphs.
- They must represent the main delivery focus of the stage.
- They must not be generic labels like "Stage 1 Work" unless strongly necessary.

10) Steps rules
- Each stage must contain 4 to 6 steps.
- Steps must be concrete, concise, and business-relevant.
- steps_ar must align item-by-item with steps_en in the same order and same meaning.
- If agile is true, each stage's steps should collectively reflect an iterative mini-cycle including analysis/refinement, design/planning, implementation, and testing/review.
- Do not repeat identical step lists across all stages.
- Keep each stage focused on its specific delivery objective.

11) Pricing awareness rule
- If total_price is provided, use it as the authoritative project budget.
- Distribute the budget evenly across all project stages unless explicit stage pricing is already defined.
- Each stage price MUST be calculated as:
  stage_price = total_price / number_of_stages
- Do not invent arbitrary pricing logic or unequal distributions unless the context explicitly specifies different stage costs.


12) Quality rules
- The timeline must feel realistic for software delivery.
- The stages must be suitable for a client-facing BRD.
- Avoid vague filler statements.
- Avoid unsupported assumptions.

13) Section title
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

2) قاعدة مدة كل مرحلة
- يجب أن تكون مدة كل مرحلة مساوية تمامًا للقيمة الموجودة في days_per_stage.
- جميع المراحل تستخدم نفس وحدة الزمن وهي الأيام.
- يجب أن تكون duration_count لكل مرحلة مساوية لـ days_per_stage تمامًا.
- يجب أن تكون duration_type_ar = "أيام".
- ممنوع استخدام أي قيمة مختلفة عن days_per_stage لأي مرحلة.

3) قاعدة السعر لكل مرحلة
- إذا كانت total_price موجودة، فيجب اعتبارها الميزانية الإجمالية المعتمدة للمشروع.
- يجب حساب سعر كل مرحلة كما يلي:
  price = total_price / num_stages
- يجب أن يكون سعر كل مرحلة مساويًا تمامًا لهذه القيمة.
- لا يجوز استخدام أي توزيع مختلف إلا إذا كانت البيانات تحتوي صراحة على أسعار مرحلية مختلفة.
- إذا لم توجد أسعار مرحلية صريحة، فجميع المراحل لها نفس السعر.

4) قاعدة المدة الإجمالية
- المدة الإجمالية ثابتة وتحسب كالتالي:
  num_stages × days_per_stage
- لا يجوز تجاوزها.
- لا يجوز تقليلها.
- يجب أن يلتزم الجدول الزمني الناتج بهذه البنية الإلزامية بالكامل.

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
- phase_number
- title_ar
- duration_count
- duration_type_ar
- steps_ar
- price

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
- duration_count في كل مرحلة = days_per_stage تمامًا
- duration_type_ar في كل مرحلة = "أيام"
- price في كل مرحلة = total_price / num_stages تمامًا
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