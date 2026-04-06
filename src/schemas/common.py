from pydantic import BaseModel, Field
from typing import Annotated

class LocalizedText(BaseModel):
    en:Annotated[str,Field(description="English text")]
    ar:Annotated[str,Field(description="Arabic text")]