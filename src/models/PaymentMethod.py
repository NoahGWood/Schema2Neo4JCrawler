from pydantic import BaseModel
from typing import Optional, Any

class PaymentMethod(BaseModel):
    acceptedPaymentMethod: Optional[Any] = None
    appliesToPaymentMethod: Optional[Any] = None
    paymentMethod: Optional[Any] = None

