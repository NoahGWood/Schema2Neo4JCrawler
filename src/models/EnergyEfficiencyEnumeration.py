from pydantic import BaseModel
from typing import Optional, Any

class EnergyEfficiencyEnumeration(BaseModel):
    hasEnergyEfficiencyCategory: Optional[Any] = None

