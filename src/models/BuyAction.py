from pydantic import BaseModel
from models.TradeAction import TradeAction

from typing import Optional, Any

class BuyAction(TradeAction):
    seller: Optional[Any] = None

