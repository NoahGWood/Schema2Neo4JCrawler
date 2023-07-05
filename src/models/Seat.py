from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Seat(Thing):
    seatNumber: Optional[Any] = None
    seatRow: Optional[Any] = None
    seatSection: Optional[Any] = None
    seatingType: Optional[Any] = None

