from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class TypeAndQuantityNode(Thing):
    amountOfThisGood: Optional[Any] = None
    businessFunction: Optional[Any] = None
    typeOfGood: Optional[Any] = None
    unitCode: Optional[Any] = None
    unitText: Optional[Any] = None

