from pydantic import BaseModel
from models.TradeAction import TradeAction

from typing import Optional, Any

class RentAction(TradeAction):
    landlord: Optional[Any] = None
    realEstateAgent: Optional[Any] = None

