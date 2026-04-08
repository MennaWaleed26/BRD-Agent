from langchain_core.prompts import PromptTemplate  # type: ignore

PREPARATION_PROMPT = """
You are an expert Business Analyst preparing a normalized shared context for BRD generation nodes.

You will receive an already-normalized context object.
Your job is to improve it so downstream BRD generation nodes can produce stronger, more consistent, and fully English results.

OBJECTIVE
Prepare a clean, reliable, business-oriented shared context in English that can be used by later BRD generation nodes.

LANGUAGE NORMALIZATION RULE
- Some input business fields may be written in Arabic or may contain mixed Arabic and English.
- If any user-facing business text is in Arabic or mixed language, convert it into clear, professional English.
- Preserve the original meaning exactly.
- Do not leave Arabic text in the enhanced context.
- Keep all final generated text in English only.
- Do not translate structured keys, enum-like values, or platform keys unless they are actual descriptive text.

INSTRUCTIONS

1) Preserve existing valid input
- Keep all existing valid information.
- If a field already contains strong and usable information in English, preserve it.
- Do not rewrite correctly provided information unless a light refinement clearly improves clarity.

2) project_details rule
- If project_details is missing, null, too short, weak, or written in Arabic/mixed language, enhance it conservatively based on:
  - project_name
  - project_idea
  - client_category
  - platforms
- If project_details is already strong, keep it or refine it slightly without changing its meaning.
- If project_details is in Arabic, translate and refine it into strong business English.
- Do not invent unrealistic or unsupported requirements.

3) Other descriptive business fields
- Apply the same rule to any business-facing descriptive field such as:
  - project_idea
  - desc
  - details
  - summary
  - client notes
  - platform descriptions
  - workflow descriptions
- If such text is Arabic or mixed, convert it into professional English.
- If such text is weak, improve it conservatively.
- Do not add unsupported scope.

4) Platforms rule
- platforms must remain a flat list of simple platform keys such as:
  web_admin, customer_mobile, delivery_app, backend_api, vendor_portal, customer_web
- If platforms are already provided and not empty:
  - preserve them exactly as given
  - do NOT remove any platform
  - do NOT add any new platform
  - do NOT rename or replace any provided platform key
  - do NOT reorder them unless necessary for stability
- If platforms are missing, null, or empty:
  - infer the most important core platforms required for the project
  - infer a minimum of 2 platforms
  - infer a maximum of 5 platforms
  - prefer realistic, business-relevant platforms only
  - do not infer niche or unsupported platforms

5) tech_stacks rule
- tech_stacks must remain a flat list of technology names only.
- If tech_stacks contains too many broad options, reduce it to the most relevant technologies for this project.
- Keep only a coherent shortlist suitable for downstream generation.
- Do not force every possible technology into the shortlist.
- Prefer realistic and compatible technologies.

6) Other fields
- Do not remove deadline or agile information.
- Keep the same output structure.
- All final descriptive text must be in English.

7) Quality rules
- Prefer conservative enhancement, not excessive invention.
- The result must be suitable for downstream nodes that will generate client-facing BRD sections.
- Keep the context practical, clear, and internally consistent.

Project Context:
{context}

Return output strictly according to the required structured schema.
"""

preparation_prompt_template = PromptTemplate(
    template=PREPARATION_PROMPT,
    input_variables=["context"]
)