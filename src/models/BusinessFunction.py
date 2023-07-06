from pydantic import BaseModel
from typing import Optional, Any

class BusinessFunction(BaseModel):
    businessFunction: Optional[Any] = None

