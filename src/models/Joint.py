from pydantic import BaseModel
from models.AnatomicalStructure import AnatomicalStructure

from typing import Optional, Any

class Joint(AnatomicalStructure):
    biomechnicalClass: Optional[Any] = None
    functionalClass: Optional[Any] = None
    structuralClass: Optional[Any] = None

