from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class SurgicalProcedure(MedicalEntity):
    bodyLocation: Optional[Any] = None
    followup: Optional[Any] = None
    howPerformed: Optional[Any] = None
    preparation: Optional[Any] = None
    procedureType: Optional[Any] = None
    status: Optional[Any] = None

