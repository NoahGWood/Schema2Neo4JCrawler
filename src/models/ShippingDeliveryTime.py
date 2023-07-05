from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ShippingDeliveryTime(Thing):
    businessDays: Optional[Any] = None
    cutoffTime: Optional[Any] = None
    handlingTime: Optional[Any] = None
    transitTime: Optional[Any] = None

