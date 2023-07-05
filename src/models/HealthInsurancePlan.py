from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class HealthInsurancePlan(Thing):
    benefitsSummaryUrl: Optional[Any] = None
    contactPoint: Optional[Any] = None
    healthPlanDrugOption: Optional[Any] = None
    healthPlanDrugTier: Optional[Any] = None
    healthPlanId: Optional[Any] = None
    healthPlanMarketingUrl: Optional[Any] = None
    includesHealthPlanFormulary: Optional[Any] = None
    includesHealthPlanNetwork: Optional[Any] = None
    usesHealthPlanIdStandard: Optional[Any] = None

