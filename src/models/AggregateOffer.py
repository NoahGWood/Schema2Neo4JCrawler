from pydantic import BaseModel
from models.Offer import Offer

from typing import Optional, Any

class AggregateOffer(Offer):
    highPrice: Optional[Any] = None
    lowPrice: Optional[Any] = None
    offerCount: Optional[Any] = None
    offers: Optional[Any] = None

