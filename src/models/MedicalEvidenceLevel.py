from pydantic import BaseModel
from typing import Optional, Any

class MedicalEvidenceLevel(BaseModel):
    evidenceLevel: Optional[Any] = None

