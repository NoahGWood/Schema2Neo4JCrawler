from pydantic import BaseModel
from models.TradeAction import TradeAction

from typing import Optional, Any

class OrderAction(TradeAction):
    deliveryMethod: Optional[Any] = None

