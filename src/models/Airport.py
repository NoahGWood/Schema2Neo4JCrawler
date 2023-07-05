from pydantic import BaseModel
from models.CivicStructure import CivicStructure

from typing import Optional, Any

class Airport(CivicStructure):
    iataCode: Optional[Any] = None
    icaoCode: Optional[Any] = None

