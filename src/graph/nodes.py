import json
from typing import Any, Dict, Type, TypeVar

from langchain_openai import ChatOpenAI
from pydantic import BaseModel

from src.graph.state import GraphState
from src.schemas.response import BRDResponsePayload
from src.schemas.sections_output import (
                                         
    ProposedSystemEnglishOutput,
    ProposedSystemArabicOutput,
    ProposedSystemSection,
    ProposedSystemSectionContent,
    TechnologyStackEnglishOutput,
    TechnologyStackArabicOutput,
    TechnologyStackSection,
    TechnologyStackSectionContent,
    FunctionalUnitsEnglishOutput,
    FunctionalUnitsArabicOutput,
    FunctionalUnitsSection,
    TimelineEnglishOutput,
    TimelineArabicOutput,
    TimelineSection,
    GenericSectionContent,
)
from src.prompts.proposed_system_prompt import proposed_system_prompt_template

llm = ChatOpenAI(model="gpt-4o", temperature=0.2)