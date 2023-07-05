from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class MoveAction(Action):
    fromLocation: Optional[Any] = None
    toLocation: Optional[Any] = None

