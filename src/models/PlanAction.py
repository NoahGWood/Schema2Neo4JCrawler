from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class PlanAction(Action):
    scheduledTime: Optional[Any] = None

