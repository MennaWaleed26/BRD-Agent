from typing import Any, Dict, List, Literal
from fastapi import status, HTTPException
from src.ai.Proposal.state import GraphState
from src.ai.Proposal.state import GraphState
from .schema import TimelineArabicOutput, TimelineEnrichedArabicOutput, TimelineLocalizedOutput, TimelineEnrichedLocalizedOutput
from .prompt import timeline_arabic_prompt_template, timeline_bill_prompt_template
from src.ai.llm.invoke import generate_section


class SectionValidationError(Exception):
    """Raised when a generated section fails validation."""
    pass

class Timeline:
    def __init__(self):
        pass

    def _enrich_timeline_ar_stages(self,context,raw_timeline_output):
    
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


    def _enrich_timeline_bi_stages(self, context, raw_timeline_output):
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

            
    
    

    async def timeline_node(self,state:GraphState,prompt_template, output_model,run_name,is_timeline):
                
            response= await generate_section(
                state=state,
                prompt_template=prompt_template,
                output_model= output_model,
                run_name= run_name,
                is_timeline=is_timeline

            )
            
            return response



    async def timeline_ar(self, state:GraphState):
        
        response= await self.timeline_node(
            state=state,
            prompt_template=timeline_arabic_prompt_template,
            output_model=TimelineArabicOutput,
            run_name="Timeline Arabic Node",
            is_timeline=True
        )
        
        
        
        enriched_timeline = self._enrich_timeline_ar_stages(state["context"], raw_timeline_output=response.model_dump())

        
        return {"timeline":enriched_timeline}

    async def validate_timeline_ar(self, state:GraphState):
        timeline=state.get("timeline")
        context=state["context"]
        try:
            expected_stages=context["num_stages"]
            actual_stages =len(timeline.get("content")) # type: ignore
            if actual_stages != expected_stages:
                raise SectionValidationError(
                    f"Expected {expected_stages} but got {actual_stages}"
                )
            return {
                "timeline_validated":timeline,
                "timeline_error": None 
            }
            
        except Exception as e :
            
            return {
                "timeline_validated":None,
                "timeline_error": f"فشلت المحاولة السابقة لانه كان مطلوب {expected_stages} بينما تم توليد {actual_stages}", # type: ignore
                "timeline_retry_count": state.get("timeline_retry_count",0)+1
            }
    
    async def timeline_fallback_ar_node(self, state:GraphState):
        context=state.get("context")
        timeline=state.get("timeline") 
        num_stages=context.get("num_stages")
        days_per_stage=context.get("days_per_stage")
        total_price=context.get("total_price",0)
        stage_price = round(total_price / num_stages, 2)
        
        remaining_stages=len(timeline.get("content"))-num_stages # type: ignore
        safe_content=[]
        j=num_stages+1 # type: ignore
        for _ in range(remaining_stages):
            safe_content.append({
                "phase_number": j,
                "title_ar": f"المرحلة {j}",
                "duration_count": days_per_stage,
                "duration_type_ar": "ايام",
                "steps_ar": ["يُستكمل لاحقًا"],
                "price":stage_price
            })
            j+=1
        return {
            "timeline_validated": {
                "key": "timeline",
                "title_ar": "الجدول الزمني للتنفيذ",
                "content": timeline.get("content",[])+safe_content
            },
            "timeline_error": "Used fallback after 3 failed validation attempts.",
        }
        


        
    async def timeline_billingual(self, state:GraphState):
        response= await self.timeline_node(
            state=state,
            prompt_template=timeline_bill_prompt_template,
            output_model=TimelineLocalizedOutput,
            run_name="Timeline Node",
            is_timeline=True
        )
        enriched_timeline = self._enrich_timeline_bi_stages(context=state["context"],raw_timeline_output=response.model_dump())
        
        return {"timeline":enriched_timeline}


    async def validate_timeline_bi(self, state:GraphState):
        timeline=state.get("timeline")
        context=state.get("context")
        try:
            expected_stages= context.get("num_stages")
            actual_stages= len(timeline.get("content",""))
            
            if expected_stages != actual_stages:
                raise SectionValidationError(f"Expected {expected_stages} but got {actual_stages}")
            return {
                "timeline_validated":timeline,
                "timeline_error":None
                
            }
            
        except Exception as e:
            return {
                "timeline_validated":None,
                "timeline_error":f"failed to generate as Expected {expected_stages} stages but got {actual_stages}", # type: ignore
                "timeline_retry_count": state.get("timeline_retry_count",0)+1
            }     

    async def timeline_fallback_bi_node(self, state:GraphState):
        context=state.get("context")
        timeline=state.get("timeline") 
        num_stages=context.get("num_stages")
        days_per_stage=context.get("days_per_stage")
        total_price=context.get("total_price",0)
        stage_price = round(total_price / num_stages, 2)
        
        remaining_stages=len(timeline.get("content"))-num_stages # type: ignore
        safe_content=[]
        j=num_stages+1 # type: ignore
        for _ in range(remaining_stages):
            safe_content.append({
                "phase_number": j,
                "title_en": f"Phase {j}",
                "title_ar": f"المرحلة {j}",
                "duration_count": days_per_stage,
                "duration_type_en": "days",
                "duration_type_ar": "ايام",
                "steps_en": ["Will be continued later. "],
                "steps_ar": ["يُستكمل لاحقًا"],
                "price":stage_price
            })
            j+=1
        return {
            "timeline_validated": {
                "key": "timeline",
                "title_en": "Implementation Timeline",
                "title_ar": "الجدول الزمني للتنفيذ",
                "content": timeline.get("content",[])+safe_content
            },
            "timeline_error": "Used fallback after 3 failed validation attempts.",
        }

    async def router_after_timeline_validation(self, state:GraphState)-> Literal[
        "next_node",
        "timeline_generate_node",
        "timeline_fallback_node",
    ]:
        if state.get("timeline_validated") is not None:
            return "next_node"

        if state.get("timeline_retry_count", 0) < 3:
            return "timeline_generate_node"

        return "timeline_fallback_node"

    async def finish_timeline_ar_node(self, state: GraphState):
        return {}

    async def finish_timeline_bi_node(self, state: GraphState):
        return {}