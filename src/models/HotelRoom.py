from pydantic import BaseModel
from models.Accommodation import Accommodation

from typing import Optional, Any

class HotelRoom(Accommodation):
    bed: Optional[Any] = None
    occupancy: Optional[Any] = None

