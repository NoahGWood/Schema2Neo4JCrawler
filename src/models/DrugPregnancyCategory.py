from pydantic import BaseModel
from typing import Optional, Any

class DrugPregnancyCategory(BaseModel):
    pregnancyCategory: Optional[Any] = None

