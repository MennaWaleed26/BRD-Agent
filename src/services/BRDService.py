from copy import deepcopy

from click import prompt

from src.schemas.request_models import BRDRequestModel  # type: ignore
from src.services.NormalizeService import normalize_request
from src.graph.workflow import brd_graph
from ..domain import build_preparation_prompt_inputs

class BRDService:
    def normalize_tech_title(self, title: str) -> str:
        return title.strip().lower()

    def build_technology_lookup(self, available_technologies) -> dict[str, dict]:
        lookup = {}

        for tech in available_technologies:
            # Support dicts
            if isinstance(tech, dict):
                title = tech.get("title")
                tech_id = tech.get("id")
            else:
                # Support Pydantic/model objects
                title = getattr(tech, "title", None)
                tech_id = getattr(tech, "id", None)

            if not title or tech_id is None:
                continue

            lookup[self.normalize_tech_title(title)] = {
                "id": tech_id,
                "title": title
            }

        return lookup

    def replace_technologies_used_with_objects(self, data, technology_lookup: dict[str, dict]):
        if isinstance(data, dict):
            updated = {}

            for key, value in data.items():
                if key == "technologies_used" and isinstance(value, list):
                    mapped_technologies = []
                    seen = set()

                    for tech_title in value:
                        if not isinstance(tech_title, str):
                            continue

                        normalized_title = self.normalize_tech_title(tech_title)

                        if normalized_title in technology_lookup and normalized_title not in seen:
                            mapped_technologies.append(deepcopy(technology_lookup[normalized_title]))
                            seen.add(normalized_title)

                    updated[key] = mapped_technologies
                else:
                    updated[key] = self.replace_technologies_used_with_objects(value, technology_lookup)

            return updated

        elif isinstance(data, list):
            return [
                self.replace_technologies_used_with_objects(item, technology_lookup)
                for item in data
            ]

        return data

    async def generate_brd(self, payload: BRDRequestModel):
        available_technologies = payload.tech_stack_ids or []
        technology_lookup = self.build_technology_lookup(available_technologies)

        context = normalize_request(raw_request=payload)
        prompt_inputs=build_preparation_prompt_inputs(context=context.to_dict())
        controls=prompt_inputs["controls"]
        context=prompt_inputs["context"]
        
        initial_state = {"context": context, "controls":controls}

        graph_result = await brd_graph.ainvoke(initial_state) # type: ignore

        final_output = graph_result["final_result"]

        if hasattr(final_output, "model_dump"):
            final_output = final_output.model_dump()

        final_output_with_ids = self.replace_technologies_used_with_objects(
            final_output,
            technology_lookup
        )

        return final_output_with_ids