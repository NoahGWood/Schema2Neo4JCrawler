from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class MedicalRiskCalculator(MedicalEntity):
    estimatesRiskOf: Optional[Any] = None
    includedRiskFactor: Optional[Any] = None

