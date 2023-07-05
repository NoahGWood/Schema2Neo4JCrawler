from pydantic import BaseModel
from models.TradeAction import TradeAction

from typing import Optional, Any

class DonateAction(TradeAction):
    recipient: Optional[Any] = None

