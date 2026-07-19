from pydantic import BaseModel, Field
from typing import Annotated, Union, List
from ..proposed_system import ProposedSystemArabicOutput,ProposedSystemLocalizedOutput
from ..timeline import NormalTimelineEnrichedArabicOutput, TimelineEnrichedLocalizedOutput
from ..requirements_writer import FunctionalRequirementsArabicOutput, FunctionalRequirementsLocalizedOutput

BRDSectionsLocalized=Annotated[
    Union[
        ProposedSystemLocalizedOutput,
        TimelineEnrichedLocalizedOutput,
        FunctionalRequirementsLocalizedOutput
    ],
    Field(discriminator="key")
]
class FinalBRDLocalizedOutput(BaseModel):
    sections: List[BRDSectionsLocalized] = Field(default_factory=list) # type: ignore








BRDSectionsArabic=Annotated[
    Union[
    ProposedSystemArabicOutput,
    NormalTimelineEnrichedArabicOutput,
    FunctionalRequirementsArabicOutput
],  Field(discriminator="key")]
class FinalBRDArabicOutput(BaseModel):
    sections: List[BRDSectionsArabic] = Field(default_factory=list) # type: ignore