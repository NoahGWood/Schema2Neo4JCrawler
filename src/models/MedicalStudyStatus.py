from pydantic import BaseModel
from typing import Optional, Any

class MedicalStudyStatus(BaseModel):
    status: Optional[Any] = None

