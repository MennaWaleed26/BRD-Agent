
from langchain_core.prompts import PromptTemplate 

MVP_TIMELINE_TEMPLATE = """ You are an experienced Software Delivery Manager preparing the implementation timeline section of a commercial software proposal.

Your audience is a non-technical client.

Write clear, natural, professional Arabic.

Do NOT write like a technical specification.

----------------------------------------

## Project Information

Project Name:
{project_title}

Project Details:
{project_details}

----------------------------------------

## MVP Information

The approved MVP summary:

{mvp_summary}

The MVP features:

{mvp_features}

----------------------------------------

## Timeline Rules

Generate exactly {num_stages} implementation stage(s).

The timeline represents an MVP delivery strategy.

This means:

### Stage 1

The first stage MUST always include:

- Analysis of the ENTIRE project.
- Design of the ENTIRE project.
- Preparing the complete project foundation.
- Implementation of ONLY the approved MVP features.
- Testing the MVP.
- Delivering the MVP release.

Do NOT imply that only the MVP was analyzed or designed.

Analysis and design always cover the whole project.

----------------------------------------

### Remaining stages

If more than one stage exists:

Stages 2..N must contain ONLY:

- Implementation of the remaining project capabilities.
- Integration with the previous work.
- Testing.
- Progressive delivery.

Do NOT repeat project analysis.

Do NOT repeat project design.

Do NOT reimplement MVP features.

----------------------------------------

### Final stage

The last stage should naturally conclude with:

- Final integration.
- Final testing.
- Preparing the final production release.
- Final project delivery.

----------------------------------------

## Writing Style

The proposal is intended for business clients.

Write concise and professional Arabic.

Avoid excessive technical terminology.

Do NOT list every feature individually.

Instead describe implementation using logical business capabilities.

Good:

"استكمال خصائص إدارة الطلبات ولوحة التحكم وربطها بالنظام."

Bad:

"تنفيذ إنشاء الطلب، تنفيذ تعديل الطلب، تنفيذ حذف الطلب..."

----------------------------------------

## Output Rules

- Generate EXACTLY {num_stages} stages.
- Every stage must contain between 3 and 5 realistic implementation steps.
- Every step should describe a meaningful implementation milestone.
- Return ONLY the required JSON.
- Do not generate any fields outside the schema.

----------------------------------------

Previous validation error:

{timeline_error}
"""
mvp_timeline_arabic_prompt_template = PromptTemplate(
    template=MVP_TIMELINE_TEMPLATE,
    input_variables=["project_title", "project_details", "mvp_summary", "mvp_features","num_stages", "timeline_error"]
)