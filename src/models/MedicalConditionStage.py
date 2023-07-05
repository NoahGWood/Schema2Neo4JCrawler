from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class MedicalConditionStage(MedicalEntity):
    stageAsNumber: Optional[Any] = None
    subStageSuffix: Optional[Any] = None

