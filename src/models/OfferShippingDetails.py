from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class OfferShippingDetails(Thing):
    deliveryTime: Optional[Any] = None
    depth: Optional[Any] = None
    doesNotShip: Optional[Any] = None
    height: Optional[Any] = None
    shippingDestination: Optional[Any] = None
    shippingLabel: Optional[Any] = None
    shippingOrigin: Optional[Any] = None
    shippingRate: Optional[Any] = None
    shippingSettingsLink: Optional[Any] = None
    transitTimeLabel: Optional[Any] = None
    weight: Optional[Any] = None
    width: Optional[Any] = None

