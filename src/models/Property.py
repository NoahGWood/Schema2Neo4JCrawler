from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Property(Thing):
    domainIncludes: Optional[Any] = None
    inverseOf: Optional[Any] = None
    rangeIncludes: Optional[Any] = None
    supersededBy: Optional[Any] = None

