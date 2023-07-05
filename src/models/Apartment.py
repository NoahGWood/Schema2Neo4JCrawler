from pydantic import BaseModel
from models.Accommodation import Accommodation

from typing import Optional, Any

class Apartment(Accommodation):
    numberOfRooms: Optional[Any] = None
    occupancy: Optional[Any] = None

