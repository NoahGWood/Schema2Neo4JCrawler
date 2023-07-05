from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class Hotel(LocalBusiness):
    amenityFeature: Optional[Any] = None
    audience: Optional[Any] = None
    availableLanguage: Optional[Any] = None
    checkinTime: Optional[Any] = None
    checkoutTime: Optional[Any] = None
    numberOfRooms: Optional[Any] = None
    petsAllowed: Optional[Any] = None
    starRating: Optional[Any] = None

