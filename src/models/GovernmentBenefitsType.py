from pydantic import BaseModel
from typing import Optional, Any

class GovernmentBenefitsType(BaseModel):
    serviceType: Optional[Any] = None

