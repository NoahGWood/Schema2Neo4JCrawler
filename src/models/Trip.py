from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Trip(Thing):
    arrivalTime: Optional[Any] = None
    departureTime: Optional[Any] = None
    itinerary: Optional[Any] = None
    offers: Optional[Any] = None
    partOfTrip: Optional[Any] = None
    provider: Optional[Any] = None
    subTrip: Optional[Any] = None
    tripOrigin: Optional[Any] = None

