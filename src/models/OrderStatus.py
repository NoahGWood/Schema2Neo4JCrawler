from pydantic import BaseModel
from typing import Optional, Any

class OrderStatus(BaseModel):
    orderItemStatus: Optional[Any] = None
    orderStatus: Optional[Any] = None

