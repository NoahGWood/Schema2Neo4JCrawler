from pydantic import BaseModel
from models.LocalBusiness import LocalBusiness

from typing import Optional, Any

class StadiumOrArena(LocalBusiness):
    openingHours: Optional[Any] = None

