from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class CommunicateAction(Action):
    about: Optional[Any] = None
    inLanguage: Optional[Any] = None
    recipient: Optional[Any] = None

