from pydantic import BaseModel
from models.Trip import Trip

from typing import Optional, Any

class Flight(Trip):
    aircraft: Optional[Any] = None
    arrivalAirport: Optional[Any] = None
    arrivalGate: Optional[Any] = None
    arrivalTerminal: Optional[Any] = None
    boardingPolicy: Optional[Any] = None
    departureAirport: Optional[Any] = None
    departureGate: Optional[Any] = None
    departureTerminal: Optional[Any] = None
    estimatedFlightDuration: Optional[Any] = None
    flightDistance: Optional[Any] = None
    flightNumber: Optional[Any] = None
    mealService: Optional[Any] = None
    seller: Optional[Any] = None
    webCheckinTime: Optional[Any] = None

