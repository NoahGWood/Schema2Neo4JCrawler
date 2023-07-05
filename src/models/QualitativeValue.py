from pydantic import BaseModel
from models.Enumeration import Enumeration

from typing import Optional, Any

class QualitativeValue(Enumeration):
    additionalProperty: Optional[Any] = None
    equal: Optional[Any] = None
    greater: Optional[Any] = None
    greaterOrEqual: Optional[Any] = None
    lesser: Optional[Any] = None
    lesserOrEqual: Optional[Any] = None
    nonEqual: Optional[Any] = None
    valueReference: Optional[Any] = None

