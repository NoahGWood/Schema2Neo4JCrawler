from pydantic import BaseModel
from models.Trip import Trip

from typing import Optional, Any

class BoatTrip(Trip):
    arrivalBoatTerminal: Optional[Any] = None
    departureBoatTerminal: Optional[Any] = None

