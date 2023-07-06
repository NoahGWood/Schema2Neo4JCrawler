from pydantic import BaseModel
from typing import Optional, Any

class PaymentStatusType(BaseModel):
    paymentStatus: Optional[Any] = None

