from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class ConsumeAction(Action):
    actionAccessibilityRequirement: Optional[Any] = None
    expectsAcceptanceOf: Optional[Any] = None

