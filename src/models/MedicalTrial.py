from pydantic import BaseModel
from models.MedicalStudy import MedicalStudy

from typing import Optional, Any

class MedicalTrial(MedicalStudy):
    trialDesign: Optional[Any] = None

