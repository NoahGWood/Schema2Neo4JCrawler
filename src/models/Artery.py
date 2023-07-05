from pydantic import BaseModel
from models.AnatomicalStructure import AnatomicalStructure

from typing import Optional, Any

class Artery(AnatomicalStructure):
    arterialBranch: Optional[Any] = None
    supplyTo: Optional[Any] = None

