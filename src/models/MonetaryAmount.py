from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class MonetaryAmount(Thing):
    currency: Optional[Any] = None
    maxValue: Optional[Any] = None
    minValue: Optional[Any] = None
    validFrom: Optional[Any] = None
    validThrough: Optional[Any] = None
    value: Optional[Any] = None

