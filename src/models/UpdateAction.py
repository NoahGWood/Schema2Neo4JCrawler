from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class UpdateAction(Action):
    targetCollection: Optional[Any] = None

