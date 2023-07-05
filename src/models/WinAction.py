from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class WinAction(Action):
    loser: Optional[Any] = None

