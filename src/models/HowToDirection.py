from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class HowToDirection(CreativeWork):
    afterMedia: Optional[Any] = None
    beforeMedia: Optional[Any] = None
    duringMedia: Optional[Any] = None
    performTime: Optional[Any] = None
    prepTime: Optional[Any] = None
    supply: Optional[Any] = None
    tool: Optional[Any] = None
    totalTime: Optional[Any] = None

