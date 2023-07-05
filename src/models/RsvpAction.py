from pydantic import BaseModel
from models.InformAction import InformAction

from typing import Optional, Any

class RsvpAction(InformAction):
    additionalNumberOfGuests: Optional[Any] = None
    comment: Optional[Any] = None
    rsvpResponse: Optional[Any] = None

