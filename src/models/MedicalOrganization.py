from pydantic import BaseModel
from models.Organization import Organization

from typing import Optional, Any

class MedicalOrganization(Organization):
    healthPlanNetworkId: Optional[Any] = None
    isAcceptingNewPatients: Optional[Any] = None
    medicalSpecialty: Optional[Any] = None

