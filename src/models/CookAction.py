from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class CookAction(Action):
    foodEstablishment: Optional[Any] = None
    foodEvent: Optional[Any] = None
    recipe: Optional[Any] = None

