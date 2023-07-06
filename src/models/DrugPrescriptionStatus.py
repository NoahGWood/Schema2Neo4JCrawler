from pydantic import BaseModel
from typing import Optional, Any

class DrugPrescriptionStatus(BaseModel):
    prescriptionStatus: Optional[Any] = None

