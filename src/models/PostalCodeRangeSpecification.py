from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class PostalCodeRangeSpecification(Thing):
    postalCodeBegin: Optional[Any] = None
    postalCodeEnd: Optional[Any] = None

