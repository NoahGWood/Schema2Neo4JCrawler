from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class LoseAction(Action):
    winner: Optional[Any] = None

