from pydantic import BaseModel
from models.Trip import Trip

from typing import Optional, Any

class TouristTrip(Trip):
    touristType: Optional[Any] = None

