from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class FloorPlan(Thing):
    amenityFeature: Optional[Any] = None
    floorSize: Optional[Any] = None
    isPlanForApartment: Optional[Any] = None
    layoutImage: Optional[Any] = None
    numberOfAccommodationUnits: Optional[Any] = None
    numberOfAvailableAccommodationUnits: Optional[Any] = None
    numberOfBathroomsTotal: Optional[Any] = None
    numberOfBedrooms: Optional[Any] = None
    numberOfFullBathrooms: Optional[Any] = None
    numberOfPartialBathrooms: Optional[Any] = None
    numberOfRooms: Optional[Any] = None
    petsAllowed: Optional[Any] = None

