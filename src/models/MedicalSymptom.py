from pydantic import BaseModel
from models.MedicalCondition import MedicalCondition

from typing import Optional, Any

class MedicalSymptom(MedicalCondition):
    possibleTreatment: Optional[Any] = None

