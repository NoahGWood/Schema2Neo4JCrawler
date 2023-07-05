from pydantic import BaseModel
from models.Place import Place

from typing import Optional, Any

class Residence(Place):
    accommodationFloorPlan: Optional[Any] = None

