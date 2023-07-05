from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class QuantitativeValue(Thing):
    additionalProperty: Optional[Any] = None
    maxValue: Optional[Any] = None
    minValue: Optional[Any] = None
    unitCode: Optional[Any] = None
    unitText: Optional[Any] = None
    value: Optional[Any] = None
    valueReference: Optional[Any] = None

