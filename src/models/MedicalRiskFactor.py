from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class MedicalRiskFactor(MedicalEntity):
    increasesRiskOf: Optional[Any] = None

