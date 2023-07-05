from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class ExchangeRateSpecification(Thing):
    currency: Optional[Any] = None
    currentExchangeRate: Optional[Any] = None
    exchangeRateSpread: Optional[Any] = None

