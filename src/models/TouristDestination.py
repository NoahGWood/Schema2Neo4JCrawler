from pydantic import BaseModel
from models.Place import Place

from typing import Optional, Any

class TouristDestination(Place):
    includesAttraction: Optional[Any] = None
    touristType: Optional[Any] = None

