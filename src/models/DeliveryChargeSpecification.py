from pydantic import BaseModel
from models.PriceSpecification import PriceSpecification

from typing import Optional, Any

class DeliveryChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod: Optional[Any] = None
    areaServed: Optional[Any] = None
    eligibleRegion: Optional[Any] = None
    ineligibleRegion: Optional[Any] = None

