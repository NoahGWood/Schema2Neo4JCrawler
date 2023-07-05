from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class QuoteAction(Action):
    price: Optional[Any] = None
    priceCurrency: Optional[Any] = None
    priceSpecification: Optional[Any] = None

