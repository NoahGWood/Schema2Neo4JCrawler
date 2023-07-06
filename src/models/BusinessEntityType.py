from pydantic import BaseModel
from typing import Optional, Any

class BusinessEntityType(BaseModel):
    eligibleCustomerType: Optional[Any] = None

