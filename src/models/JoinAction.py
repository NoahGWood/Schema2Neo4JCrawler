from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class JoinAction(Action):
    event: Optional[Any] = None

