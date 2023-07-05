from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class BloodTest(MedicalEntity):
    affectedBy: Optional[Any] = None
    normalRange: Optional[Any] = None
    signDetected: Optional[Any] = None
    usedToDiagnose: Optional[Any] = None
    usesDevice: Optional[Any] = None

