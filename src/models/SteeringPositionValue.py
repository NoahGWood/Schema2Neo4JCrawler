from pydantic import BaseModel
from typing import Optional, Any

class SteeringPositionValue(BaseModel):
    steeringPosition: Optional[Any] = None

