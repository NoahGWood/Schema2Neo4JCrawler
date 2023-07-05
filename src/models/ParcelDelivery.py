from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ParcelDelivery(Thing):
    deliveryAddress: Optional[Any] = None
    deliveryStatus: Optional[Any] = None
    expectedArrivalFrom: Optional[Any] = None
    expectedArrivalUntil: Optional[Any] = None
    hasDeliveryMethod: Optional[Any] = None
    itemShipped: Optional[Any] = None
    originAddress: Optional[Any] = None
    partOfOrder: Optional[Any] = None
    provider: Optional[Any] = None
    trackingNumber: Optional[Any] = None
    trackingUrl: Optional[Any] = None

