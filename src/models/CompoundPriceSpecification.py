from pydantic import BaseModel
from models.PriceSpecification import PriceSpecification

from typing import Optional, Any

class CompoundPriceSpecification(PriceSpecification):
    priceComponent: Optional[Any] = None
    priceType: Optional[Any] = None

