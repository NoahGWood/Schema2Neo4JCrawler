from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class TrainReservation(Thing):
    bookingTime: Optional[Any] = None
    broker: Optional[Any] = None
    modifiedTime: Optional[Any] = None
    priceCurrency: Optional[Any] = None
    programMembershipUsed: Optional[Any] = None
    provider: Optional[Any] = None
    reservationFor: Optional[Any] = None
    reservationId: Optional[Any] = None
    reservationStatus: Optional[Any] = None
    reservedTicket: Optional[Any] = None
    totalPrice: Optional[Any] = None
    underName: Optional[Any] = None

