from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class GovernmentPermit(Thing):
    issuedBy: Optional[Any] = None
    issuedThrough: Optional[Any] = None
    permitAudience: Optional[Any] = None
    validFor: Optional[Any] = None
    validFrom: Optional[Any] = None
    validIn: Optional[Any] = None
    validUntil: Optional[Any] = None

