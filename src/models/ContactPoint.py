from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ContactPoint(Thing):
    areaServed: Optional[Any] = None
    availableLanguage: Optional[Any] = None
    contactOption: Optional[Any] = None
    contactType: Optional[Any] = None
    email: Optional[Any] = None
    faxNumber: Optional[Any] = None
    hoursAvailable: Optional[Any] = None
    productSupported: Optional[Any] = None
    telephone: Optional[Any] = None

