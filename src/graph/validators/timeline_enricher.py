
from typing import Any, Dict, List

from fastapi import status, HTTPException

from src.graph.state import GraphState







def enrich_timeline_ar_stages(context,raw_timeline_output):
    
    num_stages=context.get("num_stages")
    total_price=context.get("total_price")
    days_per_stage=context.get("days_per_stage")

    
    if num_stages<=0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The number of required stages is invalid")
    if days_per_stage <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The number of required days per stage is invalid")
    content=raw_timeline_output.get("content")

    if total_price is not None:
        stage_price = round(total_price / num_stages, 2)
        
    enriched_content: List[Dict[str, Any]] = []

    for idx, stage in enumerate(content, start=1):
        if not isinstance(stage, dict):
            raise ValueError(f"Stage {idx} must be an object.")

        steps = stage.get("steps_ar") or []
        if not isinstance(steps, list):
            steps = [str(steps)]

        enriched_stage = {
            "phase_number": idx,
            "title_ar": stage.get("title_ar", ""),
            "duration_count": days_per_stage,
            "duration_type_ar": "أيام",
            "steps_ar": steps,
            "price": stage_price, # type: ignore
        }

        enriched_content.append(enriched_stage)

    return {
        "key": raw_timeline_output.get("key", "timeline"),
        "title_ar": raw_timeline_output.get("title_ar", "الجدول الزمني للتنفيذ"),
        "content": enriched_content,
    }


def enrich_timeline_bi_stages(context, raw_timeline_output):
    num_stages=context.get("num_stages")
    total_price=context.get("total_price")
    days_per_stage=context.get("days_per_stage")
    if num_stages<=0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The number of required stages is invalid")
    if days_per_stage <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="The number of required days per stage is invalid")
    if total_price is not None:
        stage_price = round(total_price / num_stages, 2)

    content=raw_timeline_output.get("content")
    enriched_content: List[Dict[str, Any]] = []

    for idx, stage in enumerate(content, start=1):
        if not isinstance(stage, dict):
            raise ValueError(f"Stage {idx} must be an object.")

        steps_ar = stage.get("steps_ar") or []
        if not isinstance(steps_ar, list):
            steps_ar = [str(steps_ar)]
            
        steps_en = stage.get("steps_en") or []
        if not isinstance(steps_en, list):
            steps_en = [str(steps_en)]

        enriched_stage = {
            "phase_number": idx,
            "title_en": stage.get("title_en"," "),
            "title_ar": stage.get("title_ar", ""),
            "duration_count": days_per_stage,
            "duration_type_en":"days",
            "duration_type_ar": "أيام",
            "steps_ar": steps_ar,
            "steps_en":steps_en,
            "price": stage_price, # type: ignore
        }

        enriched_content.append(enriched_stage)

    return {
        "key": raw_timeline_output.get("key", "timeline"),
        "title_en": raw_timeline_output.get("title_en", "Implementation Timeline"),
        "title_ar": raw_timeline_output.get("title_ar", "الجدول الزمني للتنفيذ"),
        "content": enriched_content,
    }

        
    
    