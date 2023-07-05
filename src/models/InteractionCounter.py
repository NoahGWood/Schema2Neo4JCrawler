from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class InteractionCounter(Thing):
    endTime: Optional[Any] = None
    interactionService: Optional[Any] = None
    interactionType: Optional[Any] = None
    location: Optional[Any] = None
    startTime: Optional[Any] = None
    userInteractionCount: Optional[Any] = None

