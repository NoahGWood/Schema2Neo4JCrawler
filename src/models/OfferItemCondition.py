from pydantic import BaseModel
from typing import Optional, Any

class OfferItemCondition(BaseModel):
    itemCondition: Optional[Any] = None

