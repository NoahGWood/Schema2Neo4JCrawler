from pydantic import BaseModel
from models.MoveAction import MoveAction

from typing import Optional, Any

class TravelAction(MoveAction):
    distance: Optional[Any] = None

