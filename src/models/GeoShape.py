from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class GeoShape(Thing):
    address: Optional[Any] = None
    addressCountry: Optional[Any] = None
    box: Optional[Any] = None
    circle: Optional[Any] = None
    elevation: Optional[Any] = None
    line: Optional[Any] = None
    polygon: Optional[Any] = None
    postalCode: Optional[Any] = None

