from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class Ticket(Thing):
    dateIssued: Optional[Any] = None
    issuedBy: Optional[Any] = None
    priceCurrency: Optional[Any] = None
    ticketNumber: Optional[Any] = None
    ticketToken: Optional[Any] = None
    ticketedSeat: Optional[Any] = None
    totalPrice: Optional[Any] = None
    underName: Optional[Any] = None

