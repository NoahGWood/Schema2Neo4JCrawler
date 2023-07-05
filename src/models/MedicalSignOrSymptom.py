from pydantic import BaseModel
from models.MedicalCondition import MedicalCondition

from typing import Optional, Any

class MedicalSignOrSymptom(MedicalCondition):
    possibleTreatment: Optional[Any] = None

