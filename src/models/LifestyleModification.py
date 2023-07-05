from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class LifestyleModification(Thing):
    code: Optional[Any] = None
    funding: Optional[Any] = None
    guideline: Optional[Any] = None
    legalStatus: Optional[Any] = None
    medicineSystem: Optional[Any] = None
    recognizingAuthority: Optional[Any] = None
    relevantSpecialty: Optional[Any] = None
    study: Optional[Any] = None

