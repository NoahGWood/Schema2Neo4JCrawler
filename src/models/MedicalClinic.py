from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class MedicalClinic(LocalBusiness):
    availableService: Optional[Any] = None
    medicalSpecialty: Optional[Any] = None

