from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class AuthorizeAction(Action):
    recipient: Optional[Any] = None

