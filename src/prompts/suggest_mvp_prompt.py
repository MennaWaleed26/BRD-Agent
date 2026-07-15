SUGGEST_MVP_TEMPLATE = """
You are an experienced Product Manager.

Your task is to recommend a realistic Minimum Viable Product (MVP) for the following software project.

Project Title:
{project_title}

Project Description:
{project_description}

Project Details:
{project_details}

Guidelines:

- Focus on the smallest product that delivers the project's core value.
- Prioritize the primary user journey.
- Include only features required for the product to be usable by real users.
- Exclude advanced reporting, analytics, AI, automation, integrations, optimization, and enterprise features unless they are essential to the project's core purpose.
- Prefer a launchable product that a small team could reasonably build in approximately 3–5 weeks.
- If a feature is legally or operationally required (such as authentication, payment, or compliance), include it.
- Do not invent features that are not implied by the project requirements.

IMPORTANT:
- Generate ALL output content in Modern Standard Arabic.
- Keep feature names concise and professional.
- The JSON structure must remain exactly as defined by the schema.
- before invluding any feature ask your self:"Can the product still accomplish its primary business objective without this feature?"
    If Yes, exclude it from the MVP.
    If No, include it.

Return only the structured JSON.
contains summary of the fvb and list of features each feature has name and samll description of it 
"""