from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class DefinedRegion(Thing):
    addressCountry: Optional[Any] = None
    addressRegion: Optional[Any] = None
    postalCode: Optional[Any] = None
    postalCodePrefix: Optional[Any] = None
    postalCodeRange: Optional[Any] = None

