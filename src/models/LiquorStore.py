from pydantic import BaseModel
from models.Organization import Organization

from typing import Optional, Any

class LiquorStore(Organization):
    currenciesAccepted: Optional[Any] = None
    openingHours: Optional[Any] = None
    paymentAccepted: Optional[Any] = None
    priceRange: Optional[Any] = None

