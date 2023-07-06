from pydantic import BaseModel
from typing import Optional, Any

class Specialty(BaseModel):
    specialty: Optional[Any] = None

