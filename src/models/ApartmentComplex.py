from pydantic import BaseModel
from models.Residence import Residence

from typing import Optional, Any

class ApartmentComplex(Residence):
    numberOfAccommodationUnits: Optional[Any] = None
    numberOfAvailableAccommodationUnits: Optional[Any] = None
    numberOfBedrooms: Optional[Any] = None
    petsAllowed: Optional[Any] = None
    tourBookingPage: Optional[Any] = None

