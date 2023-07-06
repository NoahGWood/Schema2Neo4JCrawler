from pydantic import BaseModel
from typing import Optional, Any

class BoardingPolicyType(BaseModel):
    boardingPolicy: Optional[Any] = None

