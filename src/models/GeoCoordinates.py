from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class GeoCoordinates(Thing):
    address: Optional[Any] = None
    addressCountry: Optional[Any] = None
    elevation: Optional[Any] = None
    latitude: Optional[Any] = None
    longitude: Optional[Any] = None
    postalCode: Optional[Any] = None

