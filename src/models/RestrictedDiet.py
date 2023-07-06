from pydantic import BaseModel
from typing import Optional, Any

class RestrictedDiet(BaseModel):
    suitableForDiet: Optional[Any] = None

