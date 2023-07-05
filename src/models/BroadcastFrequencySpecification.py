from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class BroadcastFrequencySpecification(Thing):
    broadcastFrequencyValue: Optional[Any] = None
    broadcastSignalModulation: Optional[Any] = None
    broadcastSubChannel: Optional[Any] = None

