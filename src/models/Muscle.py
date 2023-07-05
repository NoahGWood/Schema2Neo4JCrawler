from pydantic import BaseModel
from models.AnatomicalStructure import AnatomicalStructure

from typing import Optional, Any

class Muscle(AnatomicalStructure):
    antagonist: Optional[Any] = None
    bloodSupply: Optional[Any] = None
    insertion: Optional[Any] = None
    muscleAction: Optional[Any] = None
    nerve: Optional[Any] = None

