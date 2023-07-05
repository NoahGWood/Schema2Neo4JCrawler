from pydantic import BaseModel
from models.Trip import Trip

from typing import Optional, Any

class TrainTrip(Trip):
    arrivalPlatform: Optional[Any] = None
    arrivalStation: Optional[Any] = None
    departurePlatform: Optional[Any] = None
    departureStation: Optional[Any] = None
    trainName: Optional[Any] = None
    trainNumber: Optional[Any] = None

