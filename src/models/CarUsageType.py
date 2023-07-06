from pydantic import BaseModel
from typing import Optional, Any

class CarUsageType(BaseModel):
    vehicleSpecialUsage: Optional[Any] = None

