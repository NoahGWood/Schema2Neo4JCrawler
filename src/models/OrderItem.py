from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class OrderItem(Thing):
    orderDelivery: Optional[Any] = None
    orderItemNumber: Optional[Any] = None
    orderItemStatus: Optional[Any] = None
    orderQuantity: Optional[Any] = None
    orderedItem: Optional[Any] = None

