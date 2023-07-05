from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class DeliveryTimeSettings(Thing):
    deliveryTime: Optional[Any] = None
    isUnlabelledFallback: Optional[Any] = None
    shippingDestination: Optional[Any] = None
    transitTimeLabel: Optional[Any] = None

