from pydantic import BaseModel
from models.PropertyValue import PropertyValue

from typing import Optional, Any

class LocationFeatureSpecification(PropertyValue):
    hoursAvailable: Optional[Any] = None
    validFrom: Optional[Any] = None
    validThrough: Optional[Any] = None

