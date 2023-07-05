from pydantic import BaseModel
from models.LodgingBusiness import LodgingBusiness

from typing import Optional, Any

class Campground(LodgingBusiness):
    openingHours: Optional[Any] = None

