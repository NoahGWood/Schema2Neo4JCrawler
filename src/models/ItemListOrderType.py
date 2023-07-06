from pydantic import BaseModel
from typing import Optional, Any

class ItemListOrderType(BaseModel):
    itemListOrder: Optional[Any] = None

