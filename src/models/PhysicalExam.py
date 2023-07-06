from pydantic import BaseModel
from typing import Optional, Any

class PhysicalExam(BaseModel):
    identifyingExam: Optional[Any] = None

