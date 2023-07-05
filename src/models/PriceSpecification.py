from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class PriceSpecification(Thing):
    eligibleQuantity: Optional[Any] = None
    eligibleTransactionVolume: Optional[Any] = None
    maxPrice: Optional[Any] = None
    minPrice: Optional[Any] = None
    price: Optional[Any] = None
    priceCurrency: Optional[Any] = None
    validFrom: Optional[Any] = None
    validThrough: Optional[Any] = None
    valueAddedTaxIncluded: Optional[Any] = None

