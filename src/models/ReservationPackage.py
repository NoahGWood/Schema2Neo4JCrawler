from pydantic import BaseModel
from models.Reservation import Reservation

from typing import Optional, Any

class ReservationPackage(Reservation):
    subReservation: Optional[Any] = None

