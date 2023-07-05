from pydantic import BaseModel
from models.Organization import Organization

from typing import Optional, Any

class AutomotiveBusiness(Organization):
    currenciesAccepted: Optional[Any] = None
    openingHours: Optional[Any] = None
    paymentAccepted: Optional[Any] = None
    priceRange: Optional[Any] = None

