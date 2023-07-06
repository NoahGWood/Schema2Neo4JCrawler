from pydantic import BaseModel
from typing import Optional, Any

class ReservationStatusType(BaseModel):
    reservationStatus: Optional[Any] = None

