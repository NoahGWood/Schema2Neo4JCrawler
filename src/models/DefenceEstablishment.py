from pydantic import BaseModel
from models.Place import Place

from typing import Optional, Any

class DefenceEstablishment(Place):
    openingHours: Optional[Any] = None

