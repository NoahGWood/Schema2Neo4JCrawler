from pydantic import BaseModel
from typing import Optional, Any

class PhysicalActivityCategory(BaseModel):
    category: Optional[Any] = None

