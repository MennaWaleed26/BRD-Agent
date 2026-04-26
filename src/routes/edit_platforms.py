from fastapi import APIRouter, status,HTTPException
from src.schemas.request_models import PlatformRequestModel
from src.services.PlatformService import platform_service

platforms_router=APIRouter()


@platforms_router.patch('/modify/platforms')
async def update_proposed_systems(payload:PlatformRequestModel):
    enhanced_context=payload.enhanced_context
    original_content=payload.original_content
    edit_content=payload.edit_content

    try:
        new_proposed_systems = await platform_service.modify_proposed_system(
            enhanced_context=enhanced_context,
            original_content=original_content,
            edit_content=edit_content
        )

        return new_proposed_systems
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )