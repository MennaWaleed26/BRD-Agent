
from pydantic import BaseModel, Field
from typing import List,Annotated,Any,Dict,Literal
from .preparation import PreparationOutput
from .sections_output import ProposedSystemArabicOutput,TimelineEnrichedArabicOutput,FunctionalRequirementsArabicOutput

class ClientModel(BaseModel):
    name:Annotated[str,Field(description="The name of the client company ")]
    category:Annotated[str,Field(description="The category of industry of the client company ")]
    country:Annotated[List[str],Field(description="The different countries that the project should support ")]

class ProjectModel(BaseModel):
    title:Annotated[str,Field(description="The title of the clients project idea that should be displayed in the brd as it is ")]
    desc:Annotated[str,Field(description="The quick description of the project that the sales will enter")]
    details:Annotated[str|None,Field(description="The details of the project that the sales took from the client ")]=None

class PlatformTypeModel(BaseModel):
    id: int
    title: str 
      
class PlatformModel(BaseModel):
    key:Annotated[str,Field(description="The type of platform that the client want to build")]
    type:PlatformTypeModel
    
class TechStackModel(BaseModel):
    id:str
    title:str
    desc:str
      
class DeadlineModel(BaseModel):
    num_stages:Annotated[int,Field(gt=0)]
    days_per_stage:Annotated[int,Field(gt=0)]=20
    timeline_details:str|None=None
    
class ConstraintsModel(BaseModel):
    deadline:DeadlineModel
    is_agile:bool
    total_price:Annotated[int,Field(gt=0)]
    
class BRDRequestModel(BaseModel):
    language_targets:Annotated[List[str],Field(description="the difference languages that the project should support")]
    client:Annotated[ClientModel,Field(description="Information about the client that the brd is generated to")]
    project:Annotated[ProjectModel,Field(description="Information about the client's idea we generate the brd for")]
    platforms:Annotated[List[PlatformModel]|None,Field(description="the platforms that the client asked to have")]=None
    tech_stack_ids:List[TechStackModel]
    constraints:ConstraintsModel





class PlatformRequestModel(BaseModel):
    enhanced_context: PreparationOutput
    original_content: ProposedSystemArabicOutput
    edit_content: str


class TimelineRequestModel(BaseModel):
    enhanced_context:PreparationOutput
    original_content: TimelineEnrichedArabicOutput
    edit_content: str
    
class FunctionalRequestModel(BaseModel):
    enhanced_context:PreparationOutput
    original_content: FunctionalRequirementsArabicOutput
    edit_content: str