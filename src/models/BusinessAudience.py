from pydantic import BaseModel
from models.Audience import Audience

from typing import Optional, Any

class BusinessAudience(Audience):
    numberOfEmployees: Optional[Any] = None
    yearlyRevenue: Optional[Any] = None
    yearsInOperation: Optional[Any] = None

