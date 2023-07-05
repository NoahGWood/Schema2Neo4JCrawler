from pydantic import BaseModel
from models.CivicStructure import CivicStructure

from typing import Optional, Any

class MovieTheater(CivicStructure):
    screenCount: Optional[Any] = None

