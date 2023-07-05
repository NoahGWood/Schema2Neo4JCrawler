from pydantic import BaseModel
from models.Event import Event

from typing import Optional, Any

class DeliveryEvent(Event):
    accessCode: Optional[Any] = None
    availableFrom: Optional[Any] = None
    availableThrough: Optional[Any] = None
    hasDeliveryMethod: Optional[Any] = None

