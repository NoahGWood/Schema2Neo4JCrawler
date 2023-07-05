from pydantic import BaseModel
from models.AnatomicalStructure import AnatomicalStructure

from typing import Optional, Any

class Nerve(AnatomicalStructure):
    nerveMotor: Optional[Any] = None
    sensoryUnit: Optional[Any] = None
    sourcedFrom: Optional[Any] = None

