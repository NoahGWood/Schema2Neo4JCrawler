from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class ShareAction(Action):
    about: Optional[Any] = None
    inLanguage: Optional[Any] = None
    recipient: Optional[Any] = None

