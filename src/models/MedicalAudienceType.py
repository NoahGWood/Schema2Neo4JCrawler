from pydantic import BaseModel
from typing import Optional, Any

class MedicalAudienceType(BaseModel):
    medicalAudience: Optional[Any] = None

