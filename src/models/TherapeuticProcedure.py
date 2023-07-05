from pydantic import BaseModel
from models.MedicalProcedure import MedicalProcedure

from typing import Optional, Any

class TherapeuticProcedure(MedicalProcedure):
    adverseOutcome: Optional[Any] = None
    doseSchedule: Optional[Any] = None
    drug: Optional[Any] = None

