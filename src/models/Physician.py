from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class Physician(LocalBusiness):
    availableService: Optional[Any] = None
    hospitalAffiliation: Optional[Any] = None
    medicalSpecialty: Optional[Any] = None

