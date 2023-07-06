from pydantic import BaseModel
from typing import Optional, Any

class RsvpResponseType(BaseModel):
    rsvpResponse: Optional[Any] = None

