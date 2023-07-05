from pydantic import BaseModel
from models.MedicalSignOrSymptom import MedicalSignOrSymptom

from typing import Optional, Any

class VitalSign(MedicalSignOrSymptom):
    identifyingExam: Optional[Any] = None
    identifyingTest: Optional[Any] = None

