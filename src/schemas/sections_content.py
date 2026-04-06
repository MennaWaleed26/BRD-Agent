from pydantic import BaseModel, Field
from typing import List, Annotated

from src.schemas.common import LocalizedText

class ProposedSystemItemtLang(BaseModel):
    """Structured content for one language of the proposed system section."""
    title: str = Field(description="Title of this proposed platform or subsystem")
    content: str = Field(description="Description of this proposed platform or subsystem")
    technologies_used: List[str] = Field(
        default_factory=list,
        description=
        "List of referenced technologies used to build this item (this platform or subsystem)"
    )
class TechnologyStackContentLang(BaseModel):
    """Structured content for one language of the technology stack section."""
    title: str = Field(description="Short internal title for the section content")
    content: str = Field(description="Main descriptive content")
    technologies_used: List[str] = Field(
        default_factory=list,
        description="List of technologies used in the system"
    )
    
class GenericContentLang(BaseModel):
    """
    Temporary generic content model for sections whose final structure
    will be designed later, like functional_units و timeline.
    """
    title: str = Field(description="Short internal title for the section content")
    content: str = Field(description="Main descriptive content")