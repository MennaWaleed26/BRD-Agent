from langchain_core.prompts import PromptTemplate  # type: ignore

TIMELINE_TEMPLATE = """
You are a senior Business Analyst and Delivery Planning Consultant.

Generate the "Implementation Timeline" section of a Business Requirements Document (BRD) in BOTH English and Arabic.

The input already comes from a preparation/enhancement node, so you must treat it as the approved working context for this section.

OBJECTIVE
Create a realistic project implementation timeline that is aligned with:
- the project scope
- the provided platforms
- the delivery approach
- the total allowed deadline

SOURCE OF TRUTH
Use the enhanced context exactly as provided.
Field names in the context may include:
- project_name
- project_idea
- project_details
- client_name
- client_category
- platforms
- tech_stacks
- is_agile
- deadline_count
- deadline_type

CORE RULES

1) Language and tone
- Generate both English and Arabic.
- English must be professional, polished, and client-friendly.
- Arabic must be professional, natural, and business-friendly.
- Keep the content practical and delivery-oriented.
- Arabic must not copy English text.
- Arabic must express the same meaning as English.

2) Deadline rule
- The full timeline must exactly match the provided deadline_count and deadline_type.
- The sum of all phase durations must equal the total project deadline.
- Do not exceed the deadline.
- Do not produce a shorter total duration than the deadline.
- Use the same duration_type provided in the context for all phases.
- If deadline_type is "days", all phase durations must be in days.
- If deadline_type is "weeks", all phase durations must be in weeks.

3) Agile rule
- If is_agile is true:
  - structure the timeline into phases with equal durations as much as reasonably possible
  - create realistic agile delivery stages that fit iterative implementation
  - phases should represent meaningful delivery progress such as discovery, backend foundation, mobile development, admin/dashboard development, testing, deployment, stabilization, or similar
  - the number of phases should remain realistic
- If is_agile is false:
  - you may use unequal phase durations
  - allocate time according to realistic workload and delivery dependencies
  - use a traditional phased delivery structure

4) Phase count rule
- Generate a realistic number of phases.
- Prefer between 2 and 6 phases.
- Do not create too many tiny phases.
- Do not create one single large phase.
- Each phase must have enough meaningful work.

5) Scope alignment rule
- The timeline must reflect the actual project scope.
- If platforms are provided, the phases should realistically cover the implementation of those platforms.
- If project_details are provided, they must strongly influence the listed steps.
- Include realistic implementation activities such as:
  - analysis and planning
  - design
  - backend/API development
  - platform-specific development
  - integration
  - testing
  - deployment
  - post-launch support
- Do not include unsupported or invented scope.

6) Phase format rule
For each phase, generate:
- phase_number
- title_en
- title_ar
- duration_en
- duration_ar
- duration_count
- duration_type_en
- duration_type_ar
- steps_en
- steps_ar

7) Duration formatting rule
- duration_en must be written exactly as a readable English string such as:
  - "2 weeks"
  - "10 days"
- duration_ar must be written as a readable Arabic string such as:
  - "أسبوعان"
  - "10 أيام"
- duration_count must be numeric only.
- duration_type_en must be either "days" or "weeks".
- duration_type_ar must be either "أيام" or "أسابيع".

8) Steps rule
- Each phase must contain a realistic list of concrete activities or deliverables.
- Prefer 4 to 6 steps per phase.
- Keep steps specific, concise, and business-relevant.
- Do not repeat the same step across phases unless clearly necessary.
- steps_ar must align item-by-item with steps_en in the same order and same meaning.

9) Title rules
- title_en and title_ar must be short phase titles, not paragraphs.
- title_ar must be a concise Arabic title, not a sentence-long explanation.
- Do not place steps or descriptive paragraph text inside title_ar.
- title_ar must correspond directly in meaning to title_en.

10) Quality rules
- The timeline must feel realistic for software delivery.
- The phases must follow a logical order.
- The content must be suitable for a client-facing BRD.
- Avoid vague filler statements.
- Avoid excessive technical detail.

11) Section title
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

from langchain_core.prompts import PromptTemplate  # type: ignore


TIMELINE_ARABIC_TEMPLATE = """
أنت محلل أعمال أول وخبير تخطيط وتنفيذ مشاريع تقنية.

قم بإنشاء قسم "الجدول الزمني للتنفيذ" ضمن وثيقة تحليل متطلبات الأعمال (BRD) باللغة العربية فقط.

