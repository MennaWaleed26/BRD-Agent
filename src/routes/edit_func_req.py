from fastapi import APIRouter,HTTPException,status
from src.schemas.preparation import PreparationOutput
from src.schemas.sections_output import FunctionalRequirementsArabicOutput
from src.services.FunctionalReqService import functional_req_service
from src.schemas.request_models import FunctionalRequestModel

func_req_router=APIRouter()

@func_req_router.patch("/modify/functional_req")
async def modify_functional_requirement(raw_request:FunctionalRequestModel):
    
    try:
        new_functional_requirement= await functional_req_service.modify_functional_req(
            enhanced_context= raw_request.enhanced_context,
            original_content= raw_request.original_content,
            edit_content= raw_request.edit_content
        )
        
        return new_functional_requirement
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    
