from pydantic import BaseModel
from typing import Optional, Any

class DrugCostCategory(BaseModel):
    costCategory: Optional[Any] = None

