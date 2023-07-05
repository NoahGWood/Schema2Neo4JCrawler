from pydantic import BaseModel
from models.Service import Service

from typing import Optional, Any

class RadioBroadcastService(Service):
    broadcastAffiliateOf: Optional[Any] = None
    broadcastDisplayName: Optional[Any] = None
    broadcastFrequency: Optional[Any] = None
    broadcastTimezone: Optional[Any] = None
    broadcaster: Optional[Any] = None
    callSign: Optional[Any] = None
    hasBroadcastChannel: Optional[Any] = None
    inLanguage: Optional[Any] = None
    parentService: Optional[Any] = None
    videoFormat: Optional[Any] = None

