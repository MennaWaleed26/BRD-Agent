from typing import List, Optional
from pydantic import BaseModel, Field # type: ignore
class PreparationOutput(BaseModel):
    project_name: str = ""
    project_idea: str = ""
    project_details: str = ""
    client_name: str = ""
    client_category: str = ""
    platforms: List[str] = Field(default_factory=list)
    tech_stacks: List[str] = Field(default_factory=list)
    is_agile: Optional[bool] = None
    deadline_count: Optional[int] = None
    deadline_type: Optional[str] = None


# class PreparationOutput(BaseModel):
#     enhanced_context: NormalizedContext