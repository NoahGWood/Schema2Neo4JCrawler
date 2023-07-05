from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class ListenAction(Action):
    actionAccessibilityRequirement: Optional[Any] = None
    expectsAcceptanceOf: Optional[Any] = None

