from pydantic import BaseModel
from models.TherapeuticProcedure import TherapeuticProcedure

from typing import Optional, Any

class MedicalTherapy(TherapeuticProcedure):
    contraindication: Optional[Any] = None
    duplicateTherapy: Optional[Any] = None
    seriousAdverseOutcome: Optional[Any] = None

