from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class CancelAction(Action):
    scheduledTime: Optional[Any] = None

