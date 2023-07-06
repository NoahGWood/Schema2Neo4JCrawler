from pydantic import BaseModel
from typing import Optional, Any

class LegalForceStatus(BaseModel):
    legislationLegalForce: Optional[Any] = None

