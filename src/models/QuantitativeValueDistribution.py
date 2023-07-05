from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class QuantitativeValueDistribution(Thing):
    duration: Optional[Any] = None
    median: Optional[Any] = None
    percentile10: Optional[Any] = None
    percentile25: Optional[Any] = None
    percentile75: Optional[Any] = None
    percentile90: Optional[Any] = None

