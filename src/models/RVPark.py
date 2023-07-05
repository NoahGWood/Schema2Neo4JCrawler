from pydantic import BaseModel
from models.Place import Place

from typing import Optional, Any

class RVPark(Place):
    openingHours: Optional[Any] = None