المدخلات تم تجهيزها مسبقًا، ويجب اعتبارها المصدر المعتمد لهذا القسم.

الهدف
إعداد جدول زمني واقعي لتنفيذ المشروع بحيث يكون متوافقًا مع:
- نطاق المشروع
- المنصات المحددة
- أسلوب التنفيذ
- المدة الزمنية المحددة للمشروع

مصدر البيانات
استخدم البيانات المعطاة كما هي بدون أي افتراضات إضافية.

قد تحتوي البيانات على:
- project_name
- project_idea
- project_details
- client_name
- client_category
- platforms
- is_agile
- deadline_count
- deadline_type

القواعد الأساسية

1) اللغة والأسلوب
- يجب أن يكون الناتج باللغة العربية فقط.
- أسلوب احترافي مناسب للعميل.
- واضح ومباشر ويركز على التنفيذ.
- تجنب الترجمة الحرفية أو الركيكة.

2) قاعدة المدة الزمنية
- يجب أن يساوي مجموع مدد جميع المراحل القيمة المحددة في deadline_count و deadline_type.
- لا يجوز تجاوز المدة.
- لا يجوز تقليل المدة عن المحدد.
- يجب استخدام نفس وحدة الزمن (أيام أو أسابيع) في جميع المراحل.
- إذا كانت الوحدة "days" → استخدم "أيام".
- إذا كانت الوحدة "weeks" → استخدم "أسابيع".

3) قاعدة أسلوب التنفيذ (Agile)
- إذا كانت is_agile = true:
  - حاول توزيع المراحل بزمن متقارب قدر الإمكان
  - استخدم مراحل تعكس العمل التكراري مثل:
    - التحليل والاستكشاف
    - بناء الأساس التقني
    - تطوير المنصات
    - الاختبار
    - الإطلاق
  - اجعل المراحل منطقية وتعكس تقدم فعلي

- إذا كانت is_agile = false:
  - يمكن توزيع الزمن بشكل غير متساوٍ
  - خصص الوقت حسب حجم العمل والاعتمادية بين المهام
  - استخدم أسلوب مراحل تقليدي واضح

4) عدد المراحل
- عدد المراحل يكون بين 2 إلى 6 مراحل
- لا تنشئ مراحل صغيرة جدًا
- لا تنشئ مرحلة واحدة فقط
- كل مرحلة يجب أن تحتوي عملًا واضحًا ومهمًا

5) توافق النطاق
- يجب أن يعكس الجدول الزمني نطاق المشروع الحقيقي
- إذا كانت platforms موجودة، يجب أن تغطي المراحل تنفيذ هذه المنصات
- إذا كانت project_details موجودة، يجب أن تؤثر بشكل أساسي على توزيع العمل
- استخدم أنشطة واقعية مثل:
  - التحليل والتخطيط
  - التصميم
  - تطوير النظام
  - التكامل
  - الاختبار
  - الإطلاق
  - الدعم بعد الإطلاق
- لا تضف متطلبات غير مذكورة

6) هيكل كل مرحلة
لكل مرحلة يجب توفير:
- phase_number
- title_ar
- duration_ar
- duration_count
- duration_type_ar
- steps_ar

7) تنسيق المدة
- duration_ar يجب أن تكون بصيغة عربية طبيعية مثل:
  - "أسبوعان"
  - "10 أيام"
- duration_count رقم فقط
- duration_type_ar يجب أن تكون:
  - "أيام" أو "أسابيع"

8) خطوات التنفيذ
- كل مرحلة تحتوي على 4 إلى 6 خطوات
- الخطوات يجب أن تكون:
  - واضحة
  - عملية
  - مرتبطة بالأعمال الفعلية
- تجنب التكرار بين المراحل

9) عناوين المراحل
- العنوان يجب أن يكون قصيرًا (3 إلى 8 كلمات)
- ليس جملة
- لا يحتوي على شرح
- يعبر عن المرحلة بشكل مباشر

10) الجودة
- الجدول الزمني يجب أن يكون واقعيًا
- المراحل يجب أن تكون مرتبة منطقيًا
- مناسب لوثيقة موجهة للعميل
- تجنب العبارات العامة غير المفيدة

11) عنوان القسم
- الجدول الزمني للتنفيذ

Enhanced Context:
{enhanced_context}

أعد النتيجة وفق الهيكل المطلوب فقط.
"""

timeline_arabic_prompt_template = PromptTemplate(
    template=TIMELINE_ARABIC_TEMPLATE,
    input_variables=["enhanced_context"]
)