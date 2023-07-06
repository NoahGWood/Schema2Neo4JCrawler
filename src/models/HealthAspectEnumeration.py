from pydantic import BaseModel
from typing import Optional, Any

class HealthAspectEnumeration(BaseModel):
    hasHealthAspect: Optional[Any] = None

