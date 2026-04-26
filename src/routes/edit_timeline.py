# from fastapi import APIRouter, status,HTTPException
# from src.schemas.request_models import TimelineRequestModel
# from src.services.TimelineService import timeline_service

# timeline_router=APIRouter()


# @timeline_router.patch('/modify/timeline')
# async def update_proposed_systems(payload:TimelineRequestModel):
#     enhanced_context=payload.enhanced_context
#     original_content=payload.original_content
#     edit_content=payload.edit_content

#     try:
#         new_timeline = await timeline_service.modify_timeline(
#             enhanced_context=enhanced_context,
#             original_content=original_content,
#             edit_content=edit_content
#         )

#         return new_timeline
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=str(e)
#         )