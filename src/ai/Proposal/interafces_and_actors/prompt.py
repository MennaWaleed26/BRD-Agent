from langchain_core.prompts import PromptTemplate  # type: ignore

INTERFACES_AND_USERS_TEMPLATE = """
You are analyzing the user-facing interfaces and users of a software proposal.

The original project text is the authoritative source.
The project understanding is supporting interpretation only.

Project Title:
{project_title}

Project Description:
{project_description}

Project Details:
{project_details}


Your task is to identify:

1. The distinct user-facing interfaces.
2. The users who interact with each interface.
3. The high-level actions each user can perform through that interface.

Definitions:

- Interface:
  A distinct portal, application, dashboard, website, or other user-facing surface.

- User:
  A real-world person, organization, or user type that interacts with an interface.

Instructions:

- Preserve all provided interfaces.
- Do not remove or silently rename a provided interface.
- Use the project details to confirm, clarify, or enrich provided interfaces.
- Add an inferred interface only when the details clearly require a distinct
  user experience or delivery channel.
- Do not create a separate interface for every user.
- Multiple users may share the same interface.
- Keep each shared interface as one item, even when its users perform different actions.
- Identify separate users only when the project gives them meaningfully different
  responsibilities or access.
- Do not model roles and permission hierarchies separately.
- Represent differences directly through each user's capabilities.
- Keep capabilities high-level and client understandable.
- Do not include technical permissions, database rules, API behavior, or implementation details.
- Do not organize capabilities into modules.
- Do not make MVP or timeline decisions.
- Do not invent users merely because they are common in similar systems.
- Include short source evidence for every interface and user.
- Flag material conflicts or ambiguities.
- Normalize internal keys and titles in English.
- Preserve client-facing names and source evidence in their original language.
"""
interfaces_actors_prompt_template = PromptTemplate(
    template=INTERFACES_AND_USERS_TEMPLATE,
    input_variables=["project_title","project_description","project_details"]
)