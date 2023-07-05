from pydantic import BaseModel
from models.Reservation import Reservation

from typing import Optional, Any

class LodgingReservation(Reservation):
    checkinTime: Optional[Any] = None
    checkoutTime: Optional[Any] = None
    lodgingUnitDescription: Optional[Any] = None
    lodgingUnitType: Optional[Any] = None
    numAdults: Optional[Any] = None
    numChildren: Optional[Any] = None

