from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ShippingRateSettings(Thing):
    doesNotShip: Optional[Any] = None
    freeShippingThreshold: Optional[Any] = None
    isUnlabelledFallback: Optional[Any] = None
    shippingDestination: Optional[Any] = None
    shippingLabel: Optional[Any] = None
    shippingRate: Optional[Any] = None

