from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class LeaveAction(Action):
    event: Optional[Any] = None

