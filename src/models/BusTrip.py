from pydantic import BaseModel
from models.Trip import Trip

from typing import Optional, Any

class BusTrip(Trip):
    arrivalBusStop: Optional[Any] = None
    busName: Optional[Any] = None
    busNumber: Optional[Any] = None
    departureBusStop: Optional[Any] = None

