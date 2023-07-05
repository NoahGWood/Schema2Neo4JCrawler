from pydantic import BaseModel
from models.Event import Event

from typing import Optional, Any

class PublicationEvent(Event):
    publishedBy: Optional[Any] = None
    publishedOn: Optional[Any] = None

