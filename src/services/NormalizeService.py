from curses import raw

from src.schemas.request_models import BRDRequestModel
from typing import Dict,Any
import json

class ProjectContext:
    """Unified context object used by prompts inside LangGraph."""
    def __init__(self, raw_request: BRDRequestModel):

        self.project_name=raw_request.project.title
        self.project_idea=raw_request.project.desc
        self.project_details=raw_request.project.details
        
        self.client_name=raw_request.client.name
        self.client_category=raw_request.client.category
        
        self.languages=[]
        if raw_request.language_targets:
            self.languages=[lang.strip().lower() for lang in raw_request.language_targets]
        
        self.platforms=[]
        if raw_request.platforms :
            self.platforms=[p.key for p in raw_request.platforms]
        
        self.tech_stack=[]
        if raw_request.tech_stack_ids:
            self.tech_stack=[ tech_stack.title for tech_stack in raw_request.tech_stack_ids]
        
        c=raw_request.constraints
        if c:
            val=str(c.is_agile).strip().lower()
            self.is_agile = val in ["true", "yes","1"]
            self.num_stages=c.deadline.num_stages
            self.timeline_details=c.deadline.timeline_details
            
    def to_dict(self)->Dict[str,Any]:
        return {
            "languages": self.languages,
            "project_name": self.project_name,
            "project_idea": self.project_idea,
            "project_details": self.project_details,
            "client_name": self.client_name,
            "client_catrgory": self.client_category,
            "platforms": self.platforms,
            "tech_stacks": self.tech_stack,
            "is_agile": self.is_agile,
            "num_stages": self.num_stages,
            "timeline_details": self.timeline_details
            
        }
    def to_json_string(self):
        return json.dumps(self.to_dict(),indent=2)
    
def normalize_request(raw_request:BRDRequestModel):
    
    return ProjectContext(raw_request)
        