from pydantic import BaseModel
from typing import Optional, Any

class WarrantyScope(BaseModel):
    warrantyScope: Optional[Any] = None

