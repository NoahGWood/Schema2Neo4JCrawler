from pydantic import BaseModel
from typing import Optional, Any

class MedicalTrialDesign(BaseModel):
    trialDesign: Optional[Any] = None

