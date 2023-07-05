from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class DepartAction(Action):
    fromLocation: Optional[Any] = None
    toLocation: Optional[Any] = None

