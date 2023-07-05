from pydantic import BaseModel
from models.Accommodation import Accommodation

from typing import Optional, Any

class House(Accommodation):
    numberOfRooms: Optional[Any] = None

