from pydantic import BaseModel
from models.Reservation import Reservation

from typing import Optional, Any

class FlightReservation(Reservation):
    boardingGroup: Optional[Any] = None
    passengerPriorityStatus: Optional[Any] = None
    passengerSequenceNumber: Optional[Any] = None
    securityScreening: Optional[Any] = None

