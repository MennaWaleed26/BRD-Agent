
from pydantic import BaseModel, Field
from  typing import List

class MVPFeature(BaseModel):
    name: str
    description: str

class SuggestedMVP(BaseModel):
    summary: str
    mvp_features:List[MVPFeature] 