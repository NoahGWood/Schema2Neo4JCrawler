from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class OwnershipInfo(Thing):
    acquiredFrom: Optional[Any] = None
    ownedFrom: Optional[Any] = None
    ownedThrough: Optional[Any] = None
    typeOfGood: Optional[Any] = None

