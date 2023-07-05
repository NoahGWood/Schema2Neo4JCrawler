from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class WriteAction(Action):
    inLanguage: Optional[Any] = None

