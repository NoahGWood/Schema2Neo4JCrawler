from pydantic import BaseModel
from typing import Optional, Any

class RefundTypeEnumeration(BaseModel):
    refundType: Optional[Any] = None

