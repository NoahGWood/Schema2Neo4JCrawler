from pydantic import BaseModel
from models.Place import Place

from typing import Optional, Any

class HinduTemple(Place):
    openingHours: Optional[Any] = None

