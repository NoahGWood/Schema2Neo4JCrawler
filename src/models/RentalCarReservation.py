from pydantic import BaseModel
from models.Reservation import Reservation

from typing import Optional, Any

class RentalCarReservation(Reservation):
    dropoffLocation: Optional[Any] = None
    dropoffTime: Optional[Any] = None
    pickupLocation: Optional[Any] = None
    pickupTime: Optional[Any] = None

