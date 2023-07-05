from pydantic import BaseModel
from models.Place import Place

from typing import Optional, Any

class CampingPitch(Place):
    accommodationCategory: Optional[Any] = None
    accommodationFloorPlan: Optional[Any] = None
    amenityFeature: Optional[Any] = None
    bed: Optional[Any] = None
    floorLevel: Optional[Any] = None
    floorSize: Optional[Any] = None
    leaseLength: Optional[Any] = None
    numberOfBathroomsTotal: Optional[Any] = None
    numberOfBedrooms: Optional[Any] = None
    numberOfFullBathrooms: Optional[Any] = None
    numberOfPartialBathrooms: Optional[Any] = None
    numberOfRooms: Optional[Any] = None
    occupancy: Optional[Any] = None
    permittedUsage: Optional[Any] = None
    petsAllowed: Optional[Any] = None
    tourBookingPage: Optional[Any] = None
    yearBuilt: Optional[Any] = None

