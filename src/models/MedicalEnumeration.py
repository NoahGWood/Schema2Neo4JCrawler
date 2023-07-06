from pydantic import BaseModel
from typing import Optional, Any

class MedicalEnumeration(BaseModel):
    legalStatus: Optional[Any] = None
    normalRange: Optional[Any] = None

