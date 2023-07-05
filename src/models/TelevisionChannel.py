from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class TelevisionChannel(Thing):
    broadcastChannelId: Optional[Any] = None
    broadcastFrequency: Optional[Any] = None
    broadcastServiceTier: Optional[Any] = None
    genre: Optional[Any] = None
    inBroadcastLineup: Optional[Any] = None
    providesBroadcastService: Optional[Any] = None

