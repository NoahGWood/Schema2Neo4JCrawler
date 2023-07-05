from pydantic import BaseModel
from models.MedicalOrganization import MedicalOrganization

from typing import Optional, Any

class DiagnosticLab(MedicalOrganization):
    availableTest: Optional[Any] = None

