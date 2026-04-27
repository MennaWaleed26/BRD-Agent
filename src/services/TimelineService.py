from enum import Enum
from pydantic import BaseModel,Field
from typing import List
from src.llm.invoke import invoke_structured_async

from src.schemas.preparation import PreparationOutput

from src.llm.invoke import invoke_structured_async
from src.prompts.timeline_prompt import timeline_arabic_prompt_template
from src.prompts.edit_timeline_prompts import (timeline_edit_classifier_template,
                                               timeline_mode_a_revision_template,
                                               timeline_mode_b_context_update_template)
from src.schemas.sections_output import TimelineArabicOutput,TimelineEnrichedArabicOutput


class EditMode(str, Enum):
    A = "A"
    B = "B"


class TimelineEditClassification(BaseModel):
    mode: EditMode
    reason: str
    affected_entities: List[str] = Field(default_factory=list)


class TimelineService:
    async def modify_timeline(
        self,
        enhanced_context: PreparationOutput,
        original_content: TimelineEnrichedArabicOutput,
        edit_content: str,
    ) -> dict:
        classification = await invoke_structured_async(prompt_template=timeline_edit_classifier_template,
                                                       prompt_variables={"enhanced_context":enhanced_context,
                                                        "original_content":original_content,
                                                        "edit_content":edit_content},
                                                       output_model=TimelineEditClassification,
                                                       run_name="timeline_edit_classifier")
        if classification.mode == EditMode.A:
            raw_timeline = await invoke_structured_async(prompt_template=timeline_mode_a_revision_template,prompt_variables={
                "enhanced_context":enhanced_context,
                "original_content":original_content,
                "edit_content":edit_content
            },
            output_model=TimelineEnrichedArabicOutput,
            run_name="timeline_mode_a_revision",)

            enriched_timeline = self.preserve_existing_numbers(
                new_timeline=raw_timeline,
                original_timeline=original_content,
            )

            return {
                "mode": "A",
                "classification_reason": classification.reason,
                "affected_entities": classification.affected_entities,
                "updated_context": None,
                "timeline": enriched_timeline.model_dump(),
            }

        updated_context = await invoke_structured_async(
            prompt_template=timeline_mode_b_context_update_template,
            prompt_variables={  "enhanced_context":enhanced_context,
                "original_content":original_content,
                "edit_content":edit_content},
            output_model=PreparationOutput,
            run_name="timeline_mode_b_context_update",
        )

        regenerated_timeline =await invoke_structured_async(
            prompt_template=timeline_arabic_prompt_template,
            prompt_variables={
                "enhanced_context": updated_context.model_dump(),
                "timeline_error": ""
            },
            output_model=TimelineArabicOutput,
            run_name="timeline_mode_b_regeneration",
        )

        enriched_timeline = self.enrich_numbers_from_original(
            new_timeline=regenerated_timeline,
            original_timeline=original_content,
        )

        return {
            "mode": "B",
            "classification_reason": classification.reason,
            "affected_entities": classification.affected_entities,
            "updated_context": updated_context.model_dump(),
            "timeline": enriched_timeline.model_dump(),
        }


    def preserve_existing_numbers(
        self,
        new_timeline: TimelineEnrichedArabicOutput,
        original_timeline: TimelineEnrichedArabicOutput,
    ) -> TimelineEnrichedArabicOutput:
        original_items = original_timeline.model_dump().get("content", [])
        new_data = new_timeline.model_dump()

        for idx, stage in enumerate(new_data.get("content", [])):
            if idx < len(original_items):
                old = original_items[idx]
                stage["phase_number"] = old.get("phase_number", idx + 1)
                stage["duration_count"] = old.get("duration_count")
                stage["duration_type_ar"] = old.get("duration_type_ar")
                stage["price"] = old.get("price")
            else:
                stage["phase_number"] = idx + 1

        return TimelineEnrichedArabicOutput.model_validate(new_data)

    def enrich_numbers_from_original(
        self,
        new_timeline: TimelineArabicOutput,
        original_timeline: TimelineEnrichedArabicOutput,
    ) -> TimelineEnrichedArabicOutput:
        original_items = original_timeline.model_dump().get("content", [])
        new_data = new_timeline.model_dump()

        orig_num_stages=len(original_items)
        orig_stage_price=original_items[0]["price"]
        total_price=orig_num_stages * orig_stage_price
        
        new_num_stages=len(new_data["content"])
        new_stage_price = round(total_price / new_num_stages, 2)
        
        for idx, stage in enumerate(new_data.get("content", [])):
            stage["phase_number"] = idx + 1
            old = original_items[0]
            stage["duration_count"] = old.get("duration_count")
            stage["duration_type_ar"] = old.get("duration_type_ar")
            stage["price"] = new_stage_price


        return TimelineEnrichedArabicOutput.model_validate(new_data)





timeline_service = TimelineService()