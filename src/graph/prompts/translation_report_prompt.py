from langchain_core.prompts import PromptTemplate  # type: ignore

TRANSLATE_REPORT_TEMPLATE = """
You are a professional bilingual business analyst.

Translate the following structured English BRD report into Arabic.

Rules:
- Preserve the exact structure and hierarchy.
- Translate all user-facing text naturally into professional Arabic.
- Do not change or remove any section, group, module, feature, or step.
- Do not add any new content.
- Preserve all numeric values exactly.
- Preserve all keys exactly as they are.
- Preserve `key`, `group_key`, `phase_number`, and `duration_count` exactly as they are.
- Translate `duration_type` in timeline entries as follows:
  - "days" -> "أيام"
  - "weeks" -> "أسابيع"
- Translate all timeline phase titles, duration strings, and step texts into Arabic.
- Preserve technology and product names in English when appropriate, such as:
  Flutter, React, PostgreSQL, Firebase, Node.js, Docker, AWS, API, ERP, CRM.
- Keep the tone professional, business-friendly, and clear.
- Do not leave English text in the Arabic output unless it is a technology, product, platform, or brand name.

English report:
{english_report}
"""

translate_report_prompt_template = PromptTemplate(
    template=TRANSLATE_REPORT_TEMPLATE,
    input_variables=["english_report"],
)