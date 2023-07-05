from pydantic import BaseModel
from models.Place import Place

from typing import Optional, Any

class Dentist(Place):
    currenciesAccepted: Optional[Any] = None
    openingHours: Optional[Any] = None
    paymentAccepted: Optional[Any] = None
    priceRange: Optional[Any] = None

