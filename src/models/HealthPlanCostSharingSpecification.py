from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class HealthPlanCostSharingSpecification(Thing):
    healthPlanCoinsuranceOption: Optional[Any] = None
    healthPlanCoinsuranceRate: Optional[Any] = None
    healthPlanCopay: Optional[Any] = None
    healthPlanCopayOption: Optional[Any] = None
    healthPlanPharmacyCategory: Optional[Any] = None

