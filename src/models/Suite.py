from pydantic import BaseModel
from models.Accommodation import Accommodation

from typing import Optional, Any

class Suite(Accommodation):
    bed: Optional[Any] = None
    numberOfRooms: Optional[Any] = None
    occupancy: Optional[Any] = None

