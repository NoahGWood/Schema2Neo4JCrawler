from pydantic import BaseModel
from models.PriceSpecification import PriceSpecification

from typing import Optional, Any

class PaymentChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod: Optional[Any] = None
    appliesToPaymentMethod: Optional[Any] = None

