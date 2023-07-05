from pydantic import BaseModel
from models.MedicalEntity import MedicalEntity

from typing import Optional, Any

class DrugLegalStatus(MedicalEntity):
    applicableLocation: Optional[Any] = None

