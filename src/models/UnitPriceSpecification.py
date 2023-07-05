from pydantic import BaseModel
from models.PriceSpecification import PriceSpecification

from typing import Optional, Any

class UnitPriceSpecification(PriceSpecification):
    billingDuration: Optional[Any] = None
    billingIncrement: Optional[Any] = None
    billingStart: Optional[Any] = None
    priceComponentType: Optional[Any] = None
    priceType: Optional[Any] = None
    referenceQuantity: Optional[Any] = None
    unitCode: Optional[Any] = None
    unitText: Optional[Any] = None

