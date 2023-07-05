from pydantic import BaseModel
from models.HowToItem import HowToItem

from typing import Optional, Any

class HowToSupply(HowToItem):
    estimatedCost: Optional[Any] = None

