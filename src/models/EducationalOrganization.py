from pydantic import BaseModel
from models.CivicStructure import CivicStructure

from typing import Optional, Any

class EducationalOrganization(CivicStructure):
    alumni: Optional[Any] = None

