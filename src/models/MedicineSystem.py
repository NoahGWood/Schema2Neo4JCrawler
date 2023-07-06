from pydantic import BaseModel
from typing import Optional, Any

class MedicineSystem(BaseModel):
    medicineSystem: Optional[Any] = None

