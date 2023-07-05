from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class DatedMoneySpecification(Thing):
    amount: Optional[Any] = None
    currency: Optional[Any] = None
    endDate: Optional[Any] = None
    startDate: Optional[Any] = None

