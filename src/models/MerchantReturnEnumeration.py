from pydantic import BaseModel
from typing import Optional, Any

class MerchantReturnEnumeration(BaseModel):
    returnPolicyCategory: Optional[Any] = None

