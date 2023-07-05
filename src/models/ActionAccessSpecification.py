from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ActionAccessSpecification(Thing):
    availabilityEnds: Optional[Any] = None
    availabilityStarts: Optional[Any] = None
    category: Optional[Any] = None
    eligibleRegion: Optional[Any] = None
    expectsAcceptanceOf: Optional[Any] = None
    ineligibleRegion: Optional[Any] = None
    requiresSubscription: Optional[Any] = None

