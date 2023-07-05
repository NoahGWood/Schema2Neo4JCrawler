from pydantic import BaseModel
from models.Action import Action

from typing import Optional, Any

class DeleteAction(Action):
    targetCollection: Optional[Any] = None

