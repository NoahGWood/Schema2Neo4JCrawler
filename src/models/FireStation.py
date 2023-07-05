from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class FireStation(LocalBusiness):
    openingHours: Optional[Any] = None

