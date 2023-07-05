from pydantic import BaseModel
from models.TradeAction import TradeAction

from typing import Optional, Any

class SellAction(TradeAction):
    buyer: Optional[Any] = None

