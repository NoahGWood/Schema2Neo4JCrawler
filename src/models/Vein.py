from pydantic import BaseModel
from models.AnatomicalStructure import AnatomicalStructure

from typing import Optional, Any

class Vein(AnatomicalStructure):
    drainsTo: Optional[Any] = None
    regionDrained: Optional[Any] = None
    tributary: Optional[Any] = None

