from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class HealthPlanFormulary(Thing):
    healthPlanCostSharing: Optional[Any] = None
    healthPlanDrugTier: Optional[Any] = None
    offersPrescriptionByMail: Optional[Any] = None

