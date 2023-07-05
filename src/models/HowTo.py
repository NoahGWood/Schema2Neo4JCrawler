from pydantic import BaseModel
from models.CreativeWork import CreativeWork

from typing import Optional, Any

class HowTo(CreativeWork):
    estimatedCost: Optional[Any] = None
    performTime: Optional[Any] = None
    prepTime: Optional[Any] = None
    step: Optional[Any] = None
    supply: Optional[Any] = None
    tool: Optional[Any] = None
    totalTime: Optional[Any] = None
    yield: Optional[Any] = None

