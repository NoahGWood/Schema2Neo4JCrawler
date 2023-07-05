from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class EndorseAction(Action):
    endorsee: Optional[Any] = None

