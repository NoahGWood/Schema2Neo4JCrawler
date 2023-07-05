from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class PropertyValue(Thing):
    maxValue: Optional[Any] = None
    measurementMethod: Optional[Any] = None
    measurementTechnique: Optional[Any] = None
    minValue: Optional[Any] = None
    propertyID: Optional[Any] = None
    unitCode: Optional[Any] = None
    unitText: Optional[Any] = None
    value: Optional[Any] = None
    valueReference: Optional[Any] = None

