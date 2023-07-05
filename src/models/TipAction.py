from pydantic import BaseModel
from models.TradeAction import TradeAction

from typing import Optional, Any

class TipAction(TradeAction):
    recipient: Optional[Any] = None

