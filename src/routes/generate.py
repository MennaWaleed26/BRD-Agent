from fastapi import APIRouter, HTTPException,status # type: ignore
from src.schemas.request_models import BRDRequestModel  # type: ignore
from src.services.BRDService import BRDService # type: ignore

brd_router=APIRouter()

brd_service=BRDService()

@brd_router.post("/generate-brd")
async def create_brd(payload:BRDRequestModel):
    try :
        response= await brd_service.generate_brd(payload)
        
        return response
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e))