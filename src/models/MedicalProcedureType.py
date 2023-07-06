from pydantic import BaseModel
from typing import Optional, Any

class MedicalProcedureType(BaseModel):
    procedureType: Optional[Any] = None

