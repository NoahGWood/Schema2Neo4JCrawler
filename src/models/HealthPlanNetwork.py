from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class HealthPlanNetwork(Thing):
    healthPlanCostSharing: Optional[Any] = None
    healthPlanNetworkId: Optional[Any] = None
    healthPlanNetworkTier: Optional[Any] = None

