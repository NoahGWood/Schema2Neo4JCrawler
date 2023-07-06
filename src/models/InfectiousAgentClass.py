from pydantic import BaseModel
from typing import Optional, Any

class InfectiousAgentClass(BaseModel):
    infectiousAgentClass: Optional[Any] = None

