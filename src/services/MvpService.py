from src.schemas import SuggestMvpRequestModel
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from src.helpers.config import settings
from src.prompts import SUGGEST_MVP_TEMPLATE
from src.schemas import SuggestedMVP

class MvpService:

    def __init__(self):

        self.model = ChatOpenAI(api_key = settings.OPENAI_API_KEY, temperature=0.0, model = 'gpt-5.4-nano')

    async def suggest_mvp(self, payload: SuggestMvpRequestModel):
        

        project_title = payload.title
        project_desc = payload .desc
        project_details = payload.details
        

        final_prompt = SUGGEST_MVP_TEMPLATE.format(project_title= project_title, 
                                                   project_description = project_desc,
                                                   project_details = project_details)
        messages = [SystemMessage(content=final_prompt)]
        
        model_with_structured_output = self.model.with_structured_output(schema=SuggestedMVP)

        result =await  model_with_structured_output.ainvoke(messages)

        return result 