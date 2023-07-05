from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class EducationalOccupationalCredential(CreativeWork):
    competencyRequired: Optional[Any] = None
    credentialCategory: Optional[Any] = None
    educationalLevel: Optional[Any] = None
    recognizedBy: Optional[Any] = None
    validFor: Optional[Any] = None
    validIn: Optional[Any] = None

