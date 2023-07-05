from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class EnergyConsumptionDetails(Thing):
    energyEfficiencyScaleMax: Optional[Any] = None
    energyEfficiencyScaleMin: Optional[Any] = None
    hasEnergyEfficiencyCategory: Optional[Any] = None

