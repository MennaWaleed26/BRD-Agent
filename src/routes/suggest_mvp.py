from fastapi import APIRouter, HTTPException,status # type: ignore
from src.schemas import SuggestMvpRequestModel
from src.services import MvpService
mvp_router=APIRouter()


@mvp_router.post("/suggest_mvp")
async def suggest_mvp(payload:SuggestMvpRequestModel):
    try :
        mvp_service = MvpService()
        response= await mvp_service.suggest_mvp(payload)
        
        return response
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))
    
