from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class PlayAction(Action):
    audience: Optional[Any] = None
    event: Optional[Any] = None

