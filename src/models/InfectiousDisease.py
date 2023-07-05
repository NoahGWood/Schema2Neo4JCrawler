from pydantic import BaseModel
from models.MedicalCondition import MedicalCondition

from typing import Optional, Any

class InfectiousDisease(MedicalCondition):
    infectiousAgent: Optional[Any] = None
    infectiousAgentClass: Optional[Any] = None
    transmissionMethod: Optional[Any] = None

