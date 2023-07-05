from pydantic import BaseModel
from models.QuantitativeValueDistribution import QuantitativeValueDistribution

from typing import Optional, Any

class MonetaryAmountDistribution(QuantitativeValueDistribution):
    currency: Optional[Any] = None

