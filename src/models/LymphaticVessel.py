from pydantic import BaseModel
from models.AnatomicalStructure import AnatomicalStructure

from typing import Optional, Any

class LymphaticVessel(AnatomicalStructure):
    originatesFrom: Optional[Any] = None
    regionDrained: Optional[Any] = None
    runsTo: Optional[Any] = None

