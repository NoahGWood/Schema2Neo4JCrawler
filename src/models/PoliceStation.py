from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class PoliceStation(LocalBusiness):
    openingHours: Optional[Any] = None

