from pydantic import BaseModel
from models.Reservation import Reservation

from typing import Optional, Any

class TaxiReservation(Reservation):
    partySize: Optional[Any] = None
    pickupLocation: Optional[Any] = None
    pickupTime: Optional[Any] = None

