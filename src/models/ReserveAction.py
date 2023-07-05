from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class ReserveAction(Action):
    scheduledTime: Optional[Any] = None

