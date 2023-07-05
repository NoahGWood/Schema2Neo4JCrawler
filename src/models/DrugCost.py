from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class DrugCost(MedicalEntity):
    applicableLocation: Optional[Any] = None
    costCategory: Optional[Any] = None
    costCurrency: Optional[Any] = None
    costOrigin: Optional[Any] = None
    costPerUnit: Optional[Any] = None
    drugUnit: Optional[Any] = None

