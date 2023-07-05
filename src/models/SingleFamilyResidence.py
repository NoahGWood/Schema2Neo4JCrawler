from pydantic import BaseModel
from models.House import House

from typing import Optional, Any

class SingleFamilyResidence(House):
    numberOfRooms: Optional[Any] = None
    occupancy: Optional[Any] = None

