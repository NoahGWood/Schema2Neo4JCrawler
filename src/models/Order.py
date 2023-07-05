from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Order(Thing):
    acceptedOffer: Optional[Any] = None
    billingAddress: Optional[Any] = None
    broker: Optional[Any] = None
    confirmationNumber: Optional[Any] = None
    customer: Optional[Any] = None
    discount: Optional[Any] = None
    discountCode: Optional[Any] = None
    discountCurrency: Optional[Any] = None
    isGift: Optional[Any] = None
    orderDate: Optional[Any] = None
    orderDelivery: Optional[Any] = None
    orderNumber: Optional[Any] = None
    orderStatus: Optional[Any] = None
    orderedItem: Optional[Any] = None
    partOfInvoice: Optional[Any] = None
    paymentDueDate: Optional[Any] = None
    paymentMethod: Optional[Any] = None
    paymentMethodId: Optional[Any] = None
    paymentUrl: Optional[Any] = None
    seller: Optional[Any] = None

