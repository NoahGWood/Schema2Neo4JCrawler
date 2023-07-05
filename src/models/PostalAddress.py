from pydantic import BaseModel
from models.ContactPoint import ContactPoint

from typing import Optional, Any

class PostalAddress(ContactPoint):
    addressCountry: Optional[Any] = None
    addressLocality: Optional[Any] = None
    addressRegion: Optional[Any] = None
    postOfficeBoxNumber: Optional[Any] = None
    postalCode: Optional[Any] = None
    streetAddress: Optional[Any] = None

