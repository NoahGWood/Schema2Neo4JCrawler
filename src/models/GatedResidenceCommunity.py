from pydantic import BaseModel
from models.Place import Place

from typing import Optional, Any

class GatedResidenceCommunity(Place):
    accommodationFloorPlan: Optional[Any] = None

