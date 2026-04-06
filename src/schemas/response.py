from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

from src.schemas.sections_output import BRDSection


class BRDResponsePayload(BaseModel):
    """
    Final payload returned from the graph.
    The API layer can later reshape this if the backend engineer requests
    a different response contract.
    """
    project_name: str = Field(description="Project name")
    client_name: str = Field(description="Client name")
    sections: List[BRDSection] = Field(
        description="Final bilingual BRD sections"
    )
    metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Optional metadata for internal use"
    )