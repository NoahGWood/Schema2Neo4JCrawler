from pydantic import BaseModel
from typing import Optional, Any

class MapCategoryType(BaseModel):
    mapType: Optional[Any] = None

