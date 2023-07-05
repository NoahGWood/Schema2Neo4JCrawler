from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Invoice(Thing):
    accountId: Optional[Any] = None
    billingPeriod: Optional[Any] = None
    broker: Optional[Any] = None
    category: Optional[Any] = None
    confirmationNumber: Optional[Any] = None
    customer: Optional[Any] = None
    minimumPaymentDue: Optional[Any] = None
    paymentDueDate: Optional[Any] = None
    paymentMethod: Optional[Any] = None
    paymentMethodId: Optional[Any] = None
    paymentStatus: Optional[Any] = None
    provider: Optional[Any] = None
    referencesOrder: Optional[Any] = None
    scheduledPaymentDate: Optional[Any] = None
    totalPaymentDue: Optional[Any] = None

