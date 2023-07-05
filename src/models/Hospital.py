from pydantic import BaseModel
from models.CivicStructure import CivicStructure

from typing import Optional, Any

class Hospital(CivicStructure):
    availableService: Optional[Any] = None
    healthcareReportingData: Optional[Any] = None
    medicalSpecialty: Optional[Any] = None

