from pydantic import BaseModel
from models.Reservation import Reservation

from typing import Optional, Any

class FoodEstablishmentReservation(Reservation):
    endTime: Optional[Any] = None
    partySize: Optional[Any] = None
    startTime: Optional[Any] = None

