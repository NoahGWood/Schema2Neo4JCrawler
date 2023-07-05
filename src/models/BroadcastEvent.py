from pydantic import BaseModel
from models.PublicationEvent import PublicationEvent

from typing import Optional, Any

class BroadcastEvent(PublicationEvent):
    broadcastOfEvent: Optional[Any] = None
    isLiveBroadcast: Optional[Any] = None
    subtitleLanguage: Optional[Any] = None
    videoFormat: Optional[Any] = None

